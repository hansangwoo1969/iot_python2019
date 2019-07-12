# 첫항 0, 두번째 항 1, 이후의 항은 이전의 두항을 더한 값
# 0, 1, 1, 2, 3, 5, 8, 13,
# 정수 n을 입력 받았을 때 n이하까지의 수열을 출력하는 함수 구하기

print("=== 1안 반복문 활용 ====")
limt_num = int(input("정수를 입력하세요: "))
second_to_last = 0
last = 1

while last < limt_num:
    print(last, end=' ')
    temp = second_to_last
    second_to_last = last
    last = temp + second_to_last

print("=== 2안 답지(FIBONACCI) ====")

def fib(n):
    if n == 0: return 0     # n이 0일 때는 0을 반환
    if n == 1: return 1     # n이 1일 때는 1을 반환
    return fib(n-2) + fib(n-1)  # n이 2 이상일 때는 그 이전의 두 값을 더하여 반환

for i in range(limt_num):
    print(fib(i))
