#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Step 2: Create table and insert sample data
cursor.execute('''
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')

sales_data = [
    (1, 'Apple', 10, 2.0),
    (2, 'Banana', 5, 1.0),
    (3, 'Apple', 8, 2.0),
    (4, 'Banana', 12, 1.0),
    (5, 'Orange', 7, 1.5),
]

cursor.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', sales_data)
conn.commit()

# Step 3: Use SQL to calculate total quantity and revenue per product
query = '''
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
'''

df = pd.read_sql_query(query, conn)

# Step 4: Display results using print
print("Sales Summary:\n")
for index, row in df.iterrows():
    print(f"{row['product']}: Quantity Sold = {row['total_quantity']}, Revenue = ₹{row['total_revenue']}")

# Step 5: Plot bar chart
plt.figure(figsize=(8, 5))
plt.bar(df['product'], df['total_revenue'], color='skyblue')
plt.title('Total Revenue per Product')
plt.xlabel('Product')
plt.ylabel('Revenue (₹)')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Close connection
conn.close()


# In[ ]:




