

import sys
from PySide.QtGui import QApplication
from mainwindow import MainWindow


reload(sys)
sys.setdefaultencoding('utf8')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
