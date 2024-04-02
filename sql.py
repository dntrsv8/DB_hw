import sqlite3

conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS orders (
                ord_no INTEGER PRIMARY KEY,
                purch_amt REAL,
                ord_date TEXT,
                customer_id INTEGER,
                salesman_id INTEGER)''')

orders_data = [
    (70001, 150.5, '2012-10-05', 3005, 5002),
    (70009, 270.65, '2012-09-10', 3001, 5005),
    (70002, 65.26, '2012-10-05', 3002, 5001),
    (70004, 110.5, '2012-08-17', 3009, 5003),
    (70007, 948.5, '2012-09-10', 3005, 5002),
    (70005, 2400.6, '2012-07-27', 3007, 5001),
    (70008, 5760, '2012-09-10', 3002, 5001),
    (70010, 1983.43, '2012-10-10', 3004, 5006),
    (70003, 2480.4, '2012-10-10', 3009, 5003),
    (70012, 250.45, '2012-06-27', 3008, 5002),
    (70011, 75.29, '2012-08-17', 3003, 5007),
    (70013, 3045.6, '2012-04-25', 3002, 5001)

]
cursor.executemany('INSERT INTO orders VALUES (?, ?, ?, ?, ?)', orders_data)
conn.commit()

queries = [
    "SELECT ord_no, ord_date, purch_amt FROM orders WHERE salesman_id = 5002;",
    "SELECT DISTINCT salesman_id FROM orders;",
    "SELECT ord_date, salesman_id, ord_no, purch_amt FROM orders ORDER BY ord_date;",
    "SELECT * FROM orders WHERE ord_no BETWEEN 70001 AND 70007;"
]

for query in queries:
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)

conn.close()
