#  March Madness Predictions: Can Data Science Help Build a Championship Team?

##  Introduction: Can Analytics Predict NCAA Tournament Success?
March Madness is **one of the most unpredictable sporting events**, featuring legendary upsets, Cinderella stories, and shocking Final Four runs. But what if we could use **data science** to predict how far a team will go? 

This project focuses on building a dataset of **team efficiency metrics and tournament results** using **web scraping and APIs**. The goal is to develop **a predictive model** that identifies **which stats truly matter** for postseason success.

> **"Can advanced basketball metrics (Offensive Rating, Defensive Rating, Adjusted Tempo) predict how far a team will advance in March Madness?"**

---

##  Data Collection: Web Scraping & APIs

###  **Sources Used**
1. **[Wikipedia NCAA Tournament Results](https://en.wikipedia.org/wiki/NCAA_Division_I_men%27s_basketball_tournament) (Web Scraping)**
   - Used `BeautifulSoup` to scrape **historical tournament data**.
   - Transformed data from **wide format** (years as columns) to **long format** (one row per team-season).

2. **KenPom & Sports-Reference (APIs & Scraping)**
   - Extracted **team efficiency ratings, tempo, and shooting stats**.
   - Merged multiple sources to form a **unique dataset**.

###  **Steps to Collect & Clean Data**
- **Used `requests` and `BeautifulSoup`** to scrape Wikipedia **Results by Year**.
- **Merged historical tournament outcomes with advanced team metrics**.
- **Standardized team names** to ensure correct matching across sources.

**Ethics & Best Practices**
- Wikipedia permits **web scraping for research**.
- API data is **publicly available**, ensuring no terms of service violations.
- No private API keys were shared in the repo.

---

##  **Current Progress & Challenges**
###  **What I’ve Completed So Far**
 **Assembled a dataset combining team stats + tournament results**  
 **Successfully web scraped historical results from Wikipedia**  
 **Merged multiple sources while handling missing data**  

### **Challenges Encountered**
1. **Matching team names across datasets** (e.g., “Duke” vs. “Duke Blue Devils”).
2. **Handling missing values** in efficiency metrics.
3. **Choosing the best machine learning model for predictions.**

### **What I Expect to Find**
- **Are higher AdjEM teams more likely to advance?**  
- **Does 3-point shooting correlate with deep tournament runs?**  
- **Do slower-paced teams perform better in March Madness?**  

_(These questions will be answered in the next phase of analysis.)_

---

## **Next Steps**
### **What’s Coming Next?**
1. **Run Exploratory Data Analysis (EDA)** → Identify trends & correlations.
2. **Use Lasso Regression for feature selection** → Find the most important predictors.
3. **Run Monte Carlo simulations** → Predict **multiple tournament outcomes**.
4. **Visualize insights** → Build **charts, heatmaps, and matchup probabilities**.

---

## Links & Further Reading
-  **KenPom Advanced Basketball Metrics** → [kenpom.com](https://kenpom.com/)
-  **Sports-Reference CBB Data** → [sports-reference.com/cbb](https://www.sports-reference.com/cbb/)
-  **[Wikipedia NCAA Tournament History](https://en.wikipedia.org/wiki/NCAA_Division_I_men%27s_basketball_tournament)**
-  **[GitHub Repo with Code & Data](https://github.com/YOUR-GITHUB-REPO)**

---

##  Conclusion
While I don’t have **full analysis results yet**, this project lays the foundation for **data-driven March Madness predictions**. The next step is **identifying the most predictive stats** and running **simulations** to see if **we can predict tournament success**.

### **What do you think?**
What **other factors** do you think might impact tournament success? Drop a comment!
