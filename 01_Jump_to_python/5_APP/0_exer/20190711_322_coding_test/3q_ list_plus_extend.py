a = [1, 2, 3]
print(id(a))
# 리스트 a에 [4, 5]를 +기호를 사용하여 더한 결과
# a = a + [4, 5]  # 초기의 리스트a에 [4,5] 요소를 추가하여, 새로운 a에 할당 (주소 상이)
# print(id(a))

a.extend([4, 5])   # 기존의 a에 요소를 추가(동일 주소)
print(id(a))