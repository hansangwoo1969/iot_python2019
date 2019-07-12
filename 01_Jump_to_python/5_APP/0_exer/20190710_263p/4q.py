# filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거

print(list(filter(lambda a: a>0, [1, -2, 3, -5, 8, -3])))