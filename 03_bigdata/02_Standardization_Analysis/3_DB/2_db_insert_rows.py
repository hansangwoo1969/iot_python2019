import csv
import sqlite3
import sys

#  Path to and name of a CSV input file
# input_file = sys.argv[1]
input_file = 'supplier_data.csv'

# Create a table called sales with five attributes
con = sqlite3.connect('Suppliers.db')
c = con.cursor()
q_table = """CREATE TABLE IF NOT EXISTS Suppliers
                    (Supplier_Name VARCHAR(20),
                    Invoice_Number VARCHAR(20),
                    Part_Numbber VARCHAR(20),
                    Cost FLOAT,
                    Purchase_Date DATE);"""
c.execute(q_table)
con.commit()

# Read the CSV file
# Insert the data into the Suppliers table

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
# header = next(file_reader, None)  # header 건너뛰고 data만 접근하기 위하여
header = next(file_reader)  # header 건너뛰고 data만 접근하기 위하여
print("header", header)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO  Suppliers VALUES (?,?,?,?,?);",  data)
con.commit()

#  Query the Supplier table
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)



