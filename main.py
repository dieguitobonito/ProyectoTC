import sys
import random
from img import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

class Gui_Juego(QMainWindow):
    def __init__(self):
        super(Gui_Juego, self).__init__()
        loadUi("juego.ui", self)
        self.piedra.clicked.connect(self.img_piedra)
        self.papel.clicked.connect(self.img_papel)
        self.tijera.clicked.connect(self.img_tijera)

    def exit(self):
        app.exit()
        sys.exit()

    def moveWindow(self, e):
        if e.buttons() == Qt.LeftButton:
            self.clickPosition = e.globalPos()
            e.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def minimizar(self):
        widget.showMinimized()

    def img_piedra(self):
        self.label_yo.setStyleSheet("border-image: url(:/imagenes/piedra.png);")
        self.computadora()
        if self.decision_computadora == 0:
            self.label_msg.setStyleSheet('color: yellow;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Empate! q0->q3->q0")
        elif self.decision_computadora == 1:
            self.label_msg.setStyleSheet('color: red;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Perdiste! q0->q3->q0")
        else:
            self.label_msg.setStyleSheet('color: purple;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Ganaste! q0->q3->q6")

    def img_papel(self):
        self.label_yo.setStyleSheet("border-image: url(:/imagenes/papel.png);")
        self.computadora()
        if self.decision_computadora == 0:
            self.label_msg.setStyleSheet('color: purple;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Ganaste! q0->q2->q5")
        elif self.decision_computadora == 1:
            self.label_msg.setStyleSheet('color: green;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Empate! q0->q2->q0")
        else:
            self.label_msg.setStyleSheet('color: red;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Perdiste! q0->q2->q0")

    def img_tijera(self):
        self.label_yo.setStyleSheet("border-image: url(:/imagenes/tijera.png);")
        self.computadora()
        if self.decision_computadora == 0:
            self.label_msg.setStyleSheet('color: red;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Perdiste! q0->q1->q0")
        elif self.decision_computadora == 1:
            self.label_msg.setStyleSheet('color: purple;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Ganaste! q0->q1->q4")
        else:
            self.label_msg.setStyleSheet('color: green;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Empate! q0->q1->q0")


    def computadora(self):

        self.decision_computadora = random.randint(0, 2)
        if self.decision_computadora == 0:
            self.label_computadora.setStyleSheet("border-image: url(:/imagenes/piedra.png);")
        elif self.decision_computadora == 1:
            self.label_computadora.setStyleSheet("border-image: url(:/imagenes/papel.png);")
        else:
            self.label_computadora.setStyleSheet("border-image: url(:/imagenes/tijera.png);")


# main
app = QApplication(sys.argv)
juego = Gui_Juego()
widget = QtWidgets.QStackedWidget()
widget.addWidget(juego)
widget.setFixedHeight(510)
widget.setFixedWidth(510)
widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Saliendo")
