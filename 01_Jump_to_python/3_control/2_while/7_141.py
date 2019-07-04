#coding: cp949

total = 0
for i in range(10):
#    print(i, end = ' ')
    print("%d"%i, end = ' ')
    total = total + i
print("\t\t => total: %d"%total)

total = 0
for i in range(1,11):
    print(i, end= ' ')
    total += i
print("\t\t => total: ", total)

total = 0
for i in range(1,11, 2):
    print(i, end= ' ')
    total += i
print("\t\t => total: ", total)

