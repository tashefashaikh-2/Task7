import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------
# 1. CREATE SAMPLE DATABASE (only once)
# ---------------------------------------
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data (only on first run)
sample_data = [
    ("Laptop", 2, 50000),
    ("Laptop", 1, 50000),
    ("Mouse", 10, 500),
    ("Mouse", 5, 500),
    ("Keyboard", 3, 1500),
    ("Keyboard", 2, 1500),
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# ---------------------------------------
# 2. RUN SQL QUERY FOR PRODUCT SUMMARY
# ---------------------------------------
query = """
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
"""

df = pd.read_sql_query(query, conn)
print("📌 SALES SUMMARY (Product-wise)")
print(df)

# ---------------------------------------
# 2B. EXTRA SQL QUERY — TOTAL STORE REVENUE
# ---------------------------------------
query2 = "SELECT SUM(quantity * price) AS total_store_revenue FROM sales"
df2 = pd.read_sql_query(query2, conn)

print("\n📌 TOTAL STORE REVENUE")
print(df2)

# ---------------------------------------
# 3. PLOT BAR CHART
# ---------------------------------------
plt.figure(figsize=(8,5))
plt.bar(df['product'], df['total_revenue'])
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.title("Revenue by Product")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Close connection
conn.close()
