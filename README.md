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
[1] Fraud vs Non-Fraud Count:
Non-Fraud: 284,315
Fraud: 492

[2] Average Transaction Amount:
Non-Fraud: $88.29
Fraud: $122.21


## 🛠️ How to Run

1. **Set up a virtual environment** (recommended):
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install dependencies**:
    ```
    pip install pandas matplotlib
    ```

3. **Place the dataset** (`creditcard.csv`) in the same folder as the script.

4. **Run the script**:
    ```
    python analyze_fraud.py
    ```

5. **Check output files**:
    - `fraud_vs_nonfraud.png`
    - `avg_amount.png`
    - `fraud_stats.txt`

## 📌 Notes

- The dataset is highly imbalanced (fraud cases are less than 0.2%), so comparing distribution and average values is helpful for understanding the data.
- This is an exploratory project with no machine learning or predictive modeling.

---


