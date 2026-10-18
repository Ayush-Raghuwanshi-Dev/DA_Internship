# Task 4: Exploratory Data Analysis (EDA) Guide

**Student:** Ayush | B.Tech CSE (IoT) | PIEMR, Indore  
**Assignment:** Week 6: Git, GitHub & Final Data Analytics Project  
**Weightage:** 15 Marks  

---

## 1. Objective & Analytical Framework
Exploratory Data Analysis (EDA) investigates the cleaned omnichannel retail dataset (1,492 transactions) to discover underlying statistical distributions, correlations, outliers, and commercial trends.

---

## 2. Statistical Techniques Implemented

### Central Tendency & Dispersion
- **Mean vs Median:** Compares parametric average with non-parametric median to detect skewness in transaction value and profit.
- **Standard Deviation & Variance:** Measures volatility and operational dispersion around the mean.
- **Skewness & Kurtosis:** Quantifies distributional asymmetry and heavy-tailed extreme basket sizes.

### Outlier Detection (Tukey's IQR Method)
$$\text{IQR} = Q_3 - Q_1$$
$$\text{Lower Bound} = Q_1 - 1.5 \times \text{IQR}$$
$$\text{Upper Bound} = Q_3 + 1.5 \times \text{IQR}$$
Any data point falling outside $[\text{Lower Bound}, \text{Upper Bound}]$ is flagged as an outlier. In retail analytics, high-value sales outliers represent bulk enterprise procurement rather than errors.

### Correlation Analysis (Pearson & Spearman)
Evaluates pairwise linear and rank correlation across `Sales_Amount`, `Profit`, `Discount_Rate`, `Quantity`, and `Delivery_Days`.

---

## 3. Key Findings & Insights
1. **Sales Skewness:** Sales amount exhibits a positive right skewness due to high-value enterprise technology bundles (laptops and 4K displays).
2. **Discount Destruction:** Correlation between `Discount_Rate` and `Profit` is negative; discounts exceeding 20% severely erode gross margin.
3. **Corporate Basket Economics:** Corporate clients purchase in larger multi-item quantities and show lower sensitivity to price promotions.
4. **Logistics Performance:** 85%+ of orders are delivered within 3 business days, maintaining a high operational fulfillment SLA.
