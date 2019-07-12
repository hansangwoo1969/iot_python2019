# A학급 학생의 점수중, 50점이상 점수의 총합을 구하라

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

print("=== 1안 list comprehension ===")
total = sum([i for i in A if i > 50])
print("total: ", total)

print("\n=== 2안 반복문===")
sum = 0
for i in A:
    if i > 50:
        sum += i
print(sum)

print("\n==== 3안 답지 ===")
result = 0
while A:             # A 리스트에 값이 있는 동안
    mark = A.pop()   # A 리스트의 가장 마지막 항목을 하나씩 뽑아냄
    if mark >= 50:   # 50점 이상의 점수만 더함
        result += mark

print(result)
