import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_URL = os.getenv('API_URL', 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    UPDATE_INTERVAL = int(os.getenv('UPDATE_INTERVAL', 60))
    PRICE_THRESHOLD = float(os.getenv('PRICE_THRESHOLD', 1000))
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')