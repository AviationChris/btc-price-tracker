import pandas as pd
from datetime import datetime, timedelta

class PriceAnalyzer:
    def __init__(self, db):
        self.db = db

    def calculate_metrics(self):
        prices = self.db.get_price_history()
        if not prices:
            return None
            
        df = pd.DataFrame(prices, columns=['price', 'timestamp'])
        return {
            'average_24h': df['price'].mean(),
            'high_24h': df['price'].max(),
            'low_24h': df['price'].min(),
            'volatility': df['price'].std()
        }

    def detect_significant_changes(self, threshold=0.05):
        prices = self.db.get_price_history(2)
        if len(prices) < 2:
            return False
            
        price_change = (prices[0][0] - prices[1][0]) / prices[1][0]
        return abs(price_change) >= threshold