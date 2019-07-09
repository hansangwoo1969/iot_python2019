f = open("새파일.txt", 'r', encoding='UTF-8')

lines = f.readlines()    # 한줄만 읽고 다음줄앞에 포인트
for line in lines:
    print(line, end='')  # 아스키 모드 파일을 print함수로 읽을경우에는 줄바꿈의 왜곡이 일어날 수 있으므로,
                         # end= ''를 반드시 사용한다.

f.close()