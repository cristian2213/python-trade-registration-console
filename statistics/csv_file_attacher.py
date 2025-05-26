import csv
from pathlib import Path
from .file_sys_helper import FileSysHelper


class CSVFileAttacher:
    """
    CSVFileAttacher class is used to handle CSV file operations.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_sys_helper = FileSysHelper(file_path)

    def attach_new_row(self, trade_dict: dict[str, str | float]):
        file_exists = self.file_sys_helper.file_exists()
        with open(self.file_path, 'a', newline='') as csvFile:
            writer = csv.DictWriter(
                csvFile, fieldnames=trade_dict.keys(), delimiter=',')
            if not file_exists:
                writer.writeheader()
            writer.writerow(trade_dict)


# if __name__ == '__main__':
    # Path(__file__).parent / '../files/trades.csv')
    # csv_file_attacher = CSVFileAttacher()
    # csv_file_attacher.attach_new_row({
    #     'uuid': '123',
    #     'asset_type': 'Stock',
    #     'asset_symbol': 'AAPL',
    #     'strategy': 'ABCD',
    #     'operation_type': 'Buy',
    #     'buying_price': 100,
    #     'closing_price': 101,
    #     'volume_lot': 1,
    #     'tp': 102,
    #     'sl': 99,
    #     'hit_tp_sl': 'Hit TP',
    #     'profit_or_loss_in_pips': 1,
    #     'profit_or_loss_in_dollars': 1,
    #     'result_type': 'Profit',
    #     'date_and_time': '2025-05-26 11:52:32'
    # })
