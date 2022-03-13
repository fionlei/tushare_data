# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.limit_list(**{
    "trade_date": "",
    "ts_code": "",
    "limit_type": "",
    "start_date": "",
    "end_date": "",
    "limit": "",
    "offset": ""
}, fields=[
    "trade_date",
    "ts_code",
    "name",
    "close",
    "pct_chg",
    "amp",
    "fc_ratio",
    "fl_ratio",
    "fd_amount",
    "first_time",
    "last_time",
    "open_times",
    "strth",
    "limit"
])
print(df)

