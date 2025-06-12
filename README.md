# 📊 Sales Analysis with SQLite, Pandas, and Matplotlib

This Python script demonstrates how to:
- Create an in-memory SQLite database
- Insert and query sales data
- Perform aggregation using SQL
- Visualize results using `matplotlib`

---

## 📦 About `sqlite3` Module

The `sqlite3` module is a built-in Python library that provides a lightweight disk-based database that doesn’t require a separate server process. It allows you to create databases in memory or on disk and interact with them using SQL.

Key features:
- Zero configuration (no setup or server required)
- Ideal for small to medium-sized datasets
- Fully supports SQL syntax (SELECT, INSERT, JOIN, etc.)
- Comes pre-installed with Python (no need for external installation)

In this project, we use an **in-memory database** (`:memory:`), meaning the database is created temporarily in RAM and vanishes once the script ends.

---

## 📁 Project Structure

- **Language**: Python
- **Libraries Used**:
  - `sqlite3` – for SQL database operations
  - `pandas` – for tabular data manipulation
  - `matplotlib` – for visualization

---

## 🧾 Raw Dataset

Below is the sample dataset inserted into the SQLite table:

| sale_id | product | quantity | price |
|---------|---------|----------|-------|
| 1       | Apple   | 10       | 2.0   |
| 2       | Banana  | 5        | 1.0   |
| 3       | Apple   | 8        | 2.0   |
| 4       | Banana  | 12       | 1.0   |
| 5       | Orange  | 7        | 1.5   |

---

## 🚀 Features

1. **Database Setup**  
   Creates an in-memory SQLite database with a `sales` table.

2. **Sample Data Insertion**  
   Sample sales transactions are inserted directly.

3. **SQL Query Execution**  
   Uses SQL to calculate:
   - Total quantity per product
   - Total revenue per product (`quantity * price`)

4. **Console Output**  
   Prints a summary like:
   ```
   Sales Summary:

   Apple: Quantity Sold = 18, Revenue = ₹36.0  
   Banana: Quantity Sold = 17, Revenue = ₹17.0  
   Orange: Quantity Sold = 7, Revenue = ₹10.5
   ```

5. **Data Visualization**  
   Bar chart of total revenue per product using `matplotlib`.

---

## 🖥️ How to Run

1. Make sure Python is installed (version 3.x).
2. Install required libraries (if not already installed):

```bash
pip install pandas matplotlib
```

3. Run the script:

```bash
python sales_analysis.py
```

---

## 📉 Output

- **Console Output**: Product-level sales summary
- **Chart**: Bar chart of total revenue per product

![Example Chart](Output.png)

---

## 🧹 Cleanup

The SQLite connection is closed at the end of the script to release memory and resources.

---

## 📌 Use Cases

- Quick data analysis using temporary databases
- Learning SQL with Python
- Simple business reporting and visualization

---

## 📝 Author

**Shanmukhi Koshireddy**  
Feel free to use, modify, and share this script for educational or analytical purposes.
