# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.ggt_monthly(**{
    "month": "",
    "start_month": "",
    "end_month": "",
    "limit": "",
    "offset": ""
}, fields=[
    "month",
    "day_buy_amt",
    "day_buy_vol",
    "day_sell_amt",
    "day_sell_vol",
    "total_buy_amt",
    "total_buy_vol",
    "total_sell_amt",
    "total_sell_vol"
])
print(df)

