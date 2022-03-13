# 导入tushare
import pandas as pd
import tushare as ts
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:xiaolei20220301@localhost:3306/tushare_data')

# 初始化pro接口
pro = ts.pro_api('ca0af3044cc38461f8e4ae128c9edabc12bcab9f4628f5cf6b6d863a')

# 拉取数据
df = pro.stock_basic(**{
    "ts_code": "",
    "name": "",
    "exchange": "",
    "market": "",
    "is_hs": "",
    "list_status": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "symbol",
    "name",
    "area",
    "industry",
    "market",
    "list_date",
    "enname",
    "fullname",
    "cnspell",
    "exchange",
    "curr_type",
    "list_status",
    "delist_date",
    "is_hs"
])


# 读取mysql表中的数据
sql = ''' select * from stock_basic; '''
local_df = pd.read_sql_query(sql, engine)
local_df = local_df.drop('id', axis=1)

append_df=pd.concat([local_df, df]) #local_df.append(df)
append_df=append_df.drop_duplicates(subset=['ts_code'],keep=False)

print(local_df)
print("----------------")
print(df)
print("----------------")
print(append_df)
print("----------------")

append_df.to_sql('stock_basic',engine,if_exists='append',index=False,)