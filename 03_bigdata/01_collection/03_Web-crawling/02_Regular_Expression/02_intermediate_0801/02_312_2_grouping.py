import re

p = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')   # 문자열 단위의 반복, 1회이상
m = p.search('park 010-1234-1234')
print(m)
print(m.group(0))  # 그룹핑인덱스 0, 1, 0은 매치된 전체 문자열
# print(m.group(1))
