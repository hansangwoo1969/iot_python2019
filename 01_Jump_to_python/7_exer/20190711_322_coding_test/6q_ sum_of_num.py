# 사용자로 부터 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램 작성, 숫자는 콤마로 구분 입력
# 65,45,2,3,45,8
user_input = input("숫자를 입력하세요 (콤마로 구분: ")
user_input = user_input.split(',')
print(type(user_input))
print(user_input)
#
print(" === 1안 입력받은 a의 요소를 정수화해서 더함 ===")

total = 0
for i in user_input:
#     print(i)
    total += int(i)
#
print(f"총합 :  {total}")