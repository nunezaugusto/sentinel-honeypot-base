import os
from logger import HoneyLogger
from emulator import run_fake_service

def main():
    # 1. Preparación del entorno
    # Creamos la carpeta 'logs' si no existe para que no de error al guardar la DB
    if not os.path.exists('logs'):
        os.makedirs('logs')
        print("[+] Carpeta 'logs' creada.")

    print("""
    ######################################
    #       SENTINEL HONEYPOT v0.1       #
    #    Proyecto de Ciberseguridad      #
    ######################################
    """)

    # 2. Inicialización de componentes
    # Creamos la instancia del Logger (la base de datos)
    my_logger = HoneyLogger()
    
    # 3. Lanzamiento del servicio
    # Arrancamos el emulador en el puerto 2323 (Telnet de prueba) 
    # y le pasamos el objeto 'my_logger' para que pueda usarlo.
    try:
        run_fake_service(2323, my_logger)
    except KeyboardInterrupt:
        print("\n[-] Apagando el Honeypot de forma segura...")

if __name__ == "__main__":
    main()