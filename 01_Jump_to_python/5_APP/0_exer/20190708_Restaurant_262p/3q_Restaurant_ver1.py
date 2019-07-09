# Restaurant 클래스 생성

class restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print("\n저희 레스토랑 상호는 '{}', '{}' 전문점입니다.".format(self.name, self.type ))

    def open_restaurant(self):
        print("저희 '{}' 레스토랑 오픈 했습니다. 어서오세요".format(self.name))

restaurant_name = input("레스토랑 상호를 작명하세요: ")
cuisine_type = input("요리유형을 입력하세요: ")

a = restaurant(restaurant_name, cuisine_type)
a.describe_restaurant()
a.open_restaurant()