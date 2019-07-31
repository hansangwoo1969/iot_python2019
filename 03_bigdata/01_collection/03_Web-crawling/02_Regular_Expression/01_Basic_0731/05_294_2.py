import re

original_text ="""a1 adggfdfgdgd
b3  gdfgghdfdaads
3k gdfasasfa
5j fgfgse
u9 ggdfhhhg
"""

p = re.compile('[a-zA-Z0-9][0-9]') # 첫문자는 알파벳이나 숫자, 두번째 문자는 숫자
m = p.match(original_text)
print(m)