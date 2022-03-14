# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.ths_daily(**{
    "ts_code": "",
    "trade_date": "",
    "start_date": "",
    "end_date": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "trade_date",
    "close",
    "open",
    "high",
    "low",
    "pre_close",
    "avg_price",
    "change",
    "pct_change",
    "vol",
    "turnover_rate"
])
print(df)

