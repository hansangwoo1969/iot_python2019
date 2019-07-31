import re

original_text = 'life is too short'
p = re.compile('[a-z]+')

result = p.finditer(original_text)  # 위치값(span)이 필요한 경우
# 매칭된 결과를 'Match object'리스트로 반환
print(result)
for r in result:
    print(r)
    print(r.group())


