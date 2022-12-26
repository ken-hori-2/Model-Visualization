import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()

x = [1, 2, 3, 4, 5]
y = [0, 0, 0, 0, 0]

def update(i):
    plt.cla()

    rand = random.randint(0, 4) # 5)
    # y[rand] += 1
    y[i] = 0.5
    ax.bar(x,y)

    plt.title('i=' + str(i) + '   [ ' + str(rand+1) + ' ]')

    # if np.max(y) <100:
    #     plt.ylim(0, 100)

# ani = animation.FuncAnimation(fig, update, interval = 100)
ani = animation.FuncAnimation(fig, update, interval = 1000)
plt.show()
