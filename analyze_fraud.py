import sys
import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Ensure print output is shown immediately
sys.stdout.reconfigure(line_buffering=True)

# Load dataset
df = pd.read_csv("creditcard.csv")

# Save to SQLite
conn = sqlite3.connect("fraud.db")
df.to_sql("transactions", conn, if_exists="replace", index=False)
print("✅ Database created and populated.")

# Query 1: Fraud vs Non-Fraud Count
query1 = """
SELECT Class, COUNT(*) as count
FROM transactions
GROUP BY Class
"""
results1 = conn.execute(query1).fetchall()
labels = ['Non-Fraud' if row[0] == 0 else 'Fraud' for row in results1]
counts = [row[1] for row in results1]

# 💬 Terminal Output
print("\n📊 [1] Fraud vs Non-Fraud Count:")
for label, count in zip(labels, counts):
    print(f"{label}: {count:,}")

# Plot 1
plt.figure(figsize=(6, 4))
plt.bar(labels, counts, color=['skyblue', 'salmon'])
plt.title("Fraud vs Non-Fraud Transactions")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("fraud_vs_nonfraud.png")
print("📊 Saved fraud_vs_nonfraud.png")
plt.close()

# Query 2: Average Transaction Amount
query2 = """
SELECT Class, AVG(Amount) as avg_amount
FROM transactions
GROUP BY Class
"""
results2 = conn.execute(query2).fetchall()
avg_labels = ['Non-Fraud' if row[0] == 0 else 'Fraud' for row in results2]
avg_amounts = [row[1] for row in results2]

# 💬 Terminal Output
print("\n💰 [2] Average Transaction Amount:")
for label, avg in zip(avg_labels, avg_amounts):
    print(f"{label}: ${avg:,.2f}")

# Plot 2
plt.figure(figsize=(6, 4))
plt.bar(avg_labels, avg_amounts, color=['lightgreen', 'orange'])
plt.title("Average Transaction Amount")
plt.ylabel("Average Amount ($)")
plt.tight_layout()
plt.savefig("avg_amount.png")
print("📊 Saved avg_amount.png")
plt.close()

# Save summary to text file
summary = "[1] Fraud vs Non-Fraud Count:\n"
for label, count in zip(labels, counts):
    summary += f"{label}: {count:,}\n"

summary += "\n[2] Average Transaction Amount:\n"
for label, avg in zip(avg_labels, avg_amounts):
    summary += f"{label}: ${avg:,.2f}\n"

with open("fraud_stats.txt", "w") as f:
    f.write(summary)

print("📝 Saved fraud_stats.txt")

# Final Output
print(f"\n📁 Current directory: {os.getcwd()}")
print("📂 Contents:")
for f in os.listdir():
    if f.endswith(".png") or f.endswith(".txt"):
        print(f"✅ {f}")

# Close DB connection
conn.close()
