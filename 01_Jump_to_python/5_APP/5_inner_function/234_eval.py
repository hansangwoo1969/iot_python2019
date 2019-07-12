# 실행가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값을 반환

print("미니 계산기 ver1.0]\n")

while True:

    formula = input("  아래에 연산 수식을 입력하시고 Enter를 치세요. 수식을 계산해 드립니다.")
    print(eval(formula))
    if formula == "":
        break
