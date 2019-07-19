# 문자열 a:b:c:d  -> a#b#c#

str1 = "a:b:c:d"
temp = str1.split(':')
str2 = "#".join(temp)
print(str2)
