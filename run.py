from indicators import MA, RSI

ma = MA(window=3)
rsi = RSI(window=3)

ma.add(3)
ma.calculate_all_registered()
print(ma.data)
ma.add(4)
ma.calculate_all_registered()
print(ma.data)
ma.add(5)
ma.calculate_all_registered()
print(ma.data)
ma.add(6)
ma.calculate_all_registered()
print(ma.data)
ma.add(7)
ma.calculate_all_registered()
