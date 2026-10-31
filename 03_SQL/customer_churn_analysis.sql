CREATE DATABASE customer_churn_db;
USE customer_churn_db;

CREATE TABLE customers (
    customerID VARCHAR(20) PRIMARY KEY,
    gender VARCHAR(10),
    SeniorCitizen INT,
    Partner VARCHAR(5),
    Dependents VARCHAR(5),
    tenure INT,
    PhoneService VARCHAR(5),
    MultipleLines VARCHAR(25),
    InternetService VARCHAR(20),
    OnlineSecurity VARCHAR(25),
    OnlineBackup VARCHAR(25),
    DeviceProtection VARCHAR(25),
    TechSupport VARCHAR(25),
    StreamingTV VARCHAR(25),
    StreamingMovies VARCHAR(25),
    Contract VARCHAR(20),
    PaperlessBilling VARCHAR(5),
    PaymentMethod VARCHAR(40),
    MonthlyCharges DECIMAL(10,2),
    TotalCharges DECIMAL(10,2),
    Churn VARCHAR(5)
);

SELECT COUNT(*) FROM customers;
SELECT * FROM customers;
SHOW TABLES;

DESCRIBE customers;
SELECT COUNT(*) AS total_records From customers;

SHOW VARIABLES LIKE 'local_infile';


SET GLOBAL local_infile = 1;

SELECT
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Churn_Rate_Percentage
FROM customers;

SELECT
    Contract,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Churn_Rate
FROM customers
GROUP BY Contract
ORDER BY Churn_Rate DESC;

SELECT
    PaymentMethod,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Churn_Rate
FROM customers
GROUP BY PaymentMethod
ORDER BY Churn_Rate DESC;

SELECT
    PaymentMethod,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Churn_Rate
FROM customers
GROUP BY PaymentMethod
ORDER BY Churn_Rate DESC;

SELECT
    CASE
        WHEN tenure <= 12 THEN 'New'
        WHEN tenure <= 36 THEN 'Medium-term'
        ELSE 'Long-term'
    END AS Tenure_Group,

    COUNT(*) AS Total_Customers,

    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS Churned_Customers,

    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers

GROUP BY Tenure_Group
ORDER BY Churn_Rate DESC;

SELECT
    CASE
        WHEN MonthlyCharges <= 35 THEN 'Low'
        WHEN MonthlyCharges <= 70 THEN 'Medium'
        ELSE 'High'
    END AS Charges_Group,

    COUNT(*) AS Total_Customers,

    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS Churned_Customers,

    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers

GROUP BY Charges_Group
ORDER BY Churn_Rate DESC;

SELECT
    CASE
        WHEN SeniorCitizen = 1 THEN 'Senior Citizen'
        ELSE 'Non-Senior Citizen'
    END AS Customer_Type,

    COUNT(*) AS Total_Customers,

    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS Churned_Customers,

    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers

GROUP BY SeniorCitizen
ORDER BY Churn_Rate DESC;

SELECT
    Partner,
    COUNT(*) AS Total_Customers,

    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS Churned_Customers,

    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers
GROUP BY Partner
ORDER BY Churn_Rate DESC;

SELECT
    Dependents,
    COUNT(*) AS Total_Customers,

    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS Churned_Customers,

    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers
GROUP BY Dependents
ORDER BY Churn_Rate DESC;

