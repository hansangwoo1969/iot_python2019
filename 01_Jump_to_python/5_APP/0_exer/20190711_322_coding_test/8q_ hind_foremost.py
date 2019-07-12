# abc.txt자료를 역순 저장하기

print(" ===1안 [::-1]=== 읽고, 바꾸고, 저장")
f = open("abc.txt", 'r', encoding='UTF-8')
data = f.read()
f.close()

temp = data[::-1]
print(temp)

f = open('eee.txt', 'w', encoding='UTF-8')
f.write(temp)
f.close()

# print(" ===2안 답지 === ")
# f = open("abc.txt", 'r', encoding='UTF-8')
# lines = f.readlines()
# print(lines)
# f.close()
#
# print(lines)
# lines.reverse()
# print(lines)
# f = open('abc.txt', 'w', encoding='UTF-8')
# for line in lines:
#     line = line.strip()
#     f.write(line)
#     f.write('\n')
# f.close()

