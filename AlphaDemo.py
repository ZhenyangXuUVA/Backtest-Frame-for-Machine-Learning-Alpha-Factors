from backtest import Broker, AlphaFactor, DataLoader, HelperFunctions
import pandas as pd

class AlphaDemo(AlphaFactor):

    params = {'long_period': 250, 'short_period': 25}

    def __init__(self, data):
        super(AlphaDemo, self).__init__(data)
        self.am = HelperFunctions(size=1000)

    def on_start(self):
        print("策略开始")

    def on_stop(self):
        print("策略停止")

    def next_bar(self, bar: BarData):
        print(bar)
        self.am.update_bar(bar)
        if not self.am.inited:
            return
        if True:
            self.buy(bar.close_price, 1)
        else:
            self.sell(bar.close_price, 1)

if __name__ == '__main__':

    df1 = pd.read_pkl('股票量价数据')
    df2 = pd.read_pkl('股票基本面数据')
    df3 = pd.read_pkl('股票ST数据')
    df = df[df['open_time'] >= '2020-01-01']
    df = df[df['open_time'] <= '2023-12-30']

    df.reset_index(inplace=True, drop=True)

    broker = Broker()
    broker.set_strategy(AlphaDemo)
    broker.set_leverage(1.0)
    broker.set_cash(1000000)
    broker.set_backtest_data(df)
    broker.run()
    broker.optimize_strategy(long_period=\
    [i for i in range(100, 300, 10)], \
    short_period=[i for i in range(50, 100, 5)])

