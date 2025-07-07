## CryptoCSVgen BETA v0.1.0
 subject to change, some features may be broken.


This is a Python app that lets you download historical cryptocurrency data from Yahoo Finance using a simple interface. You can:

* Search and select from a list of crypto tickers
* Choose time intervals (like 1m, 5m, 1h, etc.)
* Select preset or custom date ranges
* Export the data to a CSV file
* View logs and test the connection directly from the app

It’s useful for anyone who wants to quickly pull precise crypto market data without writing any code or using yahoo's interface (limited timeframes)

### Requirements

* Python 3.8 or higher
* Linux (WSL or virtual machine works fine) Works on Windows and macOS in theory. 

**Note:** `tkinter` comes pre-installed with most Python distributions on Windows but this does not mean it will be in WSL by default. If not, reinstall Python with the commands seen below.

### Install/Run

1. Open this folder in WSL/Linux VM whatever you have.
2. Create python venv using `python3 -m venv cryptocsv` *if not already installed python3.10-venv library will be needed*
3. Open that python venv using `source cryptocsv/bin/activate`
4. install requirements for crypto_collector.py using `pip install -r requirements.txt` 
5. Open script with `python3 crypto_collector.py` *if not already installed python3.10-tk library will be needed* (install tkinter using `apt install python3.10-tk`)

OR run these commands inside cryptocsvgen directory

`sudo apt install python3.10-venv python3.10-tk -y`
`python3 -m venv cryptocsv`
`source cryptocsv/bin/activate`
`pip install -r requirements.txt`
`python3 crypto_collector.py`


## Notes

* For intraday intervals (like 1m or 5m), Yahoo Finance only allows data for the past \~60 days.
* Results are saved to CSV file you choose where.
