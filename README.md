# Reporting Guidelines Markdown Collection

## 概要
このレポジトリは、医学・公衆衛生学分野で広く使用されている報告ガイドライン（Reporting Guidelines）をマークダウン形式とJSON形式、およびMermaid図表で提供しています。元のPDFや文書形式のガイドラインをAIや自動化ツールで利用しやすいフォーマットに変換することを目的としています。なお、各チェックリストはマークダウン形式でのテーブル表示の体裁を整えるために、一部内容を改変しています。

## 収録ガイドライン

### PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses)
システマティックレビューとメタアナリシスの報告のためのガイドライン
- [PRISMA 2020 Checklist](./checklists/prisma/PRISMA_2020_checklist.md) - [JSON版](./checklists/prisma/PRISMA_2020_checklist_optimized.json)
- [PRISMA 2020 Abstract Checklist](./checklists/prisma/PRISMA_2020_abstract_checklist.md) - [JSON版](./checklists/prisma/PRISMA_2020_abstract_checklist_optimized.json)
- [PRISMA 2020 Expanded Checklist](./checklists/prisma/PRISMA_2020_expanded_checklist.md) - [JSON版](./checklists/prisma/PRISMA_2020_expanded_checklist.json)
- [PRISMA 2020 Flow Diagram](./checklists/prisma/PRISMA_Flowchart_Updated.md) - Mermaid形式で実装

### RECORD (REporting of studies Conducted using Observational Routinely-collected Data)
ルーチン収集された健康データを使用した観察研究の報告のためのガイドライン
- [RECORD Checklist](./checklists/record/RECORD%20Checklist.md) - [JSON版](./checklists/record/RECORD_Checklist_optimized.json)

### STROBE (STrengthening the Reporting of OBservational studies in Epidemiology)
観察研究の報告のためのガイドライン
- [STROBE Checklist](./checklists/strobe/STROBE-checklist-v4-combined.md) - [JSON版](./checklists/strobe/STROBE-checklist-v4-combined_optimized.json)

### TRIPOD-AI (Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis - Artificial Intelligence)
AIを用いた予測モデルの開発・評価の報告のためのガイドライン
- [TRIPOD-AI Checklist](./checklists/tripod_ai/TRIPODAI_checklist.md) - [JSON版](./checklists/tripod_ai/TRIPODAI_checklist_optimized.json)
- [TRIPOD-AI Abstract Checklist](./checklists/tripod_ai/TRIPODAI_abstract_checklist.md) - [JSON版](./checklists/tripod_ai/TRIPODAI_abstract_checklist_optimized.json)

### TRIPOD-LLM (Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis - Large Language Model)
LLMを用いた予測モデルの開発・評価の報告のためのガイドライン
- [TRIPOD-LLM Checklist](./checklists/TRIPOD-LLM/TRIPOD-LLM-Checklist.md) - [JSON版](./checklists/TRIPOD-LLM/TRIPOD-LLM-Checklist_optimized.json)
- [TRIPOD-LLM Abstract Checklist](./checklists/TRIPOD-LLM/TRIPOD-LLM-Abstract-Checklist.md) - [JSON版](./checklists/TRIPOD-LLM/TRIPOD-LLM-Abstract-Checklist_optimized.json)
- [TRIPOD-LLM Explanation and Elaboration](./checklists/TRIPOD-LLM/TRIPOD-LLM-Explanation-Elaboration.md) - [JSON版（最適化済）](./checklists/TRIPOD-LLM/TRIPOD-LLM-Explanation-Elaboration_optimized.json)

## サンプルコードと実装例

このリポジトリには、報告ガイドラインを活用するためのサンプルコードとAPIの実装例が含まれています。

### OpenAI API サンプル（PRISMA分析ツール）

[examples/openai_python](./examples/openai_python) ディレクトリには、OpenAI APIを使用して論文のPDFをPRISMAガイドラインに基づいて自動分析するサンプルが含まれています。

#### 主な機能
- 学術論文PDFの自動ダウンロードとテキスト抽出
- OpenAI APIを使用した論文テキストとPRISMAチェックリストの照合
- 構造化された形式での分析結果出力
  - 各チェックリスト項目の論文内での位置と準拠状況
  - PRISMAガイドラインへの全体的な準拠率
  - 分析の要約と改善提案

#### 使用方法
```bash
# 必要なパッケージのインストール
pip install -r required.txt

# 実行
python examples/openai_python/prisma_pdf_analyzer.py
```

詳細については、[OpenAI API サンプルのREADME](./examples/openai_python/README.md)を参照してください。

## JSONフォーマット

このレポジトリでは、各ガイドラインをマークダウン形式に加えて、構造化されたJSON形式でも提供しています。JSON形式には以下のような特徴と利点があります：

### JSON構造
```json
{
  "title": "チェックリスト名",
  "source": "出典URL等",
  "description": "チェックリストの説明文",
  "categories": [
    {
      "name": "カテゴリ（例: TITLE, ABSTRACT）",
      "sections": [
        {
          "name": "セクション名",
          "items": [
            {
              "item": "項目番号（例: 1, 2, 3）",
              "description": "チェックリスト項目の説明文",
              "type": "Essential または Additional または Where applicable",
              "reportLocation": ""
            }
          ]
        }
      ]
    }
  ]
}
```

### 主な特徴
- **階層構造**：カテゴリ > セクション > 項目 の3階層構造により論理的な分類を実現
- **項目タイプ分類**：必須項目（Essential）、追加項目（Additional）、条件付き項目（Where applicable）の区別
- **reportLocation**：論文内のどこに該当項目が記載されているかを記録するためのフィールド

### 利用シナリオ
- **自動チェック**：論文が各チェックリスト項目を満たしているかをプログラムで自動評価
- **AIとの連携**：構造化データにより、OpenAIなどのAPIと連携した論文評価が可能
- **カスタムツール開発**：論文執筆支援ツールや評価ツールの開発に活用可能

## ライセンス情報
このレポジトリの内容は、原著作物のクリエイティブコモンズライセンス（CC BY）を継承しています。各ガイドラインは以下の論文から派生したものです。なお、STROBEとTRIPOD-LLMについては明示がなく、各チェックリストを公開しているサイトからの引用を行っています：

- PRISMA: Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ 2021;372:n71. doi: 10.1136/bmj.n71
- RECORD: Benchimol EI, Smeeth L, Guttmann A, et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) statement. PLoS Med. 2015 Oct 6;12(10):e1001885. doi: 10.1371/journal.pmed.1001885
- STROBE: von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP; STROBE Initiative. Strengthening the reporting of observational studies in epidemiology (STROBE) statement: guidelines for reporting observational studies. BMJ. 2007 Oct 20;335(7624):806–808. doi: 10.1136/bmj.39335.541782.AD
- TRIPOD-AI: Collins GS, Moons KGM, Dhiman P, et al. Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis (TRIPOD): the TRIPOD-AI extension for studies developing or validating prediction models using artificial intelligence. BMJ 2024;385:e078378. doi:10.1136/bmj-2023-078378
- TRIPOD-LLM: Gallifant J, Afshar M, Ameen S, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nature Medicine 2025;31:60-69. doi: 10.1038/s41591-023-02595-0

## 引用方法
このレポジトリを引用する場合は、以下の形式を使用してください：

```
Yuki Kataoka. Reporting Guidelines Markdown Collections. GitHub. https://github.com/youkiti/reporting_guidelines_markdown [accsessed date]
```

また、各ガイドラインを使用する際には、上記の原著論文も併せて引用してください。
