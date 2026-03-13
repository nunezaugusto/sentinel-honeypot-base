import socket

def run_fake_service(port):
    # Creamos un socket de tipo IPv4 (AF_INET) y TCP (SOCK_STREAM)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Esto permite reutilizar el puerto si reinicias el script rápido
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind(('0.0.0.0', port))
        server.listen(5)
        print(f"[*] Escuchando en el puerto {port}...")
        
        while True:
            client, addr = server.accept()
            print(f"[!] ¡Conexión detectada desde {addr[0]}!")
            
            # Aquí enviaríamos el "banner" falso
            client.send(b"Welcome to Ubuntu 22.04 LTS\nlogin: ")
            client.close()
            
    except Exception as e:
        print(f"[-] Error en el puerto {port}: {e}")
    finally:
        server.close()