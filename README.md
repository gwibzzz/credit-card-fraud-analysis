# 🕵️‍♀️ Credit Card Fraud Analysis

This project explores a credit card transaction dataset to detect fraud patterns and compare key statistics between fraudulent and non-fraudulent transactions.

## 📂 Files

- `analyze_fraud.py` — Main Python script that:
  - Loads `creditcard.csv`
  - Saves data to a SQLite database (`fraud.db`)
  - Runs SQL queries to extract statistics
  - Generates two visualizations
  - Saves a summary report as `fraud_stats.txt`

- `fraud_vs_nonfraud.png` — Bar chart showing count of fraud vs. non-fraud transactions  
- `avg_amount.png` — Bar chart comparing average transaction amount for fraud and non-fraud  
- `fraud_stats.txt` — Text summary of the two metrics above

## 📊 Dataset

- **Source**: `creditcard.csv`
- **Features**:
  - 284,807 transactions
  - 31 columns including anonymized features (`V1` to `V28`), `Amount`, and `Class`
  - `Class = 1` indicates fraud, `Class = 0` indicates non-fraud

## 🧪 Output Summary

From the most recent analysis (`fraud_stats.txt`):

