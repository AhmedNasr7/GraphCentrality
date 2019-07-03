from PyQt5.uic import loadUiType
import sys
from os import path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QCheckBox, QGridLayout, QDesktopWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


#Ui_MainWindow,_ = loadUiType(path.join(path.dirname(__file__), "Processes.ui"))



class Graph_Input(QMainWindow):

    edges_added = pyqtSignal()

    def __init__(self, nodes_num, edges_num, parent= None):
        super(Graph_Input, self).__init__(parent)
        QMainWindow.__init__(self)
        #self.setupUi(self)
        self.columns_count = 3
        self.table_width = 600
        self.rows_count = edges_num
        self.nodes_num = nodes_num
        self.table_height = self.rows_count * 34
        self.setup_Ui()
        self.init_Button()
        self.edges = []
    
       


    def setup_Ui(self):
        '''
        UI setup goes here
        '''
        self.center_window()
        self.setWindowTitle("OS Scheduler")
        self.setFixedSize(800,600)
        #self.setGeometry(0, 0, self.table_width, self.table_height)
        self.create_table()
        self.okayBtn = QPushButton('Okay', self)
        self.okayBtn.resize(150, 40)
        self.okayBtn.move(620, 50)
        self.add_newRow = QPushButton("Add New Row", self)
        self.add_newRow.resize(150, 40)
        self.add_newRow.move(620, 100)
        self.deleteRowBtn = QPushButton('Delete Row', self)
        self.deleteRowBtn.resize(150, 40)
        self.deleteRowBtn.move(620, 150)
        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.resize(150, 40)
        self.cancelButton.move(620, 200)
        
        


    def create_table(self):
        
        columnsLabels = columnsLabels = ['Source', 'Destination', 'Weights']

        self.table = QTableWidget()
        self.layout().addWidget(self.table)
        self.table.move(0, 0)
        self.table.setFixedSize(self.table_width, self.table_height + 50)
        self.table.setRowCount(self.rows_count)
        self.table.setColumnCount(self.columns_count)
        
        for i in range(self.columns_count):
            self.table.setColumnWidth(i, self.table_width/self.columns_count - 10)
    
        self.table.setHorizontalHeaderLabels(columnsLabels)



    def init_Button(self):
        self.okayBtn.clicked.connect(self.onClick_okay)
        self.add_newRow.clicked.connect(self.add_row)
        self.cancelButton.clicked.connect(self.onClick_cancelButton)
        self.deleteRowBtn.clicked.connect(self.delete_row)


    def center_window(self):
         # centering window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())


    def onClick_okay(self):
        self.parse_tableData()
        print(self.edges)
        if len(self.edges) > 0:
            self.edges_added.emit()
            self.close()



    def parse_tableData(self):
        
        for i in range(self.rows_count):
            try: 
        
                u = int(self.table.takeItem(i, 0).text())
                v = int(self.table.takeItem(i, 1).text())
                w = int(self.table.takeItem(i, 2).text())
                if u < self.nodes_num and v < self.nodes_num: # only if exists
                    edge = (u, v, w)
                    print(edge)
                    self.edges.append(edge)
                   
            except ValueError as e:
                print("value error")



    def add_row(self):
        self.rows_count += 1
        if self.table_height < 34 * self.rows_count:
            self.table_height += 34
            
        self.table.setFixedSize(self.table_width, self.table_height)
        self.table.setRowCount(self.rows_count)
        #self.table.setItem(self.rows_count - 1, 0, QTableWidgetItem("P" + str(self.rows_count - 1)))


    def delete_row(self):
        self.rows_count -= 1
        self.table_height -= 32
        self.table.setRowCount(self.rows_count)
        self.table.setFixedSize(self.table_width, self.table_height)

    
    def get_edges(self):
        return self.edges

    def onClick_cancelButton(self):

         self.close()




  
