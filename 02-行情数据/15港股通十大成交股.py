# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.ggt_top10(**{
    "ts_code": "00570.HK",
    "trade_date": "",
    "start_date": "",
    "end_date": "",
    "market_type": "",
    "limit": "",
    "offset": ""
}, fields=[
    "trade_date",
    "ts_code",
    "name",
    "close",
    "p_change",
    "rank",
    "market_type",
    "amount",
    "net_amount",
    "sh_amount",
    "sh_net_amount",
    "sh_buy",
    "sh_sell",
    "sz_amount",
    "sz_net_amount",
    "sz_buy",
    "sz_sell"
])
print(df)

