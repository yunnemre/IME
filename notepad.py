from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import notepadadd

import re

class Ui_Notepad(object):
    def setupUi(self, Notepad):
        #Pencerin oluşturulması ve özellikleri
        Notepad.setObjectName("Notepad")
        Notepad.resize(325, 565)
        Notepad.setStyleSheet("background-color: white;")
        #Pencerenin dışını saran bir frame objesi
        self.frame = QtWidgets.QFrame(Notepad)
        self.frame.setGeometry(QtCore.QRect(0, 0, 325, 570))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #Kapatma, ekle, headmove(pencereyi tasımak için oluşturulan widget) gibi kısımların eklendigi widget
        self.head = QtWidgets.QWidget(self.frame)
        self.head.setGeometry(QtCore.QRect(0, 0, 325, 40))
        self.head.setStyleSheet("background-color: white;")
        self.head.setObjectName("head")
        #Penceresiz ekran tasarımında tasınma olmadıgı için tasıma alanı olusturmak için olusturulan widget
        self.headmove = QtWidgets.QWidget(self.head)
        self.headmove.setGeometry(QtCore.QRect(40, 0, 245, 40))
        self.headmove.setStyleSheet("background-color: transparent;")
        self.headmove.setObjectName("headmove")
        #Ekle butonu not defteriini açmak için oluşturulan buton
        self.ekle = QtWidgets.QPushButton(self.head)
        self.ekle.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.ekle.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.ekle.setFont(font)
        self.ekle.setStyleSheet("QPushButton{text-align:center;\n"
                                "padding-bottom:5px;background-color: white;border:1px solid transparent;}\n"
                                "QPushButton:hover{background-color:#ccc;}\n"
                                "QPushButton:pressed{ background-color: #a2a2a2; }\n")
        self.ekle.setIconSize(QtCore.QSize(48, 48))
        self.ekle.setObjectName("ekle")

        #Uygulamayı kapatmak için olusturulan buton
        self.kapat = QtWidgets.QPushButton(self.head)
        self.kapat.setGeometry(QtCore.QRect(285, 0, 40, 40))
        self.kapat.setMinimumSize(QtCore.QSize(40, 40))
        self.kapat.setStyleSheet("QPushButton{background-color: white;border:1px solid transparent;}\n"
                                 "QPushButton:hover{background-color:#ccc;}\n"
                                 "QPushButton:pressed{ background-color: #a2a2a2; }\n"
                                 "")
        self.kapat.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/closenoot50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kapat.setIcon(icon1)
        self.kapat.setIconSize(QtCore.QSize(20, 20))
        self.kapat.setObjectName("kapat")
        #Gövde tasarımını içine alacak main widgetı
        self.main = QtWidgets.QWidget(self.frame)
        self.main.setGeometry(QtCore.QRect(0, 105, 325, 455))
        self.main.setObjectName("main")
        #Notları açmak için oluturulan butonalrı altta dogru sıralamk için oluşturulan vertical widget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout.setContentsMargins(15, 10, 15, 0)
        self.verticalLayout.setAlignment(Qt.AlignTop)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        #aramalbl(not defteri metnini içeren label)  içine alacak widget
        self.searchwdgt = QtWidgets.QWidget(self.frame)
        self.searchwdgt.setGeometry(QtCore.QRect(0, 40, 325, 65))
        self.searchwdgt.setStyleSheet("background-color: white;")
        self.searchwdgt.setObjectName("searchwdgt")
        #Not defteri yazı eklemek için tasarıma eklenen bir tasarım objesi
        self.aramalbl = QtWidgets.QLabel(self.searchwdgt)
        self.aramalbl.setGeometry(QtCore.QRect(0, 0, 315, 30))
        self.aramalbl.setStyleSheet("background-color: white;")
        self.aramalbl.setText("Not Defteri")
        self.aramalbl.setAlignment(Qt.AlignCenter)
        self.aramalbl.setObjectName("aramalbl")
        font2 = QtGui.QFont()
        font2.setFamily("Gabriola")
        font2.setBold(True)
        font2.setPointSize(18)
        self.aramalbl.setFont(font2)

        #Butonların text ifadelerinin yer aldığı fonksiyonun çagrılması
        self.retranslateUi(Notepad)
        QtCore.QMetaObject.connectSlotsByName(Notepad)

    def retranslateUi(self, Notepad):
        _translate = QtCore.QCoreApplication.translate
        Notepad.setWindowTitle(_translate("Notepad", "Form"))
        self.ekle.setText(_translate("Notepad", "+"))


class ChildMainWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        #Ui_Notepad classını(pencere tasarımının oluşturugu kısım) init içerisine çağrılması
        self.ui = Ui_Notepad()
        self.ui.setupUi(self)
        #Çoklu uygulama çalıştırmak için eklenen window yöntemi
        self.setWindowModality(Qt.NonModal)
        #Penceresiz ekran tasarımı için eklenen windowflag(pencere bayrağı) özelliği atanması
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #Kapatma ve ekleme butonun click event yönlendirilmesi
        self.ui.kapat.clicked.connect(self.closeevent)
        self.ui.ekle.clicked.connect(self.addbtn)
        #Uygulamda kaydedilen dosyaların ekranda gösterilip eklenmsi için çağrılan fonksiyon
        self.icerik()

        #Pencereyi taşımak için eklenen fonksiyon
        def moveWindow(e):

            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.headmove.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        #Pencereyi tasımak için eklenen fonksiyona tıklandıgı kısmın konumunu göndermek için hazırlanan clickpositon objesi
        self.clickPosition = event.globalPos()

    def closeevent(self):
        #
        try:
            if self.windows.isVisible() :
                self.close()
            else:
                self.close()
        except AttributeError as e:
            self.close()

    def addbtn(self):
        self.windows = notepadadd.ChildMainWindow()
        self.windows.show()
        self.close()


    def icerik(self):
        try:
            self.blog2.deleteLater()
        except AttributeError as e:
            pass

        with open("notepad/txtpath.txt", 'r') as f:
            s=f.readlines()
            self.x=0
            for i in s:
                self.x+=1
                res_dct = dict(Name=i)
                self.fname=res_dct['Name']
                split=self.fname.replace("/"," ").split()[-1].replace(".txt\'","")



                self.blog2 = QtWidgets.QPushButton(self.ui.main)
                self.blog2.setMinimumSize(QtCore.QSize(295, 70))
                self.blog2.setStyleSheet("QWidget{background-color: #eed269;border:1px solid transparent;} \n"
                                         "QWidget:hover{background-color: #fff3c9;}\n"
                                         "")
                self.blog2.setObjectName(f"{split}")
                self.blog2lbl = QtWidgets.QLabel(self.blog2)
                self.blog2lbl.setGeometry(QtCore.QRect(0, 0, 95, 30))
                self.blog2lbl.setText("Konu:")
                self.blog2lbl.setStyleSheet(
                    "QLabel{border:1px solid;border-color:transparent transparent black transparent;\n"
                    "background-color:transparent;}")
                font3 = QtGui.QFont()
                font3.setFamily("Gabriola")
                font3.setPointSize(18)

                self.blog2lbl.setAlignment(Qt.AlignCenter)
                self.blog2lbl.setFont(font3)
                self.blog2lblic = QtWidgets.QLabel(self.blog2)
                self.blog2lblic.setGeometry(QtCore.QRect(0, 30, 295, 40))
                self.blog2lblic.setText(f"{split}")
                self.blog2lblic.setStyleSheet("QLabel{padding-left:5px;background-color:transparent;}")
                font3 = QtGui.QFont()
                font3.setFamily("Gabriola")
                font3.setPointSize(18)

                self.blog2lblic.setFont(font3)
                self.ui.verticalLayout.addWidget(self.blog2)
                self.blog2.clicked.connect(self.tb)


    def tb(self,):
        try:
            windows = notepadadd.ChildMainWindow()
            sending = self.sender().objectName()
            if True:
                with open("notepad/txtpath.txt", 'r') as f:
                    s = f.readlines()

                    for i in s:
                        res_dct = dict(Name=i)
                        fname = res_dct['Name']

                        try:
                            list=[]
                            kont=re.search(f"{sending}",fname,).group()
                            if not None==kont :
                                list.append(re.search(r"'(.*?)'",fname).group())
                                self.list=list[0]


                        except AttributeError as e:
                            pass

                path = self.list.replace("'","")
                windows.show()
                windows.ac(s=path)
                self.close()
        except:
            pass






if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = ChildMainWindow()
    window.show()

    sys.exit(app.exec_())
