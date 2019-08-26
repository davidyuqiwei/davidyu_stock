# https://www.cnblogs.com/minglex/p/9205160.html
# https://blog.csdn.net/woody1982130/article/details/53471681
import networkx as nx
#import matplotlib.pyplot as plt

FG = nx.Graph()
FG.add_weighted_edges_from([('a1','a2',0.124),('a1','a3',0.73)])
FG.add_weighted_edges_from([('a1','a6',0.124),('a2','a5',0.73)])


for n,nbrs in FG.adjacency():
    for nbr,eattr in nbrs.items():
        data = eattr['weight']
        print('(%s,%s,%0.3f)' %(n,nbr,data))
#nx.draw(FG,with_labels=True)
#plt.show()

