# 목적: 특정 조건을 충족하는 행의 필터링
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_file = 'sales_2013.xlsx'
output_file = 'output_files/4output_basic.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

sale_amount_column_index = 3
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    header = worksheet.row_values(0)
    data.append(header)
    for row_index in range(1, worksheet.nrows):
        row_list = []
        sale_amount = worksheet.cell_value(row_index,sale_amount_column_index)
        if sale_amount > 1400.0:
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index,column_index)
                cell_type = worksheet.cell_type(row_index, column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    #연습으로 원본과 똑같은 형태의 날짜도 저장 할 것
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        if row_list:
            data.append(row_list)
    for list_index, output_list in enumerate(data):
        print(list_index, '\t', output_list)
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
            # print(list_index, '\t', element_index,'\t',element)
output_workbook.save(output_file)




