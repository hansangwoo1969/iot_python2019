# 문자열 압축하기     =================== 코딩도장에서 정답 copy ======================
# 입력예시 aaabbcccccca
# 출력예시 a3b2c6a1

# raw_string = 'aaabbcccccca'
#
# result = raw_string[0]  # 첫번째 값을 결과에 넣는다
# # print(result)         # a
# # print(result[-1])     # a
# count  = 0   #
#
# for i in raw_string:
#     if i == result[-1]:  #
#         count += 1
#     else:
#         result += str(count) + i
#         count = 1
# result += str(count)
#
# print(result)

print("=== 2안 문수 코드 ===")
# input1 = input('문자열을 입력하세요: ')
input1 = 'aaabbcccccca'
check = ''
c = 0
result = 0

check = check + input1[0]
check = input1[c]

while c < len(input1):
    if check == input1[c]:
        result = result+1
        c = c+1
        if c >= len(input1):
            print(f'{check}{result}', end='')
            break
        elif check != input1[c]:
            print(f'{check}{result}', end='')
    else:
        check = input1[c]
        result = 0

