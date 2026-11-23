# SiC Power Semiconductor Market — LLM Wiki & Presentation System

> **Generative AI Course Project**  
> 主題：Understanding the SiC Market — From Technology to Market Dynamics  
> 核心理念：基於 Andrej Karpathy 的 LLM Wiki 概念（Sources are sacred, Notes are living, Links are knowledge）建置檔案式結構化知識庫，並透過 6 階段 Graph 工作流程產出面向初學者的教學簡報。

---

## 專案核心目標

1. **結構化知識庫（LLM Wiki）**：
   - 匯入 5 篇以上不同類型的權威公開文獻（學術期刊、產業研調、企業 10-K 年報）。
   - 採原子化 Markdown 筆記、YAML Frontmatter 元資料與 `[[wikilinks]]` 雙向連結。
   - 明確區分 **歷史數據（Historical Data）**、**預測數據（Forecast）** 與 **產業現況（Current Status）**，嚴禁虛構。
2. **初學者教學簡報（Reveal.js HTML Presentation）**：
   - 以 Wiki 知識庫為唯一事實來源，製作 8 頁循序漸進的教學型 HTML 簡報。
   - 提供演講者備忘稿（Speaker Notes）與完整出處對應。
3. **Graph 工作流程與自律執行紀錄**：
   - 定義 6 個明確節點（Ingest $\rightarrow$ Build/Query $\rightarrow$ Outline $\rightarrow$ Verify $\rightarrow$ Generate HTML $\rightarrow$ Evaluate）。
   - 設有 Human-in-the-loop (HITL) 審核點與最多 3 次自動修復機制。
   - 真實記錄於 `workflow/execution_log.md`。

---

## 目錄結構導覽

```text
SiC-Market-Wiki/
├── AGENTS.md                       # AI Agent 工作規範與 6 階段 Graph 流程定義
├── README.md                       # 專案總覽與使用說明文件
├── data/
│   ├── raw/                        # 原始資料存證庫（不可篡改原始文字）
│   │   ├── source_01_mdpi_sic_technology_overview.md
│   │   ├── source_02_trendforce_2023_market_share.md
│   │   ├── source_03_yole_power_sic_2024.md
│   │   ├── source_04_trendforce_8inch_fab_breakthrough.md
│   │   └── source_05_wolfspeed_2024_annual_report.md
│   └── metadata.json               # 5 篇文獻之標準化元資料登錄表
├── wiki/                           # Karpathy 風格原子化 Markdown 知識庫
│   ├── INDEX.md                    # 知識庫總導覽與主題分類樹
│   ├── concepts/                   # SiC 核心物理原理與技術優勢
│   │   ├── wide-bandgap-physics.md
│   │   ├── sic-vs-si-properties.md
│   │   └── device-structures-mosfet.md
│   ├── market/                     # 市場需求、應用與規模預測
│   │   ├── market-size-and-growth.md
│   │   ├── ev-and-automotive-demand.md
│   │   └── industrial-and-renewable-energy.md
│   ├── supply-chain/               # 製造流程、長晶磊晶與晶圓升級
│   │   ├── substrate-and-epitaxy.md
│   │   ├── 8-inch-wafer-transition.md
│   │   └── cost-breakdown-and-manufacturing.md
│   ├── entities/                   # 主要競爭者與生態系廠商
│   │   ├── stmicroelectronics.md
│   │   ├── onsemi.md
│   │   ├── wolfspeed.md
│   │   ├── infineon.md
│   │   └── chinese-suppliers.md
│   └── outlook/                    # 未來機會、挑戰與風險
│       ├── future-opportunities.md
│       └── challenges-and-risks.md
├── workflow/                       # Graph 工作流程、驗證腳本與執行日誌
│   ├── graph_spec.md               # 節點詳細輸入輸出與驗收條件規格
│   ├── verify_wiki.py              # Wiki 完整性、斷鏈與元資料自動檢查腳本
│   └── execution_log.md            # 節點執行歷程、真實錯誤與反思日誌
├── presentation/                   # 教學簡報原始檔
│   └── index.html                  # Reveal.js 教學簡報
└── docs/                           # GitHub Pages 發布目錄
    ├── index.html                  # 簡報網站首頁（自包含 + CDN 載入）
    └── .nojekyll                   # 繞過 Jekyll 靜態建置處理
```

---

## 快速開始與驗證

### 1. 檢驗 Wiki 知識庫完整性
```bash
python3 workflow/verify_wiki.py
```

### 2. 檢驗 Reveal.js 簡報品質與事實核查合規
```bash
python3 workflow/verify_presentation.py
```

### 3. 檢驗 GitHub Pages 發布目錄（docs/）
```bash
python3 workflow/verify_docs.py
```

---

## GitHub Pages 部署指引

本專案已將發布檔案準備於 `docs/` 目錄中，並配置 `.nojekyll` 避免靜態處理器干擾。
若要開啟 GitHub Pages：
1. 將專案推送到您的 GitHub 儲存庫。
2. 進入該 Repo 的 **Settings** $\rightarrow$ **Pages**。
3. 在 **Build and deployment** 下的 **Source** 選擇 **Deploy from a branch**。
4. 在 **Branch** 選取 `main`（或 `master`），資料夾下拉選單選擇 `/docs`，點擊 **Save**。
5. 稍候 1～2 分鐘即可於 `https://<帳號>.github.io/<Repo名>/` 線上瀏覽簡報。
