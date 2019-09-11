import sys
import csv

# input_file = sys.argv[1]
# output_file = sys.argv[2]
input_file = "supplier_data.csv"
output_file = "./output_files/4csv_reader_value_in_set.csv"

important_dates = ['1/20/14', '1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)  # 첫 줄
        filewriter.writerow(header)
        for row_list in filereader:
            print(row_list)  # 한 행에는 5개의 인자(요소)가 있다
            a_date = row_list[4]
            if a_date in important_dates:
                filewriter.writerow(row_list)