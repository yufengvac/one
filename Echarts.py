# -*- coding:utf-8 -*-
from pyecharts import Style
from pyecharts import Geo

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

city =[]
with open('xie_zheng_1.txt', 'r') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            city.append(row.split(',')[2].replace('\n', ''))


def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result


data = []
for item in all_list(city):
    data.append(item, all_list(city)[item])
    style = Style(
        title_color="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color="#404a59"
    )

geo = Geo('<<邪不压正》粉丝人群地址位置', **style.init_style)
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 20],
        visual_text_color="#fff", symbol_size=20,
        is_visualmap=True, is_piecewise=True,
        visual_split_number=4)
geo.render()
