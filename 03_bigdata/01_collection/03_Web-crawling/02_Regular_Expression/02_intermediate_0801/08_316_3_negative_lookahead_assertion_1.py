import re

file_name_list = ["foo.bar", "autoexec.bat", "sendmaail.cf"]
p = re.compile(".*[.].*$")

for file_name in file_name_list:
    print(p.search(file_name))

