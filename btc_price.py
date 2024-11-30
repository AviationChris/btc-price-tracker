import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_btc_price():
    api_key = os.getenv('CMC_API_KEY')
    if not api_key:
        raise ValueError('CMC_API_KEY not found in environment variables')

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {
        'X-CMC_PRO_API_KEY': api_key
    }
    params = {
        'symbol': 'BTC',
        'convert': 'USD'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        price = data['data']['BTC']['quote']['USD']['price']
        return f'Current Bitcoin Price: ${price:,.2f}'
    except requests.exceptions.RequestException as e:
        return f'Error fetching price: {str(e)}'

if __name__ == '__main__':
    print(get_btc_price())