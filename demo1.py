from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]

#设置图形的大小
plt.figure(figsize=(20,8),dpi=80, )

plt.plot(x,y)

#设置x轴的刻度
# plt.xticks(list(range(2,25))[::2])  #取步长调整刻度的密集程度
plt.xticks(range(1,25), labels=["天"]*24)

#设置y轴的刻度
plt.yticks(range(min(y),max(y)+1))

#保存图片
plt.savefig("a.png")

plt.show()