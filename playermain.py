# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
import pygame

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 167)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectbtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectbtn.setGeometry(QtCore.QRect(90, 10, 151, 51))
        self.selectbtn.setObjectName("selectbtn")
        self.playbtn = QtWidgets.QPushButton(self.centralwidget)
        self.playbtn.setGeometry(QtCore.QRect(130, 60, 75, 23))
        self.playbtn.setObjectName("playbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.stopbtn = QtWidgets.QPushButton(self.centralwidget)

        self.btnfunc()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectbtn.setText(_translate("MainWindow", "Select"))
        self.playbtn.setText(_translate("MainWindow", "Play"))

    def btnfunc(self):
        self.selectbtn.clicked.connect(self.selectfunc)
        self.stopbtn.clicked.connect(self.stopfunc)


    def selectfunc(self):
        res, _ = QFileDialog.getOpenFileName(self, 'Open File', f'D:\DOWNLOADSBROWSER', 'MP3 file (*.mp3)')
        pygame.init()
        pygame.mixer.music.load(res)
        pygame.mixer.music.play()
    def stopfunc(self):
        pygame.mixer.music.stop()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
