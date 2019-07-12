import  sys
# C:\iot_bigdata\python_workspace\01_Jump_to_python\5_APP\0_exer\20190710_263p

# print(sys.argv[1])
list=sys.argv[1:]

sum=0
for i in list:
    sum += int(i)

print(sum)