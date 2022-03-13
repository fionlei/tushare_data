# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.hk_hold(**{
    "code": "",
    "ts_code": "",
    "trade_date": "",
    "start_date": "",
    "end_date": "",
    "exchange": "",
    "limit": "",
    "offset": ""
}, fields=[
    "code",
    "trade_date",
    "ts_code",
    "name",
    "vol",
    "ratio",
    "exchange"
])
print(df)

