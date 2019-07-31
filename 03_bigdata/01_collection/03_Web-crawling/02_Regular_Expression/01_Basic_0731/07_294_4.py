import re

print("dot ==============")
p = re.compile('.') # 모든 문자 클래스와 매칭이  된다
                    # []문자열 클래스가 아닌 일반 문법으로 사용했을 경우
                    #  '.'은 모든 문자열와 매칭이 된다
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
m = p.match('1')


print("=== + ===== 1번 이상 반복")
p = re.compile('ca+t')
m = p.match('ct')
print(m)
m = p.match('cat')
print(m)
m = p.match('caat')
print(m)

p  = re.compile('goo+gle')
m = p.match('google')
print(m)
m = p.match('goooooooogle')
print(m)
p = re.compile('a.b')
m = p.match('aab')
print(m)
m = p.match('a0b')
print(m)
m = p.match('abc')  # a와 b사이에 문자가 있어야,,,
print(m)

p = re.compile('a[.]b') # 문자열 클래스 안의 dot은 특수문자 . 그 자체를 ㅇ으미
m = p.match('aab')
print(m)
m = p.match('a0b')
print(m)
m = p.match('abc')
print(m)
print(" === ..[.]")
p = re.compile('a..[.]txt')
m = p.match('aab.txt')
print(m)
m = p.match('a1.txt')
print(m)
print("======== ...")
p = re.compile('...')  # 모든 문자클래스와 매칭이 된다
m = p.match('dad')
print(m)
m = p.match('Hi!  dad')
print(m)
m = p.match('pen.')
print(m)

print("==== ....")
p = re.compile('....')
m = p.match('pen.')
print(m)
m = p.match('pen!')   # 매칭이 된다. '.'는 모든 문자열 클래스이기 때문이다
print(m)              # 하지만 '.'문자열 자체를 필터링 하는 조건으로는 사용할 수 없다
print("===== [.]")
p = re.compile('pen[.]') # '.'를 메타문자가 아닌 고유의 문자의미로 정규식을 사용하고 싶다면,
m = p.match('pen!')      # '.'를 문자열 클래스 안에서 사용해야 한다.
print(m)                 # 따라서 pen!는 '.'로 끝나지 않았기 때문에 매칭이 안된다



