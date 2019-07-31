import re

p = re.compile('[a-z]+') # 문자 1번이상
m = p.match('python')  # match는 시작을 엄격하게,,
print(m)
if m:
    print('Match found:', m.group())
else:
    print('No match')

p = re.compile('[a-z]+')
m = p.match('3python')
print(m)