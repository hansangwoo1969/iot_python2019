# 3가지 인스턴스 만들고, describe_restaurant()함수를 각 개체에서 초출
# 클래스에 __del__(self)소멸자를 정의하여 영업종료 메세지를 출력

class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print("\n저희 레스토랑 상호는 '{}', '{}' 전문점입니다.".format(self.name, self.type ))

    def open_restaurant(self):
        print("저희 '{}' 레스토랑 오픈 했습니다.".format(self.name))

    def __del__(self):
        print("{} 레스토랑 문 닫습니다".format(self.name))

restaurant = []

for i in range(3):
    name, type = (input("레스토랑 이름과 요리 종류를 선택하세요(공백으로 구분): ").split(" "))
    restaurant.append(Restaurant(name, type))
    restaurant[i].describe_restaurant()
    restaurant[i].open_restaurant()

print("저녁 10시가 되었습니다.")
# 삭제되기 때문에 뒤의 인덱스는 계속 없어짐. (out of range 오류원인)
# 반복해서 첫번째에 있는 항목만 삭제해 주면 됨.
for i in range(len(restaurant)):
    del restaurant[0]