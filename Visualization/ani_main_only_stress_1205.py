from cProfile import label
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from matplotlib import patches
from matplotlib import animation, gridspec
from sklearn import preprocessing

# from ani_integrate_test3_meet import STATE_HISTORY

# エージェントの移動の様子を可視化します
# 参考URL http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/

# animation_Edit.py の整理ver.
# ani_integrate_test3_main.py の整理ver.

class Anim():
    
    def __init__(self, STATE_HISTORY):

        self.state_history = STATE_HISTORY
        # self.fig = plt.figure(figsize=(7, 7))
        self.fig = plt.figure(figsize=(8, 8.5))
        self.ax = plt.gca()
        self.ims = []

        # self.gs = gridspec.GridSpec(2, 2, height_ratios=(1, 1))
        # self.gs = gridspec.GridSpec(2, 2, height_ratios=(3, 1))
        self.gs = gridspec.GridSpec(3, 3) # , height_ratios=(1, 1))
        # self.ax = [plt.subplot(self.gs[0, 2]), plt.subplot(self.gs[0, 1]), plt.subplot(self.gs[1, 1])]
        ss1 = self.gs.new_subplotspec((0, 0), rowspan=3,colspan=1)
        ss2 = self.gs.new_subplotspec((1, 1), rowspan=1,colspan=2)
        self.ax = [plt.subplot(ss1), plt.subplot(ss2)] # , plt.subplot(ss3), plt.subplot(ss4), plt.subplot(ss5)]
        "-----------------------------------------------------"
        # グラフデータの初期化
        self.T = []
        # Statas数推移
        self.Stress_List= []
        self.im = []
        self.TEST = []
        self.legend_flag = True

    def view_plot_text(self):

        # Σn = 0.3
        self.stress = [0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 1.2, 0.3, 0.5, 0.7, 0.8999999999999999, 1.0999999999999999, 1.9666666666666663, 0.9666666666666663, 1.1666666666666663, 1.3666666666666663, 1.5666666666666662, 1.7666666666666662, 3.109523809523809, 2.109523809523809, 2.109523809523809, 2.109523809523809, 2.109523809523809, 2.109523809523809, 2.109523809523809, 2.109523809523809, 2.109523809523809, 2.109523809523809, 2.109523809523809, 2.109523809523809, 2.109523809523809, 2.109523809523809, 2.109523809523809, 1.309523809523809, 1.309523809523809, 2.182, 2.182, 2.182, 2.182, 2.182, 2.182, 1.482, 1.482, 2.124, 2.124]
        # # 0.1
        # self.stress = [0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.6666666666666665, 0.6666666666666665, 0.8666666666666665, 1.0666666666666664, 1.2666666666666664, 1.4666666666666663, 2.8095238095238093, 1.8095238095238093, 2.0095238095238095, 2.0095238095238095, 2.0095238095238095, 2.0095238095238095, 2.0095238095238095, 2.0095238095238095, 2.0095238095238095, 2.0095238095238095, 2.0095238095238095, 2.0095238095238095, 1.0095238095238095, 1.0095238095238095, 2.045, 2.045, 2.045, 2.045, 2.045, 2.045, 1.045, 1.045, 2.266, 2.266]

        # self.stress = [0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 1.2, 0.3, 0.5, 0.7, 0.8999999999999999, 1.0999999999999999, 1.4, 0.3999999999999999, 0.5999999999999999, 0.7999999999999998, 0.9999999999999998, 1.1999999999999997, 1.5714285714285712, 0.5714285714285712, 0.7714285714285711, 0.9714285714285711, 1.171428571428571, 1.371428571428571, 1.7964285714285708, 0.7964285714285708, 0.9964285714285708, 1.4630952380952373, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 1.0630952380952374, 0.2630952380952374, 0.2630952380952374, 2.174, 2.174, 2.174, 2.174, 2.174, 2.174, 1.474, 1.474, 2.433, 2.433]
        # self.stress = [0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 1.2, 0.3, 0.5, 0.7, 0.8999999999999999, 1.0999999999999999, 1.4999999999999998, 1.4999999999999998, 1.6999999999999997, 1.8999999999999997, 2.0999999999999996, 2.0999999999999996, 2.0999999999999996, 2.0999999999999996, 2.0999999999999996, 2.0999999999999996, 2.0999999999999996, 1.3999999999999997, 1.3999999999999997, 2.083, 2.083, 2.083, 2.083, 2.083, 2.083, 1.2830000000000001, 1.2830000000000001, 2.186, 2.186]

        # # N=2
        # self.stress = [0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 1.2, 0.3, 0.5, 0.7, 0.8999999999999999, 1.0999999999999999, 1.6999999999999997, 0.6999999999999997, 0.8999999999999997, 1.0999999999999996, 1.2999999999999996, 1.4999999999999996, 2.2999999999999994, 1.2999999999999994, 1.4999999999999993, 1.6999999999999993, 1.8999999999999992, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 1.2999999999999992, 1.2999999999999992, 2.123, 2.123, 2.123, 2.123, 2.123, 2.123, 1.4230000000000003, 1.4230000000000003, 2.411, 2.411]
        # # N=5
        # self.stress = [0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 1.2, 0.3, 0.5, 0.7, 0.8999999999999999, 1.0999999999999999, 1.4999999999999998, 0.4999999999999998, 0.6999999999999997, 0.8999999999999997, 1.0999999999999996, 1.2999999999999996, 1.8428571428571423, 0.8428571428571423, 1.0428571428571423, 1.2428571428571422, 1.4428571428571422, 1.6428571428571421, 2.292857142857142, 1.2928571428571418, 1.4928571428571418, 2.226190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.826190476190475, 1.026190476190475, 1.026190476190475, 2.018, 2.018, 2.018, 2.018, 2.018, 2.018, 1.3179999999999998, 1.3179999999999998, 2.153, 2.153]

        # "1"
        # self.stress = [0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 1.2, 0.3, 0.5, 0.7, 0.8999999999999999, 1.0999999999999999, 1.633333333333333, 0.6333333333333331, 0.833333333333333, 1.033333333333333, 1.233333333333333, 1.433333333333333, 2.133333333333333, 1.1333333333333329, 1.3333333333333328, 1.5333333333333328, 1.7333333333333327, 1.9333333333333327, 2.733333333333333, 1.733333333333333, 1.933333333333333, 2.7999999999999994, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 1.5999999999999994, 1.5999999999999994, 2.072, 2.072, 2.072, 2.072, 2.072, 2.072, 1.372, 1.372, 2.045, 2.045]
        self.stress = [0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 1.2, 0.3, 0.5, 0.7, 0.8999999999999999, 1.0999999999999999, 1.9666666666666663, 0.9666666666666663, 1.1666666666666663, 1.3666666666666663, 1.5666666666666662, 1.7666666666666662, 2.966666666666666, 1.966666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 1.366666666666666, 1.366666666666666, 2.258, 2.258, 2.258, 2.258, 2.258, 2.258, 1.558, 1.558, 2.406, 2.406]


        self.stress = [0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 1.2, 0.3, 0.5, 0.7, 0.8999999999999999, 1.0999999999999999, 1.633333333333333, 0.6333333333333331, 0.833333333333333, 1.033333333333333, 1.233333333333333, 1.433333333333333, 2.133333333333333, 1.1333333333333329, 1.3333333333333328, 1.5333333333333328, 1.7333333333333327, 1.9333333333333327, 2.733333333333333, 1.733333333333333, 1.933333333333333, 2.7999999999999994, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 2.3999999999999995, 1.5999999999999994, 1.5999999999999994, 2.134, 2.134, 2.134, 2.134, 2.134, 2.134, 1.434, 1.434, 2.412, 2.412]
        self.stress = [0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 1.7, 0.7, 0.8999999999999999, 1.0999999999999999, 1.2999999999999998, 1.4999999999999998, 2.3666666666666663, 1.3666666666666663, 1.5666666666666662, 1.7666666666666662, 1.9666666666666661, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 2.166666666666666, 1.366666666666666, 1.366666666666666, 2.355, 2.355]
        self.stress = [0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 2.2, 1.2000000000000002, 1.4000000000000001, 1.6, 1.8, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.2, 1.2, 2.292, 2.292]
        self.stress = [0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.0, 0.0, 0.2, 0.4, 0.6000000000000001, 0.8, 1.3333333333333333, 0.33333333333333326, 0.5333333333333332, 0.7333333333333332, 0.9333333333333331, 1.133333333333333, 1.833333333333333, 0.833333333333333, 1.033333333333333, 1.233333333333333, 1.433333333333333, 1.6333333333333329, 2.4333333333333327, 1.4333333333333327, 1.6333333333333326, 2.499999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 2.099999999999999, 1.0999999999999992, 1.0999999999999992, 2.248, 2.248, 2.248, 2.248, 2.248, 2.248, 1.2480000000000002, 1.2480000000000002, 2.076, 2.076]

        import matplotlib.pyplot as plt

        
        import numpy as np
        from PIL import Image

        # plt.plot([20.5], [20.5], marker="s", color='black', markersize = 520, alpha = 0.8)
        self.ax[0].plot([20.5], [20.5], marker="s", color='black', markersize = 520, alpha = 0.8)

        # 描画範囲の設定と目盛りを消す設定
        self.ax[0].set_xlim(-7.5, 41.5)
        self.ax[0].set_ylim(-10.5, 51.5)
        self.ax[0].tick_params(axis='both', which='both', bottom='off', top='off',
                        labelbottom='off', right='off', left='off', labelleft='off')
        # self.ax[0].legend()
        test = [[22, 8], [23, 8], [24, 8], [25, 8], [26, 8], [27, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [11, 8], [10, 8], [9, 8], [8, 8], [7, 8], [6, 8], [5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8]]

        # 格子状
        # test = [[22, 8], [23, 8], [23, 9], [23, 7], [23, 6], [24, 6], [22, 6], [21, 6], [23, 5], [23, 4], [24, 4], [25, 4], [26, 4], [22, 4], [21, 4], [20, 4], [19, 4], [18, 4], [18, 5], [18, 6], [17, 4], [18, 3], [18, 2], [17, 2], [16, 2], [15, 2], [14, 2], [13, 2], [12, 2], [13, 3], [13, 1], [13, 0], [12, 0], [11, 0], [10, 0], [14, 0], [15, 0], [16, 0], [9, 0], [8, 0], [7, 0], [11, 2], [10, 2], [9, 2], [8, 2], [7, 2], [6, 2], [5, 2], [6, 1], [6, 3], [6, 4], [6, 5], [5, 4], [4, 4], [3, 4], [2, 4], [6, 6], [7, 6], [8, 6], [6, 7], [6, 8], [7, 8], [6, 9], [6, 10], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [13, 9], [13, 10], [12, 10], [11, 10], [10, 10], [9, 10], [8, 10], [7, 10], [5, 8], [13, 7], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8], [0, 7], [0, 9], [0, 10], [1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [13, 6], [14, 6], [15, 6], [16, 6], [17, 6], [18, 7], [18, 8], [19, 8], [17, 8], [16, 8], [15, 8], [18, 9], [18, 10], [19, 10], [17, 10], [16, 10], [15, 10], [14, 10], [18, 11], [20, 10], [21, 10], [22, 10], [23, 10], [23, 11], [23, 12], [22, 12], [23, 13], [24, 12], [25, 12], [26, 12], [24, 10], [21, 12], [23, 14], [20, 12], [19, 12], [18, 12], [18, 13], [18, 14], [18, 15], [18, 16], [19, 16], [20, 16], [21, 16], [17, 16], [22, 16], [23, 16], [24, 16], [25, 16], [23, 15], [25, 10], [24, 8], [25, 8], [21, 8], [26, 10], [22, 14], [21, 14], [24, 14], [25, 14], [26, 14], [27, 14], [28, 14], [28, 15], [20, 14], [17, 12], [19, 14], [17, 14], [16, 14], [15, 14], [14, 14], [13, 14], [13, 15], [13, 13], [13, 12], [14, 12], [13, 11], [12, 12], [11, 12], [20, 8], [19, 6], [28, 13], [25, 6], [26, 6], [27, 6], [28, 6], [28, 7], [28, 5], [28, 4], [27, 4], [23, 3], [23, 2], [22, 2], [21, 2], [20, 2], [23, 1], [24, 2], [23, 0], [22, 0], [21, 0], [20, 0], [24, 0], [25, 0], [25, 2], [26, 2], [27, 2], [28, 2], [28, 1], [28, 3], [28, 8], [26, 8], [27, 8], [27, 10], [28, 10], [28, 11], [28, 12], [27, 12], [28, 16], [27, 16], [26, 16], [28, 9], [12, 6], [13, 5], [13, 4], [14, 4], [15, 4], [12, 4], [5, 6], [9, 6], [10, 6], [11, 6], [12, 14], [13, 16], [14, 16], [15, 16], [15, 12], [12, 16], [11, 16], [10, 16], [9, 16], [8, 16], [10, 12], [9, 12], [8, 12], [7, 12], [16, 4], [11, 4], [10, 4], [9, 4], [8, 4], [7, 4], [19, 2], [18, 1], [18, 0], [17, 0], [19, 0], [6, 0], [5, 0], [4, 0], [3, 0], [28, 0], [20, 6], [1, 4], [0, 4], [0, 3], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [0, 1], [0, 5], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [16, 12], [6, 12], [6, 13], [6, 14], [7, 14], [5, 14], [6, 15], [8, 14], [9, 14], [10, 14], [11, 14], [6, 11], [0, 11], [0, 12], [1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [0, 13], [0, 0], [1, 0], [2, 0], [27, 0], [26, 0], [16, 16], [0, 14], [0, 15], [1, 14], [2, 14], [3, 14], [4, 14], [0, 16], [6, 16], [7, 16], [5, 16], [4, 16], [3, 16], [2, 16], [1, 16]]
        for t in range(len(test)):


            state = test[t]
            y = 46-(state[0] + state[0] + 0.5) # 14.5)
            x = state[1] + state[1] + 0.5

            self.ax[0].plot([x], [y], marker="s", color='grey', markersize = 18)

        LandMark = [[27, 8], [22, 8], [18, 8], [13, 8], [9, 8], [5, 8],  [0, 8]]
        "1106"
        LandMark = [[23, 8], [18, 8], [12, 8], [5, 8]] # , [5, 8],  [0, 8]]
        "マス固定"
        LandMark = [[22, 8], [17, 8], [12, 8], [7, 8], [2, 8]]


        # self.ax[0].plot([20.5], [20.5], marker="s", color='black', markersize = 520, alpha = 0.8)
        for t in range(len(LandMark)):
            state = LandMark[t]
            y = 46-(state[0] + state[0] + 0.5) # 14.5)
            x = state[1] + state[1] + 0.5

            if state == [0, 8]:
                # self.ax[0].plot([x], [y], marker="s", color='orange', markersize = 18, alpha = 0.5)
                # self.ax[0].plot([x], [y], marker="s", color='red', markersize = 18, alpha = 0.5)
                pass

            if state == [12, 8] or state == [7, 8] or state == [2, 8]:
                self.ax[0].plot([x], [y], marker="s", color='blue', markersize = 18, alpha = 0.5)
            
            # 1024
            # add 1007
            # elif state == [5, 8]: # or state == [9, 8]: # or state == [5, 8]:
            #     # self.ax[0].plot([x], [y], marker="s", color='orange', markersize = 18, alpha = 0.5)
            #     self.ax[0].plot([x], [y], marker="s", color='blue', markersize = 18, alpha = 0.5)
            #     # self.ax[0].plot([x], [y], marker="s", color='blue', markersize = 28, alpha = 0.5)
            #     # pass
            else:
                self.ax[0].plot([x], [y], marker="s", color='green', markersize = 18, alpha = 0.5)

                
    def move_history(self):

        OVER_CAPACITY = 1.0

        for t in range(len(self.stress)): # state_history)): # フレームごとの描画内容

            self.T.append(t)
            self.im = []

            self.Stress_List.append(self.stress[t])
            self.im += (self.ax[1].plot(self.T, self.Stress_List, color="orange", alpha=0.7))

            state = self.state_history[t]  # 現在の場所を描く

            try:
                prev_state = self.state_history[t-1]
            except:
                pass
            

            if state[1] != 0:
                y = 46-(state[0] + state[0] + 0.5) # 14.5)
                x = state[1] + state[1] + 0.5
            else:
                x = 0.5
                y = 46-(state[0] + state[0] + 0.5) # 14.5)
                
            try:
                if state == prev_state:
                    
                    if state[0] == prev_state[0]:
                        # self.im += self.ax[0].plot(x, y, marker="s", color='y', markersize = 18, alpha = 0.5)
                        self.im += self.ax[0].plot(x, y, marker="o", color='y', markersize = 8)
                    else:
                        # self.im += self.ax[0].plot(x, y, marker="o", color='r', markersize = 15, alpha = 0.5)
                        self.im += self.ax[0].plot(x, y, marker="o", color='r', markersize = 8)

                   
                else:
                    # self.im += self.ax[0].plot(x, y, marker="o", color='r', markersize = 15, alpha = 0.5)
                    self.im += self.ax[0].plot(x, y, marker="o", color='r', markersize = 8)
            except:
                print("エラー(初回)")
                # self.im += self.ax[0].plot(x, y, marker="s", color='r', markersize = 15, alpha = 0.5)
                self.im += self.ax[0].plot(x, y, marker="o", color='r', markersize = 8)
            self.ims.append(self.im)
            
            if t == 0:
                self.ims.append(self.im)

            #描画設定
            if self.legend_flag:  # 一回のみ凡例を描画
                self.ax[0].set_title("Sim Environment")
                # self.ax[1].axhline(OVER_CAPACITY, ls = "--", color = "black", label = "×1 standard line")
                # self.ax[1].axhline(2, ls = "--", color = "red", label = "×2 (Threshold)")
                # self.ax[1].axhline(OVER_CAPACITY, ls = "--", color = "black", label = "×1 standard")
                self.ax[1].axhline(0, ls = "--", color = "black", label = "stress free")
                self.ax[0].scatter(0, -20, marker="o", color='r', label = "Agent")
                self.ax[0].scatter(0, -20, marker="s", color='green', label="Node")
                self.ax[0].scatter(0, -20, marker="s", color='grey', label="Path")
                # self.ax[1].plot(self.T, self.Stress_List, color="orange", alpha=0.7, label = "Stress Value by Agent")
                self.ax[1].plot(self.T, self.Stress_List, color="orange", alpha=0.7, label = "Stress")
                self.legend_flag = False

            
    def view_anim(self): #　初期化関数とフレームごとの描画関数を用いて動画を作成する
        self.anim = animation.ArtistAnimation(self.fig, self.ims, interval=350, repeat = True) # False)
        # self.anim = animation.ArtistAnimation(self.fig, self.ims, interval=15, repeat = True)
        # self.anim = animation.ArtistAnimation(self.fig, self.ims, interval=250, repeat = True)
        # self.ani = animation.ArtistAnimation(self.fig, self.ims, interval=250)
        # plt.legend(loc='lower right')
        # plt.legend(loc='center')
        self.ax[0].legend(loc='upper right')
        self.ax[1].legend(loc='lower right')
        # self.ax[2].legend(loc='upper right')
        # self.ax[3].legend(loc='upper right')
        # self.ax[4].legend(loc='lower right')
        
        "1120 meeting Reluを見やすくするために追加"
        # self.ax[1].set_ylim(-0.1, 1.5)
        self.ax[1].set_xlim(-1, 50)
        plt.show()
        return True


if __name__ == "__main__":

    # 0.3
    STATE_HISTORY = [[27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [12, 8], [11, 8], [10, 8], [9, 8], [8, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [17, 8], [17, 8]]
    # # 0.1
    # STATE_HISTORY = [[27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [12, 8], [11, 8], [10, 8], [9, 8], [8, 8], [7, 8], [7, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [17, 8], [17, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8]]
    # STATE_HISTORY = [[27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [12, 8], [11, 8], [10, 8], [9, 8], [8, 8], [7, 8], [7, 8], [6, 8], [5, 8], [4, 8], [3, 8], [2, 8], [2, 8], [1, 8], [0, 8], [0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [17, 8], [17, 8]]
    # STATE_HISTORY = [[27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [12, 8], [11, 8], [10, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [17, 8], [17, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8]]
    
    # # N=2
    # STATE_HISTORY = [[27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [12, 8], [11, 8], [10, 8], [9, 8], [8, 8], [7, 8], [7, 8], [6, 8], [5, 8], [4, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [17, 8], [17, 8]]
    # # N=5
    # STATE_HISTORY = [[27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [12, 8], [11, 8], [10, 8], [9, 8], [8, 8], [7, 8], [7, 8], [6, 8], [5, 8], [4, 8], [3, 8], [2, 8], [2, 8], [1, 8], [0, 8], [0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [17, 8], [17, 8]]

    # "1"
    # STATE_HISTORY = [[27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [12, 8], [11, 8], [10, 8], [9, 8], [8, 8], [7, 8], [7, 8], [6, 8], [5, 8], [4, 8], [3, 8], [2, 8], [2, 8], [1, 8], [0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [17, 8], [17, 8]]
    STATE_HISTORY = [[27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [12, 8], [11, 8], [10, 8], [9, 8], [8, 8], [7, 8], [7, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [17, 8], [17, 8]]

    STATE_HISTORY = [[27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [12, 8], [11, 8], [10, 8], [9, 8], [8, 8], [7, 8], [7, 8], [6, 8], [5, 8], [4, 8], [3, 8], [2, 8], [2, 8], [1, 8], [0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [17, 8], [17, 8]]
    STATE_HISTORY = [[27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [12, 8], [11, 8], [10, 8], [9, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8]]
    STATE_HISTORY = [[27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [16, 8], [15, 8], [14, 8], [14, 8], [15, 8], [16, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8]]
    STATE_HISTORY = [[27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [12, 8], [11, 8], [10, 8], [9, 8], [8, 8], [7, 8], [7, 8], [6, 8], [5, 8], [4, 8], [3, 8], [2, 8], [2, 8], [1, 8], [0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [17, 8], [17, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8]]


    Env_Anim = Anim(STATE_HISTORY)

    print("STATE_HISTORY:{}".format(Env_Anim.state_history))
    print("length:{}".format(len(Env_Anim.state_history)))

    Env_Anim.view_plot_text()
    Env_Anim.move_history()
    Env_Anim.view_anim()

    