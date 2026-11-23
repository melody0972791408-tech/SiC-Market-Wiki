# Graph Workflow Specification — SiC Market LLM Wiki & Presentation System

本規格書定義本專案 6 階段 Graph 工作流程的狀態模型（State Schema）、節點行為合約（Node Contracts）、邊界條件（Edge Transitions）與品質驗證標準。

---

## 1. 狀態模型（State Schema）

```python
class SiCMarketState:
    # 專案整體狀態
    session_id: str
    current_node: str
    retry_counts: dict[str, int]  # 記錄各節點重試次數，上限 3 次
    
    # 原始資料存證
    raw_sources: list[dict]       # 來源 ID, 標題, 發布機構, 原始網址, 取得內容, 主題
    metadata_registry: dict       # data/raw/metadata.json
    
    # Wiki 知識庫
    wiki_pages: list[dict]        # 筆記路徑, 標題, 分類, 標籤, 引用來源, 內部連結
    broken_links: list[str]       # 斷鏈清單（必須為空）
    orphan_pages: list[str]       # 孤島頁面清單（必須為空）
    wiki_verified: bool           # Node 2 驗證通過標記
    
    # 教學大綱與驗證
    presentation_outline: list[dict] # 8 頁簡報大綱, 每頁概念, 比喻, Wiki 對應
    outline_approved: bool        # HITL 檢查點 2 人工核可標記
    fact_verification_report: dict# 數據核查矩陣（歷史數據 vs 預測數據 vs 原始來源）
    
    # 成果展示
    presentation_html: str        # Reveal.js HTML 內容
    evaluation_scores: dict       # 初學者理解度, 視覺層次, 真實性評分
```

---

## 2. 節點詳細合約規範（Node Contracts）

### Node 1: Ingest Sources
- **Input**: 外部原始公開文獻、網址、年報或論文（共 5 篇）。
- **Task**: 
  - 檢驗文獻之真實性與可讀性（解析 DOI、官方網址、發布單位）。
  - 將原始文本以不可篡改格式存入 `data/raw/source_*.md`。
  - 建立標準化 `data/raw/metadata.json`。
- **Output**: 5 篇 `data/raw/source_*.md` 與 `data/raw/metadata.json`。
- **Validation Criteria**:
  - 5 篇文獻具備合法真實 URL/DOI，能清楚標註公開範圍。
  - 完整覆蓋 SiC 5 大主題。
  - 嚴格分離付費完整版與公開摘要，不假冒獲取完整報告。
- **Failure / Retry Condition**:
  - 若 URL 失效或 DOI 錯誤，觸發重試重新檢索合法替代來源（最多 3 次）。若仍無效則停止並回報人類。

---

### Node 2: Build and Query Wiki
- **Input**: `data/raw/` 原始檔案與 `metadata.json`。
- **Task**:
  - 將 5 篇來源資料解構萃取，建立符合 Karpathy 概念之原子化知識庫。
  - 產出 14 篇以上專題 Markdown 檔案於 `wiki/` 各子目錄。
  - 為每頁建立 YAML Frontmatter 與雙向 `[[wikilinks]]`。
  - 產出總索引導航 `wiki/INDEX.md`。
  - 執行 `workflow/verify_wiki.py` 自動稽核。
- **Output**: `wiki/` 知識庫架構、`wiki/INDEX.md`、驗證報告。
- **Validation Criteria**:
  - 零斷鏈（Broken Links = 0）。
  - 零孤島頁面（Orphan Pages = 0）。
  - 所有具體數據（金額、百分比、尺寸）皆有標註 Source ID。
  - 完整覆蓋 5 大主題。
- **Failure / Retry Condition**:
  - 發現斷鏈或孤島頁面時自動修復補齊（最多 3 次）。
- **Human-in-the-Loop Checkpoint 1**:
  - 暫停流程，向使用者提交 Wiki 品質驗證報告與成果，確認無誤後方可進入 Node 3。

---

### Node 3: Generate Teaching Outline
- **Input**: `wiki/` 知識庫全部頁面與分類導航。
- **Task**:
  - 設計 8 頁循序漸進之教學簡報大綱，面向零半導體背景的初學者。
  - 融入生活化比喻（如水庫閘門、道路交通），降低認知門檻。
  - 明確規劃每頁之核心標題、教學概念、講者說明稿要點與對應之 Wiki 頁面及 Source ID。
- **Output**: 結構化教學大綱（8 頁）。
- **Validation Criteria**:
  - 頁數精準控制在約 8 頁。
  - 難易度由淺入深（定義 $\rightarrow$ 優勢 $\rightarrow$ 應用 $\rightarrow$ 市場 $\rightarrow$ 供應鏈 $\rightarrow$ 競爭 $\rightarrow$ 挑戰）。
  - 100% 概念可對應至 Wiki 頁面。
- **Human-in-the-Loop Checkpoint 2**:
  - 暫停流程，提交大綱由人類審查教學邏輯與節奏。

---

### Node 4: Verify Facts and Sources
- **Input**: 簡報大綱、`wiki/` 筆記、`data/raw/` 原始來源。
- **Task**:
  - 對簡報大綱中提及的每一項數值、年份、市佔率、技術參數進行交叉比對。
  - 嚴格檢查「歷史數據（2023 市佔率/市場規模）」與「機構預測（2026/2029 展望）」是否混淆。
  - 檢查市場定義（SiC Power Device vs. Substrate）是否精確。
- **Output**: `workflow/fact_verification_report.md`。
- **Validation Criteria**:
  - 零虛構數據、零未定義單位。
  - 100% 數據可溯源至 Source ID。
- **Failure / Retry Condition**:
  - 若發現未證實陳述，退回修正簡報大綱（最多 3 次）。

---

### Node 5: Generate HTML Presentation
- **Input**: 通過核查之簡報大綱與文字素材。
- **Task**:
  - 撰寫 `presentation/index.html`。
  - 採用 Reveal.js 框架（透過 CDN 載入，並清楚備註需連網環境）。
  - 設計高質感半導體科技主題（自訂 CSS、響應式卡片排版、鮮明對比）。
  - 為每張投影片編寫完整 `<aside class="notes">` 演講備忘稿。
  - 加入引用腳註與點擊跳轉提示。
- **Output**: `presentation/index.html`。
- **Validation Criteria**:
  - HTML/CSS 語法無誤，所有 Reveal.js 外掛正常初始化。
  - 支援鍵盤翻頁（方向鍵）、演講者模式（S 鍵）、全螢幕（F 鍵）。
  - 排版無字體溢出，在常見螢幕解析度下顯示完美。
- **Failure / Retry Condition**:
  - 若排版毀損或腳本報錯，自動修復 HTML/CSS（最多 3 次）。

---

### Node 6: Evaluate and Revise
- **Input**: `presentation/index.html`。
- **Task**:
  - 進行多維度品質評測（初學者可理解度、資訊層次視覺化、來源真實度）。
  - 產出最終驗收報告與自我反思。
- **Output**: 最終完成的簡報專案與更新後之 `workflow/execution_log.md`。
- **Validation Criteria**:
  - 綜合評測達標。
- **Failure / Retry Condition**:
  - 若評測指出初學者理解障礙，退回 Node 5 調整文字與排版（最多 3 次）。
