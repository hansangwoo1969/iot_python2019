import re

"""
328page Q1
"""

# p = re.compile('a[.]{3,}b')
# m = p.search('acccb')
# print(m)
# m = p.search('a....b')
# print(m)
# m = p.search('aaaab')
# print(m)
# m = p.search('a.cccb')
# print(m)

"""
# Q18
"""

# p = re.compile("[a-z]+")
# m = p.search("5 python")
# print(m.start())
# print(m.end())
# print(m.start()+m.end())

"""
#  Q 19
"""

data = """
park 010-9999-9988
kim 010-9907-7789
lee 010-8789-7768
"""
# # p = re.compile('(?P<tel>\w+\s+\d+[-]\d+)[-]\d+')
# p = re.compile('\w+\s+\d+[-]\d+[-]\d+')
# lines = p.findall(data)
#
# for line in lines:
#     line = line[:-4]+'####'
#     print(line)

# pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
# result = pat.sub("\g<1>-####", data)
# print(result)





"""
Q_20 positive_lookahead_assertion
    - 다음은 이메일 주소를 나타내는 정규식이다. 이 정규식은 park@naver.com, kim@daum.net, lee@myhome.co.kr
      등과 매치된다. 긍정형 전방 탐색기법을 사용하여 .com, .net이 아닌 이메일 주소를 제외시키는 정규식을 작성
      .*[@].*[.].*$
"""
#
p = re.compile('.*[@].*[.](?=com$|net$).*')  # .com / .net 긍정형 전방탐색
#
# p = re.compile('.*[@].*[.].(?!{2}$)')   #  ddd.ddd. 뽑기
# p = re.compile('.*[@].*[.](?!com$|net$).*')  # 부정형 전방탐색
m = p.search('park@naver.com')
print(m)
m = p.search('kim@daum.net')
print(m)

m = p.search('lee@myhome.co.kr')
print(m)
