import re

def hexrepl(match):
    "Return the hex string  for a decimal number"
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
m = p.sub(hexrepl, 'Call 65490 for printing, 49152 fo user code.')
print(m)