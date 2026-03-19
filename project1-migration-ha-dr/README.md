# 🚀 Project 1: Multi-Cloud Database Migration with High Availability & Disaster Recovery

## 📌 Overview
This project demonstrates the end-to-end migration of a local MySQL database to AWS RDS, implementing High Availability (Multi-AZ), Read Replicas for performance optimization, and Disaster Recovery using snapshots. Additionally, data is integrated with Google BigQuery for analytics, showcasing a multi-cloud data architecture.

---

## 🛠️ Technologies Used
- MySQL (Local & RDS)
- Amazon Web Services (AWS RDS)
- Google Cloud Platform (BigQuery)
- SQL
- DBeaver (Database Client)

---

## ⚙️ Architecture
Local MySQL → AWS RDS (Primary - Multi-AZ) → Read Replica → Snapshot Backup → Restore → BigQuery

---

## 🚀 Implementation Steps

### 🔹 1. Database Setup
- Created a local MySQL database (`company_db`)
- Designed and created `employees` table
- Inserted sample data

### 🔹 2. Migration to AWS RDS
- Provisioned MySQL instance in AWS RDS
- Connected using DBeaver
- Migrated schema and data

### 🔹 3. High Availability (Multi-AZ)
- Enabled Multi-AZ deployment
- Ensured automatic failover capability

### 🔹 4. Read Replica Configuration
- Created read replica instance
- Verified asynchronous replication
- Executed read queries on replica

### 🔹 5. Backup & Snapshot
- Enabled automated backups
- Created manual snapshot (`lassdb-snapshot-1`)

### 🔹 6. Disaster Recovery (Restore)
- Simulated failure by dropping table
- Restored database from snapshot
- Verified data recovery

### 🔹 7. (Optional) Data Integration
- Exported data for analytics use
- Prepared integration with Google BigQuery

---

## 📸 Screenshots

| Step | Description |
|------|------------|
| RDS Setup | Database instance creation |
| Data Insert | Table creation & data insertion |
| Read Replica | Replica setup |
| Replica Query | Data verification |
| Snapshot | Backup creation |
| Data Loss | Failure simulation |
| Restore | Database recovery |
| Restored Data | Verified recovered data |

---

## 📊 Results
- Successfully migrated database to AWS cloud
- Implemented high availability using Multi-AZ
- Improved performance using read replicas
- Ensured data protection with backup & restore
- Simulated real-world disaster recovery scenario

---

## 🧠 Key Learnings
- AWS RDS architecture and configuration
- High Availability vs Read Replica concepts
- Backup and disaster recovery strategies
- Database replication and consistency
- Multi-cloud data integration fundamentals

---

## 🔥 Interview Highlights
- Implemented end-to-end cloud database migration
- Designed HA architecture using Multi-AZ
- Configured read replicas for scalability
- Demonstrated disaster recovery using snapshots

---

## 📌 Future Enhancements
- Automate ETL pipeline to BigQuery
- Integrate CI/CD for database deployments
- Implement monitoring & alerting (CloudWatch)
