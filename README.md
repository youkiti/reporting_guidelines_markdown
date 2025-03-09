# Reporting Guidelines Markdown Collection

## 概要
このレポジトリは、医学・公衆衛生学分野で広く使用されている報告ガイドライン（Reporting Guidelines）をマークダウン形式とMermaid図表で提供しています。元のPDFや文書形式のガイドラインをAIや自動化ツールで利用しやすいフォーマットに変換することを目的としています。

## 収録ガイドライン

### PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses)
システマティックレビューとメタアナリシスの報告のための国際的に認められたガイドライン
- [PRISMA 2020 Checklist](./checklists/prisma/PRISMA_2020_checklist.md)
- [PRISMA 2020 Abstract Checklist](./checklists/prisma/PRISMA_2020_abstract_checklist.md)
- [PRISMA 2020 Expanded Checklist](./checklists/prisma/PRISMA_2020_expanded_checklist.md)
- [PRISMA 2020 Flow Diagram](./checklists/prisma/PRISMA_Flowchart_Updated.md) - Mermaid形式で実装

### RECORD (REporting of studies Conducted using Observational Routinely-collected Data)
ルーチン収集された健康データを使用した観察研究の報告のためのガイドライン
- [RECORD Checklist](./checklists/record/RECORD%20Checklist.md)

### STROBE (STrengthening the Reporting of OBservational studies in Epidemiology)
観察研究の報告のためのガイドライン
- [STROBE Checklist](./checklists/strobe/STROBE-checklist-v4-combined.md)

### TRIPOD-AI (Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis - Artificial Intelligence)
AIを用いた予測モデルの開発・評価の報告のためのガイドライン
- [TRIPOD-AI Checklist](./checklists/tripod_ai/TRIPODAI_checklist.md)

### TRIPOD-LLM (Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis - Large Language Model)
LLMを用いた予測モデルの開発・評価の報告のためのガイドライン
- [TRIPOD-LLM Checklist](./checklists/TRIPOD-LLM/TRIPOD-LLM-Checklist.md)

## マークダウンとMermaid図の利点
オリジナルのPDF形式のガイドラインをマークダウンとMermaid図に変換することで以下の利点があります：

1. **機械可読性の向上**: AIツールでの分析や処理が容易になります
2. **バージョン管理**: Gitなどのバージョン管理システムで変更履歴を追跡できます
3. **検索と参照**: テキストベースのため、特定の項目や要件の検索が容易です
4. **ウェブ上での表示**: GitHub Pages等での表示に最適化されています
5. **自動チェックツール**: 論文やプロトコルの自動チェックに利用できます

## ライセンス情報
このレポジトリの内容は、原著作物のクリエイティブコモンズライセンス（CC BY）を継承しています。各ガイドラインは以下の論文から派生したものです：

- PRISMA: Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ 2021;372:n71. doi: 10.1136/bmj.n71
- RECORD: Benchimol EI, Smeeth L, Guttmann A, et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) Statement. PLoS Medicine 2015
- STROBE: von Elm E, Altman DG, Egger M, et al. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. J Clin Epidemiol 2008;61:344-9
- TRIPOD-AI: Collins GS, Moons KGM, Dhiman P, et al. Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis (TRIPOD): the TRIPOD-AI extension for studies developing or validating prediction models using artificial intelligence. BMJ 2024;385:e078378. doi:10.1136/bmj-2023-078378

## 引用方法
このレポジトリを引用する場合は、以下の形式を使用してください：

```
Yuki Kataoka. Reporting Guidelines Markdown Collection. GitHub. https://github.com/youkiti/reporting_guidelines_markdown [accsessed date]
```

また、各ガイドラインを使用する際には、上記の原著論文も併せて引用してください。
