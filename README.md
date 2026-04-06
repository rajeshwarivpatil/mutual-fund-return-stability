# 📊 Mutual Fund Return Stability Analysis
### *A Comprehensive Statistical Study of Asian Equity Funds (2003–2026)*

<div align="center">

![Banner](https://capsule-render.vercel.app/api?type=waving&color=0:003366,100:00D4FF&height=200&section=header&text=Mutual%20Fund%20Analysis&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Return%20Stability%20%7C%20Asian%20Equity%20Funds%20%7C%202003–2026&descAlignY=55&descAlign=50)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Scikit--learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)](https://chartjs.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

### 🎯 [View Live Dashboard](https://rajeshwarivpatil.github.io/mutual-fund-return-stability/templates/dashboard.html) &nbsp;|&nbsp; 📄 [Read Report](#-deliverables) &nbsp;|&nbsp; 📊 [See Results](#-key-findings)

---

</div>

---

## 🌟 Project Highlights

<div align="center">

| 📁 Dataset | 🕐 Period | 📈 Funds | 🔬 Methods |
|:---:|:---:|:---:|:---:|
| 5,615 daily returns | 2003 – 2026 | 3 Asian equity funds | 8 statistical techniques |
| 8,278 NAV records | 23 years | Fidelity · Matthews · Invesco | 12 visualisations |

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Funds Analysed](#-funds-analysed)
- [Analysis Steps](#-analysis-steps)
- [Key Findings](#-key-findings)
- [Dashboard Preview](#-dashboard-preview)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [Deliverables](#-deliverables)
- [Results Summary](#-results-summary)
- [Contact](#-contact)

---

## 🎯 About the Project

> This project performs a **complete 8-step statistical analysis** of three Asian equity mutual funds, covering everything from basic descriptive statistics to advanced linear algebra (PCA), probability theory (Bayes' theorem), and inferential statistics (ANOVA).

The analysis was implemented as an **interactive Flask web dashboard** with 7 tabbed sections and 12 embedded charts, all derived from real fund data spanning 23 years.

```
Dataset Coverage:  Nov 2003 → Feb 2026  (5,615 trading days)
NAV History:       Apr 1993 → Feb 2026  (8,278 price records)
Funds:             Fidelity Asia | Matthews Asia | Invesco Developing
```

---

## 💼 Funds Analysed

<div align="center">

| Fund | Strategy | Ann. Return | Volatility | Sharpe Ratio |
|:-----|:---------|:-----------:|:----------:|:------------:|
| 🔵 **Fidelity Asia** | Large-cap Asian equities | 15.69% | 21.68% | **0.723** ⭐ |
| 🟠 **Matthews Asia** | Pan-Asian quality bias | 11.45% | 19.25% | 0.595 |
| 🟢 **Invesco Developing** | Emerging Asia | 23.17% | 43.15% | 0.537 |

</div>

> ⭐ **Fidelity Asia** has the best **risk-adjusted performance** (highest Sharpe Ratio)

---

## 🔬 Analysis Steps

All **8 mandatory steps** were completed:

```
Step 1  ──  Data Understanding          Variable types, dataset preview, classification
Step 2  ──  Descriptive Statistics      Mean, median, variance, IQR, 5-number summary
Step 3  ──  Visualizations              12 charts: histograms, boxplot, heatmaps, PCA
Step 4  ──  Probability Analysis        P(+), conditional probability, Bayes' theorem
Step 5  ──  Inferential Statistics      95% CIs, t-tests, one-way ANOVA
Step 6  ──  Linear Algebra & PCA        Matrix form, eigendecomposition, 2D projection
Step 7  ──  Insight Generation          Patterns, risks, anomalies, opportunities
Step 8  ──  Final Deliverable           Report + Presentation + Dashboard
```

---

## 🏆 Key Findings

<table>
<tr>
<td width="50%">

### 📈 Performance
- **Best Sharpe Ratio**: Fidelity Asia → `0.723`
- **Highest Return**: Invesco Developing → `23.17%` p.a.
- **Most Stable**: Matthews Asia → Vol `19.25%`
- All 3 funds: **statistically significant** positive returns (t-test p < 0.05)

</td>
<td width="50%">

### 🧮 Statistical Results
- **ANOVA**: F=0.87, p=0.42 → No significant mean difference
- **PCA**: PC1 explains `71.53%` of total variance
- **Correlation**: Fidelity–Matthews r = `0.834` (over-correlated)
- **Bayes**: P(gain | market up) ≈ `90%` for all funds

</td>
</tr>
<tr>
<td width="50%">

### 📊 PCA Results
```
PC1  →  71.53%  (Asian market beta)
PC2  →  22.94%  (Invesco unique risk)
PC3  →   5.54%  (discarded)
────────────────────────────────
2 PCs retain  94.46%  of variance
```

</td>
<td width="50%">

### ⚠️ Risk Findings
- **Outliers**: 305–328 per fund (~5.7%)
- **Triggers**: GFC 2008 · COVID-19 2020 · Rate hikes 2022
- **Anomaly**: Invesco max return `+164.53%` (data anomaly)
- Fat-tailed distributions — **not normally distributed**

</td>
</tr>
</table>

---

## 🖥️ Dashboard Preview

> **Live Dashboard →** [Click here to open](https://rajeshwarivpatil.github.io/mutual-fund-return-stability/templates/dashboard.html)

The interactive dashboard includes **7 tabbed sections**:

| Tab | Content |
|-----|---------|
| `01 · Overview` | Data understanding, NAV trajectory chart, dataset preview |
| `02 · Descriptive Stats` | Full statistics table, annual returns, risk-return plot |
| `03 · Distributions` | Histograms, boxplot, scatter plots, stacked bar chart |
| `04 · Probability` | Bayes' theorem table, conditional probability chart |
| `05 · Inferential` | Confidence intervals, ANOVA results, t-test table |
| `06 · Linear Algebra & PCA` | Heatmaps, scree plot, 2D PCA projection |
| `07 · Insights` | 8 insight cards, radar chart, final conclusions |

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technologies |
|:---------|:------------|
| **Language** | Python 3.10+ |
| **Web Framework** | Flask |
| **Data Analysis** | Pandas, NumPy, SciPy |
| **Machine Learning** | Scikit-learn (PCA, StandardScaler) |
| **Visualisation** | Matplotlib, Seaborn, Chart.js |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Version Control** | Git, GitHub |

</div>

---

## 📁 Project Structure

```
mutual-fund-return-stability/
│
├── 📄 app.py                        # Flask web application (main entry point)
├── 📄 README.md                     # Project documentation
├── 📄 .gitignore                    # Git ignore rules
│
├── 📁 data/
│   ├── 📊 asian_funds_returns.csv   # 5,615 daily return observations
│   └── 📊 asian_funds_5yr.csv       # 8,278 NAV price records
│
├── 📁 src/
│   ├── 🐍 descriptive_stats.py      # Mean, median, variance, IQR
│   ├── 🐍 correlation_analysis.py   # Pearson correlation matrix
│   ├── 🐍 covariance_analysis.py    # Covariance matrix
│   ├── 🐍 anova_test.py             # One-way ANOVA test
│   ├── 🐍 returns_calculation.py    # Daily return calculations
│   └── 🐍 risk_return_plot.py       # Risk-return visualisation
│
├── 📁 templates/
│   └── 🌐 dashboard.html            # Interactive analytics dashboard
│
└── 📁 static/                       # CSS, JS, images
```

---

## 🚀 How to Run

### Prerequisites
Make sure you have **Python 3.10+** installed.

### Step 1 — Clone the Repository
```bash
git clone https://github.com/rajeshwarivpatil/mutual-fund-return-stability.git
cd mutual-fund-return-stability
```

### Step 2 — Install Dependencies
```bash
pip install flask pandas numpy scipy scikit-learn matplotlib seaborn
```

### Step 3 — Run the Application
```bash
python app.py
```

### Step 4 — Open in Browser
```
http://localhost:5000
```

> 💡 **No setup needed for the dashboard** — just open `templates/dashboard.html` directly in any browser for offline use.

---

## 📦 Deliverables

| Deliverable | Description | Format |
|:-----------|:-----------|:------:|
| 🌐 **Interactive Dashboard** | 7-tab Flask web app with 12 charts | Live Web |
| 📄 **IEEE-Format Report** | Complete 8-step statistical report | `.docx` |
| 📊 **Presentation** | 18-slide professional deck | `.pptx` |
| 🐍 **Python Scripts** | Modular analysis source code | `.py` |

---

## 📊 Results Summary

<div align="center">

```
╔══════════════════════════════════════════════════════════════════╗
║              STATISTICAL ANALYSIS SUMMARY                        ║
╠══════════════════════════════╦═══════════════════════════════════╣
║  t-test (all funds)          ║  p < 0.05  →  Returns > 0  ✓     ║
║  One-way ANOVA               ║  F=0.87, p=0.42  →  H₀ accepted  ║
║  Fidelity–Matthews corr.     ║  r = 0.834  →  Over-correlated    ║
║  PCA (2 components)          ║  94.46% variance retained         ║
║  Bayes P(gain | mkt up)      ║  ~90% for all three funds         ║
║  Best Sharpe Ratio           ║  Fidelity Asia  →  0.723          ║
╠══════════════════════════════╩═══════════════════════════════════╣
║  RECOMMENDATION: Fidelity (core 60%) + Invesco (satellite 25%)   ║
╚══════════════════════════════════════════════════════════════════╝
```

</div>

---

## 📚 References

1. Sharpe, W.F. (1994). *The Sharpe Ratio*. Journal of Portfolio Management.
2. Jolliffe, I.T. (2002). *Principal Component Analysis* (2nd ed.). Springer.
3. Fama, E.F. (1965). *The Behavior of Stock-Market Prices*. Journal of Business.
4. Pandas Documentation — https://pandas.pydata.org
5. Scikit-learn Documentation — https://scikit-learn.org

---

## 👩‍💻 Contact

<div align="center">

**Rajeshwari V Patil**

[![GitHub](https://img.shields.io/badge/GitHub-rajeshwarivpatil-181717?style=for-the-badge&logo=github)](https://github.com/rajeshwarivpatil)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/rajeshwarivpatil)

</div>

---

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:00D4FF,100:003366&height=100&section=footer)

*⭐ If you found this project helpful, please give it a star!*

</div>
