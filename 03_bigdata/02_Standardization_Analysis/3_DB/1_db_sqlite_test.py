import sqlite3

# Create an in-memory SQLite3 database
# Create a table called sales with four attributes
con = sqlite3.connect(':memory:')

# :memory:는 휘발성 이기 때문에 프로그램이  종료된 후에는 그 이전에 작업한
# 모든 내용은 사라진다.


# Query the sales table
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

# Count the number of rows in the output
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1

print(f"Number of rows: {row_counter}")

