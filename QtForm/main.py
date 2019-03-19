#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'NERO'
__date__ = '2019/3/19'

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from test import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
