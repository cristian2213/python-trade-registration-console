import questionary
from uuid import uuid4
from datetime import datetime
from pathlib import Path
from .csv_file_attacher import CSVFileAttacher
from .excel_file_attacher import ExcelFileAttacher


class ConsoleRegister:
    """
    ConsoleRegister class is used to register trades in a CSV file.
    """

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.csv_file_attacher = CSVFileAttacher(self.file_path / 'trades.csv')
        self.excel_file_attacher = ExcelFileAttacher(
            self.file_path / 'trades.xlsx')

    def request_data(self):
        """
        request_data method is used to request data from the user.
        """
        pass

    def show_menu(self):
        """
        show_menu method is used to show the console menu.
        """
        # Asset Type
        asset_type = questionary.select(
            "Select asset type:",
            choices=[
                "Stock",
                "Option",
                "Future",
                "Crypto",
                "Metal",
            ],
        ).ask()

        # Asset Symbol
        asset_symbol = questionary.autocomplete('Asset Symbol:', choices=[
            'XAUUSD', 'BTCUSD', 'ETHUSD'
        ]).ask()

        # Strategy
        strategy = questionary.autocomplete(
            'Strategy:',
            choices=[
                'ABCD', 'RT-BOTTOM-REVERSAL', 'RT-TOP-REVERSAL', 'MOVING-AVERAGE', 'VWAP', 'SUPPORT&RESISTANCE', 'RED-TO-GREEN', 'OPENING-RANGE', 'FIBONACCI RETRACEMENT&EXTENSION', 'OTHER'
            ]
        ).ask()

        if strategy == 'OTHER':
            strategy = questionary.text('Enter new strategy:').ask()

        # Operation type
        operation_type = questionary.select(
            "Select operation type:",
            choices=[
                "Buy",
                "Sell",
            ],
        ).ask()

        # Buy Price
        buying_price = float(questionary.text('Buy Price:').ask())
        # Close Price
        closing_price = float(questionary.text('Close Price:').ask())
        # Volume, lot
        volume_lot = float(questionary.text('Volume/Lot:').ask())
        # TP(Take Profit)
        tp = float(questionary.text('TP:').ask())
        # SL (Stop Loss)
        sl = float(questionary.text('SL:').ask())

        # TODO: Pending to add validation and normalization for each input

        # Calculate if the operation hit "TP or SL" in "Buy or Sell"
        hit_tp_sl: str
        if operation_type == 'Buy':
            if closing_price >= tp:
                hit_tp_sl = 'Hit TP'
            elif closing_price <= sl:
                hit_tp_sl = 'HI SL'
            else:
                hit_tp_sl = 'Not Hit'
        # Sell
        else:
            if closing_price <= tp:
                hit_tp_sl = 'Hit TP'
            elif closing_price >= sl:
                hit_tp_sl = 'Hit SL'
            else:
                hit_tp_sl = 'Not Hit'

        # CALCULATE IF THE TRADE WAS A "PROFIT" OR "LOSS"
        opening_closing_diff = closing_price - buying_price

        # CALCULATE PIPs GOT
        # lots * pip_value * contract_size
        lot = volume_lot
        pip_size = 0.01
        contract_size = 100
        pip_value = lot * pip_size * contract_size

        # CALCULATE MONEY GOT
        # 100 pips = $1
        pips_per_dollar = 100
        money_got_in_pips = (
            opening_closing_diff * pips_per_dollar
        ) * pip_value
        money_got_in_dollars = money_got_in_pips / pips_per_dollar

        profit_or_loss_dict: dict[str, str | float] = {
            'result_type': None,
            'money_got_in_pips': money_got_in_pips,
            'money_got_in_dollars': money_got_in_dollars
        }

        if operation_type == 'Buy':
            if opening_closing_diff > 0:
                profit_or_loss_dict['result_type'] = 'Profit'
            else:
                profit_or_loss_dict['result_type'] = 'Loss'
        # Sell
        else:
            if opening_closing_diff < 0:
                profit_or_loss_dict['result_type'] = 'Profit'
            else:
                profit_or_loss_dict['result_type'] = 'Loss'

        # dictionary with all data to create the record
        trade_dict: dict[str, str | float] = {
            'uuid': str(uuid4().hex[:8]),
            'asset_type': asset_type,
            'asset_symbol': asset_symbol,
            'strategy': strategy,
            'operation_type': operation_type,
            'buying_price': buying_price,
            'closing_price': closing_price,
            'volume_lot': volume_lot,
            'tp': tp,
            'sl': sl,
            'hit_tp_sl': hit_tp_sl,
            'profit_or_loss_in_pips': profit_or_loss_dict['money_got_in_pips'],
            'profit_or_loss_in_dollars': profit_or_loss_dict['money_got_in_dollars'],
            'result_type': profit_or_loss_dict['result_type'],
            'date_and_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        # Add to CSV
        self.create_new_row(trade_dict)

    def create_new_row(self, trade_dict: dict[str, str | float]):
        """
        crate_record method is used to crate a new record to the CSV file.
        """
        self.csv_file_attacher.attach_new_row(trade_dict)
        # self.excel_file_attacher.attach_new_row(trade_dict)
