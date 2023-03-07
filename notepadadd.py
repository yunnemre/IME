import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QIcon)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5 import QtCore, QtGui, QtWidgets
import notepad


class Ui_NotePadeAdd(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 565)
        Form.setStyleSheet("background-color: #fff3c9;")
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #fff3c9;")
        self.headadd = QtWidgets.QWidget(self.centralwidget)
        self.headadd.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.headadd.setStyleSheet("background-color: #ffe792;")
        self.headadd.setObjectName("headadd")
        self.headmove = QtWidgets.QWidget(self.headadd)
        self.headmove.setGeometry(QtCore.QRect(30, 0, 710, 30))
        self.headmove.setStyleSheet("background-color: transparent;")
        self.headmove.setObjectName("headmove")
        self.kapatadd = QtWidgets.QPushButton(self.headadd)
        self.kapatadd.setGeometry(QtCore.QRect(770, 0, 30, 30))
        self.kapatadd.setMinimumSize(QtCore.QSize(30, 30))
        self.kapatadd.setMaximumSize(QtCore.QSize(30, 30))
        self.kapatadd.setStyleSheet("QPushButton{background-color: #ffe792;\n"
                                    "border:1px solid transparent;}\n"
                                    "QPushButton:hover{ background-color: rgb(216, 206, 170); }\n"
                                    "QPushButton:pressed{ background-color: #baa86a; }\n"

                                    "")
        self.kapatadd.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/closenoot50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kapatadd.setIcon(icon)
        self.kapatadd.setIconSize(QtCore.QSize(20, 20))
        self.kapatadd.setObjectName("kapatadd")
        self.ekleadd = QtWidgets.QPushButton(self.headadd)
        self.ekleadd.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.ekleadd.setMinimumSize(QtCore.QSize(30, 30))
        self.ekleadd.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.ekleadd.setFont(font)
        self.ekleadd.setStyleSheet("QPushButton{background-color: #ffe792;text-align:center;\n"
                                   "padding-bottom:5px;\n"
                                   "border:1px solid transparent;}\n"
                                   "QPushButton:hover{ background-color: rgb(216, 206, 170); }\n"
                                   "QPushButton:pressed{ background-color: #baa86a; }\n"

                                   "")
        self.ekleadd.setText("+")
        self.ekleadd.setObjectName("ekleadd")
        self.ucnokta = QtWidgets.QPushButton(self.headadd)
        self.ucnokta.setGeometry(QtCore.QRect(740, 0, 30, 30))
        self.ucnokta.setMinimumSize(QtCore.QSize(30, 30))
        self.ucnokta.setMaximumSize(QtCore.QSize(30, 30))
        self.ucnokta.setCheckable(True)
        self.ucnokta.setStyleSheet("QPushButton{background-color: #ffe792;\n"
                                   "border:1px solid transparent;}\n"
                                   "QPushButton:hover{ background-color: rgb(216, 206, 170); }\n"
                                   "QPushButton:pressed{ background-color: #baa86a; }\n"
                                   "QPushButton:checked{ background-color: rgb(216, 206, 170); }\n"
                                   "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/moreadd32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ucnokta.setText("")
        self.ucnokta.setIcon(icon2)
        self.ucnokta.setIconSize(QtCore.QSize(20, 20))
        self.ucnokta.setObjectName("ayarlar_3")
        self.footer = QtWidgets.QWidget(self.centralwidget)
        self.footer.setGeometry(QtCore.QRect(0, 525, 800, 50))
        self.footer.setStyleSheet("QWidget{\n"
                                  "border: 1px solid  rgb(216, 206, 170);\n"
                                  "border-color:rgb(216, 206, 170) transparent transparent transparent;\n"
                                  "}")
        self.footer.setObjectName("footer")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout.setContentsMargins(0, 0, 500, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.footer)
        self.pushButton.setCheckable(True)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "border:1px solid transparent;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "border:1px solid transparent;\n"
                                      "    background-color: rgb(216, 206, 170);\n"
                                      "}"
                                      "QPushButton:checked{border:1px solid transparent;\n"
                                      "    background-color: rgb(216, 206, 170);\n}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.footer)
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setCheckable(True)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "border:1px solid transparent;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "border:1px solid transparent;\n"
                                        "    background-color: rgb(216, 206, 170);\n"
                                        "}"
                                        "QPushButton:checked{border:1px solid transparent;\n"
                                        " background-color: rgb(216, 206, 170);\n}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.footer)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setCheckable(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "border:1px solid transparent;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "border:1px solid transparent;\n"
                                        "    background-color: rgb(216, 206, 170);\n"
                                        "}"
                                        "QPushButton:checked{border:1px solid transparent;\n"
                                        "    background-color: rgb(216, 206, 170);\n}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.footer)
        self.pushButton_4.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_4.setCheckable(True)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setItalic(False)
        font.setStrikeOut(True)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "border:1px solid transparent;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "border:1px solid transparent;\n"
                                        "    background-color: rgb(216, 206, 170);\n"
                                        "}"
                                        "QPushButton:checked{border:1px solid transparent;\n"
                                        "    background-color: rgb(216, 206, 170);\n}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QComboBox(self.footer)
        self.pushButton_5.setMinimumSize(QtCore.QSize(45, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(45, 30))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setEditable(False)

        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.addItem(QIcon("icons/icons8-align-left-48.png"), "")
        self.pushButton_5.addItem(QIcon("icons/icons8-align-center-48.png"), "")
        self.pushButton_5.addItem(QIcon("icons/icons8-align-right-48.png"), "")
        self.pushButton_5.setStyleSheet("QComboBox{border:0px;}\n"
                                        "QComboBox:hover{\n"
                                        "    background-color: rgb(216, 206, 170);\n"
                                        "}"
                                        "QComboBox::drop-down{subcontrol-position: bottom right;width:1px; }"
                                        "QComboBox QAbstractItemView {"
                                        "background-color:transparent;padding-left:4px;"
                                        "}"
                                        "QComboBox QAbstractItemView {"
                                        "border: 1px solid transparent;"
                                        "selection-background-color: rgb(216, 206, 170);"
                                        "background-color: transparent;"


                                        "}"
                                        )
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QSpinBox(self.footer)
        self.pushButton_6.setMinimumSize(QtCore.QSize(45, 30))
        self.pushButton_6.setMaximumSize(QtCore.QSize(45, 30))
        self.pushButton_6.setStyleSheet("QSpinBox{\n"
                                        "border:1px solid transparent;\n"
                                        "}\n"
                                        "QSpinBox:hover{\n"
                                        "border:1px solid transparent;\n"
                                        "    background-color: rgb(216, 206, 170);\n"
                                        "}\n"
                                        "QSpinBox::up-button {\n"
                                        "subcontrol-position: top right; /* position at the top right corner */\n"
                                        "width: 16px;\n"
                                        "}"

                                        "QSpinBox::down-button {\n"
                                        "subcontrol-position: bottom right; /* position at bottom right corner */\n"
                                        "width: 16px;\n"
                                        " }")

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/image50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setValue(14)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.plainTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 30, 800, 495))
        self.font = QtGui.QFont()
        self.font.setPointSize(14)
        self.plainTextEdit.setFont(self.font)
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextEdit.setTabChangesFocus(False)
        self.plainTextEdit.setStyleSheet("padding:15px;overflow:visible;")
        self.plainTextEdit.setPlaceholderText("Notunuzu Alınız")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "B"))
        self.pushButton_2.setText(_translate("Form", "I"))
        self.pushButton_3.setText(_translate("Form", "U"))
        self.pushButton_4.setText(_translate("Form", "ab"))


class ChildMainWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_NotePadeAdd()
        self.ui.setupUi(self)
        self.path = None

        self.setWindowModality(Qt.NonModal)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.kapatadd.clicked.connect(self.closeevent)
        self.ui.ekleadd.clicked.connect(self.addbtn)
        self.ui.ucnokta.clicked.connect(self.ucnotkacontrol)
        self.window2 = notepad.ChildMainWindow()
        self.ui.pushButton.clicked.connect(self.boldtext)
        self.ui.pushButton_2.clicked.connect(self.boldtext)
        self.ui.pushButton_3.clicked.connect(self.boldtext)
        self.ui.pushButton_4.clicked.connect(self.boldtext)
        self.ui.pushButton_5.currentIndexChanged.connect(self.boldtext)
        self.ui.pushButton_6.valueChanged.connect(self.boldtext)

        def moveWindow(e):

            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.headmove.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def closeevent(self):
        try:
            self.saving_run()
        except:
            pass
        if self.window2.isVisible():
            self.close()
        else:
            self.windows = notepad.ChildMainWindow()
            self.windows.show()
            self.close()

    def settingbtn(self):
        self.settingframe = QtWidgets.QWidget(self.ui.centralwidget)
        self.settingframe.setGeometry(QtCore.QRect(500, 30, 300, 100))
        self.settingframe.setStyleSheet("background-color: white;")
        self.settingframe.setObjectName("settingframe")

        font = QtGui.QFont()
        font.setPointSize(12)
        self.notkismi = QtWidgets.QPushButton(self.settingframe)
        self.notkismi.setGeometry(QtCore.QRect(0, 0, 300, 50))
        self.notkismi.setStyleSheet(
            "QPushButton{background-color: white;border:1px solid transparent;padding-left:15px;text-align:left;}\n"
            "QPushButton:hover{background-color: #eee;}\n"
            "QPushButton:pressed{ background-color: #ccc; }\n"
            "")
        self.notkismi.setObjectName("notkismi")
        self.notkismi.setText("Notları Görüntüle")
        self.notkismi.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/notalign48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notkismi.setIcon(icon)
        self.notkismi.setIconSize(QtCore.QSize(24, 24))
        self.notsil = QtWidgets.QPushButton(self.settingframe)
        self.notsil.setGeometry(QtCore.QRect(0, 50, 300, 50))
        self.notsil.setStyleSheet(
            "QPushButton{color:red;background-color: white;border:1px solid transparent;\n"
            "padding-left:15px;text-align:left;}\n"
            "QPushButton:hover{background-color: #eee;}\n"
            "QPushButton:pressed{ background-color: #ccc; }\n"
            "")
        self.notsil.setObjectName("notsil")
        self.notsil.setText("Notu Sil")
        self.notsil.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/copnot24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notsil.setIcon(icon2)
        self.notsil.setIconSize(QtCore.QSize(24, 24))
        self.notkismi.clicked.connect(self.notshow)
        self.notsil.clicked.connect(self.deletetxt)

    def ucnotkacontrol(self):
        if self.ui.ucnokta.isChecked():

            self.settingbtn()
            self.settingframe.show()
        else:

            self.settingframe.hide()
            self.settingframe.deleteLater()
            self.renkkismi.deleteLater()
            self.horizontalLayout3.deleteLater()
            self.siyah.deleteLater()
            self.turuncu.deleteLater()
            self.notkismi.deleteLater()
            self.notsil.deleteLater()

    def notshow(self,w):
        if self.window2.isVisible():

            self.window2.activateWindow()
            return
        self.window2.show()
        self.window2.move(self.pos().x() - 340, self.pos().y())

    def boldtext(self,message):
        if self.ui.pushButton.isChecked():

            self.ui.font.setBold(True)
        else:
            self.ui.font.setBold(False)

        if self.ui.pushButton_2.isChecked():

            self.ui.font.setItalic(True)
        else:
            self.ui.font.setItalic(False)

        if self.ui.pushButton_3.isChecked():

            self.ui.font.setUnderline(True)
        else:
            self.ui.font.setUnderline(False)

        if self.ui.pushButton_4.isChecked():

            self.ui.font.setStrikeOut(True)
        else:
            self.ui.font.setStrikeOut(False)

        if self.ui.pushButton_6.value() != 12:

            self.ui.font.setPointSize(self.ui.pushButton_6.value())
        else:
            self.ui.font.setPointSize(12)

        if self.ui.pushButton_5.currentIndexChanged:

            if self.ui.pushButton_5.currentIndex()==0:
                cursor=self.ui.plainTextEdit.textCursor()
                textblock=cursor.blockFormat()
                textblock.setAlignment(Qt.AlignLeft)
                cursor.mergeBlockFormat(textblock)
                self.ui.plainTextEdit.setTextCursor(cursor)

            elif self.ui.pushButton_5.currentIndex()==1:
                cursor = self.ui.plainTextEdit.textCursor()
                textblock = cursor.blockFormat()
                textblock.setAlignment(Qt.AlignCenter)
                cursor.mergeBlockFormat(textblock)
                self.ui.plainTextEdit.setTextCursor(cursor)

            elif self.ui.pushButton_5.currentIndex()==2:
                cursor = self.ui.plainTextEdit.textCursor()
                #textblock = QtGui.QTextBlockFormat()
                textblock = cursor.blockFormat()
                textblock.setAlignment(Qt.AlignRight)
                cursor.mergeBlockFormat(textblock)
                self.ui.plainTextEdit.setTextCursor(cursor)

        else:
            pass

        self.ui.plainTextEdit.setFont(self.ui.font)

    def addbtn(self):
        window1 = ChildMainWindow()
        window1.show()
        window1.move(self.pos().x() + 50, self.pos().y() + 50)

    def opening_run(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text files (*.txt)")

        if path:
            try:
                with open(path, 'r') as f:
                    text = f.read()

            except Exception as e:
                self.dialog_critical(str(e))

            else:
                self.path = path
                self.ui.plainTextEdit.setPlainText(text)

    def saving_run(self):
        if self.path is None:
            return self.saveac()

        self._save_to_path(self.path)

    def saveac(self):
        if self.ui.plainTextEdit.toPlainText()=="":
            return

        path, filter = QFileDialog.getSaveFileName(self, "Save file", "", "Text files (*.txt)")

        if not path:

            return

        self._save_to_path(path)

        dosya = open("notepad/txtpath.txt", "a", encoding="utf-8")
        dosya.write(f"'{path}'\n")
        dosya.close()
        self.window2.icerik()

    def _save_to_path(self, path):
        text = self.ui.plainTextEdit.toPlainText()
        print(self.ui.plainTextEdit.fontInfo().bold())
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            pass
            self.dialog_critical(str(e))

        else:
            self.path = path

    def ac(self,s):
        path= s
        if path:
            try:
                with open(path, 'r') as f:
                    text = f.read()

            except Exception as e:
                with open("notepad/txtpath.txt", 'r') as f:
                    s = f.readlines()
                    outputline = []
                    for i in s:

                        if i != f"'{path}'\n":
                            outputline.append(i)

                        else:
                            pass

                fs = open("notepad/txtpath.txt", 'w')
                fs.writelines(outputline)
                fs.close()
                #msgbox


                self.sfd()
                self.close()
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Dosya belirlenen yodla bulunamadı\n.Silinmiş olabilir.\n\t")
                msgBox.setWindowFlags(Qt.FramelessWindowHint)

                msgBox.setStandardButtons(QMessageBox.Close)
                buttony = msgBox.button(QMessageBox.Close)
                buttony.setText("Kapat")
                returnValue = msgBox.exec()
                return

            else:
                self.path = path
                self.ui.plainTextEdit.setPlainText(text)

    def deletetxt(self):
        import os
        if self.path is None:
            return self.closeevent()


        with open("notepad/txtpath.txt", 'r') as f:
            s = f.readlines()
            outputline=[]
            for i in s:

                if i!=f"'{self.path}'\n":
                    outputline.append(i)

                else:
                    pass



        fs = open("notepad/txtpath.txt", 'w')
        fs.writelines(outputline)
        fs.close()
        os.remove(self.path)
        self.windows = notepad.ChildMainWindow()
        self.windows.show()
        self.close()



    def sfd(self):
        self.window2.close()
        self.window2 = notepad.ChildMainWindow()
        self.window2.show()






"""if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ChildMainWindow()
    window.show()
    sys.exit(app.exec_())
"""