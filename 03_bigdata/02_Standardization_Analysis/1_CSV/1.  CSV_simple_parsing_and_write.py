import sys

# csv모듈 없이 파이썬 기본으로 파일읽고, 쓰기

# input_file = sys.argv[1]
# output_file = sys.argv[2]
input_file = "supplier_data.csv"
output_file = "./output_files/1output_index_false.csv"

with open(input_file, 'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        header = filereader.readline()  # 한줄읽고,
        header = header.strip()  # \n제거
        header_list = header.split(',')
        print(header_list)
        filewriter.write(','.join(map(str, header_list))+'\n') # 원본과 동일한 상태로 저장
        for row in filereader:
            # print(len(row))
            row = row.strip()  # \n제거, 길이가 -2,
            # print(len(row))
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')