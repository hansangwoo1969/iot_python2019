# coding: cp949
# 공원요금계산 프로그램 ver1
#
#    0 ~   3세 :   무료
#    4 ~  13세 : 2000원
#    14 ~ 18세 : 3000원
#    19 ~ 65세 : 5000원
#    66세 ~    : 무료
#    [화면 출력]
#    나이를 입력하세요.
#    요금은 []원 입니다.

age = int(input("나이를 입력하세요: "))

if (age>=0 and age <= 3) or age >= 66:
    print("요금은 %d원 입니다."% 0)
elif age >=4 and age <= 13:
    print("요금은 %d원 입니다." % 2000)
elif age >= 14 and age <= 18:
    print("요금은 %d원 입니다." % 3000)
elif age >= 19 and age <= 65:
    print("요금은 %d원 입니다." % 5000)
