# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.stock_company(**{
    "ts_code": "",
    "exchange": "",
    "status": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "exchange",
    "chairman",
    "manager",
    "secretary",
    "reg_capital",
    "setup_date",
    "province",
    "city",
    "website",
    "email",
    "employees",
    "introduction",
    "office",
    "ann_date",
    "business_scope",
    "main_business"
])
print(df)

