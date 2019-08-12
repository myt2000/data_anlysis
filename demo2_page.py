from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

myfont = font_manager.FontProperties(fname=r'E:/font/font45/msyh.TTF')
font={
'family':'Microsoft Yahei',
"size":"10"
}



x = range(0,120)
# y = [random.randint(20,35) for i in range(120)]
# 随机种子
random.seed(10)
y = [random.uniform(20,35) for i in range(120)]

plt.figure(figsize=(20,8), dpi=80)
plt.plot(x,y)

_xtick_labels = ["10点{}分".format(i) for i in range(0,60)]
_xtick_labels += ["11点{}分".format(i) for i in range(0,60)]

plt.xticks(ticks=list(x)[::5], labels=_xtick_labels[::5], rotation=45, fontproperties=myfont)

plt.show()


