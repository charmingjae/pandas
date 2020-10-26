# _*_coding:utf-8 _*_
'''
Created on 2019. 11. 5.

@author: jacknsun
'''

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = "/Library/Fonts/Arial unicode.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('./temp/2012MonthlyTypeAccident.xlsx')
# 사고유형(사고유형_대분류)에 따른 사망자수 데이터 추출 및 합계 구하기
typeList = [u'차대사람', u'차대차', u'차량단독', u'철길건널목']
columnList = [u'차대사람사망자수', u'차대차사망자수', u'차량단독사망자수', u'철길건널목사망자수']

data_result = pd.DataFrame()

for i in range(len(typeList)):
    # 사고유형_대분류(대사람, 차대차, 차량단독, 철길건널목)& 월별 사망자수의 값만 가져옴
    data_type = df[(df[u'사고유형_대분류'] == typeList[i]) & (df[u'월'] == u'사망자수')]
    data_result[columnList[i]] = data_type.sum().tail(
        12)  # 합산 값 12월까지 뽑은 후  컬럼에 넣기


print("typeList에 속하는 월별 사망자수를 가져옴 \n")
print(data_type)
print("\n각 분류별 합계를 보여줌 \n")
print(data_result)


list_array = np.arange(data_result[u'차대사람사망자수'].shape[0])
bar_width = 0.3
fig, ax = plt.subplots()
car_vs_car_local = list_array + bar_width
chart_car_vs_people = ax.bar(
    list_array, data_result[u'차대사람사망자수'], bar_width, label=u'차대사람')
chart_car_vs_car = ax.bar(
    car_vs_car_local, data_result[u'차대차사망자수'], bar_width, label=u'차대차')

ax.set_xlabel(u'월')
ax.set_ylabel(u'사망자수')
ax.set_title(u'교통사고 유형별 월별 사망자수 비교')
ax.set_xticks(list_array + bar_width/2)
ax.set_xticklabels(data_result.index)
ax.legend()
plt.show()
