import re

p = re.compile(".+:")
m = p.search('http://google.com')


print(m.group())
print(m.group('second_number'))
# print(m.group('t/hird_number'))
# print(m.group(3))
# print(m.group(0))
# print(m.group('firs/t_number'))
