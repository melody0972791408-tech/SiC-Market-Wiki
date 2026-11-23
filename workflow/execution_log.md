# Workflow Execution & Verification Log（執行與檢驗反思紀錄）

本文件真實記錄專案多階段 Graph 工作流程的實際執行歷程、發現之真實錯誤、修改重試次數與反思建議。

> **執行準則**：本紀錄僅反映實際已發生的執行動作，嚴禁預先編造未執行節點之執行成功紀錄。未執行之節點狀態統一標記為 `Pending`。

---

## 總覽狀態面板（Status Dashboard）

| 節點編號與名稱 | 當前狀態 | 重試次數 | 人工審核點（HITL） | 備註說明 |
| :--- | :---: | :---: | :---: | :--- |
| **Node 1: Ingest Sources** | **COMPLETED** | 1 次修正 | 已通過來源清單確認 | 修正 3 處來源驗證問題（DOI、URL、SEC PDF） |
| **Node 2: Build and Query Wiki** | **COMPLETED** | 1 次修正 | 已通過審核 | 自動檢查發現 1 處斷鏈並修復，完成 18 篇 Wiki 筆記 |
| **Node 3: Generate Teaching Outline** | **COMPLETED** | 1 次修正 | 已通過審核（HITL 2） | 依審查意見全面校正 7 大事實與數據描述 |
| **Node 4: Verify Facts and Sources** | **COMPLETED** | 0 次 | 已完成核查表 | 完成 8 頁大綱之斷言級核查 `fact_verification_report.md` |
| **Node 5: Generate HTML Presentation** | **COMPLETED** | 0 次 | - | 完成 8 頁 Reveal.js 科技風格教學簡報 `presentation/index.html` |
| **Node 6: Evaluate and Revise** | **COMPLETED** | 0 次 | **交付成果待驗收** | 執行 `verify_presentation.py`，8 項指標全數 PASS |

---

## 詳細節點執行歷程

### Node 1: Ingest Sources（原始資料收錄與驗證）

- **執行時間**：2026-11-18
- **輸入**：5 篇原始資料來源需求（MDPI 論文、TrendForce 2023 市佔報告、Yole 2024 功率 SiC 報告、TrendForce 8 吋晶圓追蹤報導、Wolfspeed 2024 年報）。
- **輸出成果**：
  - `data/raw/metadata.json`
  - `data/raw/source_01_mdpi_sic_technology_overview.md`
  - `data/raw/source_02_trendforce_2023_market_share.md`
  - `data/raw/source_03_yole_power_sic_2024.md`
  - `data/raw/source_04_trendforce_8inch_fab_breakthrough.md`
  - `data/raw/source_05_wolfspeed_2024_annual_report.md`
- **初步來源驗證中發現之真實問題（Errors Encountered）**：
  1. **Source 01（MDPI 論文）DOI 錯誤**：初步檢索時引用之 DOI `10.3390/ma17246098` 指向早期草稿捲期，經查驗與使用者提醒，正確正式出版之 DOI 為 `10.3390/ma18010012`（*Materials*, Vol. 18, Issue 1, Article 12, 2024-12-24）。
  2. **Source 02（TrendForce 市佔）URL 不精準**：原先使用之新聞中心重導向網址改為精確的官方發布永久網址 `https://www.trendforce.com/presscenter/news/20240620-12196.html`，並確認其中提及之 2023 年歷史數據（22.8 億美元，YoY 41.4%，前五大 91.9%）。
  3. **Source 03（Yole Group）公開內容範圍核對**：確認 `https://www.yolegroup.com/press-release/power-sic-a-10b-market-by-2029-facing-short-term-turbulence/` 能夠完整取得官方新聞稿核心內容（2029 年 98.73 億美元、CAGR 24%、300 億美元投資、車用 >70%）。
  4. **Source 04（TrendForce 8 吋廠）時間維度界定**：避免將 2024 年初規劃當作 2026 年現狀，特別在原始資料中區分為已進入初期量產（1座）、建設中（5座）、規劃中（5座）。
  5. **Source 05（Wolfspeed）版本替換**：依要求改用 SEC 官方完整 2024 年報 PDF 來源：`https://www.sec.gov/Archives/edgar/data/895419/000089541924000081/wolfspeed_2024xars.pdf`。
