# 목적: 통합문서 및 워크시트별 합계 및 평균 구하기
import glob
import os
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_folder = '.'
output_file = 'output_files/14output_basic.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('sums_and_averages')

data = []
first_worksheet = True
for input_file in glob.glob(os.path.join(input_folder, '*.xls*')):
    print(os.path.basename(input_file))
    with open_workbook(input_file) as workbook:
        for worksheet in workbook.sheets():
            if first_worksheet:
                header_row = worksheet.row_values(0)
                data.append(header_row)
                first_worksheet = False
            for row_index in range(1, worksheet.nrows):
                row_list = []
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)
                data.append(row_list)

for list_index, output_list in enumerate(data):
    # print(list_index, '\t', output_list)
    for element_index, element in enumerate(output_list):
        print(element_index, '\t', element)
        output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)


