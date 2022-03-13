# 导入tushare
import tushare as ts

#取000001的前复权行情
df = ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='20180101', end_date='20181011')
print(df)


#取上证指数行情数据
df = ts.pro_bar(ts_code='000001.SH', asset='I', start_date='20180101', end_date='20181011')
print(df)

#均线
df = ts.pro_bar(ts_code='000001.SZ', start_date='20180101', end_date='20181011', ma=[5, 20, 50])
print(df)