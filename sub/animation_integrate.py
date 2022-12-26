import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from matplotlib import patches
from matplotlib import animation, gridspec

# エージェントの移動の様子を可視化します
# 参考URL http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/

# animation_Edit.py の整理ver.

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

        # ss1 = self.gs.new_subplotspec((0, 2), rowspan=3)  # ax3 を配置する領域
        # ss2 = self.gs.new_subplotspec((0, 0), colspan=2)  # ax1 を配置する領域
        # ss3 = self.gs.new_subplotspec((1, 0), colspan=2) # , colspan=2)  # ax2 を配置する領域
        # ss4 = self.gs.new_subplotspec((2, 0), colspan=2)
        # 逆ver.
        # ss1 = self.gs.new_subplotspec((0, 0), rowspan=3)
        # ss2 = self.gs.new_subplotspec((0, 1), colspan=2)
        # ss3 = self.gs.new_subplotspec((1, 1), colspan=2)
        # ss4 = self.gs.new_subplotspec((2, 1), colspan=2)
        ss1 = self.gs.new_subplotspec((0, 0), rowspan=3,colspan=1)
        ss2 = self.gs.new_subplotspec((0, 1), rowspan=1,colspan=2)
        ss3 = self.gs.new_subplotspec((1, 1), rowspan=1,colspan=2)
        ss4 = self.gs.new_subplotspec((2, 1), rowspan=1,colspan=2)


        self.ax = [plt.subplot(ss1), plt.subplot(ss2), plt.subplot(ss3), plt.subplot(ss4)]
        "-----------------------------------------------------"

        # グラフデータの初期化
        self.T = []
        # Statas数推移
        self.Stress_List= []
        self.im = []





        # Dを発見できないver.
        # self.history_S = [0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.history_G = [0, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.history_A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.history_B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.history_C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.history_D = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.history_S = [0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.history_G = [0, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.history_A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.history_B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.history_C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.history_D = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.history_S = [0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.history_G = [0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.history_A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.history_B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.history_C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.history_D = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        "-----------------------------"


        self.S_x = [0]
        self.G_x = [1] # "O"
        self.A_x = [2]
        self.B_x = [3]
        self.C_x = [4]
        self.D_x = [5]
        # G_x = [5]
        self.S = []
        self.A = []
        self.B = []
        self.C = []
        self.D = []
        self.G = []

        self.legend_flag = True

    def view_plot_text(self):

        self.stress = [0, 0, 1, 2, 3, 4, 0, 0, 1, 2, 3, 0, 0, 1, 2, 3, 4, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10]
        # self.stress = [0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0.5, 0.75, 0, 0, 0.25, 0.5, 0.75, 1.0, 0, 0, 1.0, 2.0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10]
        # self.stress = [0, 0, 0.25, 0.5, 0.75, 1.0, 0, 0, 0.25, 0.5, 0.75, 0, 0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 0, 0, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10]
        # self.stress = [0, 0, 0.25, 0.5, 0.75, 1.0, 0, 0, 0.25, 0.5, 0.75, 0, 0, 1.0, 2.0, 3.0, 4.0, 0, 0, 0.11, 0.22, 0.33, 0, 0, 0.33, 0.66, 0.99, 1.32, 1.6500000000000001, 1.9800000000000002, 2.31, 2.64, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10]
        # self.stress = [0, 0, 0.25, 0.5, 0.75, 1.0, 0, 0, 0.25, 0.5, 0.75, 0, 0, 1.0, 2.0, 3.0, 4.0, 0, 0, 0.11, 0.22, 0.33, 0, 0, 0.33, 0.66, 0.99, 1.32, 1.6500000000000001, 1.9800000000000002, 2.31, 2.64, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 2.97, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2]
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
        # self.ax[0].plot([20.5], [20.5], marker="s", color='black', markersize = 520, alpha = 0.8)
        for t in range(len(LandMark)):
            state = LandMark[t]
            y = 46-(state[0] + state[0] + 0.5) # 14.5)
            x = state[1] + state[1] + 0.5

            if state == [0, 8]:
                # self.ax[0].plot([x], [y], marker="s", color='orange', markersize = 18, alpha = 0.5)
                # self.ax[0].plot([x], [y], marker="s", color='red', markersize = 18, alpha = 0.5)
                pass
            
            # 1024
            # add 1007
            elif state == [5, 8]: # or state == [9, 8]: # or state == [5, 8]:
                # self.ax[0].plot([x], [y], marker="s", color='orange', markersize = 18, alpha = 0.5)
                self.ax[0].plot([x], [y], marker="s", color='blue', markersize = 18, alpha = 0.5)
                # self.ax[0].plot([x], [y], marker="s", color='blue', markersize = 28, alpha = 0.5)
                # pass
            else:
                self.ax[0].plot([x], [y], marker="s", color='green', markersize = 18, alpha = 0.5)

        
    
    def move_history(self):
        # self.im += self.ax[0].plot([], [])
        # self.im += self.ax[1].plot([], [])

        # self.im.append([line])
        # fig, ax = self.ax[0].subplots(figsize=(4, 4))


        OVER_CAPACITY = 1

        



        for t in range(len(self.stress)): # state_history)): # フレームごとの描画内容

            self.T.append(t)
            self.im = []
            
            self.Stress_List.append(self.stress[t])
            # self.ims += self.ax[1].plot(self.T, self.Stress_List, color="orange", alpha=0.7)
            # self.ims.append(self.ims)
            # self.ims += (self.ax[1].plot(self.T, self.Stress_List, color="orange", alpha=0.7))
            self.im += (self.ax[3].plot(self.T, self.Stress_List, color="orange", alpha=0.7))


            try:
                self.S.append(self.history_S[t])
                self.A.append(self.history_A[t])
                self.B.append(self.history_B[t])
                self.C.append(self.history_C[t])
                self.D.append(self.history_D[t])
                self.G.append(self.history_G[t])
                # self.im += self.ax[2].bar(self.S_x, self.S, color='blue')
                self.im += self.ax[2].bar(self.S_x, self.S, color='purple')
                self.im += self.ax[2].bar(self.G_x, self.G, color='blue')
                self.im += self.ax[2].bar(self.A_x, self.A, color='green')
                self.im += self.ax[2].bar(self.B_x, self.B, color='yellow')
                self.im += self.ax[2].bar(self.C_x, self.C, color='orange')
                self.im += self.ax[2].bar(self.D_x, self.D, color='red')
                # self.im += self.ax[2].bar(self.G_x, self.G, color='purple')

            except:
                pass






            # title = self.ax[0].title('step = {0}'.format(t))
            # title = self.ax[0].title('data={}'.format(t))
            "---- comment out ----"
            # title = self.ax[0].text(0.5, 1.01, 'Steps={}'.format(t),
            # ha='center', va='bottom',
            # transform=self.ax[0].transAxes, fontsize='large')
            "---- comment out ----"
            
            state = self.state_history[t]  # 現在の場所を描く
            
            # try:
            #     next_state = self.state_history[t+1]
            # except:
            #     pass

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

            # self.ax[0].plot([x], [y], marker="s", color='black', markersize = 10)

            

            
            try:
                if state == prev_state:
                    

                    # if state[0] == prev_state[0] == next_state[0] or state[0] == prev_state[0] == prev2[0]: #  or state[1] == prev_state[1] == next_state[1]:
                    #     self.ims += self.ax[0].plot(x, y, marker="o", color='y', markersize = 15, alpha = 0.5)
                    # elif state == prev_state:
                    #     self.ims += self.ax[0].plot(x, y, marker="s", color='r', markersize = 15, alpha = 0.5)
                    # else:
                    #     self.ims += self.ax[0].plot(x, y, marker="s", color='b', markersize = 15, alpha = 0.5)

                    if state[0] == prev_state[0]: #  == next_state[0] == prev2[0] == prev3[0] == prev4[0] == prev5[0] == prev6[0] == prev7[0] == prev8[0]:
                        self.im += self.ax[0].plot(x, y, marker="s", color='y', markersize = 18, alpha = 0.5)
                    else:
                        self.im += self.ax[0].plot(x, y, marker="o", color='r', markersize = 15, alpha = 0.5)

                   
                else:
                    self.im += self.ax[0].plot(x, y, marker="o", color='r', markersize = 15, alpha = 0.5)
            except:
                print("エラー(初回)")
                self.im += self.ax[0].plot(x, y, marker="s", color='r', markersize = 15, alpha = 0.5)
            self.ims.append(self.im)
            if t == 0:
                self.ims.append(self.im)

            #描画設定
            if self.legend_flag:  # 一回のみ凡例を描画
                # ax[0].set_title("Simulation")
                self.ax[0].set_title("Sim Environment")
                # self.ax[0].axhline(OVER_CAPACITY, ls = "--", color = "black")
                
                self.ax[3].set_title("Change in stress values(Line ver.)")
                self.ax[3].axhline(OVER_CAPACITY, ls = "--", color = "black")

                self.ax[2].set_title("Change in stress values(Stackplot ver.)")
                self.ax[2].axhline(OVER_CAPACITY, ls = "--", color = "black")
        
                self.legend_flag = False

            # self.ax[0].legend()

            # # ステップ数表示
            # step_text = self.ax[0].text(0.05, 0.9, '', transform=self.ax[0].transAxes)

            # # 時間
            # step_text.set_text('step = {0}'.format(t))
            # line = self.ax[0].title('step = {0}'.format(t))



    def view_anim(self): #　初期化関数とフレームごとの描画関数を用いて動画を作成する
        self.anim = animation.ArtistAnimation(self.fig, self.ims, interval=450, repeat = False)
        # self.anim = animation.ArtistAnimation(self.fig, self.ims, interval=15, repeat = True)
        # self.anim = animation.ArtistAnimation(self.fig, self.ims, interval=250, repeat = True)
        # self.ani = animation.ArtistAnimation(self.fig, self.ims, interval=250)
        plt.show()
        return True


