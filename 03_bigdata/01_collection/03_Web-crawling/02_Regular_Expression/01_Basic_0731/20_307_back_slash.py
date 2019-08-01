import re

# p  = re.compile('\')  <= 정규식으로 표현이 불가능하다.
# p = re.compile('\\')   # 정규식으로 표현이 불가능
p = re.compile('\\\\')
m = p.match('\\section')
print(m)

p = re.compile(r'\\section')  #  정확한 이해 필요,,,,,,, 숙지할 것,,,
m = p.match('\section')
print(m)
