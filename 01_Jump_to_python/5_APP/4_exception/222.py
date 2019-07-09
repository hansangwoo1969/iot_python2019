print('작업1')


f = open('나없는 파일', 'r')
# 파일이 없는 경우 아래와 같은 메시지를 생성하고 런타임 에러를 발생한다.
# FileNotFoundError: [Errno 2] No such file or directory: '나없는 파일'
#

print('작업2')
print("정상종료")