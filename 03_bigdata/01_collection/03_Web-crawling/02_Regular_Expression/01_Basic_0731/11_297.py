import re

p = re.compile('ab?c')  # ?바로앞의 문자를 0번 또는 1번 반복
m = p.match('ac')
print(m)
m = p.match('abc')
print(m)
m = p.match('abbc')
print(m)
m = p.match('abbbc')
print(m)
m = p.match('abcd')     #매칭이 된다. 2자리 3자리(c)
print(m)