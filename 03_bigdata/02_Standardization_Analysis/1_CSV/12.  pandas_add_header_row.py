import sys
import pandas as pd
import glob
import os

# input_file = sys.argv[1]
# output_file = sys.argv[2]
input_file = "supplier_data_no_header_row.csv"
output_file = "./output_files/12pandas_reader_add_header_row.csv"

header_list = ['Supplier Name', 'Invoice Number',
               'Part Number', 'Cost', ' Purchase Date']
data_frame = pd.read_csv(input_file, header=None, names=header_list)
print(data_frame)
data_frame.to_csv(output_file, index=False)

