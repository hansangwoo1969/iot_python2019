# DashInsert함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두수 사이에 -추가
# 짝수가 연속되면 *를 추가하는 기능,   DashInsert함수 완성하기
# 4546792
# 454*67-9-3

# print("=== 1안 내가 만든 함수 ===")
# def DasdhInsert(a):
#     for i in range(len(a) - 1):
#         print(a[i], end='')
#         if (int(a[i]) % 2 == 0) and (int(a[i + 1]) % 2 == 0):
#             print("*", end='')
#         elif (int(a[i]) % 2 == 1) and (int(a[i + 1]) % 2 == 1):
#             print("-", end='')
#
#     print(a[-1], end='')
#
# a = input("숫자를 입력하세요: ")
# DasdhInsert(a)

print("=== 2안 교재 풀이===")
data = "4546793"
# print(data)
# print(type(data))
numbers = list(map(int, data))                         # 숫자문자열을 숫자 리스트로 변경
# print(numbers)
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:                             # 다음수가 있다면
        is_odd = num % 2 == 1                          # 현재 수가 홀수
        is_next_odd = numbers[i+1] % 2 == 1            # 다음수가 홀수
        if is_odd and is_next_odd:                     # 연속홀수
            result.append("-")
        elif not is_odd and not is_next_odd:           # 연속짝수
            result.append("*")

print("".join(result))

