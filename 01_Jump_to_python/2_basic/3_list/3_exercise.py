#coding: cp949

print("�� 1")
avg =(80+75+55)/3
print(avg)

print("\n �� 2 ")
print(13%2)

print("\n��3")
pin = "881120-1068234"
yymmdd=pin[:6]
num=pin[7:]
print(yymmdd)
print(num)

print ("\n�� 4")
pin = "881120-1068234"
print(pin[7])

print ("\n�� 5") 
a="a:b:c:d"
b=a.replace(':','#')
print(b)

print ("\n�� 6")
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

print("\n�� 7")
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

print("\n�� 8")
a=(1,2,3)
a = a + (4,)
print(a)

print("\n�� 9")
a = dict()
#a[[1]]='python'    # unhashable type: 'list'

print("\n�� 10")
a={'A':90, 'B':80, 'C':70}
result=a.pop('B')
print(result)
print(a)

print("\n�� 11")
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet= set(a)
print(aSet)
b=list(aSet)
print(b)

print("\n�� 12")
a = b = [1,2,3]
a[1] = 4
print(b)
id(a)
id(b)

