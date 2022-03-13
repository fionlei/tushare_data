# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.ccass_hold_detail(**{
    "ts_code": "",
    "trade_date": "",
    "start_date": "",
    "end_date": "",
    "hk_code": "",
    "limit": "",
    "offset": ""
}, fields=[
    "trade_date",
    "ts_code",
    "name",
    "col_participant_id",
    "col_participant_name",
    "col_shareholding",
    "col_shareholding_percent"
])
print(df)

