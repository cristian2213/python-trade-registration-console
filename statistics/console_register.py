import questionary
import csv
from uuid import uuid4


class ConsoleRegister:
    """
    ConsoleRegister class is used to register trades in a CSV file.
    """

    def __init__(self, file_path="trades.csv"):
        self.file_path = file_path

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
        profit_loss: str
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
            'uuid': str(uuid4()),
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
        self.attach_record(trade_dict)

    def attach_record(self, trade_dict: dict[str, str | float]):
        """
        attach_record method is used to attach a new record to the CSV file.
        """
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=trade_dict.keys())
            writer.writerow(trade_dict)

    def update_record(self, uuid: str):
        """
        update_record method is used to update an existing record in the CSV file.
        """
        pass

    def delete_record(self, uuid: str):
        """
        delete_record method is used to delete an existing record in the CSV file.
        """
        pass
