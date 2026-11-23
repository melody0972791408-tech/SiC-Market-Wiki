# Raw Source 01: MDPI Materials Review Paper

- **Source ID**: SRC-01
- **Title**: The Overview of Silicon Carbide Technology: Status, Challenges, Key Drivers, and Product Roadmap
- **Publisher**: MDPI (*Materials*, Volume 18, Issue 1, Article 12)
- **Authors**: Maciej Kamiński, Krystian Król, Norbert Kwietniewski, Marcin Myśliwiec, Mariusz Sochacki, Bartłomiej Stonio, Ryszard Kisiel, Agnieszka Martychowiec, Katarzyna Racka-Szmidt, Arkadiusz Werbowy, Jarosław Żelazko, Piotr Niedzielski, Jacek Szmidt, Andrzej Strójwąs
- **Publication Date**: 2024-12-24
- **Original URL**: https://doi.org/10.3390/ma18010012
- **Retrieved Date**: 2026-11-18
- **Accessible Content**: Full Open-Access Paper (Creative Commons CC BY 4.0)
- **Data Classification**: Technical & Material Fundamentals / Physical Principles

---

## 1. 核心材料物理性質比較（Physical & Electrical Properties）

論文對比了傳統矽（Silicon, Si）、4H 碳化矽（4H-Silicon Carbide, 4H-SiC）及氮化鎵（Gallium Nitride, GaN）之物理材料特性：

| 物理參數（Property） | 矽（Si） | 4H 碳化矽（4H-SiC） | 氮化鎵（GaN） | 4H-SiC 相對 Si 之倍數優勢 |
| :--- | :--- | :--- | :--- | :--- |
| **能隙寬度（Bandgap Energy, $E_g$）[eV]** | 1.12 | **3.26** | 3.4 | 約 **3 倍**（Wide Bandgap 寬能隙） |
| **臨界擊穿電場（Critical Electric Field, $E_c$）[MV/cm]** | 0.3 | **3.0** | 3.3 | 約 **10 倍**（高耐壓、允許極薄漂移層） |
| **熱導率（Thermal Conductivity, $k$）[W/cm·K]** | 1.5 | **4.9** | 1.3 | 超過 **3 倍**（極佳散熱、耐高溫運行） |
| **飽和電子漂移速度（Electron Saturation Velocity, $v_s$）[$10^7$ cm/s]** | 1.0 | **2.0** | 2.5 | 約 **2 倍**（支援高頻切換） |
| **介電常數（Relative Dielectric Constant, $\varepsilon_r$）** | 11.8 | **9.7** | 9.0 | 稍低（有利於降低寄生電容） |
| **最高理論工作結溫（Maximum Junction Temp, $T_{j,\max}$）[°C]** | 150 | **> 300** | ~200 | 耐高溫能力大幅提升 |

---

## 2. 功率元件結構與製程關鍵技術（Manufacturing & Structures）

### 2.1 晶體結構與長晶挑戰
- **4H-SiC 多型體（Polytype）**：在眾多 SiC 結構中，4H-SiC 因具備高載子遷移率與各向同性較佳之特性，成為功率半導體（MOSFET 與 SBD）的首選晶相。
- **長晶技術（Crystal Growth）**：主要採用物理氣相傳輸法（Physical Vapor Transport, PVT）。生長溫度高達 2000°C～2400°C，晶體生長速度極為緩慢（每小時僅數毫米），且極易產生結晶缺陷（如微管缺陷 Micropipes、基面位錯 Basal Plane Dislocations, BPD 與螺位錯 Threading Screw Dislocations, TSD）。

### 2.2 元件架構演進
- **Planar MOSFET（平面閘極）**：製程成熟，可靠度高，但 JFET 區域電阻較大，比導通電阻（Specific On-Resistance, $R_{DS(on)} \cdot A$）較難進一步降低。
- **Trench MOSFET（溝槽閘極）**：透過在晶圓表面蝕刻垂直溝槽，大幅縮減單元間距並消除 JFET 區，顯著降低導通損耗。然而溝槽底部轉角處電場集中，對閘極氧化層（Gate Oxide, $\text{SiO}_2$）的耐壓可靠性要求極高。

### 2.3 核心製造挑戰
1. **離子植入與超高溫退火**：SiC 中雜質擴散係數極低，無法使用傳統熱擴散製程，必須使用高能離子植入（Ion Implantation），隨後需在 1600°C～1800°C 下進行晶格修復與活化退火。
2. **SiC/$\text{SiO}_2$ 界面態密度（Interface Trap Density, $D_{it}$）**：氧化層與 SiC 交界處存在較高界面缺陷，導致電子遷移率下降，需透過一氧化氮（NO/$\text{N}_2\text{O}$）退火鈍化。

---

## 3. 主要應用領域與市場推動力（Key Drivers）

論文明確指出 SiC 功率元件的主要驅動市場：
1. **電動車牽引逆變器（BEV Traction Inverter）**：
   - 傳統 400V 系統轉向 800V 高壓架構，SiC 能將系統損耗降低 5%～10%，延長續航里程並縮減散熱模組體積。
2. **車載充電機（OBC）與直流快充樁（DC Fast Charging Stations）**：
   - 實現高功率密度（$>3\text{ kW/L}$）與高頻化切換，大幅縮短充電時間。
3. **太陽能光電與儲能逆變器（Solar PV & ESS Inverters）**：
   - 轉換效率突破 99%，在 1500V 直流電壓架構下大幅縮減磁性元件體積。
4. **高壓工業馬達與智慧電網（Industrial Motor Drives & Smart Grid）**：
   - 取代傳統 Si IGBT，提供更高系統可靠性與能源節約。
