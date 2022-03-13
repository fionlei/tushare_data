# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.fina_audit(**{
    "ts_code": "000001.SZ",
    "ann_date": "",
    "start_date": "",
    "end_date": "",
    "period": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "ann_date",
    "end_date",
    "audit_result",
    "audit_agency",
    "audit_sign",
    "audit_fees"
])
print(df)

