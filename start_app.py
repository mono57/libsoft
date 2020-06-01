#!/usr/bin/python3

# import sys
# from PyQt5.QtWidgets import QApplication

# from views.main_window import MainWindowLib

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
    
#     win = MainWindowLib()
#     win.show()
#     sys.exit(app.exec_())

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from views.main_window import MainWindowLib
# import win32com.client

import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindowLib()
    # window.resize(250, 150)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)