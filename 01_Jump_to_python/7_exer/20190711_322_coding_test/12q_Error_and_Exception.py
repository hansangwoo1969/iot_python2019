# 실행결과를 예측하고 그 이유에 대해 설명,,
result = 0
try:
    [1, 2, 3][3]    # 처음막히는 곳에서 에러표시
    "a" + 1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)
