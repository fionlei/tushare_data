# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.fina_mainbz(**{
    "ts_code": "000001.SZ",
    "period": "",
    "type": "",
    "start_date": "",
    "end_date": "",
    "is_publish": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "end_date",
    "bz_item",
    "bz_sales",
    "bz_profit",
    "bz_cost",
    "curr_type",
    "bz_code",
    "update_flag"
])
print(df)

