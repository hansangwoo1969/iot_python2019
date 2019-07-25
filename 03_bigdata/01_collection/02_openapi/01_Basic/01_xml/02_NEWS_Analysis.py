import json

news_domain_all_list = []
domain_info_list = []
num_of_corrupted_data=0

with open("아베_naver_news_1.json", encoding="utf-8") as json_data:
    json_data_load = json.load(json_data)
    json_data_string = json.dumps(json_data_load)
    jsonResult = json.loads(json_data_string)
print("데이터 분석을 시작합니다..")

# news_domain_all_list 수집
for i in range(900):
    print(jsonResult[i]['org_link'].split('/')[2])
# news_domain_unique_list 생성
# news_domain_unique_list=

# total_count=0

# domain_info_list 수집

# 내림 차순 소팅
# sorted_num_of_domain_info =

# 분석 정보 출력

# 내림 차순 출력
