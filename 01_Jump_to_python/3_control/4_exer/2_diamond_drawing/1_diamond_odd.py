# 홀수를 입력 하세요

col = int(input("밑변의 길이(홀수)를 입력하세요: "))

row = int((col/2)+1)
i = 1
print('-'*(col+8))
while row > 0 :
    print("|", " "*row, "*"*i, " " * row,"|")
    # print("|", end = '')
    # print(" "*row, end ='')
    # print("*" * i, end='')
    # print(" "*row, end= '')
    # print("|")
    row -= 1
    i += 2

i = i-2
row = row+1
while i > 0:
    print("|", " "* row, "*" * i, " "* (row-1), " |")
    # print("|", end='')
    # print(" " * row, end = ' ')
    # print("*" * i, end= ' ')
    # print(" " * (row-1), end = ' ')
    # print("|")
    row += 1
    i -= 2
print('-'*(col+8))




