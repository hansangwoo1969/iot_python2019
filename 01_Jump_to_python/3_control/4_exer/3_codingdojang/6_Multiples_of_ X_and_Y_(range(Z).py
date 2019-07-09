# (ex: X:7, Y:9 Z: 10000 인 경우
# 1~10000 까지 7과 9의 공배수를 구함)
# 0이 프로그램 종료를 하도록 반복문으로 작성)

result = [ i for i in range(10000) if (i % 7 == 0) and (i % 9 == 0)]
print(result)
print(len(result))
