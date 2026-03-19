# 🚀 Project 2: End-to-End ETL Pipeline (AWS RDS → GCP BigQuery)

## 📌 Overview

This project demonstrates building an end-to-end ETL (Extract, Transform, Load) pipeline by extracting data from AWS RDS (MySQL), transforming it using Python, and loading it into Google BigQuery for analytics.

---

## 🛠️ Technologies Used

* AWS RDS (MySQL)
* Python (Pandas, MySQL Connector)
* Google BigQuery
* SQL

---

## ⚙️ Architecture

AWS RDS (MySQL) → Python ETL Script → CSV → GCP BigQuery → Analytics

---

## 🚀 Steps Implemented

### 1. Data Preparation (RDS)

* Created `users` and `orders` tables
* Inserted sample data

### 2. Data Extraction

* Connected Python to AWS RDS
* Extracted data using SQL queries

### 3. Data Transformation

* Joined users and orders tables
* Applied transformations (e.g., calculated total amount)

### 4. Data Loading

* Exported transformed data to CSV
* Uploaded CSV to BigQuery

### 5. Analytics

* Ran SQL queries in BigQuery for insights

---

## 📊 Results

* Built a complete ETL pipeline
* Successfully moved data from AWS to GCP
* Enabled analytical reporting using BigQuery

---

## 🧠 Key Learnings

* ETL pipeline development
* Cross-cloud data integration
* Data transformation using Python
* Cloud-based analytics

---

## 📂 Project Structure

* `sql/` → SQL scripts for tables and data
* `data/` → Output CSV file
* `screenshots/` → Execution proof
* `etl_pipeline.py` → ETL logic

---

## 🔥 Future Improvements

* Automate pipeline using Airflow
* Add incremental data loading
* Implement scheduling

---

## 👨‍💻 Author

Anil Pirla
