import time
from btc_price import get_btc_price, BTCPriceError
from database import BTCDatabase
from analysis import PriceAnalyzer
from config import Config
from logger_config import setup_logger

logger = setup_logger('btc_tracker')

class BTCTracker:
    def __init__(self):
        self.db = BTCDatabase()
        self.analyzer = PriceAnalyzer(self.db)
        self.config = Config()

    def track_price(self):
        try:
            data = get_btc_price()
            if not data or 'bitcoin' not in data:
                raise BTCPriceError("Invalid price data format")

            price = data['bitcoin']['usd']
            self.db.add_price(price)
            
            metrics = self.analyzer.calculate_metrics()
            if metrics:
                logger.info(f"Price: ${price:,.2f} | 24h Avg: ${metrics['average_24h']:,.2f}")
                
                if self.analyzer.detect_significant_changes():
                    logger.warning(f"Significant price change detected! Current: ${price:,.2f}")
            
            return price
            
        except BTCPriceError as e:
            logger.error(f"Error tracking price: {str(e)}")
            return None

    def run(self):
        logger.info("Starting BTC price tracker...")
        while True:
            try:
                self.track_price()
                time.sleep(self.config.UPDATE_INTERVAL)
            except KeyboardInterrupt:
                logger.info("Stopping BTC price tracker...")
                break
            except Exception as e:
                logger.error(f"Unexpected error: {str(e)}")
                time.sleep(self.config.UPDATE_INTERVAL)

if __name__ == "__main__":
    tracker = BTCTracker()
    tracker.run()