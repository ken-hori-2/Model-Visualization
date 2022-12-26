from turtle import color
import matplotlib.pyplot as plt

import numpy as np


# data = [0, 0, 1, 2, 3, 4, 4, 0, 0, 1, 2, 3, 0, 0, 1, 2, 3, 4, 0, 0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10]

# data = [0.4, 0.2, 0.7, 0.3, 0.6]
        # O A B C
# data = [20.0, 16.0, 11.0, 7.0]
# data = [9.0, 5.0, 0.0, 4.0]
# data = [0.0, 4.0, 0.0, 13.0]
# data = [0.0, 0.0, 0.0, 9.0]

data = [0.25, 0.46, 0.38, 0.6]

data = [20.0, 16.0, 11.0, 7.0]
data = [9.0, 5.0, 0, 4.0]
data = [0, 4.0, 0, 13.0]
data = [0, .0, 0, 9.0]


x = np.arange(0, len(data), 1)


# 平均気温データ表示
fig = plt.figure()
subplot = fig.add_subplot(1,1,1)
# subplot.plot(x,data)
subplot.bar(x,data, color="green")
plt.show()