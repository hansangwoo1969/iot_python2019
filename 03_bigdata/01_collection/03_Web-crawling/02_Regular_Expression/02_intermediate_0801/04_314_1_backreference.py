import re

p = re.compile(r'(\b\w+)\s+\1')   # 1번그룹을 재참조
m = p.search('Paris in the the spring. It It was really great').group()
print(m)
# print(m.group(0))  # 그룹인덱스 0은 매치된 전체 문자열
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))
# print(m.group(4))
# print(m.group(5))
