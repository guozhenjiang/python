# https://www.bilibili.com/video/av75871530?p=6

# coding=utf-8

from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

plt.figure(figsize=(20, 8), dpi=80)                     # 设置图片大小

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

# 调整 x 轴刻度
_x = list(x)
_xtick_labels = ['10点{}分'.format(i) for i in range(60)]
# _xtick_labels += ['11点{}分'.format(i-60) for i in range(60, 120)]
_xtick_labels += ['11点{}分'.format(i) for i in range(60)]

# 取步长，数字和字符串一一对应，数据的长度一样
# plt.xticks(_x[::3], _xtick_labels[::3], rotation=270)    # rotation 旋转的度数
plt.xticks(_x[::5], _xtick_labels[::5], rotation=-45)    # rotation 旋转的度数

plt.plot(x, y)

plt.savefig('./0605.png')

plt.show()