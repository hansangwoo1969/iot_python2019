import re

p = re.compile('blue|white|red')
print(p.sub('colour', 'blue socks and red shoes'))
print(p.sub('colour', 'blue socks and red shoes', count=1))
print(p.sub('colour', 'blue socks and red shoes',count=2))
print(p.subn('colour', 'blue socks and red shoes'))



# file_name_list = ["foo.bar", "autoexec.bat", "sendmaail.cf"]
# p = re.compile(".*[.][^b].*$"