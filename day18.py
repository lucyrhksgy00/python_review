import pandas as pd
import numpy as np
from Color import *

cprint("1. Series")
s = pd.Series([1.0, 3.0, 5.0, 7.0, 9.0])
print(s)
print(type(s))
print()

# 1. 스칼라(Scalar) 데이터
s1 = pd.Series(7, index=['a','b','c'])
print(s1)
print()

# 2. 1차원 배열 데이터
s2 = pd.Series(np.random.randn(5))   # 정규분포(Gaussian distribution)
print(s2)
print()
s3 = pd.Series(np.random.randn(5),
               index=['jan','feb','mar','apr','may'])
print(s3)
print()

# 3. 리스트 데이터
s4 = pd.Series([1,2,3,4,5],
               index=['봄','ㅇㅇㅇ','ddd','ths','e'])
print(s4)
print()

# 4. 딕셔너리 데이터
s5 = pd.Series({'a':0, 'subject':'sci', 'score':9})
print(s5)
print()

# 5. range 데이터
s6 = pd.Series(range(10), index=range(9, -1, -1))
print(s6)
print()

cprint("2. date_range")
# 1. start와 end를 지정해서 날짜 생성
date1 = pd.date_range(start='2022-09-01', end='2022-09-10')
print("2-1", date1)
print()

# 2. start와 periods를 지정해서 날짜 생성
date2 = pd.date_range(start='2022-09-01', periods=7)
print("2-2", date2)
print()

# 3. 2일씩 증가하는 날짜 데이터 생성
date3 = pd.date_range(start='2023-01-01', periods=10, freq='2D')
print("2-3", date3)
print()

# 4. 1시간 주기로 10시간 생성
date4 = pd.date_range(start='2022-09-01 08:00', periods=10, freq='H')
print("2-4", date4)
print()

# 5. 30분 단위로 4개 시간 생성(30분 : 0.5H, 30MIN, 30min, 30T)
date5 = pd.date_range(start='2022-09-01 10:00', periods=4, freq='0.5H')
print("2-5", date5)
print()

# 6. 10초 단위로 4개 시간 생성
date6 = pd.date_range(start='2022-09-01 22:07:11', periods=4,
                      freq='10S')
print("2-6", date6)
print()

# 7. 1개월 단위로 10개월
date7 = pd.date_range(start='2022-01-15 08:00', periods=10,
                      freq='1M')
print("2-7", date7)
print()

cprint("3. DataFrame")
# 1. numpy의 2차원 배열 데이터 사용
data1 = np.array([[10,20,30],[40,50,60]])
print(data1.shape)
df1 = pd.DataFrame(data1)
print("3-1"); print(df1); print()

# 2. index와 column을 지정된 날짜와 문자로 출력
data2 = np.array([[10,20,20],[0,0,5],[5,10,15]])
index_date = pd.date_range('2022-09-01', periods=3)
col_name = ['py','C','Java']
df2 = pd.DataFrame(data2, index=index_date, columns=col_name)
print(RED); print("3-2"); print(df2); print(); print(END)

# 3. 어느 회사의 연도 및 지사별 고객수 데이터
# 데이터가 딕셔너리 형태임
data = {'연도':[2020, 2021, 2021, 2022, 2022],
        '지사':['kor','kor','usa','kor','usa'],
        '고객':[200, 250, 450, 300, 500]}
df3 = pd.DataFrame(data)
print("3-3"); print(df3); print()
print(list(df3.index))
print(list(df3.columns))
print(df3.values)
print()

cprint("4. Key")
# 데이터 프레임 생성
data = {'weight':[80, 70, 65, 46, 51],
        'height':[50, 30, 80, 45, 50],
        'type':['f', 's', 'f', 'o', 'o']}
df4 = pd.DataFrame(data)
print(df4); print()
# weight 목록 추출
print(df4[['weight']])
# weight와 height 목록 추출
print(df4[['weight', 'height']])
print()

cprint("5. Slice")
df5 = pd.DataFrame(data)
print(df5); print()
# 2, 3 index 데이터 출력
print(df5[2:4])   # 값 1개만 주면 Key로 인식
# 3번째 이후 모두 출력
print(df5[3:])
print()

cprint("6. Filter")
df6 = pd.DataFrame(data)
print(df6); print()
# height가 50 이상인 것만 추출
print(df6[df6.height >= 50])
# type이 o인 것들만 추출
print(df6[df6.type == 'o'])

# height가 50 이상이면서 type이 o인것만 추출
df7 = df6[df6.height >= 50]
print(df7[df7.type == 'o'])
print()

cprint("7. Sort")
df7 = pd.DataFrame(data)
# height로 오름차순 (작은 것부터)
print(df7.sort_values(by='height')); print()
# weight로 내림차순 (큰 것부터)
print(df7.sort_values(by='weight', ascending=False)); print()

cprint("8. Rot")
df8 = df7
print(df8); print()
print(df8.T); print()

## ************
cprint('Special')
df9 = df8.T
print(df9); print()
print(df9[[2]])   # 2열 선택
print(df9[0:2])   # 0, 1열 선택 (이름을 지정했어도 내부적으로 숫자 인덱스 보관)
print(df9.loc[['height', 'weight']])