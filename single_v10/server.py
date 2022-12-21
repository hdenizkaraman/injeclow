import os
import socket
from master import World

controlside = World()
# HOST = "10.90.158.151"  # Standard loopback interface address (localhost)
HOST = "192.168.1.102"
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode("utf-8")
            if not data: pass
            else:
                # FUNCTIONS HERE!
                for thekey in controlside.posibilites.keys:
                    if data==thekey:
                        rundef = getattr(World, controlside.posibilites[thekey])
                        rundef(controlside)