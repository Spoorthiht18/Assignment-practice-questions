import sqlite3

# Step 1: Connect to Database
conn = sqlite3.connect('customer_orders.db')
cursor = conn.cursor()

# Step 2: Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customer (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    address TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Product (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Order_Item (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);
""")

conn.commit()
print("✅ Database and tables created successfully.")
conn.close()
