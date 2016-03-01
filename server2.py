__author__ = 'andrey.levanovich'
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)
conn, addr = s.accept()
while True:
    dataapi = conn.recv(1024)
    data = str(dataapi)
    if data.find('close') == -1 :
        conn.send(dataapi)
        print ('not close')
    else :
        print("brek")
        break
print(data)
conn.close()