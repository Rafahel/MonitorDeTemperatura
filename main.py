from PyQt4 import QtCore, QtGui
import sys
import Interface
import serial
import datetime
from Interface import _fromUtf8
'''

    Listas necessárias para salvar dados.

'''

listaTemperaturas = []
listaHorarios = []

'''

    Classe principal para gerar o programa.

'''


class MainUiClass(QtGui.QMainWindow, Interface.Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)
        self.thread = ThreadLeitura()
        self.iniciado = False
        self.iniciar.clicked.connect(self.inicia)
        self.finalizar.clicked.connect(self.finaliza)
        self.finalizar.setEnabled(False)
        '''

            Conectores para recebimento de SIGNAL da Thread secundaria.

        '''
        self.connect(self.thread, QtCore.SIGNAL("temp"), self.atualizaDisplay)
        self.connect(self.thread, QtCore.SIGNAL("SEGUNDOS"), self.atualizaSegundos)
        self.connect(self.thread, QtCore.SIGNAL("MINUTOS"), self.atualizaMinutos)
        self.connect(self.thread, QtCore.SIGNAL("HORAS"), self.atualizaHoras)
        self.connect(self.thread, QtCore.SIGNAL("GERAARQUIVO"), self.geraArquivoNovo)

        '''

            Muda as cores do display LCD.

        '''
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




    '''

        Métodos para iniciar e finalizar o programa, eles atualizam os status dos botões para evitar problemas.

    '''

    def inicia(self):
        if self.iniciado == False:
            self.iniciado = True
            self.iniciar.setEnabled(False)
            self.thread.start()
            self.finalizar.setEnabled(True)



    def finaliza(self):
        self.geraArquivo()
        app.close()

    '''

        Métodos para gerar arquivos, um deles gera ao finalizar, outro gera quando o dia passa
        e o programa atualiza o dia.

    '''

    def geraArquivo(self):
        try:
            self.now = datetime.datetime.now()
            arquivo = open(format(self.now.day) + "-" + format(self.now.month)
                           + "-" + format(self.now.year) + ".txt", 'w')
            for i in range(len(listaTemperaturas)):
                arquivo.write("%.1f" % listaTemperaturas[i] + "  " + format(listaHorarios[i]) + "\n")
            listaHorarios[:] = []
            listaTemperaturas[:] = []
            arquivo.close()

        except:
            print("Erro ao escrever arquivo n1")

    def geraArquivoNovo(self, diaInicial):
        try:
            arquivo = open(diaInicial + ".txt", 'w')
            for i in range(len(listaTemperaturas)):
                arquivo.write("%.1f" % listaTemperaturas[i] + "  " + format(listaHorarios[i]) + "\n")
                listaHorarios.pop(i)
                listaTemperaturas.pop(i)
            listaHorarios[:] = []
            listaTemperaturas[:] = []
            arquivo.close()
        except:
            print("Erro ao escrever arquivo n2")

    '''

        Métodos utilizados para atualizar o contador de tempo da janela e o display LCD que mostra a temperatura.

    '''

    def atualizaSegundos(self, segundos):
        self.sec.setText(segundos)


    def atualizaMinutos(self, minutos):
        self.min.setText(minutos)


    def atualizaHoras(self, horas):
        self.h.setText(horas)

    def atualizaDisplay(self, temperatura):
        self.lcdDisplay.display("%.1f" % float(temperatura))


'''

    Thread secundaria do QT para fazer leitura e atualizar Janela.

'''


class ThreadLeitura(QtCore.QThread):
    def __init__(self, parent=None):
        super(ThreadLeitura, self).__init__(parent)
        try:
            self.port = serial.Serial("COM3", 9600)
        except:
            print("Nada detectado na porta serial...")
        self.hor = 0
        self.m = 0
        self.s = 0
        self.now = datetime.datetime.now()
        self.diaAtual = format(self.now.day) + "-" + format(self.now.month) + "-" + format(self.now.year)
        self.diaInicial = format(self.now.day) + "-" + format(self.now.month) + "-" + format(self.now.year)
        self.horaAtual = format(self.now.hour) + "-" + format(self.now.minute) + "-" + format(self.now.second)
        self.segundosParaSalvarDados = 0
        self.primeiraLeitura = True

    def run(self):
        while True:
            try:
                '''

                    Faz a leitura da porta.

                '''
                temperatura = float(self.port.readline())
                self.emit(QtCore.SIGNAL("temp"), str(temperatura))
                self.horaAtual = format(self.now.hour) + ":" + format(self.now.minute) + ":" + format(
                    self.now.second)

                '''

                    Se for a primeira passada no looping ele salva na lista os primeiros dados lidos pelo sistema.

                '''

                if self.primeiraLeitura == True:
                    listaTemperaturas.append(temperatura)
                    listaHorarios.append(self.horaAtual)
                    self.primeiraLeitura = False

                '''

                   Contador de tempo para atulizar nas labels da janela.

                '''
                self.s += 1
                if self.s == 60:
                    self.s = 0
                    self.m += 1
                    if self.m == 60:
                        self.hor += 1
                        self.m = 0
                '''

                    Sinais que são enviados para fazer a atulaização de labels da janela.

                '''
                self.emit(QtCore.SIGNAL("SEGUNDOS"), str(self.s))
                self.emit(QtCore.SIGNAL("MINUTOS"), str(self.m))
                self.emit(QtCore.SIGNAL("HORAS"), str(self.hor))
                self.diaAtual = format(self.now.day) + "-" + format(self.now.month) + "-" + format(self.now.year)

                '''

                    Contador de tempo que esta rodando para salvar dados na lista de tempo em tempo
                    definido em segundos.

                '''

                self.segundosParaSalvarDados += 1
                if self.segundosParaSalvarDados == 300:
                    listaTemperaturas.append(temperatura)
                    listaHorarios.append(self.horaAtual)
                    self.segundosParaSalvarDados = 0

                '''

                    Checa se o dia em que o programa começou é o mesmo dia atual, caso não seja ele gera um arquivo
                    com as temperaturas do dia passado e atualiza o dia atual para o novo dia.

                '''
                if self.diaInicial != self.diaAtual:
                    self.emit(QtCore.SIGNAL("GERAARQUIVO"), str(self.diaInicial))
                    self.diaInicial = format(self.now.day) + "-" + format(self.now.month) + "-" + format(
                        self.now.year)

            except:
                print("Erro na leitura da porta")


'''

        Instância os objetos e adiciona o icone na janela

'''

if __name__ == '__main__':
    a = QtGui.QApplication(sys.argv)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8("term.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    app = MainUiClass()
    app.setWindowIcon(icon)
    app.setFixedSize(301, 309)
    app.show()
    a.exec_()

