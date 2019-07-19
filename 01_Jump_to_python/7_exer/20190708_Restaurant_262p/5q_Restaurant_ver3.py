# ver1에서 기본값이 0인 number_served속성 추가, 이 클래스에서 restaurant객체를 만드시오
# Restaurant 클래스 생성

number_served = 0
class Restaurant:

    def __init__(self, name, type, number_seved):
        self.name = name
        self.type = type
        self.number_served = number_served

    def describe_restaurant(self):
        print("\n저희 레스토랑 상호는 '{}', '{}' 전문점입니다.".format(self.name, self.type ))
        # input("레스토랑을 오픈하시겠습니까?(y/n) ")

    def open_restaurant(self):
        print("저희 '{}' 레스토랑이 오픈 했습니다.".format(self.name))

    def reset_number_served(self, number):
        #number = 0
        print("손님카운팅을  {}으로 초기화 하였습니다.".format(number))

    def increment_number_served(self, number):
        print("손님 {}명 들어오셨습니다.".format(number))


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
            number_served += int(manual_choice)
            continue
else:
    del restaurant
