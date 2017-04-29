from PySide.QtCore import *
from PySide.QtGui import *


class SubscribingWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(0, 0, 270, 100)
        vb_layout = QVBoxLayout()
        comboBoxProduct = QComboBox()
        vb_layout.addWidget(comboBoxProduct)
        self.setLayout(vb_layout)



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(30, 30, 300, 400)
        self.setWindowTitle('Shaving accessories')

        tab1 = SubscribingWidget()
        tab_widget = QTabWidget(self)
        tab_widget.setGeometry(10, 10, 280, 380)
        tab_widget.addTab(tab1, "Subscribing")
        # tab_widget.addTab(tab2, "Shipping")

        vb_layout = QVBoxLayout()
        vb_layout.addWidget(tab_widget)
        self.setLayout(vb_layout)
