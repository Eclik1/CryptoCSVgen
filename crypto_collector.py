import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

class CryptoDataCollector:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptocurrency Data Collector")
        self.root.geometry("700x650")
        
        # Variables
        self.collecting = False
        
        # Cryptocurrency list
        self.crypto_list = [
            # Major cryptocurrencies (verified on Yahoo Finance)
            'BTC-USD', 'ETH-USD', 'USDT-USD', 'BNB-USD', 'XRP-USD', 'SOL-USD', 'USDC-USD', 'DOGE-USD', 'ADA-USD', 'TRX-USD',
            'TON-USD', 'AVAX-USD', 'SHIB-USD', 'DOT-USD', 'LINK-USD', 'BCH-USD', 'NEAR-USD', 'MATIC-USD', 'ICP-USD', 'LTC-USD',
            'UNI-USD', 'LEO-USD', 'DAI-USD', 'ETC-USD', 'XLM-USD', 'HBAR-USD', 'CRO-USD', 'APT-USD', 'ATOM-USD', 'FIL-USD',
            'ARB-USD', 'OP-USD', 'MKR-USD', 'AAVE-USD', 'GRT-USD', 'ALGO-USD', 'FLOW-USD', 'MANA-USD', 'SAND-USD', 'LRC-USD',
            'BAT-USD', 'ENJ-USD', 'CHZ-USD', 'COMP-USD', 'YFI-USD', 'SNX-USD', 'SUSHI-USD', 'CRV-USD', 'BAL-USD', 'ZRX-USD',
            'KNC-USD', 'BAND-USD', 'NMR-USD', 'STORJ-USD', 'SKL-USD', 'ANKR-USD', 'AMP-USD', 'FORTH-USD', 'CTSI-USD', 'FET-USD',
            'NKN-USD', 'OXT-USD', 'REP-USD', 'XTZ-USD', 'ZEC-USD', 'DASH-USD', 'EOS-USD', 'NEO-USD', 'QTUM-USD', 'ZIL-USD',
            'ICX-USD', 'LSK-USD', 'WAVES-USD', 'DCR-USD', 'DGB-USD', 'RVN-USD', 'NANO-USD', 'MINA-USD', 'CELO-USD', 'KSM-USD',
            'KAVA-USD', 'ROSE-USD', 'RUNE-USD', 'AUDIO-USD', 'OCEAN-USD', 'PERP-USD', 'TRU-USD', 'BADGER-USD', 'MASK-USD',
            'FTM-USD', 'RNDR-USD', 'GALA-USD', 'AXS-USD', 'INJ-USD', 'APE-USD', 'ENS-USD', 'JASMY-USD', 'DYDX-USD', 'LQTY-USD',
            'SPELL-USD', 'BICO-USD', 'POWR-USD', 'QUICK-USD', 'REQ-USD', 'POLY-USD', 'LPT-USD', 'BOND-USD', 'TRAC-USD',
            'VEGA-USD', 'IDEX-USD', 'MCO2-USD', 'GODS-USD', 'IMX-USD', 'PRIME-USD', 'MAGIC-USD', 'NEXO-USD', 'CELR-USD',
            'AUCTION-USD', 'SYLO-USD', 'LSETH-USD', 'HOPR-USD', 'AERGO-USD', 'INDEX-USD', 'WBTC-USD', 'CBETH-USD', 'RETH-USD',
            'STETH-USD', 'WSTETH-USD', 'BLUR-USD', 'PEPE-USD', 'FLOKI-USD', 'BONK-USD', 'WIF-USD', 'BOME-USD', 'TURBO-USD',
            'RARE-USD', 'SUPER-USD', 'UNFI-USD', 'BOBA-USD', 'ORCA-USD', 'RAY-USD', 'SRM-USD', 'STEP-USD', 'COPE-USD',
            'STAR-USD', 'LIKE-USD', 'OXY-USD', 'MEDIA-USD', 'MAPS-USD', 'HNT-USD', 'PYTH-USD', 'JTO-USD', 'RENDER-USD',
            'JUP-USD', 'WEN-USD', 'MYRO-USD', 'PENDLE-USD', 'EIGEN-USD', 'ETHFI-USD', 'ENA-USD', 'OMNI-USD', 'SAGA-USD',
            'TAO-USD', 'W-USD', 'TNSR-USD', 'AEVO-USD', 'METIS-USD', 'STRK-USD', 'MANTA-USD', 'ALT-USD', 'PIXELS-USD',
            'PORTAL-USD', 'SUI-USD', 'WETH-USD', 'WTRX-USD', 'SWETH-USD', 'HYPERLIQUID-USD', 'LUNC-USD', 'USTC-USD',
            'VET-USD', 'MNT-USD', 'IOTA-USD', 'ONT-USD', 'SC-USD', 'HIVE-USD', 'STEEM-USD', 'GLMR-USD', 'MOVR-USD',
            'OSMO-USD', 'JUNO-USD', 'LUNA-USD', 'SCRT-USD', 'ALPHA-USD', 'BETA-USD', 'CLV-USD', 'FARM-USD', 'KEEP-USD',
            'NU-USD', 'TRIBE-USD', 'CREAM-USD', 'PICKLE-USD', 'RARI-USD', 'GMT-USD', 'GST-USD', 'LOOKS-USD', 'WCFG-USD',
            'BTRST-USD', 'WAMPL-USD', 'SHPING-USD', 'MUSD-USD', 'PUNDIX-USD', 'MOBILE-USD', 'IOT-USD', 'DRIFT-USD',
            'FOXY-USD', 'CHEX-USD', 'CLOUD-USD', 'ZEUS-USD', 'HONEY-USD', 'MNDE-USD', 'LIDO-USD'
        ]
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Data Source Label
        ttk.Label(main_frame, text="Data Source: Yahoo Finance").grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        # Cryptocurrency Selection with Search
        ttk.Label(main_frame, text="Cryptocurrency:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        # Search frame
        search_frame = ttk.Frame(main_frame)
        search_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Search entry
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=15)
        search_entry.grid(row=0, column=0, padx=(0, 5))
        search_entry.bind('<KeyRelease>', self.filter_cryptos)
        
        # Crypto combobox
        self.crypto_var = tk.StringVar(value="BTC-USD")
        self.crypto_combo = ttk.Combobox(search_frame, textvariable=self.crypto_var, width=15)
        self.crypto_combo['values'] = self.crypto_list
        self.crypto_combo.grid(row=0, column=1, padx=(5, 0))
        
        # Search info label
        ttk.Label(search_frame, text="Search:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        search_entry.grid(row=0, column=1, padx=(0, 5))
        ttk.Label(search_frame, text="Select:").grid(row=0, column=2, sticky=tk.W, padx=(5, 5))
        self.crypto_combo.grid(row=0, column=3, padx=(0, 0))
        
        # Configure search frame columns
        search_frame.columnconfigure(1, weight=1)
        search_frame.columnconfigure(3, weight=1)
        
        # Interval Selection
        ttk.Label(main_frame, text="Interval:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.interval_var = tk.StringVar(value="1h")
        interval_combo = ttk.Combobox(main_frame, textvariable=self.interval_var, width=20)
        interval_combo['values'] = ('1m', '5m', '15m', '30m', '1h', '4h', '1d', '1w')
        interval_combo.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Date Range Selection
        ttk.Label(main_frame, text="Date Range:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.range_var = tk.StringVar(value="60d")
        range_combo = ttk.Combobox(main_frame, textvariable=self.range_var, width=20)
        range_combo['values'] = ('7d', '30d', '60d', '90d', '1y', '2y', '5y', 'max', 'custom')
        range_combo.grid(row=3, column=1, sticky=tk.W, pady=5)
        range_combo.bind('<<ComboboxSelected>>', self.on_range_change)
        
        # Custom date range (hidden by default)
        self.custom_frame = ttk.Frame(main_frame)
        self.custom_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(self.custom_frame, text="Start Date:").grid(row=0, column=0, sticky=tk.W)
        self.start_date_var = tk.StringVar(value="2023-01-01")
        ttk.Entry(self.custom_frame, textvariable=self.start_date_var, width=12).grid(row=0, column=1, padx=5)
        
        ttk.Label(self.custom_frame, text="End Date:").grid(row=0, column=2, sticky=tk.W, padx=(20,0))
        self.end_date_var = tk.StringVar(value="2024-01-01")
        ttk.Entry(self.custom_frame, textvariable=self.end_date_var, width=12).grid(row=0, column=3, padx=5)
        
        self.custom_frame.grid_remove()  # Hide initially
        
        # Output File
        ttk.Label(main_frame, text="Output File:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.output_var = tk.StringVar(value="crypto_data.csv")
        ttk.Entry(main_frame, textvariable=self.output_var, width=30).grid(row=5, column=1, sticky=tk.W, pady=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_output).grid(row=5, column=2, padx=5)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=3, pady=20)
        
        self.collect_button = ttk.Button(button_frame, text="Collect Data", command=self.start_collection)
        self.collect_button.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Test Connection", command=self.test_connection).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear Log", command=self.clear_log).pack(side=tk.LEFT, padx=5)
        
        # Log Area
        ttk.Label(main_frame, text="Log:").grid(row=7, column=0, sticky=tk.W, pady=(10,0))
        self.log = scrolledtext.ScrolledText(main_frame, width=80, height=15)
        self.log.grid(row=8, column=0, columnspan=3, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(8, weight=1)
    
    def filter_cryptos(self, event=None):
        """Filter cryptocurrency list based on search input"""
        search_term = self.search_var.get().upper()
        
        if not search_term:
            # If search is empty, show all cryptocurrencies
            filtered_list = self.crypto_list
        else:
            # Filter cryptocurrencies that contain the search term
            filtered_list = [crypto for crypto in self.crypto_list if search_term in crypto.upper()]
        
        # Update combobox values
        self.crypto_combo['values'] = filtered_list
        
        # If there's exactly one match, select it automatically
        if len(filtered_list) == 1:
            self.crypto_var.set(filtered_list[0])
        elif len(filtered_list) > 1 and search_term:
            # If multiple matches, show first one but don't auto-select
            self.crypto_combo.event_generate('<Down>')
    
    def on_range_change(self, event=None):
        if self.range_var.get() == 'custom':
            self.custom_frame.grid()
        else:
            self.custom_frame.grid_remove()
    
    def browse_output(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if filename:
            self.output_var.set(filename)
    
    def log_message(self, message):
        self.log.insert(tk.END, f"{datetime.now().strftime('%H:%M:%S')}: {message}\n")
        self.log.see(tk.END)
        self.root.update()
    
    def clear_log(self):
        self.log.delete(1.0, tk.END)
    
    def test_connection(self):
        """Test connection to Yahoo Finance"""
        self.log_message("Testing connection...")
        
        def test_thread():
            try:
                # Test Yahoo Finance
                test_data = yf.download("BTC-USD", period="1d", interval="1d")
                if not test_data.empty:
                    self.log_message("✓ Yahoo Finance connection successful")
                else:
                    self.log_message("✗ Yahoo Finance connection failed")
                        
            except Exception as e:
                self.log_message(f"✗ Connection test failed: {str(e)}")
        
        threading.Thread(target=test_thread, daemon=True).start()
    
    def start_collection(self):
        if self.collecting:
            return
        
        # Validate inputs
        if not self.output_var.get():
            messagebox.showerror("Error", "Please specify an output file")
            return
        
        self.collecting = True
        self.collect_button.config(text="Collecting...", state="disabled")
        self.log_message("Starting data collection...")
        
        threading.Thread(target=self.collect_data, daemon=True).start()
    
    def collect_data(self):
        try:
            interval = self.interval_var.get()
            output_file = self.output_var.get()
            
            df = self.collect_yfinance_data()
            
            if df is not None and not df.empty:
                # Fix column names - handle MultiIndex columns
                if isinstance(df.columns, pd.MultiIndex):
                    # For MultiIndex columns, use the first level (usually the metric name)
                    df.columns = [col[0].lower() if isinstance(col, tuple) else str(col).lower() for col in df.columns]
                else:
                    # For regular columns, convert to lowercase
                    df.columns = [str(col).lower() for col in df.columns]
                
                # Save to CSV
                df.to_csv(output_file, index=True)
                self.log_message(f"✓ Data saved to {output_file}")
                self.log_message(f"✓ Total records: {len(df)}")
                self.log_message(f"✓ Date range: {df.index[0]} to {df.index[-1]}")
                
                # Show data preview
                self.log_message("\nData Preview:")
                self.log_message(str(df.head()))
                
            else:
                self.log_message("✗ No data collected")
                
        except Exception as e:
            self.log_message(f"✗ Error: {str(e)}")
        finally:
            self.collecting = False
            self.collect_button.config(text="Collect Data", state="normal")
    
    def collect_yfinance_data(self):
        crypto = self.crypto_var.get()
        interval = self.interval_var.get()
        date_range = self.range_var.get()
        
        self.log_message(f"Collecting {crypto} data from Yahoo Finance...")
        
        try:
            if date_range == 'custom':
                start_date = self.start_date_var.get()
                end_date = self.end_date_var.get()
                
                # Check if requesting intraday data for old dates
                if interval in ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h'] and start_date < '2023-01-01':
                    self.log_message("⚠ Warning: Yahoo Finance limits intraday data to ~2 years")
                
                df = yf.download(crypto, start=start_date, end=end_date, interval=interval)
            else:
                # Check limitations for intraday data
                if interval in ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h']:
                    if date_range in ['1y', '2y', '5y', 'max']:
                        self.log_message("⚠ Warning: Switching to 60d for intraday data (Yahoo Finance limit)")
                        date_range = '60d'
                
                df = yf.download(crypto, period=date_range, interval=interval)
            
            if df.empty:
                self.log_message("✗ No data returned from Yahoo Finance")
                return None
            
            self.log_message(f"✓ Downloaded {len(df)} records")
            return df
            
        except Exception as e:
            self.log_message(f"✗ Yahoo Finance error: {str(e)}")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoDataCollector(root)
    root.mainloop()