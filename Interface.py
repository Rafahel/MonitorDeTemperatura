# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medidor.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

'''

    Neste arquivo esta o cógigo gerado pelo Qt Designer, NÃO MUDAR NADA.

'''

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(301, 309)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("term.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lcdDisplay = QtGui.QLCDNumber(self.centralwidget)
        self.lcdDisplay.setGeometry(QtCore.QRect(60, 40, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lcdDisplay.setFont(font)
        self.lcdDisplay.setSmallDecimalPoint(False)
        self.lcdDisplay.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdDisplay.setProperty("value", 0.0)
        self.lcdDisplay.setObjectName(_fromUtf8("lcdDisplay"))
        self.iniciar = QtGui.QPushButton(self.centralwidget)
        self.iniciar.setGeometry(QtCore.QRect(80, 180, 75, 23))
        self.iniciar.setObjectName(_fromUtf8("iniciar"))
        self.finalizar = QtGui.QPushButton(self.centralwidget)
        self.finalizar.setGeometry(QtCore.QRect(170, 180, 75, 23))
        self.finalizar.setObjectName(_fromUtf8("finalizar"))
        self.h = QtGui.QLabel(self.centralwidget)
        self.h.setGeometry(QtCore.QRect(110, 230, 46, 13))
        self.h.setObjectName(_fromUtf8("h"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 230, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.min = QtGui.QLabel(self.centralwidget)
        self.min.setGeometry(QtCore.QRect(140, 230, 46, 13))
        self.min.setObjectName(_fromUtf8("min"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 230, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.sec = QtGui.QLabel(self.centralwidget)
        self.sec.setGeometry(QtCore.QRect(170, 230, 46, 13))
        self.sec.setObjectName(_fromUtf8("sec"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 210, 91, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 301, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Temperatura", None))
        self.iniciar.setText(_translate("MainWindow", "Iniciar", None))
        self.finalizar.setText(_translate("MainWindow", "Finalizar", None))
        self.h.setText(_translate("MainWindow", "0", None))
        self.label_2.setText(_translate("MainWindow", ":", None))
        self.min.setText(_translate("MainWindow", "0", None))
        self.label_4.setText(_translate("MainWindow", ":", None))
        self.sec.setText(_translate("MainWindow", "0", None))
        self.label_6.setText(_translate("MainWindow", "Tempo Decorrido", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

