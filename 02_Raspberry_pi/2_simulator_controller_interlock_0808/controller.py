from socket import *
from bluetooth import *
 
server_ip = '192.168.0.17'
port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind((server_ip, port))
serverSock.listen(1)

#client_socket1 = BluetoothSocket(RFCOMM)
#client_socket2 = BluetoothSocket(RFCOMM)
#client_socket1.connect(("B8:27:EB:47:5B:95",1))
#client_socket2.connect(("B8:27:EB:41:2B:FC",2))

print('Server(%s) is waiting on %d port...' % (server_ip, port))

connectionSock, addr = serverSock.accept()

print(str(addr), ' connecting..')

while True:
    try:
        recvData = connectionSock.recv(1024).decode('utf-8')
        print('Receive Command : %s' % recvData)
        if recvData == '1':
            pass
            #client_socket1.send('1')
        elif recvData == '2':
            pass
            #client_socket1.send('2')
        elif recvData == 'q':
            connectionSock.send('close'.encode('utf-8'))
            connectionSock.close()
            break
        connectionSock.send('Receive OK'.encode('utf-8'))
    except Exception as e:
        print(e)
        
print('Server is shutdown')
