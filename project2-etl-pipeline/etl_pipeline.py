
import pandas as pd
import mysql.connector

# Connect to AWS RDS
conn = mysql.connector.connect(
    host="YOUR_RDS_ENDPOINT",
    user="admin",
    password="YOUR_PASSWORD",
    database="company_db"
)

# Extract
users = pd.read_sql("SELECT * FROM users", conn)
orders = pd.read_sql("SELECT * FROM orders", conn)

# Transform
merged = pd.merge(users, orders, on="user_id")
merged['amount'] = merged['amount'] * 1.1  # Increase by 10%

# Load (save CSV)
merged.to_csv("data/final_data.csv", index=False)

print("ETL completed successfully!")
