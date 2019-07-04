#coding: cp949

#step 1] 파이썬 기본문법
a = [1,2,3,4]
result = []

for num in a:
    result.append(num*3)

print(result)

#step 2] 파이썬 list comprehension
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

#step 3] 파이썬 list comprehension
a = [1,2,3,4]
result = [num*3 for num in a if num % 2 == 0]
print(result)

result = [ x*y for x in range(2,10)
        for y in range(1,10)]
print(result)
