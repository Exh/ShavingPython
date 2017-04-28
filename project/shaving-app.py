import sys
from PySide.QtGui import QApplication

reload(sys)
sys.setdefaultencoding('utf8')

app = QApplication(sys.argv)

sys.exit(app.exec_())
