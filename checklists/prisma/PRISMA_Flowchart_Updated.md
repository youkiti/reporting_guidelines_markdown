# PRISMA 2020 Flow Diagram

Source: https://www.prisma-statement.org/

```mermaid
flowchart TD
    %% 識別のセクション
    subgraph Identification [Identification]
        A1["Records identified from:
Databases (n = )
Registers (n = )"]
        A2["Records identified from:
Websites (n = )
Organisations (n = )
Citation searching (n = )
etc."]
    end
    
    B["Records removed before screening:
Duplicate records removed (n = )
Records marked as ineligible by automation tools (n = )
Records removed for other reasons (n = )"]
    
    %% スクリーニングのセクション
    subgraph Screening [Screening]
        C["Records screened
        (n = )"]
        D["Records excluded
(n = )"]
        E1["Reports sought for retrieval
(n = )"]
        F1["Reports not retrieved
(n = )"]
        G1["Reports assessed for eligibility
(n = )"]
        H1["Reports excluded:
Reason 1 (n = )
Reason 2 (n = )
Reason 3 (n = )
etc."]
        
        E2["Reports sought for retrieval
(n = )"]
        F2["Reports not retrieved
(n = )"]
        G2["Reports assessed for eligibility
(n = )"]
        H2["Reports excluded:
Reason 1 (n = )
Reason 2 (n = )
Reason 3 (n = )
etc."]
    end
    
    %% 含めるセクション
    subgraph Included [Included]
        I["Studies included in review
(n = )
Reports of included studies
(n = )"]
    end
    
    %% フローの接続 - 左側のパス
    A1 --> C
    A1 --> B
    C --> D
    C --> E1
    E1 --> F1
    E1 --> G1
    G1 --> H1
    G1 ---> I
    
    %% フローの接続 - 右側のパス
    A2 --> E2
    E2 --> F2
    E2 --> G2
    G2 --> H2
    G2 ---> I
    
    %% ノードの明示的な配置
    %% 左右のパスを明確に分離するための位置調整
    A1 & C & D & E1 & F1 & G1 & H1:::leftPath
    A2 & E2 & F2 & G2 & H2:::rightPath
    
    %% スタイル定義
    classDef leftPath fill:#f9f9f9
    classDef rightPath fill:#f9f9f9
```

*Consider, if feasible to do so, reporting the number of records identified from each database or register searched (rather than the total number across all databases/registers).

**If automation tools were used, indicate how many records were excluded by a human and how many were excluded by automation tools.

From: Page MJ, et al. BMJ 2021;372:n71. doi: 10.1136/bmj.n71.  
This work is licensed under CC BY 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/
