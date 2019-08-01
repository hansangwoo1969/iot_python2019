import re

# '이름 + 전화번호'   => '전화번호 + 이름' 으로 순서바꾸기

p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(p.sub("\g<phone> \g<name>", "park 010-1234-4567"))   # 이름으로 순서 변경
print(p.sub("\g<2> \g<1>", "park 010-1234-4567"))          # 참조번호를 가지고 순서 변경
