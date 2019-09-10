import sys
import csv
import glob
import os
import string

# input_file = sys.argv[1]
# output_file = sys.argv[2]
input_file = "supplier_data_unnecessary_header_footer.csv"
output_file = "./output_files/11csv_reader_select_continuous-rows.csv"

row_counter = 0
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as  csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row in filereader:
            if row_counter >=3 and row_counter <= 15:
                filewriter.writerow([value.strip() for value in row])
            row_counter += 1