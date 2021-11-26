import socket

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 9090


def host_or_default(host):
    try:
        lst = host.split('.')
        if len(lst) != 4:
            return DEFAULT_HOST
        for i in range(4):
            lst[i] = int(lst[i])
            if lst[i] > 255 or lst[i] < 0:
                return DEFAULT_HOST
        return host
    finally:
        return DEFAULT_HOST


def port_or_default(port):
    try:
        port = int(port)
        return port if 1023 < port < 65536 else DEFAULT_PORT
    finally:
        return DEFAULT_PORT


inp = input("Host: ")
main_host = host_or_default(inp)

inp = input("Port: ")
main_port = port_or_default(inp)

with socket.socket() as s:
    s.connect((main_host, main_port))
    print(f"Connected to: {(main_host, main_port)}")
    while True:
        msg = input("Message: ")
        if msg == "exit":
            exit()
        s.send(msg.encode())
        print(f"Data sent: {msg}")
        data = s.recv(4096)
        print(f"Server reply: {data.decode()}")
