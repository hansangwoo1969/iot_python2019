#coding: cp949

print("문 1")
avg =(80+75+55)/3
print(avg)

print("\n 문 2 ")
print(13%2)

print("\n문3")
pin = "881120-1068234"
yymmdd=pin[:6]
num=pin[7:]
print(yymmdd)
print(num)

print ("\n문 4")
pin = "881120-1068234"
print(pin[7])

print ("\n문 5") 
a="a:b:c:d"
b=a.replace(':','#')
print(b)

print ("\n문 6")
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

print("\n문 7")
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

print("\n문 8")
a=(1,2,3)
a = a + (4,)
print(a)

print("\n문 9")
a = dict()
#a[[1]]='python'    # unhashable type: 'list'

print("\n문 10")
a={'A':90, 'B':80, 'C':70}
result=a.pop('B')
print(result)
print(a)

print("\n문 11")
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet= set(a)
print(aSet)
b=list(aSet)
print(b)

print("\n문 12")
a = b = [1,2,3]
a[1] = 4
print(b)
id(a)
id(b)

