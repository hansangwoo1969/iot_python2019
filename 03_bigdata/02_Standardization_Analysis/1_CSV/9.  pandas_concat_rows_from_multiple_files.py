import sys
import pandas as pd
import glob
import os

# input_file = sys.argv[1]
# output_file = sys.argv[2]
input_path = "."
output_file = "./output_files/9pandas_reader_concat_rows_from_multiple_files.csv"

all_files = glob.glob(os.path.join(input_path, 'sales_*'))

all_data_frames = []
for file in all_files:
    data_frame = pd.read_csv(file, index_col=None)
    # data_frame = pd.read_csv(file)  # 위의 내용과  동일, index대상이 되는 열이 없다(defalult).
    # print(data_frame)
    all_data_frames.append(data_frame)
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index = False)
