from socket import *
from bluetooth import *

'''
1조 프로그램_문수
소켓서버(rpi_1)
'''
server_ip = '192.168.0.17'
port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind((server_ip, port))
serverSock.listen(1)

client_socket1 = BluetoothSocket(RFCOMM)
client_socket1.connect(("B8:27:EB:41:2B:FC",2))

print('Server(%s) is waiting on %d port...' % (server_ip, port))

connectionSock, addr = serverSock.accept()

print(str(addr), ' connecting..')

# 컨트롤러 프로토콜(rpi_2 제어/동작)
while True:
    try:
        recvData = connectionSock.recv(1024).decode('utf-8')
        print('Receive Command : %s' % recvData)
        if recvData == '1':
            client_socket1.send('1')
        elif recvData == '2':
            client_socket1.send('2')
        elif recvData == '3':
            client_socket1.send('3')
        elif recvData == '4':
            client_socket1.send('4')
        elif recvData == 'q':
            connectionSock.send('close'.encode('utf-8'))
            client_socket1.send('q')
            connectionSock.close()
            break
        connectionSock.send('Receive OK'.encode('utf-8'))
    except Exception as e:
        print(e)
        
print('Server is shutdown')
