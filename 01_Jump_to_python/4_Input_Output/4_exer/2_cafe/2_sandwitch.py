# 샌드위치 만들기

base = '''
안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.
1. 주문
2. 종료
입력: '''

def input_ingredient():
    ingredient_list=[]
    while True:
        ingredient = input("원하는 재료를 입력하세요: ")
        ingredient_list.append(ingredient)
        if ingredient == "":

            return ingredient_list

def make_sandwitch(ingredient_list):
    print("샌드위치를 만들겠습니다.")
    for i in ingredient_list:
        print("%s를 추가합니다"% i)
    print("여기 주문하신 샌드위치를 만들었습니다. 맛있게 드세요")

while True:
    welcome = int(input(base))
    if welcome == 2:
        break
    list = input_ingredient()
    make_sandwitch(list)
