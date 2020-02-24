import numpy as np
import pandas as pd

## 경로
data_path = 'C:\\Users\\bbjjh\\OneDrive\\바탕 화면\\파이썬 스터디\\판다스과제\\auto-mpg.csv'
newData_path = 'C:\\Users\\bbjjh\\OneDrive\\바탕 화면\\파이썬 스터디\\판다스과제\\auto-mpg-2.xlsx'

## csv파일 읽어오기
df = pd.read_csv(data_path, header=None, sep=',')

## 2-1) 다음에 맞추어서 해당 데이터셋에 column name을 붙여 엑셀파일 auto-mpg-2.xlsx로 저장하라.

## 칼럼추가
df.columns = ['mpg(연비)', 'cylinders(실린더 수)', 'displacement(배기량)',
                               'horsepower(출력)', 'weight(차중)', 'acceleration(가속능력)',
                               'model_year(출시년도)', 'origin number(제조국 번호)', 'name(모델 명)']
## 엑셀파일로 새로운 이름으로 저장
df.to_excel(newData_path)

## 연비와 차중에 대한 mean 값을 구하라
mpg_mean = df['mpg(연비)'].mean()
weight_mean = df['weight(차중)'].mean()
print(mpg_mean, weight_mean)

## 연비와 출력의 표준편차를 구하라.
mpg_std = df['mpg(연비)'].std()
# horsepower_std = df['horsepower(출력)'].std()
# print(mpg_std, horsepower_std
# print(df.info())

## 출력의 표준편차는 실행이 안됨
# -> 336행에 '?' 데이터가 있음  df.info()로 확인한 결과 type = object 임
# 파이썬은 하나라도 값이 잘못 되있으면 표준편차 계산 오류가 뜸

## 출시년도를 최신순에 따라 데이터를 정렬해서 auto-mpg-2.xlsx의 sheet 2에 저장
# 출시년도 최신순으로 정렬, ascending = False : 내림차순 정렬
sorted_df = df.sort_values(by = ['model_year(출시년도)'], ascending= False)

#확인 코드
print(sorted_df['model_year(출시년도)'])

# XlsxWriter 엔진으로 Pandas writer 객체 만들기
writer = pd.ExcelWriter(newData_path, engine='xlsxwriter')

# DataFrame을 xlsx에 쓰기
df.to_excel(writer, sheet_name = 'Sheet1')
sorted_df.to_excel(writer, sheet_name = 'Sheet2')

## Pandas writer 객체 닫기
writer.close()

# 이건 왜 안되냐
# df = pd.DataFrame(df, columns=['mpg(연비)', 'cylinders(실린더 수)', 'displacement(배기량)',
#                                'horsepower(출력)', 'weight(차중)', 'acceleration(가속능력)',
#                                'model_year(출시년도)', 'origin number(제조국 번호)', 'name(모델 명)'])


## 깊은 복사 df = df[:], df.copy()