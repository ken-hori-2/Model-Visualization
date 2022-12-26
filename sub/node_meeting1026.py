import numpy as np
import matplotlib.pyplot as plt



# 利用するライブラリ
import numpy as np
from regex import D
from scipy.stats import beta # ベータ分布
#import matplotlib.pyplot as plt
import matplotlib.animation as animation




S_x = [0]
A_x = [1]
B_x = [2]
C_x = [3]
D_x = [4]
G_x = [5]
S = [0]
A = [0]
B = [0]
C = [0]
D = [0]
G = [0]
# history_S = [0,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6]
# history_A = [0,0  ,0  ,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4]
# history_B = [0,0  ,0  ,0  ,0  ,0.7,0.7,0.7,0.7,0.7,0.7,0.7]
# history_C = [0,0  ,0  ,0  ,0  ,0  ,0  ,0.5,0.5,0.5,0.5,0.5]
# history_D = [0,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,z,0.3,0.3]
# history_G = [0,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0.8]
# history_S = [0,0.6,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
history_S = [0,0.6,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0]
history_A = [0,0  ,0  ,0.4,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
history_B = [0,0  ,0  ,0  ,0  ,0.7,0.0,0.0,0.0,0.0,0.0,0.0]
history_C = [0,0  ,0  ,0  ,0  ,0  ,0  ,0.5,0.0,0.0,0.0,0.0]
history_D = [0,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0.3,0.0,0.0]
history_G = [0,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0.8]


from matplotlib import animation
from IPython.display import HTML
import matplotlib.cm as cm  # color map
fig, axes = plt.subplots(ncols=2,figsize=(6,6))
ax = axes.ravel()


def animate(i):
        '''フレームごとの描画内容'''
        # plt.cla()
        ax[1].cla()
            
        
        S[0] = history_S[i]
        A[0] = history_A[i]
        B[0] = history_B[i]
        C[0] = history_C[i]
        D[0] = history_D[i]
        G[0] = history_G[i]
                        
               
        # ax[1].bar(S_x, S, color='#00AAFF', ec="#0000FF")#blue
        # ax[1].bar(A_x, A, color='red', ec="red")#blue
        # ax[1].bar(B_x, B, color='yellow', ec="yellow")#blue
        # ax[1].bar(C_x, C, color='#00AAFF', ec="#0000FF")#blue
        # ax[1].bar(D_x, D, color='red', ec="red")#blue
        # ax[1].bar(G_x, G, color='yellow', ec="yellow")#blue
        ax[1].bar(S_x, S)
        ax[1].bar(A_x, A)
        ax[1].bar(B_x, B)
        ax[1].bar(C_x, C)
        ax[1].bar(D_x, D)
        ax[1].bar(G_x, G)

        # plt.plot([-1,2], [5, 5], color='red', linewidth=2,alpha=0.5)
        # plt.pause(1)




#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, frames=10, interval=1500, repeat=True)

#HTML(anim.to_jshtml())
plt.show()
