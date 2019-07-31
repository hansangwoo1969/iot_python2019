import re

original_text = 'life is too short'
p = re.compile('[a-z]+') # 문자 1번이상
m = p.search(original_text)  # 찾는 값 중에 처음자료만 반환
print(m)

match_list = p.findall(original_text)  # 검색결과는 매칭된 문자열들을 리스트로 반환
print(match_list)
for match_element in match_list:
    print(match_element)
