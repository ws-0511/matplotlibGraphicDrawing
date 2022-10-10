# 导入pyplot
from matplotlib import pyplot as plt
# 导入numpy
import numpy as np

# 一天24小时为横坐标
x_time = range(0, 24, 1)
# 每个小时对应的温度为纵坐标
y_temperature = np.random.randint(20, 38, 24)

# 绘图:传入x和y ,通过plot绘制出折线图
plt.plot(x_time, y_temperature)

# 显示图形
plt.show()
