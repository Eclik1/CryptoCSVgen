### CryptoCSVgen BETA v0.1.0
Subject to change; some features may be broken.

Python app to download historical cryptocurrency data from Yahoo Finance with a simple interface.

Features

Search and select crypto tickers
Choose time intervals (1m, 5m, 1h, etc.)
Select preset or custom date ranges
Export data to CSV
View logs and test connection

### Requirements
Python 3.8 or higher
Linux (WSL or VM works fine). Windows and macOS support untested.
Note: tkinter may not be installed by default on WSL. Install it if missing.

### Installation & Usage

Run these commands in your terminal:

sudo apt install python3.10-venv python3.10-tk -y # if needed
python3 -m venv cryptocsv
source cryptocsv/bin/activate
pip install -r requirements.txt
python3 crypto_collector.py

Alternatively, run everything in one command inside the project folder:

sudo apt install python3.10-venv python3.10-tk -y && python3 -m venv cryptocsv && source cryptocsv/bin/activate && pip install -r requirements.txt && python3 crypto_collector.py

Notes

Intraday data (1m, 5m) only available for last ~60 days via Yahoo Finance

CSV files are saved to the location you specify

Use responsibly. This is a beta version.
