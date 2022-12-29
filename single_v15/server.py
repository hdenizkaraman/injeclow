import os
import socket
from master import World

controlside = World()
HOST = "10.90.158.183"  # Standard loopback interface address (localhost)
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
                for thekey in controlside.posibilites.keys():
                    if thekey in data:
                        if thekey=="cmd":
                            print("in cmd")
                            datanew = data.split()
                            datanew.remove("cmd")
                            datanewstr = " ".join(str(x) for x in datanew)
                            print(datanewstr)
                            getattr(controlside, controlside.posibilites[thekey])(datanewstr)
                        else:
                            print("in nocmd")
                            rundef = getattr(World, controlside.posibilites[thekey])
                            rundef(controlside)
