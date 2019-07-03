from PyQt5.uic import loadUiType
import sys
from os import path
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from figure import *
from graph_input import *

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))


class MainApp(QMainWindow, FORM_CLASS):

    def __init__(self, parent= None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setup_Ui()
        self.init_Buttons()
        self.nodes_num = 0
        #self.window_width = 1100
        #self.window_height = 1000
        self.edges = []


    def setup_Ui(self):
        '''
        UI setup goes here
        '''
        self.center_window()
        self.setWindowTitle("Graph Visualizer")
        self.setFixedSize(1000, 1000)
        
       

        self.algorithmsMenu = QComboBox(self)
        self.algorithmsMenu.move(700, 70)
        self.algorithmsMenu.resize(210, 31)
        self.algorithmsMenu.addItem("  Degree Centrality")
        self.algorithmsMenu.addItem("  Closeness Centrality")
        self.algorithmsMenu.addItem("  Betweeness Centrality")
        self.algo_label = QLabel("Pick an algorithm: ", self)
        self.algo_label.move(550, 60)
        self.algo_label.resize(200, 50)
        self.compute_button = QPushButton('Compute Centrality! ', self)
        self.compute_button.move(550, 140)
        self.compute_button.resize(170, 31)

        self.centrality_label = QLabel("Centrality: ", self)
        self.centrality_label.move(750, 127)
        self.centrality_label.resize(200, 50)
        self.centrality_label.setVisible(0)

        
        

    def center_window(self):
        # centering window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def init_Buttons(self):
        '''
        Buttons initializations and slots connections goes here
        '''
        self.enterGraph.clicked.connect(self.goto_input)


    def goto_input(self):
        self.nodes_num = int(self.nodesNum_input.toPlainText())
        self.edges_num = int(self.edgesNum_input.toPlainText())
        self.graph_input = Graph_Input(self.nodes_num, self.edges_num)
        self.graph_input.edges_added.connect(self.receive_edges)
        self.graph_input.show()
        

    def receive_edges(self):
        self.edges = self.graph_input.get_edges()
        self.graph_input.close()
        self.chart = PlotCanvas(self.edges, self.nodes_num)
        self.layout().addWidget(self.chart)
        self.chart.move(20, 120)
        self.chart.resize(900, 600)
        self.chart.setVisible(0)
        #print(self.edges)

   


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

