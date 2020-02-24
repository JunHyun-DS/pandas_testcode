import numpy as np
import pandas as pd

## 경로
data_path = 'C:\\Users\\bbjjh\\OneDrive\\바탕 화면\\파이썬 스터디\\판다스과제\\남북한발전전력량.xlsx'
newData_path = 'C:\\Users\\bbjjh\\OneDrive\\바탕 화면\\파이썬 스터디\\판다스과제\\남북한발전전력량2.xlsx'

## excel파일 읽어오기
df = pd.read_excel(data_path)# XlsxWriter 엔진으로 Pandas writer 객체 만들기
## 원본 데이터
original_df = df

## 남한 : 인덱싱 -> 연도별 부터 시작 -> 수력 값 + 화력 값 = 합게의 값
df.iloc[0, 2:] = df.iloc[1, 2:] + df.iloc[2, 2:]
df_south_kr = df.iloc[0:3, :]

## 북한 : 인덱싱 -> 연도별 부터 시작 -> 수력 값 + 화력 값 = 합게의 값
df.iloc[5, 2:] = df.iloc[6, 2:] + df.iloc[7, 2:]
df_north_kr = df.iloc[5:8, :]

# 분리한거 합치기
df_kr = pd.concat([df_south_kr, df_north_kr])

writer = pd.ExcelWriter(newData_path, engine='xlsxwriter')

# DataFrame을 xlsx에 쓰기
original_df.to_excel(writer, sheet_name = 'Sheet1')
df_kr.to_excel(writer, sheet_name = 'Sheet2')

# Pandas writer 객체 닫기
writer.close()