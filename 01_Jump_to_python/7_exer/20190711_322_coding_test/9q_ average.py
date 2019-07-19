# 평균값 구하기

f = open("sample.txt", 'r', encoding='UTF-8')
data = f.readlines()
f.close()

sum=0
for i in range(len(data)):
    sum += int(data[i])
# print(sum)
average = sum / len(data)
# print("average = ", sum / len(data))
if len(data) > 0:
    with open('result.txt', 'w', encoding='UTF-8') as f:
        f.write(str(average))



