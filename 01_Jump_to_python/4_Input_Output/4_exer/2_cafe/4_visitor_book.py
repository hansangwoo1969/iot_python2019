# 방명록 작성하기

base = """
임꺽정 900327
홍길동 871021
"""

# f = open("./visitor.txt", 'w')
# f.write(base)
# f.close()

name = input("이름을 입력하세요: ")

def search(name):
    with open("./visitor.txt", 'r') as f :
        if f.read().find(name) != -1:
            print("{0}님 다시 방문해 주셔서 감사합니다. 즐거운 시간 되세요.".format(name))
            return
        else:
            born_date = input("생년월일을 입력하세요.")
            register(name, born_date)

def register(name, borndate):
    print("{0}님 환영합니다. 아래 내용을 입력하셨습니다.".format(name))
    print("{0} {1}".format(name, borndate))
    with open("./visitor.txt",'a') as f:
        f.write("{} {}".format(name, borndate))

search(name)



