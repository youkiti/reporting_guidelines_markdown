"""
OpenAI APIを使用した論文からのPRISMAチェックリスト項目抽出例

このスクリプトは、BMJ論文のPDFをダウンロードし、そのテキストからPRISMAチェックリストの
項目に関連する情報を抽出する方法を示しています。OpenAIのstructured output機能を
使用して、論文テキストから構造化データを取得します。
"""

import os
import json
import requests
import tempfile
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
import pypdf  # PDFからテキストを抽出するためのライブラリ
from openai import OpenAI
from dotenv import load_dotenv

# .envファイルから環境変数を読み込み
load_dotenv()

# OpenAIクライアントを初期化（APIキーは環境変数から取得）
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# PRISMAチェックリスト項目の要素を表すPydanticモデル
class ChecklistElement(BaseModel):
    description: str = Field(..., description="チェックリスト項目の説明")
    found_in_paper: bool = Field(..., description="論文内で該当項目が見つかったかどうか")
    evidence: Optional[str] = Field(None, description="論文内の該当箇所のテキスト（見つかった場合）")
    page_number: Optional[int] = Field(None, description="該当箇所のページ番号（見つかった場合）")
    comments: Optional[str] = Field(None, description="分析に関する追加コメント")

# PRISMAチェックリスト項目を表すPydanticモデル
class ChecklistItem(BaseModel):
    item: str = Field(..., description="項目番号（例: 1a, 1b, 2）")
    elements: List[ChecklistElement] = Field(..., description="チェックリスト項目の要素リスト")

# PRISMAチェックリストセクションを表すPydanticモデル
class ChecklistSection(BaseModel):
    name: str = Field(..., description="セクション名（例: TITLE, ABSTRACT）")
    items: List[ChecklistItem] = Field(..., description="セクション内の項目リスト")

# 論文からのPRISMA抽出結果を表すPydanticモデル
class PrismaExtractionResult(BaseModel):
    paper_title: str = Field(..., description="論文のタイトル")
    paper_authors: List[str] = Field(..., description="論文の著者リスト")
    publication_year: int = Field(..., description="出版年")
    prisma_sections: List[ChecklistSection] = Field(..., description="PRISMAセクションとその項目")
    overall_compliance: float = Field(..., description="PRISMAガイドラインへの全体的な準拠率（%）")
    summary: str = Field(..., description="PRISMAガイドライン準拠に関する要約分析")

def download_pdf(url: str, output_path: str = None) -> str:
    """論文のPDFをダウンロードする

    Args:
        url: 論文PDFのURL
        output_path: 保存先のパス（指定がない場合は一時ファイルを作成）

    Returns:
        str: ダウンロードしたPDFのパス
    """
    response = requests.get(url, stream=True)
    response.raise_for_status()  # エラーチェック
    
    if output_path is None:
        # 一時ファイルを作成
        fd, output_path = tempfile.mkstemp(suffix='.pdf')
        os.close(fd)
    
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    print(f"PDFをダウンロードしました: {output_path}")
    return output_path

def extract_text_from_pdf(pdf_path: str) -> str:
    """PDFからテキストを抽出する

    Args:
        pdf_path: PDFファイルのパス

    Returns:
        str: 抽出されたテキスト
    """
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text() + "\n\n--- Page Break ---\n\n"
    
    return text

