import pandas as pd

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_file = 'sales_2013.xlsx'
output_file = 'output_files/10output_pandas.xls'

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)

column_output = []
for worksheet_name, data in data_frame.items():
    column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
selected_columns = pd.concat(column_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)

selected_columns.to_excel(writer, sheet_name='selected_colums_all_worksheets', index=False)

print(selected_columns)

writer.save()