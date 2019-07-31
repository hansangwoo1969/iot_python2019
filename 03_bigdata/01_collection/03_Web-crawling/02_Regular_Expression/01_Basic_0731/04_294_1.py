import re

p = re.compile('[a-c]')  # abc중 한 문자로 시작
m = p.match('apple')
print(m)
m = p.match('travel')
print(m)

p = re.compile('[a-z]')
m = p.match('travel')
print(m)

p = re.compile('[a-z]')  # 알파벳 소문자가 첫 문자
m = p.match('Travel')
print(m)

p = re.compile('[a-zA-Z]')
m = p.match('Travel')
print(m)

p = re.compile('[0-9]')
m = p.match('1st')
print(m)

p = re.compile('[0-9]')
m = p.match('2nd')
print(m)

p = re.compile('[^0-9]')
m = p.match('iris2019')
print(m)

p = re.compile('[^0-9]')    #
m = p.match('2iris2019')
print(m)

p = re.compile('^h')     # 시작이 알파벳 소문자 h
m =p.match('han')
print(m)