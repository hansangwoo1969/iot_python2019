# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.

print('===  방안 1 ===')
result = sum([i for i in range(1000) if (i % 3 == 0) or (i % 5 == 0)])
print(result)

print('===  방안 2 ===  TypeError 반환')
set3 = set(range(3, 1000, 3))
set5 = set(range(5, 1000, 5))
print(sum(set3.union(set5)))

print("=== 방안 3 ===")  # 리스트에 입력하고, 집합으로 변경해서 중복제거하고 합집합// 다시 리스트로 변경해서 합
m3=[]
m5=[]
for i in range(1000):
    if i % 3 == 0:
        m3.append(i)
    if i % 5 == 0:
        m5.append(i)

print(m3)
print(m5)
set3 = set(m3)
set5 = set(m5)
result3 = set3.union(set5)

print(sum(result3))