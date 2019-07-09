print('작업1')
num1 = 2
num2 = 0
try:
    result = num1 / num2
    f = open('나없는 파일', 'r')
except ZeroDivisionError as e:
    print(e)
    print("알고리즘 수행을 생략하고 다음 단계 진행 합니다")
except FileNotFoundError as e:
    print(e)
    print("파일을 준비하고 다시 수행하십시오.")
finally:
    print("""예외가 발생하였습니다.
        준비된 알고리즘은 모두 수행되지 않았음을 알려 드립니다.""")

print('작업2')
print("정상종료")
