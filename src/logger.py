import sqlite3
from datetime import datetime

class HoneyLogger:
    def __init__(self, db_name="logs/honeypot.db"):
        self.db_name = db_name
        # Al arrancar, nos aseguramos de que la tabla exista
        self._create_table()

    def _create_table(self):
        """Crea la estructura de la base de datos si no existe"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        # Definimos las columnas: ID, fecha, IP del atacante, puerto y datos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                ip_address TEXT,
                port INTEGER,
                data_received TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def log_attack(self, ip, port, data):
        """Inserta un nuevo ataque en la base de datos"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
            INSERT INTO attacks (timestamp, ip_address, port, data_received)
            VALUES (?, ?, ?, ?)
        ''', (now, ip, port, data))
        
        conn.commit()
        conn.close()
        print(f"✅ Ataque de {ip} registrado en la DB.")