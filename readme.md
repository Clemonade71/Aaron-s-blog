#  March Madness Tournament Prediction Project

##  Overview
This project aims to **predict how far a team will advance** in March Madness using **machine learning and basketball analytics**. We gathered data via **web scraping (Wikipedia) and APIs (KenPom, Sports-Reference)** and applied **Lasso Regression** for feature selection.

---

##  Data Sources
###  **Web Scraped Data**
- **[Wikipedia NCAA Tournament Results](https://en.wikipedia.org/wiki/NCAA_Division_I_men%27s_basketball_tournament)**
  - Scraped **historical team performances** in the NCAA tournament.
  - Converted from **wide format** (years as columns) to **long format** (team-season data).

###  **APIs & External Data**
- **KenPom Efficiency Ratings** → Adjusted Tempo, Offensive/Defensive Ratings.
- **Sports-Reference CBB Data** → Shooting %, Turnover Rates, Free Throw Rates.
- **Merged all sources** to create a **comprehensive team dataset**.

 **All data was collected ethically from public sources**.

---

##  Installation & Setup
###  Requirements
- **Python 3.11+**
- **Libraries:** `pandas`, `numpy`, `sklearn`, `beautifulsoup4`, `requests`, `matplotlib`

###  Setup Instructions
1. **Clone this repository:**
   ```bash
   git clone https://github.com/YOUR-GITHUB-REPO
   cd march-madness-predictions
