import socket

def run_fake_service(port, logger):
    # Creamos un socket de tipo IPv4 y TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind(('0.0.0.0', port))
        server.listen(5)
        print(f"[*] Honeypot escuchando en el puerto {port}...")
        
        while True:
            client, addr = server.accept()
            ip_atacante = addr[0]
            print(f"[!] ¡Conexión detectada desde {ip_atacante}!")
            
            # 1. Enviamos el "banner" falso
            client.send(b"Welcome to Ubuntu 22.04 LTS\nlogin: ")
            
            # 2. Recibimos lo que el atacante intente escribir (máximo 1024 bytes)
            # El strip() limpia espacios y saltos de línea
            data = client.recv(1024).decode('utf-8', errors='ignore').strip()
            
            # 3. LLAMADA AL LOGGER: Guardamos la IP, el puerto y lo que escribió
            logger.log_attack(ip_atacante, port, data)
            
            # 4. Cerramos la conexión
            client.send(b"Access denied.\n")
            client.close()
            
    except Exception as e:
        print(f"[-] Error en el puerto {port}: {e}")
    finally:
        server.close()