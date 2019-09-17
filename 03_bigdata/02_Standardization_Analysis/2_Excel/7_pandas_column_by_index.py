import pandas as pd

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_file = 'sales_2013.xlsx'
output_file = 'output_files/7output_pandas.xls'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_column_by_index = data_frame.iloc[:, [1, 4]]

writer = pd.ExcelWriter(output_file)

data_frame_column_by_index.to_excel(writer, sheet_name='jan_13_output', index=False)
# 엑셀에서의 날짜열의 기본값은 년월일시분초임_ 필요시 엑셀에서 날짜서식을 변경하고,
# 코드로 읽어온 데이터프레임의 기본값은 년월일로 조회됨,
print(data_frame_column_by_index)

writer.save()