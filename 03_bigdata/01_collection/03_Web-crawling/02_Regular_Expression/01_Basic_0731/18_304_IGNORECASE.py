import re

# original_text = "a\nb"
original_text = """a
b"""
p = re.compile('[a-z]', re.I)  # [a-z]는 소문자를 의미하나, re.I에 의해 대소문자 무시
p.match('python')
p.match('Python')
p.match('PYTHON')

print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))
