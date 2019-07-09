# 객체 생성시 number_served 값을 "고객서빙 현황로그.txt"(초기값은 0)에  저장된 값을 읽어와서 세팅
# 고객서빙현황로그에는  지금까지 누적고객수가 저장되어 있어야
# 당일 고객수는 todays_customer라는 클래스 멤버 변수에 저장
# 당일 서빙한 고객은 increment_number_served(number)에서 todays_customer 변수에 누적시키고
# 프로그램 종료시 소멸자에서 최종 number_served값과 todays_customer의 값을 더해서 저장
# Restaurant 클래스 생성
number_served = 0
with open("고객서빙현황로그.txt", "w", encoding='UTF-8') as f:
    f.write(str(number_served))



#number_served = 0

class Restaurant:

    def __init__(self, name, type, number_seved, todays_customer):
        self.name = name
        self.type = type
        self.number_served = number_served
        self.todays_customer = 0

    def describe_restaurant(self):
        print("\n저희 레스토랑 상호는 '{}', '{}' 전문점입니다.".format(self.name, self.type ))
        # input("레스토랑을 오픈하시겠습니까?(y/n) ")

    def open_restaurant(self):
        print("저희 '{}' 레스토랑이 오픈 했습니다.".format(self.name))

    def reset_number_served(self, number):
        #number = 0
        print("손님카운팅을  {}으로 초기화 하였습니다.".format(number))

    def increment_number_served(self, number):
        print("손님 {}명 들어오셨습니다. 자리를 안내해 드리겠습니다.".format(number))


    def check_customer_number(self):
        print("지금까지 총 {}명 손님께서 오셨습니다.".format(number_served))

    def __del__(self):
        print("{} 레스토랑 문 닫습니다".format(self.name))

restaurant_name,cuisine_type = input("레스토랑 상호와 요리 종류를 입력하세요(공백으로 구분) : ").split()

restaurant = Restaurant(restaurant_name, cuisine_type, number_served)
restaurant.describe_restaurant()
open_or_close = input("레스토랑을 오픈하시겠습니까?(y/n) ")

if open_or_close == 'y':
    restaurant.open_restaurant()

    while True:
        manual_choice = input("어서오세요. 몇 명이십니까? (초기화:0, 종료:-1, 누적고객확인:p :  ")
        if manual_choice == '0':
            number_served = 0
            restaurant.reset_number_served(number_served)
            continue
        elif manual_choice == '-1':
            # del restaurant
            break
        elif manual_choice == 'p':
             restaurant.check_customer_number()
        else:
            restaurant.increment_number_served(manual_choice)
            # number_served += int(manual_choice)
            todays_customer += int(manual_choice)
            continue
else:
    del restaurant
