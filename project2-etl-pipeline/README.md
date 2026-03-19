# 🚀 Project 2: End-to-End ETL Pipeline (AWS RDS → GCP BigQuery → Looker Studio)

---

## 📌 Overview

This project demonstrates building a complete end-to-end ETL (Extract, Transform, Load) pipeline by extracting data from AWS RDS (MySQL), transforming it using Python, loading it into Google BigQuery, and visualizing insights using Looker Studio.

---

## 🛠️ Technologies Used

* AWS RDS (MySQL)
* Python (Pandas, MySQL Connector)
* Google BigQuery
* Looker Studio (Data Visualization)
* SQL

---

## ⚙️ Architecture

AWS RDS (MySQL) → Python ETL Script → CSV → GCP BigQuery → Looker Studio Dashboard

---

## 🚀 Steps Implemented

### 1. Data Preparation (RDS)

* Created `users` and `orders` tables
* Inserted sample transactional data

### 2. Data Extraction

* Connected Python script to AWS RDS
* Extracted data using SQL queries

### 3. Data Transformation

* Joined users and orders tables
* Applied transformations (e.g., increased amount by 10%)

### 4. Data Loading

* Exported transformed data to CSV
* Uploaded CSV into BigQuery table

### 5. Data Analytics (BigQuery)

* Ran aggregation queries (SUM, GROUP BY)
* Generated business insights

### 6. Data Visualization (Looker Studio)

* Connected BigQuery dataset to Looker Studio
* Built interactive dashboard (charts + tables)

---

## 📊 Sample Query Output

| Name | Total Sales |
| ---- | ----------- |
| Anil | 2750        |
| Ravi | 2200        |
| John | 3300        |

---

## 📊 Dashboard Visualization

Interactive dashboard created using Looker Studio to visualize sales distribution and insights.

---

## 📂 Project Structure

```
project2-etl-pipeline/
│
├── README.md
├── etl_pipeline.py
├── requirements.txt
│
├── sql/
│   ├── create_tables.sql
│   └── insert_data.sql
│
├── data/
│   └── final_data.csv
│
├── screenshots/
│   ├── rds-data.png
│   ├── etl-script.png
│   ├── csv-output.png
│   ├── bigquery-table.png
│   ├── query-result.png
│   └── looker-dashboard.png
```

---

## 📸 Screenshots

* RDS Data (Source)
* ETL Script Execution
* CSV Output
* BigQuery Table
* Query Results
* Looker Dashboard

---

## 🧠 Key Learnings

* Built end-to-end ETL pipeline
* Performed cross-cloud data integration (AWS → GCP)
* Applied data transformation using Python
* Designed analytical queries in BigQuery
* Created interactive dashboards using Looker Studio

---

## 🔗 Multi-Cloud Architecture

This project demonstrates integration between:

* AWS (RDS) for transactional storage
* Python for ETL processing
* Google Cloud (BigQuery) for analytics
* Looker Studio for visualization

---

## 💡 Real-World Use Case

Simulates how organizations move data from operational databases to analytics platforms for reporting and business insights.

---

## 🔥 Future Improvements

* Automate pipeline using Apache Airflow
* Implement incremental data loading
* Add real-time streaming pipeline (Kafka)
* Schedule ETL jobs

---

## 👨‍💻 Author

Anil Pirla
