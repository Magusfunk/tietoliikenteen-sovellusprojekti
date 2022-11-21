import socket

HOST = "172.20.241.9"
PORT = 20000
REQUEST = b"60\n"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(REQUEST)
response = b""
while True:
    chunk = s.recv(4096)
    if len(chunk) == 0:  
        break
    response = response + chunk  
s.close()

with open('./mittausData.txt', mode='w') as f:
    f.write(response.decode('utf-8'))