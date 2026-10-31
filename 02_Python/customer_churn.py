import pandas as pd
print("Customer Churn Retention Analysis")
print("Pandas imported successfully")


print("Customer Churn Analysis Project")

file_path = "01_Raw_Data/Telco-Customer-Churn.csv"

df = pd.read_csv(file_path)

print("\nFirst 5 rows of dataset:")
print(df.head())


print("\nDataset Shape:")
print(df.shape)

print("\nTotal Rows and Columns:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nBlank Values in TotalCharges:")
print(df["TotalCharges"].str.strip().eq("").sum())

print("\nTotalCharges Data Type:")
print(df["TotalCharges"].dtype)

print("\nCustomers with Blank TotalCharges:")

blank_rows = df[df["TotalCharges"].str.strip() == ""]

print(blank_rows[["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Churn"]])

# Convert TotalCharges into numeric format

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Replace missing TotalCharges with 0

df["TotalCharges"] = df["TotalCharges"].fillna(0)

print("\nTotalCharges Data Type After Cleaning:")
print(df["TotalCharges"].dtype)

print("\nMissing Values After Cleaning:")
print(df["TotalCharges"].isnull().sum())

print("\nTotalCharges of First 5 Customers:")
print(df["TotalCharges"].head())

print("\nFinal Dataset Information:")
df.info()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum().sum())

print("\nDuplicate Records After Cleaning:")
print(df.duplicated().sum())

print("\nFinal Dataset Shape:")
print(df.shape)

# Overall Customer Churn Analysis

print("\n--- Overall Customer Churn Analysis ---")

total_customers = df["customerID"].count()

churned_customers = (df["Churn"] == "Yes").sum()

retained_customers = (df["Churn"] == "No").sum()

churn_rate = (churned_customers / total_customers) * 100

retention_rate = (retained_customers / total_customers) * 100

print("Total Customers:", total_customers)

print("Churned Customers:", churned_customers)

print("Retained Customers:", retained_customers)

print("Churn Rate:", round(churn_rate, 2), "%")

print("Retention Rate:", round(retention_rate, 2), "%")


print("\n--- Contract Wise Churn Analysis ---")

contract_churn = df.groupby("Contract")["Churn"].value_counts().unstack()

print(contract_churn)

print("\nChurn Percentage by Contract:")

