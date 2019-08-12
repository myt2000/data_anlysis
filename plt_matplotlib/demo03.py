# coding=utf-8
from matplotlib import pyplot as plt
from matplotlib import  font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")


y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]

x = range(11,31)

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y,label="自己",color='#FF69B4',linestyle="--")
plt.plot(x,y2,label="同桌",color='#3CB371',linestyle=':',linewidth=7)


#设置x轴的刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels,fontproperties=my_font)

#设置图例
plt.legend(loc=0,prop=my_font)

plt.show()