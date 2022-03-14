# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.daily_info(**{
    "trade_date": "",
    "ts_code": "",
    "exchange": "",
    "start_date": "",
    "end_date": "",
    "limit": "",
    "offset": ""
}, fields=[
    "trade_date",
    "ts_code",
    "ts_name",
    "com_count",
    "total_share",
    "float_share",
    "total_mv",
    "float_mv",
    "amount",
    "vol",
    "trans_count",
    "pe",
    "tr",
    "exchange"
])
print(df)

