# "test.txt"라는 파일에 "Life is too short"문자열을 저장한 후 다시 그파일을 읽어서 출력하는 프로그램

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt",'r')
print(f2.readline())
f2.close()