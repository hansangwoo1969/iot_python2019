"""
서버를 먼저 실행, 클라이언트를 그 다음으로 실행. 연결이 되고 나면,
서버는 자신에게 접속한 사람의 정보를 표시하고, 클라이언트로부터 데이터 수신을 대기.
클라이언트는 서버에게 메시지를 하나 보내고, 서버는 메시지를 확인 해 출력하고,
다시 클라이언트에게 답례 메시지를 하나 보냅니다.
클라이언트까지 메시지 수신 확인이 끝나면 두 프로그램이 종료됩니다.
"""

from socket import *

server_ip = '192.168.0.17'    # 여건에 맞게 변경
port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)   # AF_INET:IPv4, SOCK_STREAM: 타입
serverSock.bind((server_ip, port))          # bind: 생성된 소켓의 번호와 실제 어드레스 패밀리를 연결해주는 것
# bind 함수 내에 튜플을 입력했다는 점을 유의하셔야 합니다. bind('',8080)가 아니라 bind(('',8080))입니다. 앞서
# 말한대로 bind는 소켓과 AF를 연결하는 과정이라 하였으므로, 이 인자는 어드레스 패밀리가 됩니다. 앞부분은 ip,
# 뒷부분은 포트로 (ip, port) 형식으로 한 쌍으로 구성된 튜플이 곧 어드레스 패밀리인 것이죠.
# 주소에 해당하는 부분에 빈 문자열만 들어가 있습니다. 파이썬 공식 문서를 참조해보니, AF_INET에서 ''는
# INADDR_ANY를 의미한다고 합니다. 즉, 모든 인터페이스와 연결하고 싶다면 빈 문자열을 넣으면 된다

serverSock.listen(1)  # bind가 서버소켓에서 필수로 사용, listen도 서버소켓에서밖에 쓰일 일이 없습니다.
# listen()안에 인자로 숫자 1이 입력되어 있는데, 이는 해당 소켓이 총 몇개의 동시접속까지를 허용할 것이냐는
# 이야기입니다. 1을 입력하면 단 한 개의 접속만을 허용할 것이고, 인자를 입력하지 않으면 파이썬이 자의적으로
# 판단해서 임의의 숫자로 listen한다고 합니다.

print('Server(%s) is waiting on %d port...' % (server_ip, port))

connectionSock, addr = serverSock.accept() # accept()는 소켓에 누군가가 접속하여 연결되었을 때에 비로소 결과값이 return되는 함수입니다
# 즉, 소스코드 내에 serverSock.accept()가 있더라도, 누군가가 접속할 때까지 프로그램은 바로 이 부분에서 계속
# 멈춰있게 된단 이야기죠. 상대방이 접속함으로써 accept()가 실행되면, return 값으로 새로운 소켓과, 상대방의 AF를
# 전달해주게 됩니다.

print(str(addr), ' connecting..')

while True:
    try:
        recvData = connectionSock.recv(1024).decode('utf-8')
        # 서버에 접속한 상대방과 데이터를 주고받기 위해서는 accept()를 통해 생성된 connectionSock이라는
        # 소켓을 이용하면 됩니다. 이제부터 serverSock 소켓을 이용할 일은 거의 없으며, connectionSock을
        # 주로 이용합니다.
        """
        recv()를 실행하면 소켓에 메시지가 실제로 수신될 때까지 파이썬 코드는 대기하게 됩니다. 
        위에 언급한 accept()처럼 말이죠. 인자로는 수신할 바이트의 크기를 지정할 수 있습니다. recv(1024)는 
        소켓에서 1024바이트만큼을 가져오겠단 소리입니다. 만일 소켓에 도착한 데이터가 1024바이트보다 많다면,
        다시 recv(1024)를 실행할 때 전에 미처 가져오지 못했던 것을 끌어오게 됩니다.
        
        아까 send()를 실행할 때는 문자열을 인코딩해서 보냈었는데요, recv()를 할 때는 데이터를 바이트로 
        수신하므로, 문자열로서 활용하기 위해선 디코딩을 해야합니다. 이 또한 decode()를 이용하여 적절하게 
        문자열로 디코딩할 수 있습니다.
        
        소켓에서 주고받는 데이터는 바이트이므로, 굳이 문자열을 주고받지 않아도 됩니다. 예를 들어 이미지 
        파일이나 동영상 파일을 읽어서 1024바이트 단위로 전송을 해도 실제로 상대방 컴퓨터에 파일을 전송할 
        수 있습니다.
        """
        print('Receive Command : %s' % recvData)
        if recvData == 'q':
            connectionSock.send('close'.encode('utf-8'))
            connectionSock.close()   # 소켓종료
            break
        connectionSock.send('Receive OK'.encode('utf-8'))
    except Exception as e:
        print(e)

print('Server is shutdown')