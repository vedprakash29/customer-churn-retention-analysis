
Customer Churn & Retention Analysis

📌 Project Overview

An end-to-end Data Analytics portfolio project focused on analyzing customer churn and retention patterns in a telecommunications company.

The project explores customer behavior, service usage, contract types, payment methods, customer tenure, and monthly charges to identify high-churn customer segments and potential revenue exposure.

Using Python, MySQL, Microsoft Excel, and Power BI, this project transforms raw customer data into meaningful business insights through data cleaning, exploratory analysis, SQL queries, Excel reporting, and interactive dashboard development.

---

🎯 Business Objectives

The main objectives of this project are to:

- Analyze overall customer churn and retention rates.
- Identify customer segments with higher churn rates.
- Understand the impact of contract types on customer retention.
- Analyze customer behavior across different payment methods.
- Examine the relationship between customer tenure and churn.
- Compare churn patterns across internet service categories.
- Analyze monthly charges and their relationship with customer churn.
- Identify potential revenue exposure associated with customer churn.
- Present key findings through Excel and Power BI dashboards.
- Generate actionable business insights to support customer retention strategies.

---

🛠️ Tools & Technologies

Tool| Purpose
Microsoft Excel| Data analysis, pivot tables, charts, and reporting
MySQL| SQL queries, aggregations, subqueries, and business analysis
Python| Data cleaning and exploratory data analysis
Pandas| Data manipulation, transformation, and analysis
Power BI| Data visualization, DAX measures, KPIs, and interactive dashboards
GitHub| Project documentation, code storage, and portfolio presentation

---

📊 Dataset Overview

The project uses the Telco Customer Churn dataset, which contains customer information, subscribed services, account details, and churn status.

Dataset Attribute| Details
Industry| Telecommunications
Total Customer Records| 7,043
Original Features| 21
Cleaned Dataset Features| 23
Target Variable| Churn
Churn Categories| Yes / No

The dataset contains customer demographics, tenure, contract information, internet services, payment methods, monthly charges, and total charges.

---

🧹 Data Cleaning & Preparation

Python and Pandas were used to inspect, clean, and prepare the original dataset.

Major activities included:

- Loading and inspecting the original CSV dataset.
- Checking dataset dimensions and column names.
- Identifying missing and blank values.
- Checking duplicate records.
- Reviewing data types and column consistency.
- Handling blank values in the TotalCharges column.
- Creating additional analytical columns.
- Creating customer tenure groups.
- Creating monthly charges groups.
- Exporting the cleaned dataset for further analysis.
- Validating the cleaned dataset before using it in SQL, Excel, and Power BI.

The original dataset was retained separately from the cleaned dataset.

---

🐍 Python Analysis

Python and Pandas were used for data cleaning, data validation, and exploratory data analysis.

Analysis Performed

- Dataset structure and shape analysis.
- Missing-value analysis.
- Duplicate-record analysis.
- Customer churn distribution.
- Churn and retention rate calculation.
- Customer segmentation by tenure.
- Customer segmentation by monthly charges.
- Analysis of customer demographics.
- Preparation of cleaned data for SQL, Excel, and Power BI.

The cleaned dataset and Python scripts are stored in the "02_Python" folder.

---

🗄️ SQL Analysis

MySQL was used to perform customer churn and retention analysis.

A total of 26 SQL queries were completed to explore customer behavior and identify high-risk customer segments.

SQL Concepts Used

- SELECT and DISTINCT
- WHERE and ORDER BY
- GROUP BY
- Aggregate Functions
- CASE WHEN
- HAVING
- Subqueries
- Common Table Expressions (CTEs)
- Window Functions
- RANK()

Business Analysis Performed

- Overall customer count and churn distribution.
- Churn rate by contract type.
- Churn rate by payment method.
- Churn analysis by internet service.
- Customer tenure group analysis.
- Monthly charges group analysis.
- Senior citizen churn analysis.
- Gender-based churn analysis.
- Customer retention analysis.
- Identification of high-churn customer segments.

The SQL analysis queries are stored in the "03_SQL" folder.

---

📈 Excel Analysis & Dashboard

Microsoft Excel was used to perform additional analysis and create an interactive reporting dashboard.

Excel Work Performed

- Data analysis using Pivot Tables.
- Customer churn and retention analysis.
- Contract-wise churn analysis.
- Payment-method analysis.
- Internet-service analysis.
- Tenure-group analysis.
- Monthly-charges analysis.
- Creation of Pivot Charts.
- Interactive slicers for filtering analysis.
- Preparation of a multi-sheet analytical report.

Excel Dashboard

"Customer Churn Excel Dashboard"
(06_Documentation/Customer_Churn_Excel_Dashboard1.png)

