import re

p = re.compile('ca+t')  # 문자 a, 1회이상 반복,  0회는 안됨
m = p.match('ct')
print(m)
m = p.match('cat')
print(m)
m = p.match('caat')
print(m)

p  = re.compile('goo+gle')  # 헷갈릴 수 있어 명확한 이해 필요
m = p.match('gogle')  # 최소 직전문자인 o가 하나는 있어야
print(m)
m = p.match('goooooooogle')
print(m)
