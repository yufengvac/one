# encoding : utf-8
# -*- coding: utf-8 -*-
from pyecharts import Bar
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


bar = Bar('我的第一个图表', "附标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 12, 4, 25, 89, 1, 32], is_more_utils= True)
bar.show_config()
bar.render()
