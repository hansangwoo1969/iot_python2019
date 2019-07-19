# 사용자로부터 단을 입력받아 해당숫자의 구구단을 한줄로 출력

dan = int(input("단을 입력하세요: "))

for i in range(1, 10):
    print(dan * i, end=' ' )