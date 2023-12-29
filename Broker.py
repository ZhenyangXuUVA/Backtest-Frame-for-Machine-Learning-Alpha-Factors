import os
import itertools
import numpy as np
import pandas as pd
import collections
from .strategy import BaseStrategy, BarData

class Broker(object):
    def __init__(self):
        super(Broker, self).__init__()

        self.strategy_instance = None
        self.commission = 5/1000
        self.leverage = 1.0
        self.slipper_rate = 5/10000
        self.asset_value = 0
        self.min_margin_rate = 0.15
        self.cash = 2000000
        self.strategy_class = None
        self.trades = []
        self.active_orders = []
        self.backtest_data = None
        self.pos = 0
        self.is_optimizing_strategy = False


    def set_strategy(self, strategy_class:BaseStrategy):
        self.strategy_class = strategy_class

    def set_leverage(self, leverage: float):
        self.leverage = leverage

    def set_commission(self, commission: float):
        self.commission = commission

    def set_backtest_data(self, data: pd.DataFrame):
        self.backtest_data = data

    def set_cash(self, cash):
        self.cash = cash

    def buy(self, price, volume):
        print(f"做多下单: {volume}@{price}")


    def sell(self, price, volume):
        print(f"做多平仓下单: {volume}@{price}")

    def short(self, price, volume):
        print(f"做空下单: {volume}@{price}")

    def cover(self, price, volume):
        print(f"做空平仓下单: {volume}@{price}")

    def run(self):

        self.trades = []
        self.active_orders = []
        self.strategy_instance = self.strategy_class(self.backtest_data)
        self.strategy_instance.broker = self
        self.strategy_instance.on_start()
        for index, candle in self.backtest_data.iterrows():
            bar = BarData(candle['open_time'], candle['open'],
                          candle['high'], candle['low'], candle['close'], candle['volume'])
            self.check_order(bar)
            self.strategy_instance.next_bar(bar)
        self.strategy_instance.on_stop()
        self.calculate()

    def calculate(self):
        for trade in self.trades:
            pass

    def check_order(self, bar):
            pass


    def optimize_strategy(self, **kwargs):
        self.is_optimizing_strategy = True

        optkeys = list(kwargs)
        vals = iterize(kwargs.values())
        optvals = itertools.product(*vals)
        optkwargs = map(zip, itertools.repeat(optkeys), optvals)
        optkwargs = map(dict, optkwargs)

        for params in optkwargs:
            print(params)

        cash = self.cash
        leverage = self.leverage
        commission = self.commission
        for params in optkwargs:

            self.strategy_class.params = params
            self.set_cash(cash)
            self.set_leverage(leverage)
            self.set_commission(commission)
            self.run()

def iterize(iterable):
    niterable = list()
    for elem in iterable:
        if isinstance(elem, str):
            elem = (elem,)
        elif not isinstance(elem, collections.Iterable):
            elem = (elem,)
        niterable.append(elem)
    return niterable