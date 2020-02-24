import numpy as np
import pandas as pd

## 1.1) 엑셀을 Pandas.DataFrame으로 읽어온 뒤, 한국column의 데이터를 추가하고 다시 저장하기
data_path = 'C:\\Users\\bbjjh\\OneDrive\\바탕 화면\\파이썬 스터디\\판다스과제\\corona.xlsx'
df = pd.read_excel(data_path)
data_kr = [1, 1, 2, 3, 4, 7]
df['한국'] = data_kr

## 1.2) 위 파일을 불러와서 원래 데이터는 sheet1에, 중국에 대한 데이터는 sheet2에, 타국은 sheet3에, 한국은 sheet4에 저장하기
# XlsxWriter 엔진으로 Pandas writer 객체 만들기
writer = pd.ExcelWriter(data_path, engine='xlsxwriter')
# DataFrame을 xlsx에 쓰기
df.to_excel(writer, sheet_name = 'Sheet1')
df['중국'].to_excel(writer, sheet_name = 'Sheet2')
df['타국'].to_excel(writer, sheet_name = 'Sheet3')
df['한국'].to_excel(writer, sheet_name = 'Sheet4')
## Pandas writer 객체 닫기
writer.close()


## pip install xlsxwriter
## engine이 무엇인지