- **修正次數**：1 次（將所有更正納入 `metadata.json` 與 `data/raw/` 檔案中）。
- **節點驗證結果**：`PASS`。

---

### Node 2: Build and Query Wiki（知識庫建置與關聯檢索）

- **執行時間**：2026-11-18
- **輸入**：`data/raw/` 下 5 篇不可篡改原始來源與 `metadata.json`。
- **輸出成果**：
  - `wiki/INDEX.md`（總導覽索引與 Mindmap）
  - `wiki/concepts/`（3 篇核心物理與元件結構）
  - `wiki/market/`（3 篇市場規模、車用與工業/AI應用）
  - `wiki/supply-chain/`（3 篇基板長晶、8 吋轉型與成本拆解）
  - `wiki/entities/`（6 篇企業畫像：ST、onsemi、Wolfspeed、Infineon、ROHM、中國廠商）
  - `wiki/outlook/`（2 篇未來機會與潛在挑戰風險）
  - 驗證工具：`workflow/verify_wiki.py`
- **自動檢查發現之真實問題（Errors Encountered）**：
  - **斷鏈錯誤（Broken Link）**：執行 `python3 workflow/verify_wiki.py` 時，腳本報告錯誤：
    ```text
    [ERROR] Broken Link: [[rohm]] referenced in 'device-structures-mosfet.md' does not exist!
    ```
  - **失敗根本原因（Root Cause）**：在撰寫 `device-structures-mosfet.md` 時提及了羅姆（ROHM）原創的雙溝槽架構並加上了 Wikilink，但 `wiki/entities/` 初步僅規劃了五家企業，漏建了 `wiki/entities/rohm.md`。
  - **修正內容與重試（Fix & Retry）**：
    1. 補建 `wiki/entities/rohm.md`，詳述其全球前五大市佔地位、德國 SiCrystal 子公司基板自給、日本宮崎國富 8 吋廠佈局及原創雙溝槽技術。
    2. 同步更新 `wiki/INDEX.md` 知識導覽樹與分類清單。
    3. 重新執行 `python3 workflow/verify_wiki.py`（重試次數：1 次）。
  - **重試驗證結果**：
    ```text
    Total Wiki Pages: 18
    Total Raw Sources: 5
    Broken Links: 0
    Orphan Pages: 0
    Total Errors: 0
    Total Warnings: 0
    SUCCESS: All Wiki Integrity Checks Passed Cleanly!
    ```
- **節點驗證結果**：`PASS`。
- **Human-in-the-Loop 檢查點 1**：**審核通過**（使用者確認通過 HITL 1，正式啟動 Node 3）。

---

### Node 3: Generate Teaching Outline（初學者教學大綱生成）

- **執行時間**：2026-11-23
- **輸入**：`wiki/` 知識庫全部 18 篇筆記與架構導覽。
- **輸出成果**：8 頁教學大綱（含生活化比喻、可視化規劃與講者備忘稿）。
- **審核回饋與 7 大項事實修正（Refinements Made）**：
  1. *Slide 2（溫度區分）*：材料理論耐溫（>300°C）與實際商用元件額定工作結溫（150°C～175°C，部分車規達 200°C）嚴格解耦，不再誇大。
  2. *Slide 3（材料參數解耦）*：澄清 10 倍電場、3 倍熱導率為材料本徵參數，不等於整機改善 10 倍；高壓導通損耗實際降低約 50%～70%。
  3. *Slide 4（800V 與續航條件化）*：將 SiC 定位為「主流首選」（非唯一選擇，1200V Si IGBT 亦能運作但損耗大）；續航提升 5%～10% 標明為特定行車循環模擬條件，刪除無直接依據之固定節省金額。
  4. *Slide 5（2023 市場數據核查）*：查證確認 22.8 億美元（+41.4% YoY）實為 TrendForce 於 2023 年 3 月發布之預測數據；補充 Yole 於 2024 年報告中回溯統計 2023 實際市場約為 27 億美元，並標明 TrendForce 2024 年 6 月發布之歷史數據聚焦於市佔率排名（前五大佔 91.9%）。
  5. *Slide 6（8 吋晶圓產出與成本細緻化）*：區分晶圓表面積增加（1.78 倍）、理論總晶粒數增加（Gross Dies ~1.8 倍）與實際良品晶粒數（Good Dies，取決於實際良率）；載明基板佔總成本 45%～50% 與降低 30%～35% 成本乃是「成熟良率下之預估潛力」。
  6. *Slide 7（競爭排名時間標示）*：明確標註為「2023 年歷史市佔排名（依據 TrendForce 2024 年 6 月報告）」，非當前最新即時數據。
  7. *Slide 8（剔除過度樂觀斷言）*：將「必然成熟」、「趨勢不可逆」等字眼改為條件性、客觀平衡之分析（取決於長晶熱應力突破、良率爬坡速度與總體車市需求）。
