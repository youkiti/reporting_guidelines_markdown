# OpenAI API Pythonサンプル

このディレクトリには、OpenAI APIを使用したPythonのサンプルコードが含まれています。

## 環境設定

1. 必要なライブラリをインストールします：

```bash
# 個別にインストールする場合
pip install openai python-dotenv pydantic pypdf requests

# または、プロジェクトルートの required.txt を使用する場合
pip install -r ../../required.txt
```

2. プロジェクトのルートディレクトリにある`.env.example`をコピーして`.env`ファイルを作成します：

```bash
cp .env.example .env
```

3. `.env`ファイルを編集して、OpenAI APIキーを設定します：

```
OPENAI_API_KEY=your_actual_api_key_here
```

## サンプル一覧

### PRISMA PDF論文分析 (`prisma_pdf_analyzer.py`)

このサンプルは、学術論文のPDFをダウンロードし、そのテキストからPRISMAチェックリストの項目に関連する情報を抽出します。
OpenAIの`parse`機能とPydanticのデータモデルを使用して、論文テキストを構造化された形式で分析します。

#### 主な機能

- PDFのダウンロードと自動テキスト抽出
- PRISMAチェックリストJSONファイルの読み込み
- 論文テキストとPRISMAチェックリストの項目を照合
- 構造化された形式での分析結果出力
  - 論文のタイトル、著者、出版年
  - 各PRISMAチェックリスト項目の論文内での対応状況
  - PRISMAガイドラインへの全体的な準拠率
  - 分析の要約と詳細

#### 使用例

```bash
python prisma_pdf_analyzer.py
```

実行すると以下の処理が行われます：
1. 論文PDF（デフォルトではarXivの論文：https://arxiv.org/pdf/2304.01852.pdf）をダウンロード
   * 注：一部の学術誌PDFはアクセス制限がある場合があります
2. PDFからテキストを抽出
3. リポジトリ内のPRISMAチェックリストJSONファイルを読み込み
4. OpenAI APIを使用して論文をPRISMAガイドラインに基づいて分析
5. 分析結果を表示（論文情報、PRISMAガイドライン準拠率、詳細分析など）

## 注意事項

- 使用するにはOpenAI APIキーが必要です
- 使用料金が発生するため、APIキーの管理には注意してください
- テキスト処理に大量のトークンを使用するため、APIコスト管理に注意してください
- 最新のOpenAIのモデルやAPIの仕様は変更される可能性があるため、公式ドキュメントを参照してください
- PDFの構造によってはテキスト抽出の精度が変わる可能性があります
- 一部の学術誌PDFはアクセス制限がかかっていて直接ダウンロードできない場合があります。アクセス可能なPDFのURLに変更するか、ローカルのPDFファイルを使用するように修正してください

## スクリプトのカスタマイズ

PDFのURLをカスタマイズするには、`prisma_pdf_analyzer.py`の以下の部分を編集します：

```python
# オープンアクセス論文のPDFのURL
pdf_url = "https://arxiv.org/pdf/2304.01852.pdf"
```

他の公開PDFのURLに変更するか、ローカルファイルパスを使用することも可能です。
