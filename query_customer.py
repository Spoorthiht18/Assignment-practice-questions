import sqlite3

conn = sqlite3.connect('customer_orders.db')
cursor = conn.cursor()

customer_name = input("Enter customer name: ")
order_date = input("Enter order date (YYYY-MM-DD): ")

query = """
SELECT c.name, c.email, o.order_id, o.order_date, p.name, oi.quantity, p.price
FROM Customer c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Order_Item oi ON o.order_id = oi.order_id
JOIN Product p ON oi.product_id = p.product_id
WHERE c.name = ? AND o.order_date = ?;
"""

cursor.execute(query, (customer_name, order_date))
rows = cursor.fetchall()

if rows:
    print(f"\nOrders for {customer_name} on {order_date}:")
    for row in rows:
        print(f"OrderID: {row[2]}, Product: {row[4]}, Quantity: {row[5]}, Price: ₹{row[6]}")
else:
    print("No orders found for that customer on that date.")

conn.close()
