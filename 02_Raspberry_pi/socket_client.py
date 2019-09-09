# ip주소 맞추고, 알FTP통해 RPI로 전송
# RPI간 연동

from socket import *

port = 8080
server_ip = '192.168.0.3'     # 내 컴퓨터 IP
clientSock = socket(AF_INET,  SOCK_STREAM)
clientSock.connect((server_ip, port))
"""
bind와 listen, accept 과정이 빠지고 대신 connect가 추가되었습니다. 
클라이언트에서 서버에 접속하기 위해선 connect()만 실행해주면 됩니다. 
여기에도 어드레스 패밀리가 인자로 들어가고, 호스트 주소와 포트번호로 구성된 튜플이 요구됩니다. 
192.168.0.3은 자기 자신을 의미, 위의 어드레스 패밀리는 자기 자신에게 8080번 포트로 연결하란 소리가 되겠네요.
"""
print('Conecting to the server(%s) on %d port' % (server_ip, port))

while True:
    sendData = input('>>> ')
    clientSock.send(sendData.encode('utf-8'))
    # 문자열을 전송할 때 encode()가 들어간다는 점을 유의해야.
    # 파이썬 문자열의 encode() 메소드는 문자열을 byte로 변환해주는 메소드.
    # 파이썬 내부에서 다뤄지는 문자열은 파이썬에서 생성된 객체이고,
    # 이를 바로 트랜스포트에 그대로 싣는 것은 불가능합니다. 그러므로 적절한 인코딩을 하여 보내야만 합니다.
    # 인코딩을 하지 않고 보내면 에러가 뜨니까 주의하셔야 합니다.

    recvData = clientSock.recv(1024).decode('utf-8')
    print('서버: ', recvData)
    if(recvData=='close'):
        print('Server notify that service is over')
        break

clientSock.close()
print('Client is shutdown')
