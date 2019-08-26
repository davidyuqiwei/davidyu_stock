import networkx as nx
import pandas as pd
import os

data_dir = "/home/davidyu/stock/data/test/for_liutong"

file_name = "test.csv"
df1 = pd.read_csv(os.path.join(data_dir,file_name))

col_name = [x.split(".")[1] for x in df1.columns]

df1.columns = col_name
owner_list = df1.owner_name.values.tolist()  


stock_index = [str(x) for x in df1.stock_index.values.tolist()]

FG = nx.Graph()
for i in range(0,df1.shape[0]):
    FG.add_weighted_edges_from([(owner_list[i],stock_index[i].zfill(6),0.124)])
'''
for n,nbrs in FG.adjacency():
    for nbr,eattr in nbrs.items():
        data = eattr['weight']
        print('(%s,%s,%0.3f)' %(n,nbr,data))

'''

for c in nx.connected_components(FG):
    print(c)
