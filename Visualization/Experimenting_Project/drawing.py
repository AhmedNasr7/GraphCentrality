import networkx as nx
import matplotlib.pyplot as plt


def fill_graph_object(graph_list):
    my_graph = nx.Graph()
    for i in range(len(graph_list)):
        for j in range(len(graph_list[i])):
            my_graph.add_edge(i, graph_list[i][j][0], weight=graph_list[i][j][1])
    return my_graph


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    node_sizes = [3 + 1000 * i for i in range(len(graph))]
    labels = {}
    for node in graph.nodes():
        labels[node] = node
    label = str(i for i in range(len(graph)))
    nx.draw_networkx_nodes(graph, pos=pos, node_size=node_sizes, node_color='#83C6FB')
    nx.draw_networkx_edges(graph, pos=pos, node_size=node_sizes, node_color='#83C6FB')
    nx.draw_networkx_labels(graph, pos=pos, labels=labels, font_size=16, font_color='#142C69')
    # nx.draw(graph, with_labels=True)
    plt.savefig("graph_fig.png")
    plt.show()




