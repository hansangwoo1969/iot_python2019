# 목적: 날짜 형식 할당
import pandas as pd

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_file = 'sales_2013.xlsx'
output_file = 'output_files/3output_pandas.xls'

data_frame = pd.read_excel(input_file, sheet_name='january_2013')
# 이동평균 열 추가 연습
# data_frame['Acc'] = data_frame['Sale Amount'].rolling(window=3).mean()
# print(data_frame)
# data_frame = data_frame[data_frame['Acc'] != 'Null']
# print(data_frame)

writer = pd.ExcelWriter(output_file)

data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()