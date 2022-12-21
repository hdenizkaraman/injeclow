import socket

HOST = "10.90.158.151"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.connect((HOST, PORT))
    while 1:
        girdi = str(input("Enter Command: "))
        conn.send(girdi.encode("utf-8"))
        print(conn.recv(1024).decode("utf-8"))