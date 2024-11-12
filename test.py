import tushare as ts

ts.set_token('c1b67fa34c1c27f1f02ab48485b2d0cefa255e64f40286527f9df767')
pro = ts.pro_api()

# to get trade canlender
df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')

