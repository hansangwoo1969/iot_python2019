import re

print(re.search('short$', 'life is too short'))
print(re.search('life$', 'life is too short'))
print(re.search('too$', 'life is too short'))

print(re.search('short$', 'life is too short, you need python'))

print("==== \\b ==")
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

print("==== \B ")
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))

