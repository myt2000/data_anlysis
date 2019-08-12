# from matplotlib import pyplot as plt
# import random
# from matplotlib import font_manager
#
# myfont = font_manager.FontProperties(fname=r'E:/font/font45/msyh.TTF')
# font={
# 'family':'Microsoft Yahei',
# "size":"10"
# }
#
#
#
# x = range(0,120)
# # y = [random.randint(20,35) for i in range(120)]
# # 随机种子
# random.seed(10)
# y = [random.uniform(20,35) for i in range(120)]
#
# plt.figure(figsize=(20,8), dpi=80)
# plt.plot(x,y)
#
# _xtick_labels = ["10点{}分".format(i) for i in range(0,60)]
# _xtick_labels += ["11点{}分".format(i) for i in range(0,60)]
#
# plt.xticks(ticks=list(x)[::5], labels=_xtick_labels[::5], rotation=45, fontproperties=myfont)
#
# plt.show()
#

# coding=utf-8
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager


#设置字体，实例化一个fontproperties
my_font = font_manager.FontProperties(r'/root/data_analysis/data_anlysis/msyh.TTF')
my_font_larger = font_manager.FontProperties(fname=r'/root/data_analysis/data_anlysis/msyh.TTF',size="larger")

# myfont = font_manager.FontProperties(fname=r'/root/data_analysis/data_anlysis/msyh.TTF')
font={
'family':'Microsoft Yahei',
"size":"10"
}




x = range(0,120)
random.seed(10)
y= [random.randint(20,35) for i in range(120)]

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

#设置x轴的刻度,`10点2分`
_xtick_labels = ["10点{}分".format(i) for i in range(0,60)]
_xtick_labels += ["11点{}分".format(i) for i in range(0,60)]
plt.xticks(list(x)[::5],_xtick_labels[::5],rotation=45,fontproperties=my_font)

#添加图形信息
plt.xlabel("时间",fontproperties=my_font_larger)
plt.ylabel("温度 （℃）",fontproperties=my_font_larger)
plt.title("10-12点每隔一分钟气温的变化情况",fontproperties=my_font_larger)


plt.show()