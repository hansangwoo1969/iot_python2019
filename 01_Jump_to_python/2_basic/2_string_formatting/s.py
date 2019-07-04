# coding: cp949

print("I eat %d apples."%3) # 포맷스트링 결과를 바로 print

str = " In addition, I eat %d bananas"%2 
# 포맷 스트링은 문자열의 기능을 확장하는 파이썬 문법
print(str)

number = 4
print("Further more, I eat %d mangoes" %number)

number = "five"
print("Moreover, I eat %s tangerine" % number)

number = 0.25
print("At the end, I eat %s melon" %number)
# %s는 기본적으로 문자열을 지원하지만 모든 형에 사용할 수 있다.

print("My Satisfaction Rate for the dessert is 98%")
# 포맷팅연산자 %d와 %를 같이 쓸때는 %%를 쓴다.
print("My Satisfaction Rate for the dessert is %d%%"%98)


