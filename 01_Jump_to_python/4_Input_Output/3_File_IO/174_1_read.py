f = open("새파일.txt", 'r', encoding='UTF-8')
line = f.readline()    # 한줄만 읽고 다음줄앞에 포인트
print(line)

f.close()