The Excel dashboard provides an interactive overview of customer churn patterns and supports exploration of different customer segments.

The Excel workbook is stored in the "04_Excel" folder.

---

📊 Power BI Dashboard

An interactive Power BI dashboard was developed to visualize customer churn and retention performance.

Power BI Dashboard


Dashboard Components

- Total Customers
- Churned Customers
- Retained Customers
- Overall Churn Rate
- Overall Retention Rate
- Customer Churn by Contract Type
- Churn Rate by Payment Method
- Churn Rate by Internet Service
- Churn Rate by Tenure Group
- Churn Rate by Monthly Charges Group
- Churned Customers by Senior Citizen
- Churned Customers by Gender

Interactive Slicers

- Contract
- Gender
- Internet Service
- Tenure Group

The dashboard helps explore customer churn patterns through interactive filters and visual comparisons.

The Power BI dashboard file is stored in the "05_Power_BI" folder.

---

🔑 Key KPIs & Findings

The following metrics were calculated from the cleaned customer dataset.

KPI| Result
Total Customers| 7,043
Churned Customers| 1,869
Retained Customers| 5,174
Overall Churn Rate| 26.54%
Overall Retention Rate| 73.46%

Customer Churn Distribution

- 26.54% of customers have churned.
- 73.46% of customers have been retained.
- The analysis indicates that customer retention is an important area for business improvement.

---

💡 Key Business Insights

Contract Analysis

- Month-to-month contract customers have a churn rate of approximately 42.71%.
- One-year contract customers have a churn rate of approximately 11.27%.
- Two-year contract customers have a churn rate of approximately 2.83%.
- Long-term contract customers show substantially lower churn rates.

Payment Method Analysis

- Electronic check users have a churn rate of approximately 45.29%.
- Electronic check customers represent an important segment for further retention analysis.

Internet Service Analysis

- Fiber optic customers have a churn rate of approximately 41.89%.
- DSL customers have a churn rate of approximately 18.96%.
- Customers without internet service have a churn rate of approximately 7.40%.

Customer Tenure Analysis

- New customers have the highest churn rate at approximately 47.44%.
- Medium-tenure customers have a churn rate of approximately 25.54%.
- Long-tenure customers have a churn rate of approximately 11.93%.

Monthly Charges Analysis

- Customers in the high monthly charges group have a churn rate of approximately 35.36%.
- Higher monthly charges are associated with increased customer churn in the analyzed dataset.

Customer Demographics

- Senior citizens have a churn rate of approximately 41.68%.
- Non-senior customers have a churn rate of approximately 23.61%.

Additional Service Insights

- Customers without Online Security and Tech Support show higher churn rates than customers subscribed to these services.

Business Interpretation: The findings suggest that new customers, month-to-month contract customers, electronic check users, and certain service segments deserve additional attention when designing customer retention strategies.

Note: These findings describe observed relationships in the dataset and do not establish causation.

---

📁 Project Structure

Customer-Churn-Retention-Analysis/
│
├── 01_Raw_Data/
│   └── Original Telco Customer Churn dataset
│
├── 02_Python/
│   ├── Python analysis scripts
│   └── Cleaned customer dataset
│
├── 03_SQL/
│   └── SQL analysis queries
│
├── 04_Excel/
│   └── Customer churn Excel analysis and dashboard
│
├── 05_Power_BI/
│   └── Customer churn Power BI dashboard (.pbix)
│
├── 06_Documentation/
│   ├── customer_churn_excel_dashboard.png
│   └── customer_churn_power_bi_dashboard.png
│
└── README.md

---

📈 Business Value

This project demonstrates how data analytics can help telecommunications businesses understand customer behavior and improve retention strategies.

Potential business applications include:

- Identifying customer segments with high churn risk.
- Improving customer retention strategies.
- Understanding the relationship between contracts and customer loyalty.
- Evaluating payment-method-related churn patterns.
- Identifying service categories associated with higher churn.
- Understanding customer behavior across different tenure groups.
- Supporting data-driven customer retention decisions.
- Monitoring key business metrics through interactive dashboards.

---

🚀 Future Enhancements

- Develop a customer churn prediction model using Machine Learning.
- Perform deeper customer segmentation.
- Build customer lifetime value analysis.
- Develop targeted customer retention recommendations.
- Explore automated dashboard refresh workflows.
- Create advanced customer risk scoring.
- Improve revenue exposure analysis using validated customer-level revenue metrics.

---

👨‍💻 Project Type

End-to-End Data Analytics Portfolio Project

Focus Areas: Business Intelligence | Customer Analytics | Churn Analysis | Data Cleaning | Excel | MySQL | Python | Pandas | Power BI | Data Visualization
