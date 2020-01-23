
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import networkx as nx

import requests

response = requests.get('http://partymax.pl/io/output.php')
resData = response.json()

G = nx.DiGraph()

G.add_edge(str(resData[0]['imported_file']), str(resData[0]['source_file']), weight=0)
G.add_edge(str(resData[1]['imported_file']), str(resData[1]['source_file']), weight=1)
G.add_edge(str(resData[2]['imported_file']), str(resData[2]['source_file']), weight=2)
G.add_edge(str(resData[3]['imported_file']), str(resData[3]['source_file']), weight=3)



zero = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 0]
one = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 1]
two = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 2]
three = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 3]

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=300, alpha=0.5)

nx.draw_networkx_edges(G, pos, edgelist=zero,
                       width=6, edge_color='y', arrowsize=30, arrowstyle='simple')
nx.draw_networkx_edges(G, pos, edgelist=one,
                       width=6, edge_color='b', arrowsize=30, arrowstyle='simple')
nx.draw_networkx_edges(G, pos, edgelist=two,
                       width=6, edge_color='b', arrowsize=30, arrowstyle='simple')
nx.draw_networkx_edges(G, pos, edgelist=three,
                       width=6, edge_color='g', arrowsize=30, arrowstyle='simple')

nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

plt.axis('off')
plt.show()
