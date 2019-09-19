import csv
import sqlite3
import sys

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
# 전체 레코드 조회  readlines()와 유사
# output = c.execute("SELECT * FROM Suppliers")

# 열 필터링 하는 조건
# SQL은 대소문자를 구분하지 않는다. 그렇지만 성능을 위해
# SQL문 필드, 테이블명은 일관된 대소문자 정책을 적용해야 한다.
# output = c.execute("SELECT Supplier_Name FROM Suppliers")
# output = c.execute("SELECT Supplier_Name, Cost FROM Suppliers")
# output = c.execute("SELECT supplier_name, cost FROM Suppliers")
# output = c.execute("select supplier_name, cost from suppliers")
# output = c.execute("select SUPPLIER_NAME,COST from SUPPLIERS")

# 행 필터링 조건
# output = c.execute("SELECT * FROM Suppliers WHERE Supplier_name = 'Supplier X' ")
# output = c.execute("SELECT * FROM Suppliers WHERE Part_Numbber > 7000 ")

# 행, 열 필터링 하는 조건
output = c.execute("SELECT Supplier_Name, Cost FROM Suppliers WHERE Supplier_name = 'Supplier X' ")
rows = output.fetchall()
print("SELECT 결과")
for row in rows:
    # print('#1', row, '\t', len(row))
    output = []
    for column_index in range(len(row)):
        # print(column_index, str(row[column_index]))
        output.append(str(row[column_index]))
    print(output)