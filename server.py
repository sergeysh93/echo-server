import socket
import sys
from datetime import datetime

LOG_FILE_NAME = "log.txt"
DEFAULT_PORT = 9090


def port_or_default(text):
    try:
        res = int(text)
        return res if 1023 < res < 65536 else DEFAULT_PORT
    finally:
        return DEFAULT_PORT


def logger(text):
    with open(LOG_FILE_NAME, "a") as f:
        f.write(f"{datetime.now()} {text}\n")


logger("Server started")
args = sys.argv[1:]
main_port = port_or_default(args[0]) if len(args) > 0 else DEFAULT_PORT

with socket.socket() as s:
    s.bind(('', main_port))
    s.listen(5)
    logger(f"Listening on port: {main_port}")
    while True:
        conn, addr = s.accept()
        with conn:
            logger(F"Connected by {addr}")
            while True:
                data = conn.recv(4096)
                msg = data.decode()
                if not data:
                    logger(F"Disconnected by {addr}")
                    break
                logger(F"Received {msg} from {addr}")
                conn.send(data)
                logger(F"Sent {msg} back to {addr}")

logger(f"Server stopped")
