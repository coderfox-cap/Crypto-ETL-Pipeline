# 🚀 Crypto ETL Pipeline with Databricks, Neon PostgreSQL & Power BI

## 📌 Project Overview

This project implements an end-to-end cloud-based ETL pipeline that extracts real-time cryptocurrency market data from the CoinGecko API, transforms and cleans the data using Python and Pandas, stores both current and historical snapshots in a cloud PostgreSQL database hosted on Neon, and visualizes insights through an interactive Power BI dashboard.

The entire pipeline is orchestrated and automated using Databricks Jobs, enabling scheduled execution without relying on traditional workflow tools such as Airflow.

---

# 🏗 Architecture

```text
CoinGecko API
       ↓
Databricks Job
       ↓
Python ETL Pipeline
       ↓
Neon PostgreSQL
       ↓
Power BI Dashboard
```

---

# 🎯 Objectives

* Build a production-style ETL pipeline.
* Automate data ingestion and updates.
* Maintain both current and historical cryptocurrency data.
* Visualize trends and market metrics through Power BI.
* Explore modern cloud-based data engineering workflows.

---

# ⚙️ Tech Stack

| Category                    | Technologies        |
| --------------------------- | ------------------- |
| Programming Language        | Python              |
| Data Processing             | Pandas              |
| API Source                  | CoinGecko API       |
| Database                    | Neon PostgreSQL     |
| ORM / Database Connectivity | SQLAlchemy + pg8000 |
| Orchestration               | Databricks Jobs     |
| Visualization               | Power BI            |
| SQL                         | PostgreSQL          |

---

# 📂 Project Structure

```
Crypto-ETL-Pipeline
│
├── pipeline.py
├── requirements.txt
├── README.md
│
├── sql
│   ├── create_crypto_prices.sql
│   └── create_crypto_price_history.sql
│
├── dashboard
│   └── Crypto_Dashboard.pbix
│
├── screenshots
│   ├── databricks_job_success.png
│   ├── neon_tables.png
│   ├── powerbi_dashboard.png
│   └── architecture.png
│
└── docs
```

---

# 🔄 ETL Workflow

## 1. Extract

Cryptocurrency market data is fetched from the CoinGecko API.

Retrieved attributes include:

* Coin ID
* Symbol
* Name
* Current Price
* Market Capitalization
* Market Cap Rank
* Trading Volume
* 24-hour High and Low
* Supply Metrics
* Last Updated Timestamp

---

## 2. Transform

Data preprocessing is performed using Pandas:

* Column selection
* Datatype conversion
* Timestamp formatting
* Symbol standardization
* Duplicate removal
* Data sorting

---

## 3. Load

### Current Table (`crypto_prices`)

Maintains the latest state of each cryptocurrency.

Features:

* Primary key based on coin ID.
* Incremental updates using PostgreSQL UPSERT.

---

### Historical Table (`crypto_price_history`)

Stores snapshots of cryptocurrency metrics over time.

Features:

* Appends new records at every pipeline execution.
* Enables historical trend analysis.

---

# 🗄 Database Schema

## Current Table

`crypto_prices`

Stores the latest cryptocurrency information.

Main columns:

* id
* symbol
* name
* current_price
* market_cap
* market_cap_rank
* total_volume
* high_24h
* low_24h
* price_change_percentage_24h
* circulating_supply
* total_supply
* max_supply
* last_updated

---

## Historical Table

`crypto_price_history`

Stores historical snapshots.

Main columns:

* coin_id
* symbol
* name
* current_price
* market_cap
* total_volume
* price_change_percentage_24h
* last_updated

---

# ⏰ Automation

The pipeline is automated using Databricks Jobs.

Schedule:

* Hourly execution

Benefits:

* Automatic data refresh
* Centralized monitoring
* Failure detection
* Cloud-native orchestration

---

# 📊 Power BI Dashboard

The Power BI dashboard provides:

### KPI Cards

* Current Bitcoin Price
* Market Capitalization
* Trading Volume

### Trend Analysis

* Cryptocurrency price movement over time

### Comparative Analysis

* Top cryptocurrencies by market capitalization
* Trading volume comparison

### Historical Insights

* Time-series analysis
* Snapshot-based trend exploration

---

# ✨ Key Features

✅ End-to-end ETL Pipeline

✅ Automated hourly execution

✅ Cloud-hosted PostgreSQL database

✅ Historical data tracking

✅ Incremental updates using UPSERT

✅ Power BI dashboard integration

✅ Databricks-based orchestration

---

# 📈 Skills Demonstrated

### Python

* API Integration
* Exception Handling
* Data Processing

### Pandas

* Cleaning
* Transformation
* Data Manipulation

### SQL

* UPSERT Operations
* Table Design
* Query Writing

### PostgreSQL

* Database Modeling
* Historical Data Storage

### Databricks

* Jobs
* Scheduling
* Cloud Workflow Automation

### Power BI

* Dashboard Development
* Data Visualization
* KPI Monitoring

---

# Challenges and Learnings

During the development process, several architectural approaches were explored, including:

* Local PostgreSQL
* Docker-based deployment
* Apache Airflow orchestration

After evaluating complexity and maintainability, the project evolved into a simpler and more scalable architecture using:

* Databricks Jobs
* Neon PostgreSQL
* Power BI

This approach reduced infrastructure overhead and enabled a cleaner cloud-native workflow.

---

# Future Improvements

* PySpark implementation
* Delta Lake integration
* Bronze-Silver-Gold architecture
* Data quality checks
* Logging framework
* Email notifications
* Workflow modularization
* Analytics engineering best practices

---

# Future Architecture

```text
CoinGecko API
       ↓
Bronze Layer
       ↓
Silver Layer
       ↓
Gold Layer
       ↓
Power BI
```

---

# Acknowledgements

* CoinGecko API
* Databricks
* Neon PostgreSQL
* Microsoft Power BI

---

## ⭐ If you found this project interesting, feel free to fork the repository or connect with me on LinkedIn.
