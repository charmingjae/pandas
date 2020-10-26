#!/usr/bin/env python
# coding: utf-8


# import
import pandas as pd
import numpy as np
from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt


# Fonts
font_loc = '/Library/fonts/Arial unicode.ttf'
font_name = font_manager.FontProperties(fname=font_loc).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

# read excel file
df = pd.read_excel('./temp/2012MonthlyTypeAccident.xlsx')
# typeList
typeList = [u'차대사람', u'차대차', u'차량단독', u'철길건널목']
# ColumnList
columnList = [u'차대사람사망자수', u'차대차사망자수', u'차량단독사망자수', u'철길건널목사망자수']

# Make empty dataframe
results = pd.DataFrame()

# add dummy column
results['test'] = ' '

# merge filtered dataframe with empty dataframe
for f in range(len(typeList)):
    data = df[(df[u'사고유형_대분류'] == typeList[f]) & (
        df[u'월'] == u'사망자수')].iloc[:, 4:].sum()
    data.name = columnList[f]
    data.to_frame()
    results = results.merge(
        data, how='outer', left_index=True, right_index=True)
# convert 'NaN' to space character
results['test'] = ' '

print(results)

fig, ax = plt.subplots()
# index : x축 좌표
index = np.arange(results[u'차대사람사망자수'].shape[0])
# index-0.15, +0.15는 그래프 두 개를 눈금을 기준으로 정확히 좌우에 위치시키기 위함.
ax.bar(index-0.15, results['차대사람사망자수'], width=0.3, label=u'차대사람')
ax.bar(index+0.15, results['차대차사망자수'], width=0.3, label=u'차대차')
# set title, xlabel, ylabel
ax.set_title(u'교통사고 유형별 월별 사망자수 비교')
ax.set_xlabel(u'월')
ax.set_ylabel(u'사망자수')
ax.legend()
ax.set_xticks(index)
ax.set_xticklabels(results.index)

plt.show()

ax.figure.savefig('./fig.png', dpi=1000)
