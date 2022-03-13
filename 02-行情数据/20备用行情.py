# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.bak_daily(**{
    "ts_code": "",
    "trade_date": "",
    "start_date": "",
    "end_date": "",
    "offset": "",
    "limit": ""
}, fields=[
    "ts_code",
    "trade_date",
    "name",
    "pct_change",
    "close",
    "change",
    "open",
    "high",
    "low",
    "pre_close",
    "vol_ratio",
    "turn_over",
    "swing",
    "vol",
    "amount",
    "selling",
    "buying",
    "total_share",
    "float_share",
    "pe",
    "industry",
    "area",
    "float_mv",
    "total_mv",
    "avg_price",
    "strength",
    "activity",
    "avg_turnover",
    "attack",
    "interval_3",
    "interval_6"
])
print(df)

