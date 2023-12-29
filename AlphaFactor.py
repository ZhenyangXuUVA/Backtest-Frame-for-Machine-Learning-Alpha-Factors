import numpy as np
import pandas as pd
from .data import DataLoader

class AlphaFactor(object):

    Broker = None
    DataLoader = None

    def __init__(self, data: pd.DataFrame):
        super(BaseStrategy, self).__init__()
        self.data = data

    def on_start(self):
        pass

    def on_stop(self):
        pass

    def next_bar(self, bar: BarData):
        raise NotImplementedError("在子类中实现")

    def buy(self, price, volume):
        self.broker.buy(price, volume)

    def sell(self, price, volume):
        self.broker.sell(price, volume)

    def short(self, price, volume):
        self.broker.short(price, volume)

    def cover(self, price, volume):
        self.cover(price, volume)

