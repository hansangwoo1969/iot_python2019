import re

p = re.compile('(ABC)+')   # 문자열 단위의 반복, 1회이상
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))  # 그룹인덱스 0은 매치된 전체 문자열


m = p.search('ABCABCAB OK?')
print(m)
print(m.group(0))

p = re.compile('(김혜경)+')
m = p.search('김혜경김혜경김혜경 OK?')
print(m)
print(m.group(0))

m = p.search('김혜경김혜경 우리 막내 김혜경!')
print(m.group(0))