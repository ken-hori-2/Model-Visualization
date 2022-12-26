import matplotlib.pyplot as plt

# jupyter notebookの場合
# %matplotlib

country = ['JPN', 'USA'] # 国名
# country = ['s', 'A', 'B', 'C', 'D', 'g'] # 国名
population = [131, 301] # 国別の人口（約）
# population = [131, 301, 100, 200, 300, 400, 250] # 国別の人口（約）
jpn = list(range(population[0])) + [130] * 170 # データの数を米国に合わせた日本のデータ
usa = range(population[1]) # 米国のデータ
print(len(jpn), len(usa)) # 日本と米国のデータを揃える
# 301 301

fontsize=15 # 図に挿入されるテキストの大きさ

plt.figure(figsize=(10, 5))

for j, u in zip(jpn, usa):
    plt.cla() # 描画されたグラフをクリアにする
    plt.bar(country, [j, u], width=0.3, color=['b', 'r'])
    plt.title("Population comparison between Japan and the United States", fontsize=fontsize)
    plt.text(country[0], j+5, "{} Million".format(j), fontsize=fontsize)
    plt.text(country[1], u+5, "{} Million".format(u), fontsize=fontsize)
    plt.xlabel("Country", fontsize=fontsize)
    plt.ylabel("Population", fontsize=fontsize)
    plt.xlim(-1, 2)
    plt.ylim(0, 330)
    plt.grid()
    plt.pause(0.1) # 一時グラフを停止する（引数には間隔を指定）
    # plt.show()

# 終わったらグラフを閉じる場合
#plt.close()
# plt.show()