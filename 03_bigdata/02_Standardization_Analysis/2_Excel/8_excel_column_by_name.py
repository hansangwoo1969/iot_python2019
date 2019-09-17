# 목적: 헤더 행을 사용하여 특정열 선택하기
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_file = 'sales_2013.xlsx'
output_file = 'output_files/8output_basic.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

my_colums = ['Customer ID', 'Purchase Date']

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = [my_colums]
    header_list = worksheet.row_values(0)
    header_index_list=[]
    for header_index in range(len(header_list)):
        if header_list[header_index] in my_colums:
            header_index_list.append(header_index)
    for row_index in range(1, worksheet.nrows):
        row_list = []
        for column_index in header_index_list:
            cell_value = worksheet.cell_value(row_index, column_index)
            cell_type = worksheet.cell_type(row_index, column_index)
            if cell_type == 3:
                date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                # print(date_cell)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                # print(date_cell)
                #연습으로 원본과 똑같은 형태의 날짜도 저장 할 것
                row_list.append(date_cell)
            else:
                row_list.append(cell_value)

        data.append(row_list)
    for list_index, output_list in enumerate(data):
        # print(list_index, '\t', output_list)
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
            # print(list_index, '\t', element_index,'\t',element)
output_workbook.save(output_file)




