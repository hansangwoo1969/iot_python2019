import pandas as pd
import glob
import os

# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_path = '.'
output_file = 'output_files/13output_pandas.xls'

all_workbooks = glob.glob(os.path.join(input_path,  '*.xls*'))

data_frames = []
for workbook in all_workbooks:
    # all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
    all_worksheets = pd.read_excel(workbook, sheet_name=None)
    for worksheet_name, data in all_worksheets.items():
        data_frames.append(data)

all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)

print(all_data_concatenated)

writer.save()