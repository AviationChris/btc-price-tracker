import requests
import time
from datetime import datetime
from api_config import API_KEY

def get_btc_prices():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': 'BTC',
        'convert': 'USD,AUD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY
    }

    try:
        response = requests.get(url, headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()
        usd_price = data['data']['BTC']['quote']['USD']['price']
        aud_price = data['data']['BTC']['quote']['AUD']['price']
        return usd_price, aud_price
    except requests.exceptions.RequestException as e:
        print(f'Error fetching price: {e}')
        return None, None

def main():
    print('Bitcoin Price Tracker Started')
    print('Press Ctrl+C to exit')
    
    try:
        while True:
            usd_price, aud_price = get_btc_prices()
            if usd_price and aud_price:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f'[{timestamp}] BTC: ${usd_price:,.2f} USD | ${aud_price:,.2f} AUD')
            time.sleep(60)  # Update every minute
    except KeyboardInterrupt:
        print('\nTracker stopped')

if __name__ == '__main__':
    main()