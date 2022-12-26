import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from matplotlib import animation, gridspec

ax = plt.gca()
gs = gridspec.GridSpec(1, 2)
ss1 = gs.new_subplotspec((0, 0), rowspan=3,colspan=1)
ss2 = gs.new_subplotspec((0, 1), rowspan=1,colspan=2)

ax = [plt.subplot(ss1), plt.subplot(ss2)]

# left = np.array([1, 2, 3, 4, 5])
left = [1, 2, 3, 4, 5]
# height = np.array([100, 200, 300, 400, 500])
data = [20.0, 16.0, 11.0, 7.0, 0]
data2 = [9.0, 5.0, 0, 4.0, 0]

# カラーマップインスタンス生成
cm = plt.get_cmap("Blues")

seikika = np.round(preprocessing.minmax_scale(data), 3)

# color_maps = [cm(0.1), cm(0.3), cm(0.5), cm(0.7), cm(0.9)]
color_maps = [cm(seikika[0]), cm(seikika[1]), cm(seikika[2]), cm(seikika[3])] # , cm(data[4])]

# plt.bar(left, data, color=color_maps)
ax[0].bar(left, data, color=color_maps)

ax[1].bar(left, data2, color=color_maps)

plt.show()