import re

p = re.compile('ca{2}t')  # {} 숫자가 한개만 올때는 해당 반복수를 정확히 지킨 문자열만 매칭이 된다.
m = p.match('ct')
print(m)
m = p.match('cat')
print(m)
m = p.match('caat')   # 해당문자 a 두번 반복,,, 매칭
print(m)
m = p.match('caaaat')
print(m)

p = re.compile('ca{2, 5}t')  # a가 2번이상, 5번이하 반복하고 뒤에 t,
m = p.match('ct')
print(m)
m = p.match('cat')
print(m)
m = p.match('caat')
print(m)
m = p.match('caaaaat')
print(m)
m=p.match('caaaaaaaaaat')
print(  "===")
print(m)

p  = re.compile('ca{2,}t')  # a가 2번이상 반복인  경우에 매칭이 된다.
m = p.match('cat')
print(m)
m = p.match('caat')
print(m)
m = p.match('caaaaat')
print(m)
m=p.match('caaaaaaaaaat')
print(m)

p=re.compile('ca{,5}t')  # a가 5이하 반복인 경우에 매칭이 된다.
m = p.match('cat')
print(m)
m = p.match('caat')
print(m)
m = p.match('caaaaat')
print(m)
m = p.match('caaaaaaaaaat')
print(m)


