# coding:cp949

import json
news_domain_all_list = []
err_domain = 0
num_of_domain = 0
num_of_news_by_press = {}
crop_domain_list = []

with open('�ƺ�_naver_news.json', encoding='UTF8') as f:
    data = json.loads(f.read())
    num_of_data = len(data)
    # print(data)
    # print(data[5]['org_link'].split('/')[2])
# �����θ���Ʈ ��ü ���� ======================================
for i in range(num_of_data):
    if data[i]['org_link'] != "":
        # print(data[i]['org_link'].split('/')[2])
        news_domain_all_list.append(data[i]['org_link'].split('/')[2])
        num_of_domain += 1
    else:
        # print(data[i]['org_link'].split('/')[2])
        err_domain += 1

# ������ ����Ʈ ����_�ߺ�����, www.����==================================
unique_domain_list = set(news_domain_all_list)
for i in unique_domain_list:
    if 'www' in i:
        crop_domain_list.append(i[4:])
    else:
        crop_domain_list.append(i)

# ��ųʸ� �߰� =========================================================
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

# ��ųʸ� ���� �������� �������� ����====================================
Snum_of_news_by_press = sorted(num_of_news_by_press.items(), key=lambda x: x[1], reverse=True)
# print(Snum_of_news_by_press)
# for i in Snum_of_news_by_press:
#     print(" >> %s : %s" % (i.key(),i.val))
# print(unique_domain_list)
print("�˻���: �ƺ�")
print("��ü �����μ�: %s" % len(unique_domain_list))  # �����μ� ����Ʈ -> set
print("��ü�Ǽ�: %s" % num_of_domain)
print("����Ȯ�� ������ ��: %s" % err_domain)
print(" - ������ �� ���� ��� �м� ")
for i in Snum_of_news_by_press:
    print("  >> %s: %s��" % (i[0], i[1]))



