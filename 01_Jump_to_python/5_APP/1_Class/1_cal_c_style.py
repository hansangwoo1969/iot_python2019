result1=0
result2=0
result3=0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

def add3(num):
    global result3
    result3 += num
    return result3

print("result1 # 1더하기: {0}".format(add1(1)))
print("result1 # 2더하기: {0}".format(add1(2)))

print(f"result2 # 3더하기: {add2(3)}")
print(add2(4))

print(add3(5))
print(add3(6))