#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication

from views.main_window import MainWindowLib

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    win = MainWindowLib()
    win.show()
    sys.exit(app.exec_())