if __name__ == "__main__":


    # 可視化1029
    STATE_HISTORY = [[27, 8], [27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [18, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [13, 8], [12, 8], [11, 8], [10, 8], [9, 8], [9, 8], [8, 8], [7, 8], [6, 8], [5, 8], [5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [13, 8], [13, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8], [23, 8], [24, 8], [25, 8], [26, 8], [27, 8], [27, 8], [27, 8], [27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [18, 8], [18, 8], [18, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [11, 8], [10, 8], [9, 8], [9, 8], [9, 8], [9, 8], [8, 8], [7, 8], [6, 8], [5, 8], [5, 8], [5, 8], [5, 8]]
    STATE_HISTORY = [[27, 8], [27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [18, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [13, 8], [12, 8], [11, 8], [10, 8], [9, 8], [9, 8], [8, 8], [7, 8], [6, 8], [5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [13, 8], [13, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [22, 8], [22, 8], [22, 8], [23, 8], [24, 8], [25, 8], [26, 8], [27, 8], [27, 8], [27, 8], [27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [18, 8], [18, 8], [18, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [11, 8], [10, 8], [9, 8], [9, 8], [9, 8], [9, 8]]



    
    Env_Anim = Anim(STATE_HISTORY)

    print("STATE_HISTORY:{}".format(Env_Anim.state_history))
    print("length:{}".format(len(Env_Anim.state_history)))

    Env_Anim.view_plot_text()
    Env_Anim.move_history()
    Env_Anim.view_anim()

    