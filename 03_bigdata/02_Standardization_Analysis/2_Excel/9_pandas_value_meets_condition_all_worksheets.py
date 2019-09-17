import pandas as pd

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_file = 'sales_2013.xlsx'
output_file = 'output_files/9output_pandas.xls'

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)

row_output = []
for worksheet_name, data in data_frame.items():
    # row_output.append(data[data['Sale Amount'].replace('$','').replace(',','').astype(float) >2000.0])
    row_output.append(data[data['Sale Amount'].astype(float) > 2000.0])
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)

filtered_rows.to_excel(writer, sheet_name='sale_amount_gt_2000', index=False)

print(filtered_rows)

writer.save()