from PySide.QtCore import *
from PySide.QtGui import *

from shaving import *

class SubscribingWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(0, 0, 270, 100)
        vb_layout = QVBoxLayout()
        self.setLayout(vb_layout)
        self.comboBoxProduct = QComboBox()
        vb_layout.addWidget(self.comboBoxProduct)

        self.productPrice = QLabel('', self)
        vb_layout.addWidget(self.productPrice)

        self.comboBoxProduct.currentIndexChanged.connect(self.changeProduct)

        self._products = getProducts()
        for product in self._products:
            self.comboBoxProduct.addItem(product.title)


        self.comboBoxInterval = QComboBox()
        vb_layout.addWidget(self.comboBoxInterval)

        self.comboBoxInterval.addItem("Once two month")
        self.comboBoxInterval.addItem("Once a month")
        self.comboBoxInterval.addItem("Twice a month")

        self.comboBoxProduct.currentIndexChanged.connect(self.changeInterval)

        self.calendar = QCalendarWidget()
        vb_layout.addWidget(self.calendar)
        self.calendar.setGridVisible(True)

        self.button_accept = QPushButton("Accept")
        vb_layout.addWidget(self.button_accept)
        self.button_accept.clicked.connect(self.on_button_accept_click)

    @Slot()
    def changeProduct(self, i):
        self.productPrice.setText("Price: " + str(self._products[i].price))

    @Slot()
    def changeInterval(self, i):
        pass

    @Slot()
    def on_button_accept_click(self):
        msgBox = QMessageBox(QMessageBox.Information, "Dialog title",  "on_button_accept_click info")
        msgBox.exec_()

        qdate = self.calendar.selectedDate()
        startDay = date(qdate.year(),
                        qdate.month(),
                        qdate.day())
        self.subscribingUpdated.emit(self.comboBoxProduct.currentIndex(), self.comboBoxInterval.currentIndex(), [qdate.day()], startDay)

    subscribingUpdated = Signal(int, int, list, date)

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

        self.subscribing = None

        tab1.subscribingUpdated.connect(self.on_subscribing_updated)


    @Slot()
    def on_subscribing_updated(self, product, interval, days, startDay):
        msgBox = QMessageBox(QMessageBox.Information, "on_subscribing_updated title",  str(product) + " " + str(interval) + str(days) + str(startDay))
        msgBox.exec_()