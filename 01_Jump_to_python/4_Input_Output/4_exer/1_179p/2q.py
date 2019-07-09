# 입력으로 들어오는 모든수의 평균값을 계산하는 함수 작성 (입력으로 들어오는 수의 개수는 정해 지지 않음)

def avg_numbers(*args):
    result = 0

    for i in args:
        result += i
    return (result/len(args))

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))