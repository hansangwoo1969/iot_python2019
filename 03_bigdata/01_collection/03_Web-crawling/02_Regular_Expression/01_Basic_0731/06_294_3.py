import re

p  = re.compile('[\d]')  # [0-9]
m = p.match('1')
print(m)
m = p.match('5')
print(m)
m = p.match('a')
print(m)

Vp  = re.compile('[\D]')  # [^0-9]
m = p.match('1')
print(m)
m = p.match('5')
print(m)
m = p.match('a')
print(m)

print("=== '[\s]'====")
p  = re.compile('[\s]')  # [ ] or re.compile(' ')
m = p.match('1')
print(m)
m = p.match(' 1')
print(m)
m = p.match('   1') # \t
print(m)
m = p.match('''
1''')  # \n 개행문자는 공백문자가 아니다.

print("===='[\w]'====")
p  = re.compile('[\w]')  # [a-zA-Z0-9]
m = p.match('1')
print(m)
m = p.match('a')
print(m)
m = p.match('K')
print(m)
m = p.match('-')
print(m)
m = p.match('$')
print(m)
m = p.match(' ')
print(m)

