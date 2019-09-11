import sys
import csv
import re

# input_file = sys.argv[1]
# output_file = sys.argv[2]
input_file = "supplier_data.csv"
output_file = "./output_files/5csv_reader_value_matches_pattern.csv"

# 그룹이름을 사용하는 것을 예정하였으나,
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number = row_list[1]
            if pattern.search(invoice_number):
                filewriter.writerow(row_list)