SELECT
    gender,
    COUNT(*) AS Total_Customers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS Churned_Customers,

    ROUND(
        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers

GROUP BY gender
ORDER BY Churn_Rate DESC;


SELECT
    OnlineSecurity,
    COUNT(*) AS Total_Customers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS Churned_Customers,

    ROUND(
        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers
GROUP BY OnlineSecurity
ORDER BY Churn_Rate DESC;

SELECT
    TechSupport,
    COUNT(*) AS Total_Customers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS Churned_Customers,

    ROUND(
        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers
GROUP BY TechSupport
ORDER BY Churn_Rate DESC;


SELECT
    PaperlessBilling,
    COUNT(*) AS Total_Customers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS Churned_Customers,

    ROUND(
        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers
GROUP BY PaperlessBilling
ORDER BY Churn_Rate DESC;


SELECT
    Churn,
    COUNT(*) AS Total_Customers,
    ROUND(AVG(MonthlyCharges), 2) AS Average_Monthly_Charges
FROM customers
GROUP BY Churn
ORDER BY Average_Monthly_Charges DESC;

SELECT
    Churn,
    COUNT(*) AS Total_Customers,
    ROUND(AVG(tenure), 2) AS Average_Tenure_Months
FROM customers
GROUP BY Churn
ORDER BY Average_Tenure_Months DESC;

SELECT
    Contract,
    InternetService,
    COUNT(*) AS Total_Customers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS Churned_Customers,

    ROUND(
        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers
GROUP BY Contract, InternetService
ORDER BY Churn_Rate DESC;

SELECT
    Contract,
    COUNT(*) AS Total_Customers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS Churned_Customers,

    ROUND(
        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers
GROUP BY Contract

HAVING Churn_Rate > 30

ORDER BY Churn_Rate DESC;

SELECT
    Contract,

    ROUND(
        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) * 100.0 / COUNT(*), 2
    ) AS Contract_Churn_Rate,

    (
        SELECT ROUND(
            SUM(CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END) * 100.0 / COUNT(*), 2
        )
        FROM customers
    ) AS Overall_Churn_Rate

FROM customers
GROUP BY Contract
ORDER BY Contract_Churn_Rate DESC;

WITH ContractAnalysis AS
(
    SELECT
        Contract,
        COUNT(*) AS Total_Customers,

        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) AS Churned_Customers,

        ROUND(
            SUM(CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END) * 100.0 / COUNT(*), 2
        ) AS Churn_Rate

    FROM customers
    GROUP BY Contract
)

SELECT *
FROM ContractAnalysis
ORDER BY Churn_Rate DESC;

WITH ContractAnalysis AS
(
    SELECT
        Contract,
        COUNT(*) AS Total_Customers,

        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) AS Churned_Customers,

        ROUND(
            SUM(CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END) * 100.0 / COUNT(*), 2
        ) AS Churn_Rate

    FROM customers
    GROUP BY Contract
)

SELECT
    Contract,
    Total_Customers,
    Churned_Customers,
    Churn_Rate,

    RANK() OVER (
        ORDER BY Churn_Rate DESC
    ) AS Churn_Rank

FROM ContractAnalysis;

 SELECT
    CASE
        WHEN tenure <= 12 THEN 'New'
        WHEN tenure <= 36 THEN 'Medium-term'
        ELSE 'Long-term'
    END AS Tenure_Group,

    PaymentMethod,

    COUNT(*) AS Total_Customers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS Churned_Customers,

    ROUND(
        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers

GROUP BY Tenure_Group, PaymentMethod

ORDER BY Churn_Rate DESC;


SELECT
    Churn,

    COUNT(*) AS Total_Customers,

    ROUND(
        SUM(MonthlyCharges), 2
    ) AS Total_Monthly_Revenue,

    ROUND(
        AVG(MonthlyCharges), 2
    ) AS Average_Monthly_Revenue_Per_Customer

FROM customers

GROUP BY Churn

ORDER BY Total_Monthly_Revenue DESC;

SELECT
    Churn,

    COUNT(*) AS Total_Customers,

    ROUND(
        SUM(TotalCharges), 2
    ) AS Total_Revenue,

    ROUND(
        AVG(TotalCharges), 2
    ) AS Average_Total_Charges

FROM customers

GROUP BY Churn

ORDER BY Total_Revenue DESC;

SELECT
    Contract,
    TechSupport,

    COUNT(*) AS Total_Customers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS Churned_Customers,

    ROUND(
        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) * 100.0 / COUNT(*), 2
    ) AS Churn_Rate

FROM customers

GROUP BY Contract, TechSupport

HAVING COUNT(*) >= 50

ORDER BY Churn_Rate DESC;


WITH ChurnRiskAnalysis AS
(
    SELECT
        Contract,
        InternetService,
        TechSupport,

        COUNT(*) AS Total_Customers,

        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) AS Churned_Customers,

        ROUND(
            SUM(CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END) * 100.0 / COUNT(*), 2
        ) AS Churn_Rate

    FROM customers

    GROUP BY
        Contract,
        InternetService,
        TechSupport

    HAVING COUNT(*) >= 50
)

SELECT
    *,
    RANK() OVER (
        ORDER BY Churn_Rate DESC
    ) AS Risk_Rank

FROM ChurnRiskAnalysis

ORDER BY Risk_Rank;

SELECT
    COUNT(*) AS Total_Customers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS Churned_Customers,

    SUM(CASE
        WHEN Churn = 'No' THEN 1
        ELSE 0
    END) AS Retained_Customers,

    ROUND(
        SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) * 100.0 / COUNT(*), 2
    ) AS Churn_Rate,

    ROUND(
        SUM(CASE
            WHEN Churn = 'No' THEN 1
            ELSE 0
        END) * 100.0 / COUNT(*), 2
    ) AS Retention_Rate

FROM customers;