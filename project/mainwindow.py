from PySide.QtCore import *
from PySide.QtGui import *

from shaving import *

class SubscribingWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(0, 0, 270, 100)
        vb_layout = QVBoxLayout()
        self.setLayout(vb_layout)
        comboBoxProduct = QComboBox()
        vb_layout.addWidget(comboBoxProduct)

        self.productPrice = QLabel('', self)
        vb_layout.addWidget(self.productPrice)

        comboBoxProduct.currentIndexChanged.connect(self.changeProduct)

        self._products = getProducts()
        for product in self._products:
            comboBoxProduct.addItem(product.title)



    @Slot()
    def changeProduct(self, i):
        self.productPrice.setText("Price: " + str(self._products[i].price))

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
