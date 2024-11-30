import sqlite3
from datetime import datetime

class BTCDatabase:
    def __init__(self, db_path='btc_prices.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS prices (
                    id INTEGER PRIMARY KEY,
                    price REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')

    def add_price(self, price):
        with self.conn:
            self.conn.execute('INSERT INTO prices (price) VALUES (?)', (price,))

    def get_price_history(self, limit=100):
        cursor = self.conn.execute(
            'SELECT price, timestamp FROM prices ORDER BY timestamp DESC LIMIT ?', 
            (limit,)
        )
        return cursor.fetchall()