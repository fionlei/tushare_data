# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.dividend(**{
    "ts_code": "000001.SZ",
    "ann_date": "",
    "end_date": "",
    "record_date": "",
    "ex_date": "",
    "imp_ann_date": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "end_date",
    "ann_date",
    "div_proc",
    "stk_div",
    "stk_bo_rate",
    "stk_co_rate",
    "cash_div",
    "cash_div_tax",
    "record_date",
    "ex_date",
    "pay_date",
    "div_listdate",
    "imp_ann_date",
    "base_date",
    "base_share",
    "update_flag"
])
print(df)

