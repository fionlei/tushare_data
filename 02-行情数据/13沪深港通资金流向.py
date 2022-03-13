# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.moneyflow_hsgt(**{
    "trade_date": "",
    "start_date": 19900101,
    "end_date": "",
    "limit": "",
    "offset": ""
}, fields=[
    "trade_date",
    "ggt_ss",
    "ggt_sz",
    "hgt",
    "sgt",
    "north_money",
    "south_money"
])
print(df)

