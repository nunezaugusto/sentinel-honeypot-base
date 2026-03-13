import socket

# Intentamos conectar al honeypot
s = socket.socket()
s.connect(('localhost', 2323))

# Recibimos el banner
print(s.recv(1024).decode())

# Enviamos un nombre de usuario falso
s.send(b"hacker_de_sevilla\n")

# Recibimos la respuesta
print(s.recv(1024).decode())
s.close()