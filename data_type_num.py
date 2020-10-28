import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
res = {}
s2n = { 'mil':"军事",
        "jinrong":"金融",
         "gat":"港澳台",
        'ty':"体育",
        'wine':"葡萄酒",
        'jk':"健康",
        'world':"世界",
        'society':"社会",
        'life':"生活",
        'car':"汽车",
        'it':"信息技术",
        'house':"房产",
        'energy':"能源",
        'yl':"娱乐"}
for root,dirs,files in os.walk('./raw_data/'):
    if(len(root) > 11):
        res[root[11:]] = len(files)

x_index = np.arange(len(res))   #柱的索引
x_data = []
y_data = []
qualify_cat = []
for (k,v) in  res.items():
    x_data.append(k)
    y_data.append(v)
    if v > 50000:
        qualify_cat.append(k)
qualify_cat
bar_width = 0.5 #定义一个数字代表每个独立柱的宽度
rects1 = plt.bar(x_index, y_data, width=bar_width,alpha=0.4, color='b',label='legend1')            #参数：左偏移、高度、柱宽、透明度、颜色、图例
plt.xticks(x_index, x_data)   #x轴刻度线
plt.legend()    #显示图例
plt.tight_layout()  #自动控制图像外部边缘，此方法不能够很好的控制图像间的间隔
plt.show()