# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.concept(**{
    "src": "",
    "limit": "",
    "offset": ""
}, fields=[
    "code",
    "name",
    "src"
])
print(df)