- **節點驗證結果**：`PASS（全面校正）`。

---

### Node 4: Verify Facts and Sources（事實與數據交叉核查）

- **執行時間**：2026-11-23
- **輸入**：校正後之 8 頁簡報大綱、`wiki/` 筆記、`data/raw/` 原始存證。
- **輸出成果**：[workflow/fact_verification_report.md](file:///Users/melody/Desktop/SiC-Market-Wiki/workflow/fact_verification_report.md)。
- **查驗機制**：針對 8 頁大綱中每一項關鍵技術數值、市場預測、產業結構與企業排名，建立覆蓋 Slide Number、Claim、Wiki Page、Source ID、Original Source URL、Source Passage、Publication Date 之斷言級對照表。
- **節點驗證結果**：`PASS`。100% 斷言均有明確出處，已排除預測與歷史混淆、材料與系統混淆。
- **Human-in-the-Loop 檢查點 2**：**暫停流程，向使用者提交校正後之 8 頁簡報大綱與斷言級事實核查表，等待使用者核准。**

---

### Node 5: Generate HTML Presentation（Reveal.js 簡報生成）

- **執行時間**：2026-11-23
- **輸入**：通過 HITL Checkpoint 2 審核之 8 頁大綱與 [workflow/fact_verification_report.md](file:///Users/melody/Desktop/SiC-Market-Wiki/workflow/fact_verification_report.md)。
- **輸出成果**：[presentation/index.html](file:///Users/melody/Desktop/SiC-Market-Wiki/presentation/index.html)。
- **落實之設計與校正規格**：
  1. *視覺風格*：深藍（`#070d1e`）、清透青綠點綴（`#00e1d9`）、高對比資訊卡片，去除繁複裝飾，呈現乾淨專業的產業研調報告質感。
  2. *初學者教學*：每頁配置生活化比喻（大腦與肌肉、水庫高防波堤、超薄特種鋼水閘、切黑金硬吐司、高空走鋼索）。
  3. *事實驗證約束*：
     - TrendForce 22.8 億美元明確標記為「2023 年 3 月預測數據」，並與 Yole 2024 回溯統計（27 億美元）並列對照。
     - 4H-SiC 理論耐溫極限（>300°C）與實際商用元件額定結溫（150°C～175°C）明確標示解耦。
     - 8 吋晶圓表面積增加（1.78x）與理論總晶粒數（Gross Dies 1.8x）及良品晶粒數（Good Dies）良率前提明確區分；30%～35% 降本標明為「成熟良率下之預估潛力」。
     - 80 PLUS Titanium 標明為業界主流追求之高效率認證標準，非通用法定要求。
     - 基板佔總成本 45%～50% 精準引用 TrendForce 數據，嚴禁自行編造無依據之成本圓餅圖切片。
     - 嚴格剔除「必然」、「唯一」、「徹底解決」、「所有廠商」等誇大絕對化措辭。
  4. *講者說明稿*：每頁均編寫包含深入淺出引導語之 `<aside class="notes">` 區塊。
  5. *來源標示*：每頁底部均配置獨立 `source-footer`（標記機構、年份與 Source ID）。
  6. *連網說明*：頂部標籤與 HTML 註解清楚說明採 Reveal.js 官方 CDN 載入樣式與腳本，需連網環境。
- **節點驗證結果**：`PASS`。

---

### Node 6: Evaluate and Revise（綜合品質審查與修正）

- **執行時間**：2026-11-23
- **輸入**：[presentation/index.html](file:///Users/melody/Desktop/SiC-Market-Wiki/presentation/index.html)。
- **驗證工具**：撰寫並執行 [workflow/verify_presentation.py](file:///Users/melody/Desktop/SiC-Market-Wiki/workflow/verify_presentation.py)。
- **自動化稽核結果**：
  - *Reveal.js 依賴與初始化*：`PASS`（CDN CSS、JS、RevealNotes 外掛與 `Reveal.initialize()` 初始化全數就緒）。
  - *投影片總頁數*：`PASS`（精準 8 頁）。
  - *演講者備忘稿*：`PASS`（8 頁皆具備完整、豐富之 `<aside class="notes">`，字數介於 270～475 字元）。
  - *來源標註引用*：`PASS`（8 頁底部皆具備合規之 `source-footer`，精準引用 `SRC-01` 至 `SRC-05`）。
  - *絕對化禁用詞檢查*：`PASS`（未出現「必然」、「徹底解決」、「所有廠商」、「唯一選擇」等違規用語）。
  - *核心事實校正*：`PASS`（22.8 億美元預測標籤、300°C 材料與 150-175°C 結溫區分、8 吋成熟良率條件、Titanium 認證標準皆完全合規）。
- **人工瀏覽器測試備註（Manual Inspection Notes）**：
  - 使用者在實體瀏覽器開啟簡報並確認第 1、5、7 頁正常顯示，針對細節提出最後微調要求：
    1. *Slide 1*：保留運算 vs 功率半導體對比，精簡文字，加入簡明教學目標卡片，改善底部導航按鍵之可讀性（增加半透明背景、圓角與邊框）。
    2. *Slide 5*：將 2026 年 53.3 億美元明確標記為「TrendForce 於 2024 年 6 月發布之預測（非已確認之實際規模）」；清楚標明 2023 年 TrendForce 早期預測（22.8 億美元）與 Yole 回溯統計（27 億美元）之口徑差異，維持三欄佈局且不混淆市場定義。
    3. *Slide 7*：將左側表格拆分為清晰的四欄（`2023 排名`、`企業名稱`、`2023 市佔率`、`企業主要競爭優勢`）；明確僅標示經來源確認之 ST 32.6%，其餘廠商市佔標明「未公布」而不擅自推算；精簡右側產業挑戰條目。
  - 完成後同步至 `docs/index.html`，並再次執行 `workflow/verify_presentation.py` 與 `workflow/verify_docs.py`，全數檢驗通過。
- **節點驗證結果**：`PASS`。最終交付成果就緒。

---

## 過程反思與前置化建議（Lessons Learned & Front-Loading）

1. **元資料與 DOI 早期嚴格驗證**：
   - *反思*：在初期檢索時若僅依賴搜尋引擎摘要的 DOI 或導向網址，容易引入早期預印本（Preprint）或舊年報的失效連結。
   - *前置化改進*：未來應將「URL 直連性檢查」與「正式出版 DOI 解析」作為 Node 1 的前置阻擋條件（Hard Gate），在建立 Markdown 之前就必須先通過元資料正規化驗證。
2. **實體清單對齊與斷鏈防範**：
   - *反思*：在撰寫技術概念頁時，隨手連結的實體（如 `[[rohm]]`）若未預先定義於綱要清單中，會直接造成知識庫斷鏈。
   - *前置化改進*：在 Node 2 撰寫筆記前，應先產出「實體與概念清單（Taxonomy Dictionary）」，並強制只有收錄於清單中的實體才能建立 `[[wikilinks]]`，降低後續修補成本。
3. **時間標籤強隔離（Temporal Grounding）**：
   - *反思*：2024 年報告中常有「預計 2024 年底裝機、2025 年量產」等預測性字眼。當前時間點為 2026 年，若未刻意區分「2024 年時的規劃」與「2026 年當前現狀」，極易造成時間混淆。
   - *前置化改進*：所有牽涉建廠與市場預測之頁面，一律強制在 Frontmatter 與正文中標註 `data_classification: "Historical Data" | "Forecast" | "Roadmap Status"`。
