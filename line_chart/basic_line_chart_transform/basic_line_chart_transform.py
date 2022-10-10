# 导入pyplot
from matplotlib import pyplot as plt
# 导入numpy
import numpy as np

# 1:设置图形大小:figsize图片大小,dpi是清晰程度,dpi越高,图像越清晰
# figure图形图标的意思,在这里指的就是我们画的图
# 通过实例化一个figure并且传递参数,能够在后台自动使用该figure实例
# 在图像模糊的时候可以传入dpi参数,让图片更加清晰
plt.figure(figsize=(20, 8), dpi=200)

# 4:调整x或者y的刻度的间距
# 取步长为间隔，下面中去步长为3，即可横轴上得到8个刻度
# 当刻度太稀疏时,可以取消步长,或者缩小间距
# 一天24小时为横坐标
x_time = range(0, 24, 3)
# 当刻度太密集时候使用列表的步长(间隔取值)来解决
y_temperature = np.random.randint(30, 38, 8)

# 绘图:传入x和y ,通过plot绘制出折线图
plt.plot(x_time, y_temperature)

# 2:保存(保存应在绘图之前进行)
plt.savefig("basic_line_chart_transform.png")

# 显示图形
plt.show()