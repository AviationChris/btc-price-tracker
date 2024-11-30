import requests
import time
from datetime import datetime
from api_config import API_KEY

def get_btc_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': 'BTC',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY
    }

    try:
        response = requests.get(url, headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()
        price = data['data']['BTC']['quote']['USD']['price']
        return price
    except requests.exceptions.RequestException as e:
        print(f'Error fetching price: {e}')
        return None

def main():
    print('Bitcoin Price Tracker Started')
    print('Press Ctrl+C to exit')
    
    try:
        while True:
            price = get_btc_price()
            if price:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f'[{timestamp}] BTC: ${price:,.2f}')
            time.sleep(60)  # Update every minute
    except KeyboardInterrupt:
        print('\nTracker stopped')

if __name__ == '__main__':
    main()