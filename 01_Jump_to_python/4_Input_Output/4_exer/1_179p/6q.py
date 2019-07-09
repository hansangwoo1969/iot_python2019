# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성. (단 프로그램을 다시 실행하더라도 기존작성분 유지,
# 새로 입력한 분은 추가

user_input = input("저장할 내용을 입력하세요: ")
f = open("test.txt", 'a')
f.write(user_input)
f.write('\n')
f.close()

