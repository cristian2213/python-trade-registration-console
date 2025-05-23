# Python Trade Registration Console

A command-line interface (CLI) application for tracking and managing trading records. This tool helps traders log their trades, calculate profits/losses, and analyze trading performance.

## Features

- 📊 Record trades with various asset types (Stocks, Options, Futures, Crypto, Metals)
- 📈 Automatic profit/loss calculation in both pips and dollars
- 🎯 Track take profit (TP) and stop loss (SL) hits
- 📋 Multiple trading strategies support
- 💾 Save trade history to CSV for further analysis
- 📊 Basic trade statistics and performance metrics

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/python-trade-registration-console.git
   cd python-trade-registration-console
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the console application:

   ```bash
   python statistics/console_register.py
   ```

2. Follow the interactive prompts to enter your trade details:

   - Select asset type (Stock, Option, Future, Crypto, Metal)
   - Enter asset symbol (e.g., XAUUSD, BTCUSD, ETHUSD)
   - Choose or enter a trading strategy
   - Input trade details (buy/sell, prices, volume, TP/SL)

3. The system will automatically calculate:
   - Whether TP/SL was hit
   - Profit/Loss in pips and dollars
   - Trade result (Profit/Loss)

## Data Storage

All trades are stored in a CSV file (`trades.csv`) with the following columns:

- uuid: Unique identifier for each trade
- asset_type: Type of asset (Stock, Option, etc.)
- asset_symbol: Trading symbol (e.g., XAUUSD)
- strategy: Trading strategy used
- operation_type: Buy/Sell
- buying_price: Entry price
- closing_price: Exit price
- volume_lot: Trade size in lots
- tp: Take Profit level
- sl: Stop Loss level
- hit_tp_sl: Whether TP/SL was hit
- profit_or_loss_in_pips: P/L in pips
- profit_or_loss_in_dollars: P/L in dollars
- result_type: Profit/Loss
- date_and_time: Timestamp of the trade

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
