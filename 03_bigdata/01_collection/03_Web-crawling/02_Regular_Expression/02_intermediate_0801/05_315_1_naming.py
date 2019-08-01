import re

# p = re.compile(r'(?P<name>\w+)\s+((?P<first_number>\d+)[-]\d+[-]\d+)')   # 문자열 단위의 반복, 1회이상
# m = p.search('park 010-1234-4567')

p = re.compile(r"""   # 원문이 'park 010-1234-4567' 일 경우에
(?P<name>\w+)\s+        # 이름과 공백문자가 매칭이 되는 정규식: 'park '매치
(?P<first_number>\d+)   # 첫 번째  전화번호 그룹: 010 매치
[-]                     # 첫 번째 전화번호 그룹 다음에 반드시 '-'가 와야함
(?P<second_number>\d+)  # 두 번째 전화번호 그룹: 1234매치
[-]
(?P<third_number>\d+)   # 세 번째 전화번호 그룹: 4567매치
""", re.VERBOSE)

m = p.search('park 010-1234-4567')

print(m)
print(m.group('name'))  # 그룹에 이름 붙이기
print(m.group('second_number'))
print(m.group('third_number'))
print(m.group(3))
print(m.group(0))
print(m.group('first_number'))
