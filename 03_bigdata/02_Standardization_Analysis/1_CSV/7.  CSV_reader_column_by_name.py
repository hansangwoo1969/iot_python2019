import sys
import csv

# 목적: 열의 헤더를 사용하여 특정 열을 선택하기
# 열의 헤드명으로 검색하는 것은 새로운 열이 추가및 삭제 되었을 경우에

# input_file = sys.argv[1]
# output_file = sys.argv[2]
input_file = "supplier_data.csv"
output_file = "./output_files/7csv_reader_column_by_name.csv"

my_columns = ['Invoice Number', 'Purchase Date']
my_columns_index  = []

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        # print(header)
        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
        filewriter.writerow(my_columns)
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns_index:
                row_list_output.append(row_list[index_value])
            # print(row_list_output)
            filewriter.writerow(row_list_output)