# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.index_dailybasic(**{
    "trade_date": "",
    "ts_code": "000001.SH",
    "start_date": "",
    "end_date": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "trade_date",
    "total_mv",
    "float_mv",
    "total_share",
    "float_share",
    "free_share",
    "turnover_rate",
    "turnover_rate_f",
    "pe",
    "pe_ttm",
    "pb"
])
print(df)

