---
title: "碳化矽與傳統矽之性能全面對比（SiC vs. Si Properties）"
category: "concepts"
tags: ["comparison", "silicon", "sic", "material-properties"]
sources:
  - id: "SRC-01"
    name: "MDPI Materials Review Paper (2024)"
last_updated: "2026-11-18"
data_classification: "Technical Fundamentals"
---

# 碳化矽與傳統矽之性能全面對比（SiC vs. Si Properties）

半導體材料的性能由其晶格結構與化學鍵能決定。矽（Silicon, Si）具備金剛石晶體結構，而碳化矽（Silicon Carbide, SiC）由碳原子與矽原子以強大的共價鍵（$sp^3$ 混成軌域）結合而成。

在常見的 200 多種多型體中，**4H-SiC** 兼具對稱性與載子傳輸特性，成為功率半導體應用的核心材料。

---

## 1. 物理參數基準對照表

本表數據採自 MDPI 開源期刊文獻（出處：`SRC-01`）：

| 物理參數指標 | 傳統矽（Si） | 碳化矽（4H-SiC） | 效能差異（SiC vs. Si） | 系統工程效益 |
| :--- | :---: | :---: | :---: | :--- |
| **能隙能量 ($E_g$)** | 1.12 eV | **3.26 eV** | **~ 2.9 倍** | 漏電流極小、高溫穩定性佳 |
| **臨界崩潰電場 ($E_c$)** | 0.3 MV/cm | **3.0 MV/cm** | **~ 10 倍** | 漂移層可縮薄至 1/10，耐壓上限高 |
| **熱導率 ($k$)** | 1.5 W/cm·K | **4.9 W/cm·K** | **~ 3.3 倍** | 散熱能力極佳，允許縮小冷卻模組 |
| **飽和漂移速度 ($v_s$)** | $1.0 \times 10^7$ cm/s | **$2.0 \times 10^7$ cm/s** | **~ 2 倍** | 高頻切換、降低開關交越損耗 |
| **相對介電常數 ($\varepsilon_r$)** | 11.8 | **9.7** | **~ 0.82 倍** | 減小寄生電容，提升切換響應速度 |
| **最高理論工作結溫 ($T_j$, 材料本徵)** | ~ 150 °C | **> 300 °C**（商用元件額定通常為 150°C~175°C） | **材料極限提升 >150 °C** | 提供更高過溫容裕度，承受極端工作突波 |

---

## 2. 功率元件特性之核心差異

基於上述物理參數，SiC MOSFET 相較於矽基 IGBT（Insulated Gate Bipolar Transistor）與矽基 Super-Junction MOSFET 具有本質級的優勢：

### 2.1 導通損耗（Conduction Loss）
- 在 650V 以上高壓場合，傳統 Si 必須依賴雙極型（Bipolar）傳導機制（如 IGBT）注入少數載子以降低電阻，這會引入約 0.7V～1.5V 的門檻電壓降（Threshold Voltage Drop）。
- SiC 即使在 1200V 甚至 1700V 下，依然可採用多數載子導電的 [[device-structures-mosfet]] 架構，無起始導通壓降，在輕負載與中負載下導通損耗大幅下降 50%～70%。

### 2.2 開關損耗（Switching Loss）
- Si IGBT 在關斷時存在顯著的「拖尾電流（Tail Current）」，開關頻率通常被限制在 20 kHz 以下。
- SiC MOSFET 無少數載子儲存效應，關斷速度極快，開關頻率可推升至 100 kHz～500 kHz，開關損耗降低超過 70%。

### 2.3 系統級微型化（System Downsizing）
- 高切換頻率使得系統中的被動元件（電感、電容、變壓器等磁性元件）體積與重量大幅縮減 40%～60%。

---

## 3. 關聯知識頁面
- 技術原理：[[wide-bandgap-physics]]
- 元件架構：[[device-structures-mosfet]]
- 產業應用：[[ev-and-automotive-demand]]
- 成本考量：[[cost-breakdown-and-manufacturing]]
