
# 주어진 자연수가 홀수 인지 짝수인지 판별해 주는 함수 작성

def is_odd(number):
    if number % 2 == 1:
        return  True
    else:
        return False

print(is_odd(8))