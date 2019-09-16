# 분산 저장 v2
# 빅 데이터 수집부를 시뮬레이션 처리
import csv

output_file = '시뮬레이션_서울특별시_관광지별_방문객.csv'
simulation_count = 100

def  get_request_url():
    pass

def getTourPointVisitor():
    pass

def getTourPointData():
    filewriter.writerow(simulation_data)
    return

csv_out_file = open(output_file, 'w', newline='')
filewriter  = csv.writer(csv_out_file)
header_list = ['addrCd', 'gungu', 'sido', 'resnNm', 'rnum','csForCnt','csNatCnt']
simulation_data = ['1111', '종로구', '서울특별시', '창덕궁','1', '14137', '43677']
filewriter.writerow(header_list)

for index in range(simulation_count):
    getTourPointData()
csv_out_file.close()
