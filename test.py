import tushare as ts

ts.set_token('c1b67fa34c1c27f1f02ab48485b2d0cefa255e64f40286527f9df767')
pro = ts.pro_api()

# to get trade canlender
df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')

# get index basic
"""
市场代码	说明
MSCI	MSCI指数
CSI	    中证指数
SSE	    上交所指数
SZSE	深交所指数
CICC	中金指数
SW	    申万指数
OTH	    其他指数
"""

df_index = pro.index_basic(market='SSE')

# get index daily data
df_sh000001 = pro.index_daily(ts_code='000001.DH', start_date = '20180101', end_date='20181010')



