import sys
import pandas as pd
import glob
import os

# input_file = sys.argv[1]
# output_file = sys.argv[2]
input_file = "supplier_data_unnecessary_header_footer.csv"
output_file = "./output_files/11pandas_reader_select_continuous-rows.csv"

data_frame = pd.read_csv(input_file, header=None)
# print(data_frame)
data_frame = data_frame.drop([0, 1, 2, 16, 17, 18])
data_frame.columns = data_frame.iloc[0]  #
# print("===1===\n",data_frame)
data_frame = data_frame.reindex(data_frame.index.drop(3))
print("===2===\n",data_frame)
data_frame.to_csv(output_file, index=False)

