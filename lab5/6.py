import matplotlib.pyplot as plt
import networkx as nx

#считывание графа
G = nx.Graph()
f = open('/Users/Zuka/PycharmProjects/labs_2017/lab5/с', 'r')
v = []
for line in f:
    v1, v2, w = list(line.split())
    if v1 not in v:
        v.append(v1)
    if v2 not in v:
        v.append(v2)
    G.add_edge(v1, v2, weight=int(w))
f.close()
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='r', node_size=100, alpha=0.8)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G,pos,font_size=12,font_family='Comic Sans MS')

nx.is_eulerian(G)
if nx.is_eulerian(G):
    print('Граф эйлеров')
    d = nx.eulerian_circuit(G)
    nx.draw_networkx_nodes(G, pos, nodelist=d, node_color='g', node_size=100, alpha=0.8)
    for i in range(0, len(d) - 1):
        nx.draw_networkx_edges(G, pos, edgelist=[(way[i], way[i + 1])], width=1, alpha=1, edge_color='g')
else:
    print('Граф не эйлеров')

plt.axis('off')
plt.savefig("simple_path.png") # сохранить как png файл
plt.show() # вывести на экран
