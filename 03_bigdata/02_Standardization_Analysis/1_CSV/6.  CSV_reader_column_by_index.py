import sys
import csv

# 열의 인덱스 값을 사용하여 특정열을 선택하기
# 열 필터링 할때는 헤드행을 읽을 필요가 없다.

# input_file = sys.argv[1]
# output_file = sys.argv[2]
input_file = "supplier_data.csv"
output_file = "./output_files/6csv_reader_column_by_index.csv"

my_columns = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list)