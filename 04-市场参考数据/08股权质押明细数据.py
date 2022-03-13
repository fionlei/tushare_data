# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.pledge_detail(**{
    "ts_code": "300103.SZ",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "ann_date",
    "holder_name",
    "pledge_amount",
    "start_date",
    "end_date",
    "is_release",
    "release_date",
    "pledgor",
    "holding_amount",
    "pledged_amount",
    "p_total_ratio",
    "h_total_ratio",
    "is_buyback",
    "holder_type",
    "desc"
])
print(df)

