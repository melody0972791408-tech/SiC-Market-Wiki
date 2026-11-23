---
title: "碳化矽長晶、基板與磊晶製程（Substrate and Epitaxy）"
category: "supply-chain"
tags: ["substrate", "epitaxy", "pvt", "crystal-growth", "defects", "kerf-loss"]
sources:
  - id: "SRC-01"
    name: "MDPI Materials Review Paper (2024)"
  - id: "SRC-04"
    name: "TrendForce 8-Inch SiC Fab Breakthrough Analysis (2024-03)"
  - id: "SRC-05"
    name: "Wolfspeed FY2024 Annual Report (2024-08)"
last_updated: "2026-11-18"
data_classification: "Technical & Supply Chain Fundamentals"
---

# 碳化矽長晶、基板與磊晶製程（Substrate and Epitaxy）

在整個半導體產業鏈中，碳化矽（SiC）的製造難度與成本分佈與傳統矽（Si）存在極大差異。

傳統矽晶圓的長晶（柴可拉斯基法 / Czochralski法）已能拉出直徑 300mm（12 吋）、長度超過 2 公尺的高純度單晶矽棒。然而，碳化矽因在高溫下不具備液態相（常壓下直接昇華），長晶製造極其艱鉅。

---

## 1. 產業鏈成本分佈重心：基板佔比近半

根據 TrendForce 研調數據（出處：`SRC-04`）：
- **基板材料（Substrate）成本佔整體功率元件總製造成本高達 45%～50%**。
- 磊晶層（Epitaxy）佔約 15%～20%。
- 前段晶圓晶片加工（Wafer Fab Front-end）與後段封裝測試（Packaging & Test）各佔約 20%～25% 與 15%。
- **結論**：誰掌控了高良率、低成本的基板長晶能力，誰就握有 SiC 產業鏈的成本話語權。

---

## 2. 核心製造工藝環節剖析

```mermaid
flowchart LR
    Powder[高純度 SiC 原料粉末] --> PVT[高溫昇華長晶 PVT<br/>2000~2400°C 緩慢沉積]
    PVT --> Ingot[SiC 單晶錠 Ingot]
    Ingot --> Slicing[高精度切割 Slicing<br/>金剛石線割 / 雷射冷剝離]
    Slicing --> Wafer[晶圓基板 Substrate<br/>研磨與拋光 CMP]
    Wafer --> Epi[CVD 化學氣相磊晶 Epitaxy<br/>生長微米級無缺陷漂移層]
    Epi --> Fab[晶圓前段製造 Fab]
```

### 2.1 物理氣相傳輸法長晶（PVT: Physical Vapor Transport）
- **環境極端**：將高純度碳化矽粉料置於石墨坩堝底部，在 **2000°C～2400°C** 高溫與極低真空氬氣分壓下使粉料昇華為氣相分子（$\text{Si}, \text{Si}_2\text{C}, \text{SiC}_2$）。
- **長晶緩慢**：氣相分子在頂部低溫區的 4H-SiC 籽晶（Seed）上凝結結晶。生長速度僅有每小時 **0.1～1.0 毫米**（矽長晶為數十公分/小時），生長一個僅有幾公分厚的晶錠（Ingot）需耗時一週以上。
- **結晶缺陷（Defects）**：
  - 微管缺陷（Micropipes）：穿透性空洞，直接導致元件漏電致死。
  - 基面位錯（Basal Plane Dislocations, BPD）：通電後會演化為堆疊層錯（Stacking Faults），導致元件電阻隨時間增大（雙極退化效應）。
  - 螺位錯與刃位錯（TSD / TED）。

### 2.2 晶圓切割與研磨拋光（Slicing & CMP）
- **極高硬度挑戰**：SiC 莫氏硬度高達 9.5（僅次於鑽石），材料極脆。
- **切割損耗（Kerf Loss）**：使用傳統多線鑽石鋸切割時，每切一片晶圓，就有與晶圓厚度相當（約 300～400 微米）的晶錠材料被磨成粉末廢料，損耗率高達 **35%～45%**（出處：`SRC-04`）。
- **雷射冷剝離（Laser Cold Split）**：新興技術利用超快皮秒雷射在內部聚焦形成改質層，再藉由機械應力剝離，可將單個晶錠切出的晶圓數量提升 30% 以上。

### 2.3 磊晶生長（CVD Epitaxy）
- 原生基板內部缺陷過多且電阻率極低，不能直接用來製作電晶體結構。
- 必須透過化學氣相沉積（CVD）在拋光基板上生長一層厚度數微米至數十微米、摻雜濃度嚴格控制的單晶漂移層（Drift Layer）。
- 耐壓 1200V 元件通常需要約 10 微米厚度的磊晶層；電壓越高，要求磊晶層越厚且摻雜越均勻。

---

## 3. 全球競爭態勢與自給率戰略
- **材料龍頭**：[[wolfspeed]] 長期為全球最大 SiC 原生基板供應商（出處：`SRC-02`, `SRC-05`）。
- **IDM 自給率提升**：[[onsemi]] 併購 GTAT 後自給率突破 50%；[[stmicroelectronics]] 於義大利 Catania 興建基板全製程工廠。
- **亞洲供應鏈崛起**：[[chinese-suppliers]]（天岳先進、天科合達）在 6 吋基板產能快速拉升，引發全球價格結構劇烈變動。

---

## 4. 關聯知識頁面
- 技術優勢來源：[[wide-bandgap-physics]]
- 晶圓尺寸轉折：[[8-inch-wafer-transition]]
- 成本結構分析：[[cost-breakdown-and-manufacturing]]
- 龍頭營運指標：[[wolfspeed]], [[stmicroelectronics]], [[onsemi]]
