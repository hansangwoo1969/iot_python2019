# 목적: 날짜 형식 할당
import pandas as pd

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_file = 'sales_2013.xlsx'
output_file = 'output_files/4output_pandas.xls'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]
# print(data_frame_value_meets_condition)
writer = pd.ExcelWriter(output_file)

data_frame_value_meets_condition.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()