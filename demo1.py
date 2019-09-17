import tushare as ts
import matplotlib.pyplot as plt

ts.set_token('8bfdd3d334d52c1c54c9c4d71595ea9b9b0a8e80cce8f7b707efd517')
pro = ts.pro_api()
x = ts.get_today_ticks('600446')
print(x)