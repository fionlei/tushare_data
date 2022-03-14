# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.index_member(**{
    "index_code": "801030.SI",
    "is_new": "",
    "ts_code": "",
    "limit": "",
    "offset": ""
}, fields=[
    "index_code",
    "con_code",
    "in_date",
    "out_date"
])
print(df)

