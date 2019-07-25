# coding:cp949

import json
news_domain_all_list = []
err_domain = 0
num_of_domain = 0
num_of_news_by_press = {}
crop_domain_list = []

with open('아베_naver_news.json', encoding='UTF8') as f:
    data = json.loads(f.read())
    num_of_data = len(data)
    # print(data)
    # print(data[5]['org_link'].split('/')[2])
# 도메인리스트 전체 취합 ======================================
for i in range(num_of_data):
    if data[i]['org_link'] != "":
        # print(data[i]['org_link'].split('/')[2])
        news_domain_all_list.append(data[i]['org_link'].split('/')[2])
        num_of_domain += 1
    else:
        # print(data[i]['org_link'].split('/')[2])
        err_domain += 1

# 도메인 리스트 정리_중복제거, www.제거==================================
unique_domain_list = set(news_domain_all_list)
for i in unique_domain_list:
    if 'www' in i:
        crop_domain_list.append(i[4:])
    else:
        crop_domain_list.append(i)

# 딕셔너리 추가 =========================================================
for media in crop_domain_list:
    article_count = 0
    for i in range(num_of_data):
        if media in data[i]['org_link']:
            article_count += 1
        else:
            continue
    # print(media, article_count)
    # num_of_news_by_press.items(media, article_count)
    num_of_news_by_press[media] = article_count
# print(num_of_news_by_press)

# 딕셔너리 값을 기준으로 내림차순 정렬====================================
Snum_of_news_by_press = sorted(num_of_news_by_press.items(), key=lambda x: x[1], reverse=True)
# print(Snum_of_news_by_press)
# for i in Snum_of_news_by_press:
#     print(" >> %s : %s" % (i.key(),i.val))
# print(unique_domain_list)
print("검색어: 아베")
print("전체 도메인수: %s" % len(unique_domain_list))  # 도메인수 리스트 -> set
print("전체건수: %s" % num_of_domain)
print("부정확한 데이터 수: %s" % err_domain)
print(" - 도메인 별 뉴스 기사 분석 ")
for i in Snum_of_news_by_press:
    print("  >> %s: %s건" % (i[0], i[1]))



