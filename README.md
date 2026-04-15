## 📊 Power BI Dashboard

### Executive Summary

![Executive Summary] <img width="1511" height="857" alt="Executive Summery" src="https://github.com/user-attachments/assets/84db21e8-4462-44a3-8d6c-c2fed030583e" />


---

### Product Analysis

![Product Analysis] <img width="1461" height="880" alt="Product Analysis Dashboard" src="https://github.com/user-attachments/assets/68a03d8c-34a5-40a5-96b1-9bd26a8524d6" />


---

### Region Analysis

![Region Analysis] <img width="1469" height="882" alt="Region Analysis Dashboard" src="https://github.com/user-attachments/assets/fcadad7b-f5df-4b28-9771-452da697fb53" />
# 📊 Sales Data EDA & Forecast Automation Project

## 📌 Project Overview

This project is an **end-to-end automated sales data analysis pipeline** built using Python.
It performs **data cleaning, exploratory data analysis (EDA), statistical analysis, trend analysis, forecasting, and automated PDF reporting**.

The main objective of this project is to **transform messy raw sales data into meaningful business insights and visual reports** that help decision-making.

---

# 🎯 Project Objectives

* Automate sales data cleaning
* Perform exploratory data analysis (EDA)
* Generate statistical insights
* Detect outliers and trends
* Forecast future sales
* Create automated PDF business reports
* Build Power BI dashboard for visualization

---

## 🛠 Tools & Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- ReportLab
- Jupyter Notebook
- Power BI

---

# 📁 Project Structure

```
Sales-Data-EDA-Automation/

│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_analysis.ipynb
│   ├── 03_statistical_analysis.ipynb
│   ├── 04_dashboard_export.ipynb
│
├── scripts/
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── sales_analysis.py
│   ├── report_generator.py
│   ├── utils.py
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── processed/
│
├── reports/
│   ├── FINAL_REPORT.pdf
│   ├── kpi_summary.csv
│   ├── summary_report.csv
│   ├── outliers_report.csv
│   ├── order_id_distribution.png
│   ├── sales_distribution.png
│   ├── profit_distribution.png
│   ├── quantity_distribution.png
│   ├── region_sales.png
│   ├── trend_analysis.png
│   ├── sales_forecast.png
│   ├── correlation.png
│
├── dashboard/
│   ├── sales_dashboard.pbix
│   ├── dashboard_page1.png
│   ├── dashboard_page2.png
│
├── requirements.txt
├── README.md
└── main.py
```

---

## 🔄 Project Workflow

Raw Data → Data Cleaning → Exploratory Data Analysis → Statistical Analysis → Forecasting → Report Generation → Power BI Dashboard

1. Raw sales data is loaded
2. Data cleaning removes nulls and inconsistencies
3. EDA generates visual insights
4. Statistical analysis calculates distributions and correlations
5. Forecasting predicts future sales trends
6. Reports are exported automatically
7. Cleaned data is used in Power BI dashboards


# 🧹 Data Cleaning Features

The cleaning module performs:

* Remove duplicate records
* Handle missing values (NaN)
* Standardize column names
* Fix inconsistent date formats
* Trim text values
* Handle outliers
* Convert data types properly

Output:

```
cleaned_sales_data.csv
```

---

# 📊 Exploratory Data Analysis (EDA)

EDA helps understand business performance through visualizations:

Generated Reports:

* Sales Trend Analysis
* Region-wise Sales
* Top Product Analysis
* Correlation Heatmap
* Summary Statistics Report

---

# 📈 Statistical Analysis Features

The statistical module generates:

* KPI Summary
* Sales Distribution
* Profit Distribution
* Quantity Distribution
* Outlier Detection
* Trend Analysis
* Sales Forecasting

---

# 📌 Key Performance Indicators (KPIs)

The project calculates:

* Total Sales
* Total Profit
* Profit Margin (%)
* Average Order Value
* Average Quantity

These metrics help evaluate **overall business performance**.

---

# 🔮 Sales Forecasting

Sales forecasting is performed using:

**Moving Average Method**

Features:

* Monthly Sales Aggregation
* Trend Smoothing
* Future Sales Prediction

This helps in:

* Inventory Planning
* Demand Forecasting
* Business Planning

---

# 📄 Automated PDF Reporting

The system generates:

```
FINAL_REPORT.pdf
```

Which includes:

* Executive Summary
* KPI Summary
* Statistical Insights
* Trend Analysis
* Forecast Visualizations
* Business Recommendations

This makes reporting **fully automated**.

---

# 📊 Power BI Dashboard

The dashboard visualizes:

* Sales KPIs
* Sales Trends
* Profit Analysis
* Regional Performance
* Forecast Insights

Dashboard outputs are stored in:

```
dashboard/
```

---

# 🚀 How to Run This Project

## Step 1 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 2 — Run Data Cleaning

```bash
python main.py
```

This will:

* Clean raw data
* Generate analysis
* Create reports
* Produce final PDF

---

# 📊 Sample Outputs

Generated outputs include:

* KPI Summary Table
* Distribution Charts
* Forecast Visualizations
* Correlation Heatmap
* Final PDF Report

All reports are stored in:

```
reports/
```

---
## 📊 Business Questions Answered

This project was designed to answer key business questions using data analytics and visualization.

---

## 📌 Page 1 — Executive Summary Dashboard

Key business questions:

1. What is the total sales performance over time?
2. What is the total profit and profit margin?
3. Which regions contribute most to revenue?
4. How do sales trends change across months and years?
5. Are there any noticeable seasonal patterns in sales?
6. What is the overall business growth trend?

---

## 📌 Page 2 — Product Analysis Dashboard

Key business questions:

1. Which products generate the highest sales?
2. Which products generate the highest profit?
3. Which product categories have the best performance?
4. Are there products with high sales but low profit?
5. What is the quantity distribution across products?
6. Which products should be promoted or discontinued?

---

## 📌 Page 3 — Region Analysis Dashboard

Key business questions:

1. Which region contributes the highest revenue?
2. Which region has the highest profitability?
3. How do sales vary across different regions?
4. Are there underperforming regions?
5. Which regions show strong growth potential?
6. Where should marketing efforts be focused?



# 📌 Business Value of This Project

This project demonstrates:

* Data Cleaning Automation
* Exploratory Data Analysis
* Statistical Thinking
* Business Insight Generation
* Forecast Modeling
* Report Automation

## 📈 Key Insights

• Sales show a consistent upward trend across months.
• Certain products contribute significantly higher revenue.
• Some products show high sales but low profit margins.
• Regional sales vary significantly across locations.
• Forecasting indicates stable future sales trends.
• Outlier detection helped identify unusual transactions.

.
## 🚀 Project Features

• Automated data cleaning pipeline
• Automated EDA visualization generation
• Statistical analysis and correlation detection
• Sales forecasting using moving average
• PDF report generation using Python
• Integration with Power BI dashboards
• End-to-end automation workflow


---

# 🎯 Future Enhancements

Possible improvements:

* ARIMA Forecasting
* Machine Learning Models
* Interactive Dashboard
* Real-time Data Pipeline
* Advanced Statistical Modeling

---

# 👤 Author

**Name:** (Debolina Sorkhel)
**Role:** Data Analyst Enthusiast
**Project Type:** End-to-End Sales Data Analysis Automation

---
