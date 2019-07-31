import re

p = re.compile("^python\s\w+")  # python으로 시작, 공백, [a-zA-Z0-9]+ ,,,

dest_str = """python one
life is too short
python two
you need python
python three"""

print(p.findall(dest_str))

p = re.compile("^python\s\w+", re.MULTILINE)  # 라인마다] python으로 시작, 공백, [a-zA-Z0-9]+ ,,,
print(p.findall(dest_str))