import re

p = re.compile('ca*t')  # a를 0 ~ 무한번 반복
m = p.match('ct')
print(m)
m = p.match('cat')
print(m)
m = p.match('caat')
print(m)

