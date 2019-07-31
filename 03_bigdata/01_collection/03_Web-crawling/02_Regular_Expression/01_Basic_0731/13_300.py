import re

p = re.compile('[a-z]+') # 문자 1번이상
m = p.match('3python')  # match는 시작을 엄격하게,,
print(m)

p = re.compile('[a-z]+')
m = p.search('3 python')  # 문자열 중에 매치되는 구간을 반환
print(m)