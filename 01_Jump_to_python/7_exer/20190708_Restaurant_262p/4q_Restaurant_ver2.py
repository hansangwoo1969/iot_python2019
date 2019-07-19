# 3가지 인스턴스 만들고, describe_restaurant()함수를 각 개체에서 초출
# 클래스에 __del__(self)소멸자를 정의하여 영업종료 메세지를 출력
# 잘못된 문제해결 안된 이유는, '4q_Restaurant_sungmin.py'보고 숙지할 것

class restaurant:                        # 클래스 이름은 대문자로 시작
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print("\n저희 레스토랑 상호는 '{}', '{}' 전문점입니다.".format(self.name, self.type ))

    def open_restaurant(self):
        print("저희 '{}' 레스토랑 오픈 했습니다.".format(self.name))

    def __del__(self):
        print("{} 레스토랑 문 닫습니다".format(self.name))

restaurant_names = []

for i in range(3):     # 3가지 인스턴스 만들어야 하는데,,, 반복하면서 인스턴스는 a하나임, 계속 덮어 쓸 뿐.
    name_and_cuisine = input("\n레스토랑 상호와 요리종류를 선정하세요: ")
    (restaurant_name, cuisine_type) = name_and_cuisine.split()
    restaurant_names.append(restaurant_name)
    a = restaurant(restaurant_name, cuisine_type)
    a.describe_restaurant()
    a.open_restaurant()

print(restaurant_names)

print("저녁 10시가 되었습니다.")
for nm in range(len(restaurant_names)):
    # print(nm)
    # b = restaurant(nm)
    del restaurant_names[0]



