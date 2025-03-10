# OpenAI API Pythonサンプル

このディレクトリには、OpenAI APIを使用したPythonのサンプルコードが含まれています。

## 環境設定

1. 必要なライブラリをインストールします：

```bash
pip install openai python-dotenv pydantic pypdf requests
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

このサンプルは、BMJ論文のPDFをダウンロードし、そのテキストからPRISMAチェックリストの項目に関連する情報を抽出します。
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
1. BMJ論文（https://www.bmj.com/content/388/bmj-2025-084613.full.pdf）をダウンロード
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
