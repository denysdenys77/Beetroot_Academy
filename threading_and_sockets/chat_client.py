import socket
import threading
import time


shutdown = False
join = False


def receiving(neme, sock):
    while not shutdown:
        while True:
            data, addr = sock.recvfrom(1024)
            print(data.decode('utf-8'))
            time.sleep(0.2)


host = socket.gethostbyname(socket.gethostname())
port = 0

server = ('127.0.1.1', 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(True)

client_name = input("Enter your name: ")

t = threading.Thread(target=receiving, args=('name', s))
t.start()

while not shutdown:
    if not join:
        s.sendto(f'{client_name} join chat.'.encode('utf-8'), server)
        join = True

    else:
        try:
            message = input()
            if message is not '':
                s.sendto(f"{client_name} --> {message}".encode('utf-8'), server)
            time.sleep(0.2)
        except:
            s.sendto(f'{client_name} left chat.'.encode('utf-8'), server)
            shutdown = True

t.join()
s.close()