def load_prisma_checklist(json_path: str) -> Dict[str, Any]:
    """PRISMAチェックリストのJSONファイルを読み込む

    Args:
        json_path: PRISMAチェックリストのJSONファイルのパス

    Returns:
        Dict[str, Any]: チェックリストの辞書
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        checklist = json.load(f)
    return checklist

def analyze_paper_with_prisma(paper_text: str, prisma_checklist: Dict[str, Any]) -> PrismaExtractionResult:
    """論文テキストをPRISMAチェックリストに基づいて分析

    Args:
        paper_text: 論文のテキスト
        prisma_checklist: PRISMAチェックリストの辞書

    Returns:
        PrismaExtractionResult: 分析結果
    """
    # テキストが長すぎる場合は最初の数ページだけを使用
    if len(paper_text) > 100000:
        paper_text = paper_text[:100000] + "...[テキスト省略]..."
    
    # チェックリストの構造に関する説明をシステムプロンプトとして構築
    system_prompt = """
    あなたは論文をPRISMAガイドラインに基づいて評価する専門家です。提供された論文テキストを分析し、
    PRISMAチェックリストの各項目が論文内でどのように対応しているかを特定してください。
    各項目については以下を判断してください：
    1. 論文内にその項目が見つかるか
    2. 見つかる場合、その証拠となるテキスト
    3. 該当箇所の推定ページ番号
    4. 項目の準拠に関するコメント
    
    分析は厳密かつ客観的に行い、すべての評価に根拠を示してください。
    """
    
    # チェックリストの概要を含めるための準備
    checklist_summary = "PRISMAチェックリスト項目:\n"
    for category in prisma_checklist.get("categories", []):
        category_name = category.get("name", "")
        checklist_summary += f"- {category_name}:\n"
        for section in category.get("sections", []):
            section_name = section.get("name", "")
            checklist_summary += f"  - {section_name}:\n"
            for item in section.get("items", []):
                item_number = item.get("item", "")
                description = item.get("description", "")
                checklist_summary += f"    - {item_number}: {description}\n"
    
    # OpenAIのparse機能を使用して論文からPRISMA項目情報を抽出
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",  # モデルを指定
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"以下の論文テキストをPRISMAガイドラインに従って分析してください。\n\n{checklist_summary}\n\n===論文テキスト===\n\n{paper_text}"}
        ],
        response_format=PrismaExtractionResult,  # レスポンスの形式を指定
    )
    
    # 分析結果を返す
    return completion.choices[0].message.parsed

# メイン処理
if __name__ == "__main__":
    # オープンアクセス論文のPDFのURL (medrXivの論文を使用)
    pdf_url = "https://www.medrxiv.org/content/10.1101/2024.03.04.24303733v1.full.pdf"
    
    try:
        # PDFをダウンロード
        pdf_path = download_pdf(pdf_url)
        
        # PDFからテキストを抽出
        paper_text = extract_text_from_pdf(pdf_path)
        print(f"PDFから{len(paper_text)}文字のテキストを抽出しました")
        
        # PRISMAチェックリストのJSONを読み込む
        prisma_checklist_path = "checklists/prisma/PRISMA_2020_checklist_optimized.json"
        prisma_checklist = load_prisma_checklist(prisma_checklist_path)
        
        # 論文をPRISMAガイドラインに基づいて分析
        result = analyze_paper_with_prisma(paper_text, prisma_checklist)
        
        # 結果表示
        print(f"\n論文タイトル: {result.paper_title}")
        print(f"著者: {', '.join(result.paper_authors)}")
        print(f"出版年: {result.publication_year}")
        print(f"PRISMAガイドライン準拠率: {result.overall_compliance:.1f}%")
        print(f"\n要約分析:\n{result.summary}")
        
        # 詳細な分析結果を表示
        print("\n詳細分析:")
        for section in result.prisma_sections:
            print(f"\nセクション: {section.name}")
            for item in section.items:
                print(f"  項目 {item.item}:")
                for element in item.elements:
                    status = "見つかりました" if element.found_in_paper else "見つかりませんでした"
                    print(f"    - {element.description}: {status}")
                    if element.found_in_paper and element.evidence:
                        print(f"      証拠: \"{element.evidence}\" (ページ: {element.page_number})")
                    if element.comments:
                        print(f"      コメント: {element.comments}")
        
        # 一時ファイルを削除
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
            
    except Exception as e:
        print(f"エラーが発生しました: {e}")
