import serial
import datetime
from threading import Thread
'''
                                                    IMPORTANTE!
    Para que esse programa funcione corretamente é necessário ter uma placa arduino conectada ao computador na porta
    COM3 e precisa estar utilizando o código descrito em Medidor_temperatura.ino junto com um sensor de temperatura
    LM35




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


        self.finalizar.setDisabled(True)
        self.finalizar.clicked.connect(self.finaliza)
        self.iniciar.clicked.connect(self.inicia)
        # get the palette
        palette = self.lcdDisplay.palette()
        # foreground color
        palette.setColor(palette.WindowText, QtGui.QColor(255, 0, 0))
        # background color
        palette.setColor(palette.Background, QtGui.QColor(0, 0, 0))
        # "light" border
        palette.setColor(palette.Light, QtGui.QColor(0, 0, 0))
        # "dark" border
        palette.setColor(palette.Dark, QtGui.QColor(0, 0, 0))
        # set the palette
        self.lcdDisplay.setPalette(palette)
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("term.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setFixedSize(301, 309)

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




    def __init__(self):
        try:
            self.port = serial.Serial("COM3", 9600)
        except:
            print("Nada detectado na porta serial...")
        self.now = datetime.datetime.now()
        self.dia = format(self.now.day) + "-" + format(self.now.month) + "-" + format(self.now.year)
        self.diaInicial = self.dia
        self.iniciar = False
        self.finalizar = False
        self.leitura = 0
        self.listaTemperatura = []
        self.listaHorarios = []
        self.contadorTempo = 0
        self.t = Thread(target=self.monitora)
        self.hor = 0
        self.m = 0
        self.s = 0
        self.teste = format(self.now.minute)
        self.testeM = format(self.now.minute)
        self.primeiraIteracao = True

    def finaliza(self):
        self.finalizar = True

    def inicia(self):
        try:
            self.t.start()
        except:
            print("Erro ao criar a thread.")

    def fechaThread(self):
        self.t.join()

    def monitora(self):
        self.finalizar.setEnabled(True)  # Habilita botão finalizar
        '''
                                           Inicia looping para leitura e amostragem de dados
        '''
        while True:
            '''
                                                Gera arquivo se o botão finalizar for selecionado
            '''
            if self.finalizar == True:
                self.geraArquivo()
                app.quit()
                break
            self.leitura = float(self.port.readline().strip())  # Faz a leitura da temperatura
            self.now = datetime.datetime.now()
            horario = (format(self.now.hour) + ":" + format(self.now.minute) + ":" + format(self.now.second))
            if self.contadorTempo == 60:
                self.listaTemperatura.append(self.leitura)
                self.listaHorarios.append(horario)
                self.contadorTempo = 0
            self.lcdDisplay.display("%.1f" % self.leitura)
            self.contadorTempo+=1
            '''
                                    Controlador de tempo do display da janela
            '''
            self.s += 1
            if self.s == 300:
                self.m += 1
                self.s = 0
                if self.m == 60:
                    self.hor +=1
                    self.m = 0
            '''
                                                Controlador dos labels de tempo decorrido da janela
            '''
            self.sec.setText(format(self.s))
            self.min.setText(format(self.m))
            self.h.setText(format(self.hor))
            '''
                                    Cria outro arquivo ao chegar a meia noite
            '''
            if self.diaInicial != self.dia:
                self.geraArquivo()
                self.diaInicial = self.dia
            self.dia = format(self.now.day) + "-" + format(self.now.month) + "-" + format(self.now.year)
            '''
                                    Salva na primeira passada do looping a temperatura e horário
            '''
            if self.primeiraIteracao:
                self.listaTemperatura.append(self.leitura)
                self.listaHorarios.append(horario)
                self.primeiraIteracao = False

    def geraArquivo(self):
        try:
            self.arquivo = open(self.diaInicial + ".txt", 'w')
            for i in range(len(self.listaTemperatura)):
                self.arquivo.write(format(self.listaTemperatura[i]) + "    " + self.listaHorarios[i] + "\n")
                self.listaTemperatura.pop(i)
                self.listaHorarios.pop(i)
            self.arquivo.close()
        except:
            print("Erro ao escrever arquivo.")



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

