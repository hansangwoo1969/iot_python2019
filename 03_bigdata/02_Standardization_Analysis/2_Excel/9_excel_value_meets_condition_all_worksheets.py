# 목적: 모든 워크시트에서 특정행 필터링 하기
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_file = 'sales_2013.xlsx'
output_file = 'output_files/9output_basic.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('filtered_rows_all_worksheets')

sales_column_index = 3
threshold = 2000.0

first_worksheet  = True
with open_workbook(input_file) as workbook:
    data = []
    for worksheet in workbook.sheets():
        if first_worksheet:
            header_row = worksheet.row_values(0)
            data.append(header_row)
            first_worksheet = False
        for row_index in range(1, worksheet.nrows):
            row_list = []
            sale_amount = worksheet.cell_value(row_index, sales_column_index)
            # 라인 31은 없어도 무관, 엑셀에서 가져오는 것은 서식은 버리고 옴,
            # 이전에는 replace가 아닌 strip함수 사용, 차이는?    없는 듯,,,
            # sale_amount = float(str(sale_amount).replace('$','').replace(',',''))
            sale_amount = float(str(sale_amount).strip('$').strip(','))
            if sale_amount > threshold:
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        # print(date_cell)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        # print(date_cell)
                        # 연습으로 원본과 똑같은 형태의 날짜도 저장 할 것
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)
            if row_list:
                data.append(row_list)

    for list_index, output_list in enumerate(data):
        # print(list_index, '\t', output_list)
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
            # print(list_index, '\t', element_index,'\t',element)
output_workbook.save(output_file)




