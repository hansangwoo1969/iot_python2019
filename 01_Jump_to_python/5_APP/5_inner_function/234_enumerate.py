# enumerate: 순서가 있는 자료형을 인덱스와 함께 반환
print("=== enumrate 1 ===")
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

print("\n=== enumrate 2 ===")
student_list = ['김혜경', '한상우', '배원제']
for i, name in enumerate(student_list):
    print(i, name)

print("\n=== enumrate 3 ===")
student_list = ['김혜경', '한상우', '배원제', '홍정우']
for i, name in enumerate(student_list):
    if ( i < 2 ):
        print(i, name, "다음손님: ", student_list[i+1])
    else:
        print(i, student_list[i], "고객님 잠시 대기 부탁드립니다.")

