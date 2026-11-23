---
title: "碳化矽功率元件結構：Planar 與 Trench MOSFET（Device Structures）"
category: "concepts"
tags: ["mosfet", "planar", "trench", "device-structure", "manufacturing"]
sources:
  - id: "SRC-01"
    name: "MDPI Materials Review Paper (2024)"
last_updated: "2026-11-18"
data_classification: "Technical Fundamentals"
---

# 碳化矽功率元件結構：Planar 與 Trench MOSFET（Device Structures）

碳化矽功率元件的核心是 **金屬-氧化物-半導體場效電晶體（MOSFET）**。與二極體（如 SBD）相比，MOSFET 作為三端可控開關，控制著逆變器與變流器的電能流向。

目前產業主流分為兩大元件架構：**平面型（Planar MOSFET）** 與 **溝槽型（Trench MOSFET）**。

---

## 1. 平面閘極結構（Planar Gate MOSFET）

### 1.1 結構特性
- 閘極氧化層與導電通道完全水平分佈在晶圓表面。
- 透過離子植入形成 P-Well 與 N+ 區域，電流先水平穿過通道，再垂直向下流經 JFET 區與漂移層（Drift Layer）。

### 1.2 優點與挑戰
- **優點**：製程相對成熟，閘極氧化層可靠度高，電場分佈均勻，抗雪崩擊穿能力強。
- **缺點**：存在 JFET 區域電阻，單元尺寸較難縮減，使得比導通電阻（$R_{DS(on)} \cdot A$）存在物理下限。
- **代表代表廠商**：[[wolfspeed]] 與 [[onsemi]] 早期主要世代元件均採用高度優化之平面架構。

---

## 2. 溝槽閘極結構（Trench Gate MOSFET）

### 2.1 結構特性
- 利用反應離子蝕刻（RIE）在晶圓表面垂直蝕刻微米級溝槽，將閘極氧化層與多晶矽閘極深埋於溝槽內。
- 導電通道分佈於溝槽側壁，電流沿側壁垂直向下流動，徹底消除了 JFET 區域。

### 2.2 優點與挑戰
- **優點**：
  - 單元單元間距（Cell Pitch）縮減超過 40%，$R_{DS(on)} \cdot A$ 降低 30%～50%。
  - 在相同導通電阻規格下，晶片面積大幅縮減，提升每片晶圓的有效晶粒產出。
- **挑戰**：
  - **溝槽轉角電場集中**：由於 SiC 臨界擊穿電場極高，在溝槽底部的二氧化矽（$\text{SiO}_2$）轉角處極易承受超過 $3\text{ MV/cm}$ 的極限電場，導致閘極氧化層早期擊穿老化。
  - 需要極其精密之 P 型底部屏蔽層（Bottom P-Shield）以保護氧化層。
- **代表代表廠商**：羅姆（[[rohm]] 雙溝槽架構）、[[infineon]]（CoolSiC 半溝槽非對稱架構）、[[stmicroelectronics]] 最新一代架構。

---

## 3. 關鍵製程難點（出處：`SRC-01`）

1. **離子植入與超高溫退火**：
   - 由於 SiC 莫氏硬度與共價鍵極強，熱擴散無法滲入摻雜離子，必須使用高能量（MeV 等級）離子注入機。
   - 注入後晶格破壞嚴重，需在 $1600^\circ\text{C}\sim 1800^\circ\text{C}$ 高溫退火爐中完成晶格修復與原子活化。
2. **$\text{SiC/SiO}_2$ 界面態鈍化**：
   - SiC 熱氧化生長過程中殘留之碳原子團簇（Carbon Clusters）會形成嚴重的界面缺陷陷阱（$D_{it}$），造成電子遷移率陡降。現今產業界普遍使用 NO 或 $\text{N}_2\text{O}$ 氣氛高溫退火進行氮化鈍化。

---

## 4. 關聯知識頁面
- 材料物理基礎：[[wide-bandgap-physics]]
- 晶圓與基板挑戰：[[substrate-and-epitaxy]]
- 晶圓尺寸轉變：[[8-inch-wafer-transition]]
- 成本結構分析：[[cost-breakdown-and-manufacturing]]
