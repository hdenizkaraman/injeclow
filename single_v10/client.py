import socket
import sys

HOST = "10.90.158.183" # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.connect((HOST, PORT))
    while 1:
        girdi = str(input("Enter Command: "))
        if girdi=="end": sys.exit()
        conn.send(girdi.encode("utf-8"))