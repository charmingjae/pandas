#!/usr/bin/env python
# coding: utf-8

# # 데이터 처리 및 시각화
import pandas as pd
import numpy as np
from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt

font_loc = '/Library/fonts/Arial unicode.ttf'
font_name = font_manager.FontProperties(fname=font_loc).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('./temp/2012MonthlyTypeAccident.xlsx')
typeList = [u'차대사람', u'차대차', u'차량단독', u'철길건널목']
columnList = [u'차대사람사망자수', u'차대차사망자수', u'차량단독사망자수', u'철길건널목사망자수']

results = pd.DataFrame()
results['test'] = ' '
for f in range(len(typeList)):
    data = df[(df[u'사고유형_대분류'] == typeList[f]) & (
        df[u'월'] == u'사망자수')].iloc[:, 4:].sum()
    data.name = columnList[f]
    data.to_frame()
    results = results.merge(
        data, how='outer', left_index=True, right_index=True)
results['test'] = ' '

results

fig, ax = plt.subplots()
index = np.arange(results[u'차대사람사망자수'].shape[0])
ax.bar(index-0.15, results['차대사람사망자수'], width=0.3, label=u'차대사람')
ax.bar(index+0.15, results['차대차사망자수'], width=0.3, label=u'차대차')
ax.set_title(u'교통사고 유형별 월별 사망자수 비교')
ax.set_xlabel(u'월')
ax.set_ylabel(u'사망자수')
ax.legend()
ax.set_xticks(index)
ax.set_xticklabels(results.index)

ax.figure.savefig('./fig.png', dpi=1000)
