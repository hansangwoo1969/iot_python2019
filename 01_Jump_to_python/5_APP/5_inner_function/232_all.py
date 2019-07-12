# all은 iterable객체 (2개 이상의 값을 담을 수 있는 자료형)에 적용가능
# all함수는 입력받은 데이터의 정합성을 체크할 때 사용할 수 있다
print("#1 ", all([1, 2, 3]))    #숫자형
print("#2 ", all([1, 2, 0]))
print("\n#3 ", all(['hello', 'world']))  #문자열
print("#4 ", all(['hello', '']))
print("#5 ", all((1,2)))      #튜플
print("#6 ", all((1,0)))
# dictionary의 값은 Key, value로 나누어서 확인
print("\n#7 ", all({'조문수':'남', '김혜경':'녀'}))  #딕셔너리
print("#8 ", all({}))
print("#9 ", all([1, '2', 0.0]))  # 복합자료형

result = [1, 2, 3].append(4)  # 상수형객체의 값을 변경하는 멤버함수사용은 주의
print("\n#10 ", result)
print("#11 ", [1, 2, 3].append(4))
result = [1, 2, 3]
result.append(4)
print("#12 ", result)

print("#1 ", [1, 2, 3].count(2))  # 상수형 객체의 값을 조회하는 멤버함수는 가능