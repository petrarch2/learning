#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'PyQt5'

import sys
from PyQt5.QtWidgets import QApplication, QWidget    #导入相应的包
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
   def setupUi(self, Form):
       Form.setObjectName("Form")
       Form.resize(400, 300)
       self.pushButton = QtWidgets.QPushButton(Form)
       self.pushButton.setGeometry(QtCore.QRect(140, 60, 99, 27))
       self.pushButton.setObjectName("pushButton")
       self.retranslateUi(Form)
       self.pushButton.clicked.connect(self.firtPyQt5_button_click)
       QtCore.QMetaObject.connectSlotsByName(Form)

   def retranslateUi(self, Form):
       _translate = QtCore.QCoreApplication.translate
       Form.setWindowTitle(_translate("Form", "Form"))
       self.pushButton.setText(_translate("Form", "PushButton"))

   #接下修改下firstPyQt5.py文件，主要是去实现slot函数，因为之前在QtDesigner里没有实现，让它弹出一个消息框

   def firtPyQt5_button_click(self):
       QtWidgets.QMessageBox.information(self.pushButton,"标题","这是第一个PyQt5 GUI程序")

if __name__ == '__main__':
   """
   主函数
   """
   app = QApplication(sys.argv)
   #app = QApplication(sys.argv)，每一个pyqt程序必须创建一个application对象，
   #sys.argv是命令行参数，可以通过命令启动的时候传递参数。
   mainWindow = QMainWindow()
   #生成过一个实例（对象）, mainWindow是实例（对象）的名字，可以随便起。
   ui = Ui_Form()
   ui.setupUi(mainWindow)
   mainWindow.show()  #用来显示窗口
   sys.exit(app.exec_())#exec_()方法的作用是“进入程序的主循环直到exit()被调
