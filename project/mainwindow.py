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

        self.comboBoxInterval.currentIndexChanged.connect(self.changeInterval)

        self.comboBoxDay = QComboBox()
        vb_layout.addWidget(self.comboBoxDay)
        for i in range(1, 32):
            self.comboBoxDay.addItem(str(i))

        self.comboBoxDay2 = QComboBox()
        vb_layout.addWidget(self.comboBoxDay2)
        for i in range(1, 32):
            self.comboBoxDay2.addItem(str(i))

        self.calendar = QCalendarWidget()
        vb_layout.addWidget(self.calendar)
        self.calendar.setGridVisible(True)
        self.calendar.setDateEditEnabled(False)
        self.calendar.setSelectionMode(QCalendarWidget.NoSelection)

        self.button_accept = QPushButton("Activate")
        vb_layout.addWidget(self.button_accept)
        self.button_accept.clicked.connect(self.on_button_accept_click)

        self.button_stop = QPushButton("Stop")
        vb_layout.addWidget(self.button_stop)
        self.button_stop.setEnabled(False)
        self.button_stop.clicked.connect(self.on_button_stop_click)

        self.on_button_stop_click()

    @Slot()
    def changeProduct(self, i):
        self.productPrice.setText("Price: " + str(self._products[i].price))

    @Slot()
    def changeInterval(self, i):
        if i == 2:
            self.comboBoxDay2.setEnabled(True)
        else:
            self.comboBoxDay2.setEnabled(False)

    @Slot()
    def on_button_accept_click(self):
        qdate = self.calendar.selectedDate()
        startDay = date(qdate.year(),
                        qdate.month(),
                        qdate.day())

        days = [self.comboBoxDay.currentText()]

        if self.comboBoxDay2.isEnabled():
            days.append(self.comboBoxDay2.currentText())

        self.subscribingUpdated.emit(self.comboBoxProduct.currentIndex(), self.comboBoxInterval.currentIndex(), days, startDay)
        self.button_accept.setEnabled(False)
        self.button_stop.setEnabled(True)
        self.comboBoxInterval.setEnabled(False)
        self.comboBoxProduct.setEnabled(False)
        self.comboBoxDay.setEnabled(False)
        self.comboBoxDay2.setEnabled(False)
        self.calendar.setSelectionMode(QCalendarWidget.SingleSelection)

    @Slot()
    def on_button_stop_click(self):
        self.button_accept.setEnabled(True)
        self.button_stop.setEnabled(False)
        self.comboBoxInterval.setEnabled(True)
        self.comboBoxProduct.setEnabled(True)
        self.comboBoxDay.setEnabled(True)
        self.changeInterval(self.comboBoxInterval.currentIndex())
        self.subscribingStop.emit()
        self.calendar.setSelectionMode(QCalendarWidget.NoSelection)

    subscribingUpdated = Signal(int, int, list, date)
    subscribingStop    = Signal()


class ShippingWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(0, 0, 270, 100)
        vb_layout = QVBoxLayout()
        self.setLayout(vb_layout)

        self.calendar = QCalendarWidget()
        vb_layout.addWidget(self.calendar)
        self.calendar.setGridVisible(True)



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(30, 30, 300, 400)
        self.setWindowTitle('Shaving accessories')

        tab1 = SubscribingWidget()
        tab2 = ShippingWidget()
        tab_widget = QTabWidget(self)
        tab_widget.setGeometry(10, 10, 280, 380)
        tab_widget.addTab(tab1, "Subscribing")
        tab_widget.addTab(tab2, "Shipping")

        vb_layout = QVBoxLayout()
        vb_layout.addWidget(tab_widget)
        self.setLayout(vb_layout)

        self._subscribing = None
        self._user = User()
        self._products = getProducts()
        tab1.subscribingUpdated.connect(self.on_subscribing_updated)


    @Slot()
    def on_subscribing_updated(self, p, i, days, startDay):
        # msgBox = QMessageBox(QMessageBox.Information, "on_subscribing_updated title",  str(p) + " " + str(i) + str(days) + str(startDay))
        # msgBox.exec_()

        product = self._products[p]
        interval = None
        if i == 0:
            interval = OnceTwoMonth(days[0])
        elif i == 1:
            interval = OnceAMonth(days[0])
        elif i == 2:
            interval = TwiceAMonth(days[0], days[1])

        if interval == None:
            return

        self._subscribing = Subscribing(self._user, product, interval, startDay)