import sqlite3

conn = sqlite3.connect('customer_orders.db')
cursor = conn.cursor()

# Insert Customers
cursor.execute("INSERT INTO Customer VALUES (1, 'John Doe', 'john@example.com', 'New York')")
cursor.execute("INSERT INTO Customer VALUES (2, 'Jane Smith', 'jane@example.com', 'California')")

# Insert Products
cursor.execute("INSERT INTO Product VALUES (101, 'Laptop', 75000)")
cursor.execute("INSERT INTO Product VALUES (102, 'Mouse', 800)")

# Insert Orders
cursor.execute("INSERT INTO Orders VALUES (501, 1, '2025-10-18')")
cursor.execute("INSERT INTO Orders VALUES (502, 2, '2025-10-19')")

# Insert Order Items
cursor.execute("INSERT INTO Order_Item VALUES (501, 101, 1)")
cursor.execute("INSERT INTO Order_Item VALUES (501, 102, 2)")
cursor.execute("INSERT INTO Order_Item VALUES (502, 102, 3)")

conn.commit()
print(" Sample data inserted.")
conn.close()
