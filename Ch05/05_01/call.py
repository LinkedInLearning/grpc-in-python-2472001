from socket import socket

with open('request.txt', 'rb') as fp:
    data = fp.read()

sock = socket()
sock.connect(('httpbin.org', 80))
sock.sendall(data)

chunks = []
for chunk in iter(lambda: sock.recv(1024), b''):
    chunks.append(chunk)
reply = b''.join(chunks)
print(reply.decode())
