import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx



#import random


class PlotCanvas(FigureCanvas):

    def __init__(self, edges, nodes_num,  parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.ax = fig.add_subplot(121)
        FigureCanvas.__init__(self, fig)

        self.setParent(parent)
        self.edges = edges
        self.nodes_num = nodes_num

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        g = nx.Graph()
        
        nodes = [x for x in range (self.nodes_num)]
        g.add_nodes_from(nodes)
        print(nodes)
        print(type(nodes))
        g.add_weighted_edges_from(self.edges)
        #self.ax = fig.add_subplot(121)
        #fig.add_subplot(121)
        deg = nx.degree_centrality(g)
        print(deg)
        centrality = []
        for k in deg.keys():
            centrality.append(deg[k])

        #centrality=[float(i) for i in nodes]
        #list_of_size=[10000*i for i in centrality]
        print(centrality)
        list_of_size= []
        for i in centrality:
            list_of_size.append(int(1500 * i))

        

        #nx.draw(g, with_labels=True)
        nx.draw_networkx(g, nodelist = nodes, node_size = list_of_size)



        plt.show()





"""

import networkx as nx 
import matplotlib.pyplot as plt


g = nx.Graph()
nodes = (x for x in range (5))
g.add_nodes_from(nodes)

g.add_node(4)
g.add_node(3)
g.add_node(3)
print(g.nodes())
edges = [(0, 1, 1), (0, 2, 1), (1, 3, 1), (2, 3, 1), (2, 4, 3), (3, 4, 1)]
g.add_weighted_edges_from(edges)
plt.subplot(121)
nx.draw(g, with_labels=True)

#nx.draw(g)
#plt.show()




"""

       





   