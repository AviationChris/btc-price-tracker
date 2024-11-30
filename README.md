# Bitcoin Price Tracker

Python script to fetch real-time Bitcoin prices using CoinMarketCap API.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AviationChris/btc-price-tracker.git
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Get API key from [CoinMarketCap](https://coinmarketcap.com/api/)

4. Update `api_config.py` with your API key

## Usage

Run the script:
```bash
python btc_tracker.py
```

Press Ctrl+C to stop tracking.

## Features
- Real-time BTC price updates
- Price updates every minute
- Timestamp for each update