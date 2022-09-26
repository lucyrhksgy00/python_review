import make_data as md
import pandas as pd
from Color import *

cprint('10. append')
df1 = pd.DataFrame(md.make_data(5))
print(df1)
df2 = pd.DataFrame(md.make_data(5))
print(df2)
df3 = df1.append(df2)
print(df3)
print()

print(df3[8:9])
# index를 새로 구성
print(df3.reset_index())
print()
# 기존 인덱스를 삭제
print(df3.reset_index(drop=True))   # df3 = df1.append(df2).reset_index(drop=True)
# append시에 바로 처리 가능
df3 = df1.append(df2, ignore_index=True)
print(df3)
print()

cprint('11. concat')
df1 = pd.DataFrame(md.make_data(5))
print("df1")
print(df1)
print()
df2 = pd.DataFrame(md.make_data(5))
print("df2")
print(df2)
print()
# axis 설정을 하지 않으면 row 기준으로 붙는다.
df3 = pd.concat([df1, df2, df1, df1, df1]).reset_index(drop=True)
print(df3)
print()
# axis=1 설정으로 column 단위로 붙일 수 있음
# 기본적으로 데이터가 많은 쪽 기준으로 생성(부족하면 NaN)
df4 = pd.concat([df3, df1], axis=1).reset_index(drop=True)
print("df4")
print(df4)
print()
# 데이터가 적은 쪽으로 생성되려면 inner join 옵션을 줄 수 있다.
df5 = pd.concat([df3, df1], axis=1, join='inner').reset_index(drop=True)
print("df5")
print(df5); print()

# inner join의 의미를 생각해보자.
df3 = pd.concat([df1, df2])
print('join without reset_index')
print('df3')
print(df3); print()
df4 = pd.concat([df3, df1], axis=1)
print('df4')
print(df4); print()

cprint('12. groupby')
g_df = pd.DataFrame(md.make_data())
print("g_df")
print(g_df)
print('size()')
result_df = g_df.groupby('Name').size().reset_index(name='Counts')
print(result_df)

# One Punch
df_end = g_df.groupby('Name').agg(['min','max','mean','median','sum','var','std']).reset_index()
print(df_end)
print()

cprint('13. select')
print(df_end.head(3))
print(df_end.tail(3))
print(df_end.loc[2:4])
print(df_end.loc[1]['Name'][''])
print()

cprint('14. csv, excel')
df1 = pd.DataFrame(md.make_data(100))

# excel writing
df1.to_excel('day19.xlsx', sheet_name='19일차', index=False,
             engine='xlsxwriter', encoding='utf-8-sig')

# excel reading
e_df = pd.read_excel('day19.xlsx', '19일차')
print(e_df)

# csv writing
df1.to_csv('day19.csv', index=False)

# csv reading
c_df = pd.read_csv('day19.csv')
print(c_df)

import time
t1 = time.time()
hos_df = pd.read_csv('1.병원정보서비스 2022.6.csv', encoding='cp949')
t2 = time.time()
print('CSV data loading time :', t2-t1)
print(hos_df.head())
print(hos_df.tail())