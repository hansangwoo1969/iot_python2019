# 목적: 디렉토리내의 워크북 파악
import glob
import os
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_directory = '.'


workbook_count = 0

for input_file in glob.glob(os.path.join(input_directory,'*.xls*')):
    workbook = open_workbook(input_file)
    print('Workbook: {}'.format(os.path.basename(input_file)))
    print('Number of worksheets: {}'.format(workbook.nsheets))
    for worksheet in workbook.sheets():
        print('Worksheet name:', worksheet.name, '\tRows:', worksheet.nrows, '\tColuns:', worksheet.ncols)
    workbook_count += 1
print(f'Number of Excel workbooks: {workbook_count}')


