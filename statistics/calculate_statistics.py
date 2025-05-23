import pandas as pd


class CalculateStatistics:
    def __init__(self, file_path):
        self.file_path = file_path

    def calculate_statistics(self):
        df = pd.read_csv(self.file_path)

        # Calculate PnL
        df['PnL'] = df['ClosePrice'] - df['BuyPrice']
        df['Result'] = df['PnL'].apply(lambda x: 'Win' if x > 0 else 'Loss')

        total_trades = len(df)
        wins = df[df['PnL'] > 0]
        losses = df[df['PnL'] <= 0]

        win_rate = (len(wins) / total_trades) * 100 if total_trades else 0
        avg_win = wins['PnL'].mean() if not wins.empty else 0
        avg_loss = losses['PnL'].mean() if not losses.empty else 0

        # Expectancy
        expectancy = (win_rate/100) * avg_win + \
            ((100 - win_rate)/100) * avg_loss

        # Risk-Reward ratio (avg)
        df['RR'] = (df['TP'] - df['BuyPrice']) / (df['BuyPrice'] - df['SL'])
        avg_rr = df['RR'].mean()

        # Group by strategy and asset
        strat_stats = df.groupby('Strategy')['PnL'].agg(['count', 'mean'])
        asset_stats = df.groupby('Asset')['PnL'].agg(['count', 'mean'])

        # Print the results
        print("\n===== Trade Statistics =====")
        print(f"Total Trades     : {total_trades}")
        print(f"Win Rate         : {win_rate:.2f}%")
        print(f"Average Win      : {avg_win:.2f}")
        print(f"Average Loss     : {avg_loss:.2f}")
        print(f"Expectancy       : {expectancy:.2f}")
        print(f"Avg Risk/Reward  : {avg_rr:.2f}")

        print("\n--- Strategy Performance ---")
        print(strat_stats)

        print("\n--- Asset Performance ---")
        print(asset_stats)
