#获取今年上证指数的日K信息，然后保存成 excel 文件，再画出每日的收盘指数的折线图。
import tushare as ts
import matplotlib.pyplot as plt

from openpyxl import Workbook
from openpyxl.compat import range

#print(ts.__version__)  #打印版本
#print(ts.get_hist_data('601688'))   #获取股票历史数据
#print(ts.get_realtime_quotes("000002")) #获取股票实时行情
#print(ts.get_deposit_rate())    #存款利率
#print(ts.get_stock_basics("2018-01-10"))

df = ts.get_hist_data("sh", "2018-01-01")
df.to_excel("stock_sh.xlsx")
df.close.plot()

ax = plt.gca()
ax.invert_xaxis()
plt.title("a simple example")
plt.show()
