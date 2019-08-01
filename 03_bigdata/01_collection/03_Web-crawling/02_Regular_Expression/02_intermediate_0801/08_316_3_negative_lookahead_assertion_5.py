import re

file_name_list = ["foo.bar", "autoexec.bat", "sendmaail.cf"]
# p = re.compile(".*[.][^b].*$")
# p = re.compile(".*[.]([^b]..|.[^a].|..[^t])$")  # 첫번째 문자가 a가 아닌 문자로 시작 or 두번째 문자가 b가 아닌,
                                                # .cf
# p = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")  # 첫번째 문자가 a가 아닌 문자로 시작 or 두번째 문자가 b가 아닌,
# p = re.compile(".*[.](?!bat$).*$")  # 첫번째 문자가 a가 아닌 문자로 시작 or 두번째 문자가 b가 아닌,
p = re.compile(".*[.](?!bat$|bar$).*$")  # 확장자가 'bat','bar'이 아닌것
for file_name in file_name_list:
    print(p.search(file_name))

