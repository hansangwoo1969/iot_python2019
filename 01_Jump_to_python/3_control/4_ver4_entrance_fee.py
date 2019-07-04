# coding: cp949
# (현금 /카드), 등급, 입장료

# 공원요금계산 프로그램 ver4

#    0 ~   3세 (유아) :   무료
#    4 ~  13세 (어린이) : 2000원
#    14 ~ 18세 (청소년) : 3000원
#    19 ~ 65세 (성인) : 5000원
#    66세 ~    (노인): 무료
#    [화면 출력]
#    나이를 입력하세요.
#    귀하는 []등급이며 요금은 []원 입니다.
#    요금유형을 선택하세요(1:현금, 2: 공원전용 신용카드
#    1. 현금인 경우
#    요금을 입력하세요
#        금액미만일 경우: " []이 모자랍니다. 입력하신 []를 반환합니다."
#        금액일치하는 경우: " 감사합니다. 티켓을 발행 합니다."
#        금액을 초과하는 경우: "감사합니다. 티켓을 발행하고 거스름돈 []를 반환합니다."
#    2. 공원전용 신용카드(결제금액의 10%할인, 60~65세 장년은 추가 5%할인)
#      []원 결제 되었습니다. 티켓을 발행 합니다.

count = 0
while True:
    age = int(input("나이를 입력하세요: "))

# age classification
    infant = (age >= 0) and (age <= 3)
    child = (age >= 4) and (age <= 13)
    youth = (age >= 14) and (age <= 18)
    adult = (age >= 19) and (age <= 65)
    aged_man = (age >= 66)

# price by age
    infant_price = 0
    child_price = 2000
    youth_price = 3000
    adult_price = 5000
    aged_man_price = 0


    if infant:
        print("귀하는 [%s]등급이며, 요금은 [%d원] 입니다."% ("유아", infant_price))
        continue
    elif child:
        print("귀하는 [%s]등급이며, 요금은 [%d원] 입니다." % ("어린이", child_price))
    elif youth:
        print("귀하는 [%s]등급이며, 요금은 [%d원] 입니다." % ("청소년", youth_price))
    elif adult:
        print("귀하는 [%s]등급이며, 요금은 [%d원] 입니다." % ("성인", adult_price))
    elif aged_man:
        print("귀하는 [%s]등급이며, 요금은 [%d원] 입니다." % ("노인", aged_man_price))
        continue
    else:
        print("다시 입력 하세요")


    payment_type = int(input("지불방법을 선택하세요 (1:현금, 2:공원 전용 신용카드): "))

    if payment_type == 1:
        my_cash = int(input("지불금액을 입력하세요: "))

        if child and (my_cash < child_price):
            print(" [%d원]이 모자랍니다. 입력하신 [%d원]을 반환 합니다."%(child_price - my_cash, my_cash))
        if youth and (my_cash < youth_price):
            print(" [%d원]이 모자랍니다. 입력하신 [%d원]을 반환 합니다."%(youth_price - my_cash, my_cash))
        if adult and (my_cash < adult_price):
            print(" [%d원]이 모자랍니다. 입력하신 [%d원]을 반환 합니다."%(adult_price - my_cash, my_cash))

        if child:
            if my_cash == child_price:
                print("감사합니다. 티켓을 발행 합니다.")
            elif my_cash > child_price:
                print("감사합니다. 티켓을 발행하고, 거스름돈 [%d원]을 반환합니다."%(my_cash - child_price))
        if youth:
            if my_cash == youth_price:
                print("감사합니다. 티켓을 발행 합니다.")
            elif my_cash > youth_price:
                print("감사합니다. 티켓을 발행하고, 거스름돈 [%d원]을 반환합니다."%(my_cash - youth_price))
        if adult_price:
            if my_cash == adult_price:
                print("감사합니다. 티켓을 발행 합니다.")
            elif my_cash > adult_price:
                print("감사합니다. 티켓을 발행하고, 거스름돈 [%d원]을 반환합니다."%(my_cash - adult_price))
        count += 1

    if payment_type == 2:
        if child:
            print("[%.0d원] 결제 되었습니다. 티켓을 발행합니다."%(child_price*.9))
        if youth:
            print("[%.0d원] 결제 되었습니다. 티켓을 발행합니다."%(youth_price*.9))
        if adult:
            if age>=60 and age<=65:
                print("[%.0d원] 결제 되었습니다. 티켓을 발행합니다."%(adult_price*.9*.95))
            else:
                print("[%.0d원] 결제 되었습니다. 티켓을 발행합니다." % (adult_price * .9))
        count += 1

    print("회원수: %d"%count)
    if count == 3:
        break
