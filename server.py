import socket

LOG_FILE_NAME = "log.txt"
sock = socket.socket()
sock.bind(('', 9090))

log_file = open(LOG_FILE_NAME, "a")


def log_print(text):
    log_file.write(text + "\n")


while True:
    sock.listen(0)
    conn, addr = sock.accept()
    log_print(F"Connected {addr}")
    msg = ''
    data = conn.recv(4096)
    msg += data.decode()
    if msg == "exit":
        log_print("Received exit signal, closing")
        break
    log_print(F"Recieved {msg}")
    conn.send(data)

log_file.close()
conn.close()
