import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setObjectName("Form")
        Form.resize(324, 498)

        self.head = QtWidgets.QWidget(Form)
        self.head.setGeometry(QtCore.QRect(0, 0, 331, 35))

        self.head.setObjectName("head")
        self.closebtn = QtWidgets.QPushButton(self.head)
        self.closebtn.setGeometry(QtCore.QRect(288, 0, 36, 33))
        self.closebtn.setMaximumSize(QtCore.QSize(36, 34))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.closebtn.setFont(font)
        self.closebtn.setStyleSheet("\n"
"QPushButton{color:black;\n"
"\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:red;\n"
"    background-color: rgba(211, 43, 46,0.8);\n"
"\n"
"\n"
"}\n"
"")
        self.closebtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Close-256.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closebtn.setIcon(icon)
        self.closebtn.setIconSize(QtCore.QSize(10, 10))
        self.closebtn.setObjectName("closebtn")
        self.minimizebtn = QtWidgets.QPushButton(self.head)
        self.minimizebtn.setGeometry(QtCore.QRect(252, 0, 36, 33))
        self.minimizebtn.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.minimizebtn.setFont(font)
        self.minimizebtn.setStyleSheet("\n"
"QPushButton{color:black;\n"
"\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(155,155,155);\n"
"}\n"
"")
        self.minimizebtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizebtn.setIcon(icon1)
        self.minimizebtn.setIconSize(QtCore.QSize(20, 20))
        self.minimizebtn.setObjectName("minimizebtn")
        self.hsblbl = QtWidgets.QLabel(self.head)
        self.hsblbl.setGeometry(QtCore.QRect(0, 0, 252, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.hsblbl.setFont(font)
        self.hsblbl.setStyleSheet("border:0px;\n"
"padding-left:3px;")
        self.hsblbl.setObjectName("hsblbl")
        self.lcd = QtWidgets.QWidget(Form)
        self.lcd.setGeometry(QtCore.QRect(0, 35, 331, 145))
        self.lcd.setObjectName("lcd")
        self.sonuc = QtWidgets.QLabel(self.lcd)
        self.sonuc.setGeometry(QtCore.QRect(0, 40, 325, 105))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.sonuc.setFont(font)
        self.sonuc.setStyleSheet("padding-right:5px;")
        self.sonuc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)


        self.sonuc.setIndent(-1)
        self.sonuc.setObjectName("sonuc")

        self.ozet = QtWidgets.QLabel(self.lcd)
        self.ozet.setGeometry(QtCore.QRect(0, 0, 324, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ozet.setFont(font)
        self.ozet.setMouseTracking(False)
        self.ozet.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ozet.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ozet.setStyleSheet("color: rgb(155,155,155);")
        self.ozet.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ozet.setObjectName("ozet")

        self.allinone = QtWidgets.QWidget(Form)
        self.allinone.setGeometry(QtCore.QRect(0, 180, 325, 321))
        self.allinone.setObjectName("allinone")
        self.gridLayoutWidget = QtWidgets.QWidget(self.allinone)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 325, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(2, 1, 3, 0)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn5.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.btn5.setFont(font)
        self.btn5.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:white;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 3, 1, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn8.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.btn8.setFont(font)
        self.btn8.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:white;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)
        self.boluxbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boluxbtn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(13)
        font.setItalic(True)
        self.boluxbtn.setFont(font)
        self.boluxbtn.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.boluxbtn.setObjectName("boluxbtn")
        self.gridLayout.addWidget(self.boluxbtn, 1, 0, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn6.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.btn6.setFont(font)
        self.btn6.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:white;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 3, 2, 1, 1)
        self.btnckar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnckar.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btnckar.setFont(font)
        self.btnckar.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btnckar.setObjectName("btnckar")
        self.gridLayout.addWidget(self.btnckar, 3, 3, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn9.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.btn9.setFont(font)
        self.btn9.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:white;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)
        self.xbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.xbtn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.xbtn.setFont(font)
        self.xbtn.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.xbtn.setObjectName("xbtn")
        self.gridLayout.addWidget(self.xbtn, 2, 3, 1, 1)
        self.btnyuzde = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnyuzde.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        font.setItalic(False)
        self.btnyuzde.setFont(font)
        self.btnyuzde.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btnyuzde.setObjectName("btnyuzde")
        self.gridLayout.addWidget(self.btnyuzde, 0, 0, 1, 1)
        self.btntopla = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btntopla.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btntopla.setFont(font)
        self.btntopla.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btntopla.setObjectName("btntopla")
        self.gridLayout.addWidget(self.btntopla, 4, 3, 1, 1)
        self.btnestle = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnestle.setMaximumSize(QtCore.QSize(80, 50))
        self.btnestle.setStyleSheet("\n"
"QPushButton{color:black;\n"
"\n"
"    background-color: rgb(6, 147, 255);\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(4, 109, 189);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btnestle.setObjectName("btnestle")
        self.gridLayout.addWidget(self.btnestle, 5, 3, 1, 1)
        self.xkarebtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.xkarebtn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(13)
        font.setItalic(True)
        self.xkarebtn.setFont(font)
        self.xkarebtn.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.xkarebtn.setObjectName("xkarebtn")
        self.gridLayout.addWidget(self.xkarebtn, 1, 1, 1, 1)
        self.cebtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cebtn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.cebtn.setFont(font)
        self.cebtn.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"box-shadow: 2px 2px 5px red;\n"
"\n"
"}\n"
"")
        self.cebtn.setObjectName("cebtn")
        self.gridLayout.addWidget(self.cebtn, 0, 1, 1, 1)
        self.clear1btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clear1btn.setMaximumSize(QtCore.QSize(80, 50))
        self.clear1btn.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.clear1btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/icons8-clear-symbol-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear1btn.setIcon(icon3)
        self.clear1btn.setIconSize(QtCore.QSize(30, 30))
        self.clear1btn.setObjectName("clear1btn")
        self.gridLayout.addWidget(self.clear1btn, 0, 3, 1, 1)
        self.karekokbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.karekokbtn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(13)
        font.setItalic(True)
        self.karekokbtn.setFont(font)
        self.karekokbtn.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.karekokbtn.setObjectName("karekokbtn")
        self.gridLayout.addWidget(self.karekokbtn, 1, 2, 1, 1)
        self.btnblme = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnblme.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnblme.setFont(font)
        self.btnblme.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btnblme.setObjectName("btnblme")
        self.gridLayout.addWidget(self.btnblme, 1, 3, 1, 1)
        self.eksiartbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.eksiartbtn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.eksiartbtn.setFont(font)
        self.eksiartbtn.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.eksiartbtn.setObjectName("eksiartbtn")
        self.gridLayout.addWidget(self.eksiartbtn, 5, 0, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn1.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:white;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 4, 0, 1, 1)
        self.btn0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn0.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.btn0.setFont(font)
        self.btn0.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:white;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btn0.setObjectName("btn0")
        self.gridLayout.addWidget(self.btn0, 5, 1, 1, 1)
        self.btnvrgul = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnvrgul.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnvrgul.setFont(font)
        self.btnvrgul.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btnvrgul.setObjectName("btnvrgul")
        self.gridLayout.addWidget(self.btnvrgul, 5, 2, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn2.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:white;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 4, 1, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn3.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:white;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 4, 2, 1, 1)
        self.cbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cbtn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        font.setItalic(False)
        font.setKerning(True)
        self.cbtn.setFont(font)
        self.cbtn.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:#f2f2f2 ;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.cbtn.setObjectName("cbtn")
        self.gridLayout.addWidget(self.cbtn, 0, 2, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn4.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.btn4.setFont(font)
        self.btn4.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:white;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 3, 0, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn7.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.btn7.setFont(font)
        self.btn7.setStyleSheet("\n"
"QPushButton{color:black;\n"
"background-color:white;\n"
"border:0 solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(190,190,190);\n"
"border:1px solid rgb(155,155,155);\n"
"\n"
"}\n"
"")
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)
        self.historywdgt = QtWidgets.QWidget(Form)
        self.historywdgt.setGeometry(QtCore.QRect(0, 496, 321, 20))
        self.historywdgt.setObjectName("historywdgt")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        #Butonların textlerinin(metinlerinin) ayarlandıgı kısım
        Form.setWindowTitle(_translate("Form", "Form"))
        self.hsblbl.setText(_translate("Form", "Hesap Makinesi"))
        self.sonuc.setText(_translate("Form", ""))
        self.ozet.setText(_translate("Form", ""))
        self.btn5.setText(_translate("Form", "5"))
        self.btn8.setText(_translate("Form", "8"))
        self.boluxbtn.setText(_translate("Form", "¹/x"))
        self.btn6.setText(_translate("Form", "6"))
        self.btnckar.setText(_translate("Form", "-"))
        self.btn9.setText(_translate("Form", "9"))
        self.xbtn.setText(_translate("Form", "X"))
        self.btnyuzde.setText(_translate("Form", "%"))
        self.btntopla.setText(_translate("Form", "+"))
        self.btnestle.setText(_translate("Form", "="))
        self.xkarebtn.setText(_translate("Form", "x²"))
        self.cebtn.setText(_translate("Form", "CE"))
        self.karekokbtn.setText(_translate("Form", "²√x"))
        self.btnblme.setText(_translate("Form", "÷"))
        self.eksiartbtn.setText(_translate("Form", "⁺/-"))
        self.btn1.setText(_translate("Form", "1"))
        self.btn0.setText(_translate("Form", "0"))
        self.btnvrgul.setText(_translate("Form", ","))
        self.btn2.setText(_translate("Form", "2"))
        self.btn3.setText(_translate("Form", "3"))
        self.cbtn.setText(_translate("Form", "C"))
        self.btn4.setText(_translate("Form", "4"))
        self.btn7.setText(_translate("Form", "7"))



class ChildMainWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        #Ui_Form pencere tasrımını içeren class objesini init fonksiyonuna çağrılıyor
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #Penceresiz ekran tasrımı ve saydam yamka için pencere özellikerli ekleniyor
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.setStyleSheet("background-color: rgba(216, 216, 216, 0.6);")

        #Kapatma butonu ve alta gönder butonu yönlendrimeleri yapılıyor
        self.ui.closebtn.clicked.connect(self.closeevent)
        self.ui.minimizebtn.clicked.connect(lambda: self.showMinimized())
        #Butun butonların tıklanma bağlantıalrını içeren fonksiyon çağrılıyor
        self.buttonclkcnnt()


        #Pencersiz ekran tasrımında pencere taşınmadıgı için pencereyi tasımak için foksiyon atanıyor
        def moveWindow(e):

            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        #Pencerenin taşınabilir olacak kısımları fonksiyona yönlendiriliyor
        self.ui.hsblbl.mouseMoveEvent = moveWindow
        self.ui.head.mouseMoveEvent=moveWindow

    def mousePressEvent(self, event):
        #Pencerenin tasınabilir olarak atandıgı widget ksımlarının sürklendiğinde konumu moveWindow objesine yollanmak için hazırlanıyor
        self.clickPosition = event.globalPos()

    def closeevent(self):
            #Uygulamayı kapatmak için yazılan kod
            self.close()


    def buttonclkcnnt(self):
        #Hesap makinesin içinde bulunan rakam ve işlem butonlarının clickeventlerin verildiği fonksiyon
        self.ui.btn0.clicked.connect(self.mainbtnconnect)
        self.ui.btn1.clicked.connect(self.mainbtnconnect)
        self.ui.btn2.clicked.connect(self.mainbtnconnect)
        self.ui.btn3.clicked.connect(self.mainbtnconnect)
        self.ui.btn4.clicked.connect(self.mainbtnconnect)
        self.ui.btn5.clicked.connect(self.mainbtnconnect)
        self.ui.btn6.clicked.connect(self.mainbtnconnect)
        self.ui.btn7.clicked.connect(self.mainbtnconnect)
        self.ui.btn8.clicked.connect(self.mainbtnconnect)
        self.ui.btn9.clicked.connect(self.mainbtnconnect)
        self.ui.cbtn.clicked.connect(self.aritmatikislemler)
        self.ui.btnblme.clicked.connect(self.aritmatikislemler)
        self.ui.btnckar.clicked.connect(self.aritmatikislemler)
        self.ui.btnestle.clicked.connect(self.esitle)
        self.ui.btntopla.clicked.connect(self.aritmatikislemler)
        self.ui.btnvrgul.clicked.connect(self.mainbtnconnect)
        self.ui.btnyuzde.clicked.connect(self.mainbtnconnect)
        self.ui.clear1btn.clicked.connect(self.mainbtnconnect)
        self.ui.boluxbtn.clicked.connect(self.aritmatikislemler)
        self.ui.xbtn.clicked.connect(self.aritmatikislemler)
        self.ui.xkarebtn.clicked.connect(self.aritmatikislemler)
        self.ui.karekokbtn.clicked.connect(self.aritmatikislemler)
        self.ui.cebtn.clicked.connect(self.mainbtnconnect)
        self.ui.eksiartbtn.clicked.connect(self.mainbtnconnect)

    def aritmatikislemler(self):
     try:
        sending = self.sender().objectName()
        if sending == "cbtn":
            self.ui.sonuc.setText("")
            self.ui.ozet.setText("")
        elif sending == "xkarebtn":
                dep = self.ui.ozet.text()
                if dep[-1] == "²":
                        dep = self.ui.ozet.text()
                        expression = eval(self.ui.sonuc.text() + "*" + self.ui.sonuc.text())
                        self.ui.sonuc.setText(str(expression))
                        self.ui.ozet.setText(dep + "²")
                        return
                elif dep[0] == "¹":
                        dep = self.ui.ozet.text()
                        expression = eval(self.ui.sonuc.text() + "*" + self.ui.sonuc.text())
                        self.ui.sonuc.setText(str(expression))
                        self.ui.ozet.setText(dep + "²")
                        return
                elif dep[0] == "√":
                        dep = self.ui.ozet.text()
                        expression = eval(self.ui.sonuc.text() + "*" + self.ui.sonuc.text())
                        self.ui.sonuc.setText(str(expression))
                        self.ui.ozet.setText(dep + "²")
                        return
                dep = self.ui.ozet.text()
                expression = eval(self.ui.ozet.text()+"*"+self.ui.ozet.text())
                self.ui.sonuc.setText(str(expression))
                self.ui.ozet.setText(dep+"²")

        elif sending == "karekokbtn":
                dep = self.ui.ozet.text()
                if dep[-1]=="²":
                        dep = self.ui.ozet.text()
                        expression = eval(self.ui.sonuc.text() + "** 0.5")
                        self.ui.sonuc.setText(str(expression))
                        self.ui.ozet.setText("√" + dep)
                        return
                elif dep[0]=="¹":
                        dep = self.ui.ozet.text()
                        expression = eval(self.ui.sonuc.text() + "** 0.5")
                        self.ui.sonuc.setText(str(expression))
                        self.ui.ozet.setText("√" + dep)
                        return
                elif dep[0]=="√":
                        dep = self.ui.ozet.text()
                        expression = eval(self.ui.sonuc.text() + "** 0.5")
                        self.ui.sonuc.setText(str(expression))
                        self.ui.ozet.setText("√" + dep)
                        return
                dep = self.ui.ozet.text()
                expression = eval(self.ui.ozet.text()+"** 0.5")
                self.ui.sonuc.setText(str(expression))
                self.ui.ozet.setText("√"+dep)

        elif sending == "boluxbtn":
                dep = self.ui.ozet.text()
                if dep[-1] == "²":
                        dep = self.ui.ozet.text()
                        expression = eval("1/" + self.ui.sonuc.text())
                        self.ui.sonuc.setText(str(expression))
                        self.ui.ozet.setText("¹/" + dep)
                        return
                elif dep[0] == "¹":
                        dep = self.ui.ozet.text()
                        expression = eval("1/" + self.ui.sonuc.text())
                        self.ui.sonuc.setText(str(expression))
                        self.ui.ozet.setText("¹/" + dep)
                        return
                elif dep[0] == "√":
                        dep = self.ui.ozet.text()
                        expression = eval("1/" + self.ui.sonuc.text())
                        self.ui.sonuc.setText(str(expression))
                        self.ui.ozet.setText("¹/" + dep)
                        return
                dep = self.ui.ozet.text()
                expression = eval("1/"+self.ui.ozet.text())
                self.ui.sonuc.setText(str(expression))
                self.ui.ozet.setText("¹/"+dep)
        elif sending == "btnblme":
            dep = self.ui.ozet.text()
            print(dep[-1])
            if dep[-1]=="/":
                return
            elif  dep[-1]=="*" :
                ldep=dep[:-1]

                self.ui.ozet.setText(ldep+"/")
            elif  dep[-1]=="+" :
                ldep=dep[:-1]

                self.ui.ozet.setText(ldep+"/")
            elif  dep[-1]=="-" :
                ldep=dep[:-1]

                self.ui.ozet.setText(ldep+"/")
            else:
                self.ui.sonuc.setText("")
                dep = self.ui.ozet.text()
                self.ui.ozet.setText(dep + "/")
                return
        elif sending=="btntopla":
                dep = self.ui.ozet.text()
                print(dep[-1])
                if dep[-1] == "+":
                        return
                elif dep[-1] == "*":
                        ldep = dep[:-1]

                        self.ui.ozet.setText(ldep + "+")
                elif dep[-1] == "/":
                        ldep = dep[:-1]

                        self.ui.ozet.setText(ldep + "+")
                elif dep[-1] == "-":
                        ldep = dep[:-1]

                        self.ui.ozet.setText(ldep + "+")
                else:
                        self.ui.sonuc.setText("")
                        dep = self.ui.ozet.text()
                        self.ui.ozet.setText(dep + "+")
                        return

                return

        elif sending == "btnckar":
                dep = self.ui.ozet.text()
                print(dep[-1])
                if dep[-1] == "-":
                        return
                elif dep[-1] == "*":
                        ldep = dep[:-1]

                        self.ui.ozet.setText(ldep + "-")
                elif dep[-1] == "/":
                        ldep = dep[:-1]

                        self.ui.ozet.setText(ldep + "-")
                elif dep[-1] == "+":
                        ldep = dep[:-1]

                        self.ui.ozet.setText(ldep + "-")
                else:
                        self.ui.sonuc.setText("")
                        dep = self.ui.ozet.text()
                        self.ui.ozet.setText(dep + "-")
                        return

                return


        elif sending == "xbtn":
                dep = self.ui.ozet.text()
                print(dep[-1])
                if dep[-1] == "*":
                        return
                elif dep[-1] == "-":
                        ldep = dep[:-1]

                        self.ui.ozet.setText(ldep + "*")
                elif dep[-1] == "/":
                        ldep = dep[:-1]

                        self.ui.ozet.setText(ldep + "*")
                elif dep[-1] == "+":
                        ldep = dep[:-1]

                        self.ui.ozet.setText(ldep + "*")
                else:
                        self.ui.sonuc.setText("")
                        dep = self.ui.ozet.text()
                        self.ui.ozet.setText(dep + "*")
                        return
     except SyntaxError as e:
             print(e)
             return




    def esitle(self):
        #Eşitle butonuna tıklandıgında işlemlerin özeti tutulan ozetin(label) içindeki metni alarak
        # eval komutuyla string ifadenin int olarak işlemlerin yapılarak sonuc ekrana yazdırılıyor
        try:
            expression = eval(self.ui.ozet.text())
            self.ui.sonuc.setText(str(expression))
        except SyntaxError as e:
                print(e)


    def mainbtnconnect(self):
        #Bu fonksiyona yönlendirilen butonların objectname oalrak atanan isimleri sending değerine atanıyor
        #sending değeri eşit oldugu fonksiyona girerek işlemler gerçekleşiyor
        sending = self.sender().objectName()
        if sending == "btnvrgul":
            text = self.ui.sonuc.text()
            self.ui.sonuc.setText(text + ",")
            dep = self.ui.ozet.text()
            self.ui.ozet.setText(dep + ".")

        elif sending == "btnyuzde":
            text = self.ui.sonuc.text()
            self.ui.sonuc.setText(text + "%")
            dep = self.ui.ozet.text()
            self.ui.ozet.setText(dep + "%")
        elif sending == "eksiartbtn":
            text = self.ui.sonuc.text()
            if text[0]=="-":
                text = text[1:]
                print(text)
                self.ui.sonuc.setText(text)
                self.ui.ozet.setText(text)
            else:
                 text = self.ui.sonuc.text()
                 self.ui.sonuc.setText("-"+text)
                 dep = self.ui.ozet.text()
                 self.ui.ozet.setText("-"+dep)
        elif sending == "cebtn":
            self.ui.sonuc.setText("")

        elif sending=="btn0":

            text = self.ui.sonuc.text()
            self.ui.sonuc.setText(text + "0")
            dep=self.ui.ozet.text()
            self.ui.ozet.setText(dep+"0")
            print(len(self.ui.sonuc.text()))
        elif sending=="btn1":
            text = self.ui.sonuc.text()
            self.ui.sonuc.setText(text + "1")
            dep = self.ui.ozet.text()
            self.ui.ozet.setText(dep + "1")
        elif sending=="btn2":
            text = self.ui.sonuc.text()
            self.ui.sonuc.setText(text + "2")
            dep = self.ui.ozet.text()
            self.ui.ozet.setText(dep + "2")
        elif sending=="btn3":
            text = self.ui.sonuc.text()
            self.ui.sonuc.setText(text + "3")
            dep = self.ui.ozet.text()
            self.ui.ozet.setText(dep + "3")
        elif sending=="btn4":
            text = self.ui.sonuc.text()
            self.ui.sonuc.setText(text + "4")
            dep = self.ui.ozet.text()
            self.ui.ozet.setText(dep + "4")
        elif sending=="btn5":
            text = self.ui.sonuc.text()
            self.ui.sonuc.setText(text + "5")
            dep = self.ui.ozet.text()
            self.ui.ozet.setText(dep + "5")
        elif sending=="btn6":
            text = self.ui.sonuc.text()
            self.ui.sonuc.setText(text + "6")
            dep = self.ui.ozet.text()
            self.ui.ozet.setText(dep + "6")
        elif sending=="btn7":
            text = self.ui.sonuc.text()
            self.ui.sonuc.setText(text + "7")
            dep = self.ui.ozet.text()
            self.ui.ozet.setText(dep + "7")
        elif sending=="btn8":
            text = self.ui.sonuc.text()
            self.ui.sonuc.setText(text + "8")
            dep = self.ui.ozet.text()
            self.ui.ozet.setText(dep + "8")
        elif sending=="btn9":
            text = self.ui.sonuc.text()
            self.ui.sonuc.setText(text + "9")
            dep = self.ui.ozet.text()
            self.ui.ozet.setText(dep + "9")
        elif sending=="clear1btn":
                text = self.ui.sonuc.text()
                self.ui.sonuc.setText(text[:-1])
                dep = self.ui.ozet.text()
                self.ui.ozet.setText(dep[:-1])







if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = ChildMainWindow()
    window.show()
    sys.exit(app.exec_())

