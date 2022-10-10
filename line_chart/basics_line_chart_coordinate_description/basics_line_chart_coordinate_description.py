# 导入pyplot
from matplotlib import pyplot as plt, font_manager
# 导入numpy
import numpy as np

# 1:设置图形大小:figsize图片大小,dpi是清晰程度,dpi越高,图像越清晰
# figure图形图标的意思,在这里指的就是我们画的图
# 通过实例化一个figure并且传递参数,能够在后台自动使用该figure实例
# 在图像模糊的时候可以传入dpi参数,让图片更加清晰
plt.figure(figsize=(20, 8), dpi=200)

# 1:设置显示中文
# 为什么无法显示中文:
# matplotlib默认不支持中文字符，因为默认的英文字体无法显示汉字
# 查看linux/mac下面支持的字体:
# fc-list   查看支持的字体
# fc-list :lang=zh 查看支持的中文(冒号前面有空格)

# 那么问题来了:如何修改matplotlib的默认字体?

# 通过matplotlib.rc可以修改
# #windows和linux设置字体的方式
# font={  'family':'MicroSoft YaHei',
#         'weight':'bold',
#          'size':'larger'}
# matplotlib.rc("font",**font)#第一种方式
# matplotlib.rc('font',family="MicroSoft YaHei",'weight'='bold')#第二种方式

# 另外一种设置字体的方式,通过matplotlib 下的font_manager可以解决(windows/linux/mac) 常用√
font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

# 4:调整x或者y的刻度的间距
# 取步长为间隔，下面中去步长为3，即可横轴上得到8个刻度
# 当刻度太稀疏时,可以取消步长,或者缩小间距
# 一天24小时为横坐标
x_time = range(0, 24, 3)
# 当刻度太密集时候使用列表的步长(间隔取值)来解决
y_temperature = np.random.randint(30, 38, 8)

# 3:调整x轴刻度,显示时间 疏密 显示为字符串
# 先转换成列表
_x_time = list(x_time)
# 设置字符串显示,{}表示后面循序产生的参数
_xtick_labels = ["{}点".format(i) for i in range(0, 24, 3)]

plt.xticks(_x_time, _xtick_labels, rotation=45, fontproperties=font)
# _x_time 和 _xtick_labels 数字和字符串一一对应
# 数字和字符串的长度一样
# 旋转角度 rotation=90
# 设置字体中文显示 fontproperties=font

# 4:添加描述信息
plt.xlabel("时间 单位(h)", fontproperties=font)
plt.ylabel("温度 单位(℃)", fontproperties=font)
plt.title("24小时气温变化情况", fontproperties=font)

# 绘图:传入x和y ,通过plot绘制出折线图
plt.plot(x_time, y_temperature)

# 2:保存(保存应在绘图之前进行)
plt.savefig("basics_line_chart_coordinate_description.png")

# 显示图形
plt.show()
