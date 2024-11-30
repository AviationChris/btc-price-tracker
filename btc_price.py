import requests
from api_config import API_URL
from logger_config import setup_logger
import logging
from typing import Dict, Optional

logger = setup_logger('btc_price')

class BTCPriceError(Exception):
    """Custom exception for BTC price fetching errors"""
    pass

def get_btc_price() -> Optional[Dict]:
    """
    Fetch current BTC price from CoinGecko API
    
    Returns:
        dict: Bitcoin price data if successful
        None: If request fails
        
    Raises:
        BTCPriceError: If there's an error fetching or parsing the data
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        
        data = response.json()
        logger.info("Successfully fetched BTC price data")
        return data
        
    except requests.RequestException as e:
        logger.error(f"Error fetching BTC price: {str(e)}")
        raise BTCPriceError(f"Failed to fetch BTC price: {str(e)}")
        
    except ValueError as e:
        logger.error(f"Error parsing response data: {str(e)}")
        raise BTCPriceError(f"Failed to parse BTC price data: {str(e)}")

if __name__ == "__main__":
    try:
        price_data = get_btc_price()
        print(f"Current BTC Price: ${price_data['bitcoin']['usd']:,.2f}")
    except BTCPriceError as e:
        logger.error(f"Main execution failed: {str(e)}")
        print(f"Error: {str(e)}")