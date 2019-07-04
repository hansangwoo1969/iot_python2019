#coding: cp949

coffee = 3
money = 0
coffee_price = 300

while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == coffee_price:
        print("커피를 줍니다")
        coffee = coffee - 1
    elif money > coffee_price:
        print("커피를 줍니다")
        print("거스럼돈 %d를 줍니다."% (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        
    print("남은 커피의 양은 %d개 입니다." % coffee)

    if coffee == 0:
        print("커피가 다 떨어 졌습니다. 판매를 중지합니다")
        break

    

