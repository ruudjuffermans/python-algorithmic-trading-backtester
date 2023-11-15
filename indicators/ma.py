# pylint: disable=C0114,C0115,R0903
from .indicator import Indicator

class MA(Indicator):

    def calc(self):
        print("calculating ma...")
        print("width data row count: ", len(self.data))
