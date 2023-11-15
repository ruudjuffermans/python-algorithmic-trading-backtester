# pylint: disable=C0114,C0115,R0903
from .indicator import Indicator

class RSI(Indicator):

    def calc(self):
        print("calculating rsi...")
        print("width data row count: ", len(self.data))
        