# 0~9의 문자로 된 숫자를 입력 받았을 때 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지
# 확인하는 함수를 작성하시오
# 입력예시: 0123456789 01234 01234567890 6789012345 012322456789
print("=== 1안 내가 만든 코드 ===")
# input_num = input("숫자를 입력하세요: ")
input_num = "0123456789 01234 01234567890 6789012345 012322456789"
result = [''.join(sorted(x)) for  x in input_num.split()]


# result = input_num.split()
print(result)
#
# result=[]
# for i in input_num:
#     result.append(sorted(i))
# print(result)

# def isnumbering(input_num):
#     num_list = input_num.split(' ')
#     for i in num_list:
#         if i == '0123456789':
#             print('true', end=' ')
#         else:
#             print('false', end=' ')
#
# isnumbering(input_num)

print("=== 2안 코딩도장 추천 풀이_list_comprehension ===")
# input_num = '0123456789 01234 01234567890 6789012345 012322456789'
# n = [''.join(sorted(x)) for x in input_num.split()]   # sorted함수는 '새로운 리스트'를 리턴  // sort메서드는 none
# # n = [''.join(x) for x in input_num.split()]
# print(n)
# for x in n:
#     print("true" if x=="0123456789" else "false", end=' ')

print("=== 3안 교재 풀이 ===")

# def chkDupNum(s):
#     result = []
#     for num in s:
#         if num not in result:
#             result.append(num)
#         else:
#             return False
#     return len(result) == 10
# print(chkDupNum("0123456789"))

print("=== 4안 문수 풀이===")
# def check(result):
#     for i in range(0, 10):
#         if result.count(str(i)) == 1:
#             pass
#         else:
#             return 'false'
#     return 'true'
#
# # input1 = input('입력: ')
# input1 = "0123456789 01234 01234567890 6789012345 012322456789"
# input1 = input1.split()
# # print(input1)
# for i in input1:
#     total = check(i)
#     print(total, end=' ')