contract_churn_rate = (
    df.groupby("Contract")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(contract_churn_rate.round(2))

print("\n--- Tenure Wise Churn Analysis ---")

tenure_churn = df.groupby("Churn")["tenure"].mean()

print("Average Customer Tenure:")
print(tenure_churn.round(2))

print("\n--- Payment Method Wise Churn Analysis ---")

payment_churn = df.groupby("PaymentMethod")["Churn"].value_counts().unstack()

print(payment_churn)

print("\nChurn Percentage by Payment Method:")

payment_churn_rate = (
    df.groupby("PaymentMethod")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(payment_churn_rate.round(2))

print("\n--- Internet Service Wise Churn Analysis ---")

internet_churn = (
    df.groupby("InternetService")["Churn"]
    .value_counts()
    .unstack()
)

print(internet_churn)

print("\nChurn Percentage by Internet Service:")

internet_churn_rate = (
    df.groupby("InternetService")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(internet_churn_rate.round(2))

print("\n--- Monthly Charges Wise Churn Analysis ---")

monthly_charges_churn = df.groupby("Churn")["MonthlyCharges"].mean()

print("Average Monthly Charges:")
print(monthly_charges_churn.round(2))

print("\n--- Total Charges Wise Churn Analysis ---")

total_charges_churn = df.groupby("Churn")["TotalCharges"].mean()

print("Average Total Charges:")
print(total_charges_churn.round(2))

print("\n--- Senior Citizen Wise Churn Analysis ---")

senior_churn = (
    df.groupby("SeniorCitizen")["Churn"]
    .value_counts()
    .unstack()
)

print(senior_churn)

print("\nChurn Percentage by Senior Citizen:")

senior_churn_rate = (
    df.groupby("SeniorCitizen")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(senior_churn_rate.round(2))

print("\n--- Gender Wise Churn Analysis ---")

gender_churn = (
    df.groupby("gender")["Churn"]
    .value_counts()
    .unstack()
)

print(gender_churn)

print("\nChurn Percentage by Gender:")

gender_churn_rate = (
    df.groupby("gender")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(gender_churn_rate.round(2))

print("\n--- Partner Wise Churn Analysis ---")

partner_churn = (
    df.groupby("Partner")["Churn"]
    .value_counts()
    .unstack()
)

print(partner_churn)

print("\nChurn Percentage by Partner:")

partner_churn_rate = (
    df.groupby("Partner")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(partner_churn_rate.round(2))

print("\n--- Dependents Wise Churn Analysis ---")

dependents_churn = (
    df.groupby("Dependents")["Churn"]
    .value_counts()
    .unstack()
)

print(dependents_churn)

print("\nChurn Percentage by Dependents:")

dependents_churn_rate = (
    df.groupby("Dependents")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(dependents_churn_rate.round(2))

print("\n--- Online Security Wise Churn Analysis ---")

security_churn = (
    df.groupby("OnlineSecurity")["Churn"]
    .value_counts()
    .unstack()
)

print(security_churn)

print("\nChurn Percentage by Online Security:")

security_churn_rate = (
    df.groupby("OnlineSecurity")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(security_churn_rate.round(2))

print("\n--- Online Backup Wise Churn Analysis ---")

backup_churn = (
    df.groupby("OnlineBackup")["Churn"]
    .value_counts()
    .unstack()
)

print(backup_churn)

print("\nChurn Percentage by Online Backup:")

backup_churn_rate = (
    df.groupby("OnlineBackup")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(backup_churn_rate.round(2))


print("\n--- Tech Support Wise Churn Analysis ---")

support_churn = (
    df.groupby("TechSupport")["Churn"]
    .value_counts()
    .unstack()
)

print(support_churn)

print("\nChurn Percentage by Tech Support:")

support_churn_rate = (
    df.groupby("TechSupport")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(support_churn_rate.round(2))

print("\n--- Paperless Billing Wise Churn Analysis ---")

billing_churn = (
    df.groupby("PaperlessBilling")["Churn"]
    .value_counts()
    .unstack()
)

print(billing_churn)

print("\nChurn Percentage by Paperless Billing:")

billing_churn_rate = (
    df.groupby("PaperlessBilling")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(billing_churn_rate.round(2))

print("\n--- Phone Service Wise Churn Analysis ---")

phone_churn = (
    df.groupby("PhoneService")["Churn"]
    .value_counts()
    .unstack()
)

print(phone_churn)

print("\nChurn Percentage by Phone Service:")

phone_churn_rate = (
    df.groupby("PhoneService")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(phone_churn_rate.round(2))

print("\n--- Multiple Lines Wise Churn Analysis ---")

multiple_lines_churn = (
    df.groupby("MultipleLines")["Churn"]
    .value_counts()
    .unstack()
)

print(multiple_lines_churn)

print("\nChurn Percentage by Multiple Lines:")

multiple_lines_churn_rate = (
    df.groupby("MultipleLines")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(multiple_lines_churn_rate.round(2))

print("\n--- Device Protection Wise Churn Analysis ---")

device_churn = (
    df.groupby("DeviceProtection")["Churn"]
    .value_counts()
    .unstack()
)

print(device_churn)

print("\nChurn Percentage by Device Protection:")

device_churn_rate = (
    df.groupby("DeviceProtection")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(device_churn_rate.round(2))

print("\n--- Streaming TV Wise Churn Analysis ---")

streaming_tv_churn = (
    df.groupby("StreamingTV")["Churn"]
    .value_counts()
    .unstack()
)

print(streaming_tv_churn)

print("\nChurn Percentage by Streaming TV:")

streaming_tv_churn_rate = (
    df.groupby("StreamingTV")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(streaming_tv_churn_rate.round(2))

print("\n--- Streaming Movies Wise Churn Analysis ---")

streaming_movies_churn = (
    df.groupby("StreamingMovies")["Churn"]
    .value_counts()
    .unstack()
)

print(streaming_movies_churn)

print("\nChurn Percentage by Streaming Movies:")

streaming_movies_churn_rate = (
    df.groupby("StreamingMovies")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(streaming_movies_churn_rate.round(2))

print("\n--- Customer Tenure Group Analysis ---")

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 36, float("inf")],
    labels=["New", "Medium-term", "Long-term"]
)

tenure_group_churn = (
    df.groupby("TenureGroup", observed=False)["Churn"]
    .value_counts()
    .unstack()
)

print(tenure_group_churn)

print("\nChurn Percentage by Tenure Group:")

tenure_group_churn_rate = (
    df.groupby("TenureGroup", observed=False)["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(tenure_group_churn_rate.round(2))

print("\n--- Monthly Charges Group Analysis ---")

df["MonthlyChargesGroup"] = pd.cut(
    df["MonthlyCharges"],
    bins=[-1, 35, 70, float("inf")],
    labels=["Low", "Medium", "High"]
)

monthly_group_churn = (
    df.groupby("MonthlyChargesGroup", observed=False)["Churn"]
    .value_counts()
    .unstack()
)

print(monthly_group_churn)

print("\nChurn Percentage by Monthly Charges Group:")

monthly_group_churn_rate = (
    df.groupby("MonthlyChargesGroup", observed=False)["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(monthly_group_churn_rate.round(2))

print("\n--- Contract and Internet Service Combined Analysis ---")

combined_churn = (
    df.groupby(
        ["Contract", "InternetService"],
        observed=False
    )["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .unstack()
)

print(combined_churn.round(2))

print("\n========== FINAL CUSTOMER CHURN INSIGHTS ==========")

print("\n1. Overall Churn Rate:")
print(round((df["Churn"] == "Yes").mean() * 100, 2), "%")

print("\n2. Highest Churn Contract:")
print(contract_churn_rate.idxmax(),
      "-", round(contract_churn_rate.max(), 2), "%")

print("\n3. Highest Churn Payment Method:")
print(payment_churn_rate.idxmax(),
      "-", round(payment_churn_rate.max(), 2), "%")

print("\n4. Highest Churn Internet Service:")
print(internet_churn_rate.idxmax(),
      "-", round(internet_churn_rate.max(), 2), "%")

print("\n5. Highest Churn Tenure Group:")
print(tenure_group_churn_rate.idxmax(),
      "-", round(tenure_group_churn_rate.max(), 2), "%")

print("\n6. Highest Churn Monthly Charges Group:")
print(monthly_group_churn_rate.idxmax(),
      "-", round(monthly_group_churn_rate.max(), 2), "%")

print("\n========== ANALYSIS COMPLETED ==========")


print("\n--- Exporting Cleaned Dataset ---")

output_path = "02_Python/customer_churn_cleaned.csv"

df.to_csv(output_path, index=False)

print("Cleaned dataset exported successfully!")
print("File saved at:", output_path)

print("\n--- Exporting Python Analysis Report ---")

with pd.ExcelWriter(
    "02_Python/customer_churn_analysis_report.xlsx",
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Cleaned_Data",
        index=False
    )

    contract_churn.to_excel(
        writer,
        sheet_name="Contract_Churn"
    )

    payment_churn.to_excel(
        writer,
        sheet_name="Payment_Churn"
    )

    internet_churn.to_excel(
        writer,
        sheet_name="Internet_Churn"
    )

    tenure_group_churn.to_excel(
        writer,
        sheet_name="Tenure_Group"
    )

    monthly_group_churn.to_excel(
        writer,
        sheet_name="Monthly_Charges"
    )

    contract_churn_rate.to_frame("Churn_Rate").to_excel(

        writer, sheet_name="Contract_Churn_Rate"
    )

    payment_churn_rate.to_frame("Churn_Rate").to_excel(
        writer, sheet_name="Payment_Churn_Rate"
    )

    internet_churn_rate.to_frame("Churn_Rate").to_excel(
        writer, sheet_name="Internet_Churn_Rate"
    )

    tenure_group_churn_rate.to_frame("Churn_Rate").to_excel(
        writer, sheet_name="Tenure_Churn_Rate"
    )

print("Excel Analysis Report Exported Successfully!")

print("CSV columns:", df.columns.tolist())
print("Total columns:", len(df.columns))



import pandas as pd
import mysql.connector

# Step 1: Read cleaned CSV
df = pd.read_csv("02_Python/customer_churn_cleaned.csv")

# Step 2: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vedprakash@29",
    database="customer_churn_db"
)

cursor = conn.cursor()

# Step 3: Prepare SQL query
sql = """
INSERT INTO customers (
    customerID, gender, SeniorCitizen, Partner, Dependents,
    tenure, PhoneService, MultipleLines, InternetService,
    OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
    StreamingTV, StreamingMovies, Contract, PaperlessBilling,
    PaymentMethod, MonthlyCharges, TotalCharges, Churn
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""

# Step 4: Insert records
data = [
    tuple(None if pd.isna(value) else value for value in row)
    for row in df.iloc[:, :21].itertuples(index=False, name=None)
]

cursor.executemany(sql, data)

conn.commit()

print("Total records inserted:", cursor.rowcount)

cursor.close()
conn.close()




 