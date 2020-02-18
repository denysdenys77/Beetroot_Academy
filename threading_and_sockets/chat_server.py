# Реализовать чат комнату - то есть вместо одного клиента будет несколько и если один пользователь отправляет сообщение
# его должны получить остальные клиенты (используя потоки)


import socket

host = socket.gethostbyname(socket.gethostname())
port = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))


quit_server = False
print('Server started.')

while not quit_server:
    try:
        data, addr = s.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)

        print(f'[{addr[0]}]=[{addr[1]}]=[{data.decode("utf-8")}]')

        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:
        print('\nServer stopped.')
        quit_server = True

s.close()
