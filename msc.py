from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import time,os
from qtacrylic import WindowEffect


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(261, 266)
        """Form.setStyleSheet("QWidget#Form{background-image: url(\'C:/xampp/htdocs/anasayfa/background/deneme1a.jpg\');\n"
"background-position:center;\n"
"background-repeat: no-repeat;\n"
"background-size: cover;\n}")"""
        self.main = QtWidgets.QWidget(Form)
        self.main.setGeometry(QtCore.QRect(0, 30, 261, 237))
        self.main.setStyleSheet("")
        self.main.setObjectName("main")
        self.main.setStyleSheet(
            "QWidget#main{background-color:rgba(0,0,0,0.1);border:1px solid transparent;border-bottom-left-radius:25px;border-bottom-right-radius:25px;}")
        self.center = QtWidgets.QWidget(self.main)
        self.center.setGeometry(QtCore.QRect(10, 0, 241, 231))
        self.center.setObjectName("center")
        self.muzikimg = QtWidgets.QLabel(self.center)
        self.muzikimg.setGeometry(QtCore.QRect(70, 0, 110, 110))
        self.muzikimg.setMinimumSize(QtCore.QSize(110, 110))
        self.muzikimg.setMaximumSize(QtCore.QSize(110, 110))
        """self.muzikimg.setStyleSheet("QLabel{\n"
"text-align:center;\n"
"}")"""
        self.muzikimg.setText("")
        self.muzikimg.setObjectName("muzikimg")
        self.progresssong = QtWidgets.QFrame(self.center)
        self.progresssong.setGeometry(QtCore.QRect(0, 190, 241, 41))
        self.progresssong.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.progresssong.setFrameShadow(QtWidgets.QFrame.Raised)
        self.progresssong.setObjectName("progresssong")
        self.filetime = QtWidgets.QSlider(self.progresssong)
        self.filetime.setGeometry(QtCore.QRect(32, 10, 171, 22))
        self.filetime.setStyleSheet("QSlider::groove:horizontal {\n"
                                    "    border-radius: 1px;\n"
                                    "    height: 3px;\n"
                                    "    margin: 0px;\n"
                                    "    background-color: rgb(52, 59, 72);\n"
                                    "}\n"
                                    "QSlider::groove:horizontal:hover {\n"
                                    "    background-color: rgb(55, 62, 76);\n"
                                    "}\n"
                                    "QSlider::handle:horizontal {\n"
                                    "    background-color: rgb(85, 170, 255);\n"
                                    "    border: none;\n"
                                    "    height: 15px;\n"
                                    "    width: 15px;\n"
                                    "    margin: -6px 0;\n"
                                    "    border-radius: 7px;\n"
                                    "    padding: -6px 0px;\n"
                                    "}\n"
                                    "QSlider::handle:horizontal:hover {\n"
                                    "    background-color: rgb(155, 180, 255);\n"
                                    "}\n"
                                    "QSlider::handle:horizontal:pressed {\n"
                                    "    background-color: rgb(65, 255, 195);\n"
                                    "}")
        self.filetime.setProperty("value", 0)
        self.filetime.setSliderPosition(0)
        self.filetime.setTracking(True)
        self.filetime.setOrientation(QtCore.Qt.Horizontal)
        self.filetime.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.filetime.setTickInterval(0)
        self.filetime.setObjectName("filetime")
        self.nowtime = QtWidgets.QLabel(self.progresssong)
        self.nowtime.setGeometry(QtCore.QRect(0, 10, 30, 21))
        self.nowtime.setObjectName("nowtime")
        self.nowtime.setStyleSheet("color:white;")
        self.endtime = QtWidgets.QLabel(self.progresssong)
        self.endtime.setGeometry(QtCore.QRect(211, 10, 30, 21))
        self.endtime.setStyleSheet("color:white;")
        self.endtime.setObjectName("endtime")
        self.playbtnset = QtWidgets.QFrame(self.center)
        self.playbtnset.setGeometry(QtCore.QRect(0, 121, 241, 70))
        self.playbtnset.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playbtnset.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playbtnset.setObjectName("playbtnset")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.playbtnset)
        self.horizontalLayout.setContentsMargins(0, 9, 0, -1)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.srufflebtn = QtWidgets.QPushButton(self.playbtnset)
        self.srufflebtn.setMinimumSize(QtCore.QSize(40, 40))
        self.srufflebtn.setMaximumSize(QtCore.QSize(40, 40))
        self.srufflebtn.setStyleSheet("QPushButton{\n"
                                      "border:1px solid ;\n"
                                      "border-radius:20px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgba(20, 20, 20,0.5);\n"
                                      "border:1px solid ;\n"
                                      "border-radius:20px;\n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:checked{\n"
                                      "background-color: rgba(20, 20, 20,0.5);\n"
                                      "border:1px  rgba(20, 20, 20,0.5) ;\n"
                                      "border-radius:15px;\n"
                                      "\n"
                                      "}")
        self.srufflebtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icons8-shuffle-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.srufflebtn.setIcon(icon)
        self.srufflebtn.setIconSize(QtCore.QSize(24, 24))
        self.srufflebtn.setCheckable(True)
        self.srufflebtn.setObjectName("srufflebtn")
        self.horizontalLayout.addWidget(self.srufflebtn)
        self.backbtn = QtWidgets.QPushButton(self.playbtnset)
        self.backbtn.setMinimumSize(QtCore.QSize(45, 45))
        self.backbtn.setMaximumSize(QtCore.QSize(40, 40))
        self.backbtn.setStyleSheet("QPushButton{\n"
                                   "border:1px solid ;\n"
                                   "border-radius:22px;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color: rgba(20, 20, 20,0.5);\n"
                                   "border:1px solid ;\n"
                                   "border-radius:15px;\n"
                                   "\n"
                                   "}")
        self.backbtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/icons8-back-forward-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backbtn.setIcon(icon1)
        self.backbtn.setIconSize(QtCore.QSize(20, 20))
        self.backbtn.setObjectName("backbtn")
        self.horizontalLayout.addWidget(self.backbtn)
        self.palybtn = QtWidgets.QPushButton(self.playbtnset)
        self.palybtn.setMinimumSize(QtCore.QSize(55, 55))
        self.palybtn.setMaximumSize(QtCore.QSize(50, 50))
        self.palybtn.setStyleSheet("QPushButton{\n"
                                   "border:1px solid  ;\n"
                                   "    \n"
                                   "border-radius:27px;\n"
                                   "\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color: rgba(20, 20, 20,0.5);\n"
                                   "border:1px solid transparent ;\n"
                                   "border-radius:15px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:checked{\n"
                                   "background-color: rgba(20, 20, 20,0.5);\n"
                                   "border:1px solid transparent ;\n"
                                   "border-radius:15px;\n"
                                   "}")
        self.palybtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/icons8-play-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.palybtn.setIcon(icon2)
        self.palybtn.setIconSize(QtCore.QSize(35, 35))
        self.palybtn.setCheckable(True)
        self.palybtn.setObjectName("palybtn")
        self.horizontalLayout.addWidget(self.palybtn)
        self.forwardbtn = QtWidgets.QPushButton(self.playbtnset)
        self.forwardbtn.setMinimumSize(QtCore.QSize(45, 45))
        self.forwardbtn.setMaximumSize(QtCore.QSize(40, 40))
        self.forwardbtn.setStyleSheet("QPushButton{\n"
                                      "border:1px solid ;\n"
                                      "border-radius:22px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgba(20, 20, 20,0.5);\n"
                                      "border:1px solid ;\n"
                                      "border-radius:15px;\n"
                                      "\n"
                                      "}")
        self.forwardbtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/icons8-fast-forward-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forwardbtn.setIcon(icon3)
        self.forwardbtn.setIconSize(QtCore.QSize(20, 20))
        self.forwardbtn.setObjectName("forwardbtn")
        self.horizontalLayout.addWidget(self.forwardbtn)
        self.repeatbtn = QtWidgets.QPushButton(self.playbtnset)
        self.repeatbtn.setMinimumSize(QtCore.QSize(35, 35))
        self.repeatbtn.setMaximumSize(QtCore.QSize(40, 40))
        self.repeatbtn.setStyleSheet("QPushButton{\n"
                                     "border:1px solid ;\n"
                                     "border-radius:20px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: rgba(20, 20, 20,0.5);\n"
                                     "border:1px solid ;\n"
                                     "border-radius:20px;\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:checked{\n"
                                     "background-color: rgba(20, 20, 20,0.5);\n"
                                     "border:1px  rgba(20, 20, 20,0.5); ;\n"
                                     "border-radius:15px;\n"
                                     "\n"
                                     "}")
        self.repeatbtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/icons8-repeat-one-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.repeatbtn.setIcon(icon4)
        self.repeatbtn.setIconSize(QtCore.QSize(24, 24))
        self.repeatbtn.setCheckable(True)
        self.repeatbtn.setObjectName("repeatbtn")
        self.horizontalLayout.addWidget(self.repeatbtn)
        self.musicvalue = QtWidgets.QSlider(self.center)
        self.musicvalue.setGeometry(QtCore.QRect(215, 6, 21, 61))
        self.musicvalue.setStyleSheet("QSlider::groove:vertical{\n"
                                      "    border-radius: 1px;\n"
                                      "    width: 3px;\n"
                                      "    margin: 0px;\n"
                                      "    background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:vertical :hover {\n"
                                      "    background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:vertical{\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "    border: none;\n"
                                      "    height: 10px;\n"
                                      "    width: 10px;\n"
                                      "    margin: 0px -4px;\n"
                                      "    border-radius:5px;\n"
                                      "    padding: 0px -4px;\n"
                                      "}\n"
                                      "QSlider::handle:vertical :hover{\n"
                                      "    background-color: rgb(155, 180, 255);\n"
                                      "}\n"
                                      "QSlider::handle:vertical :pressed{\n"
                                      "    background-color: rgb(65, 255, 195);\n"
                                      "}")
        self.musicvalue.setOrientation(QtCore.Qt.Vertical)
        self.musicvalue.setObjectName("musicvalue")
        self.musicvalue.setValue(50)
        self.valuebtn = QtWidgets.QPushButton(self.center)
        self.valuebtn.setGeometry(QtCore.QRect(210, 80, 30, 30))
        self.valuebtn.setMinimumSize(QtCore.QSize(30, 30))
        self.valuebtn.setMaximumSize(QtCore.QSize(30, 30))
        self.valuebtn.setStyleSheet("QPushButton{\n"
                                    "border:1px solid transparent;\n"
                                    "border-radius:15px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color: rgb(95, 95, 95);\n"
                                    "\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "background-color: rgb(195,195, 195);\n"
                                    "\n"
                                    "}")
        self.valuebtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/volume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.valuebtn.setIcon(icon5)
        self.valuebtn.setCheckable(False)
        self.valuebtn.setObjectName("valuebtn")
        self.head = QtWidgets.QFrame(Form)
        self.head.setGeometry(QtCore.QRect(0, 0, 261, 30))
        self.head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.head.setObjectName("head")
        self.head.setStyleSheet(
            "QWidget#head{background-color:rgba(0,0,0,0.1);border:1px solid transparent;border-top-left-radius:25px;border-top-right-radius:25px;}")
        self.list = QtWidgets.QPushButton(self.head)
        self.list.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.list.setMinimumSize(QtCore.QSize(30, 30))
        self.list.setMaximumSize(QtCore.QSize(30, 30))
        self.list.setStyleSheet("QPushButton{\n"
                                "border:1px solid transparent;\n"
                                "\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "background-color:#d3d3d3;\n"
                                "\n"
                                "\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed{\n"
                                "background-color:#d5d1d3;\n"
                                "\n"
                                "\n"
                                "}")
        self.list.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/icons8-menu-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.list.setIcon(icon6)
        self.list.setIconSize(QtCore.QSize(24, 24))
        self.list.setCheckable(True)
        self.list.setObjectName("list")
        self.closebtn = QtWidgets.QPushButton(self.head)
        self.closebtn.setGeometry(QtCore.QRect(231, 0, 30, 30))
        self.closebtn.setMinimumSize(QtCore.QSize(30, 30))
        self.closebtn.setMaximumSize(QtCore.QSize(30, 30))
        self.closebtn.setStyleSheet("QPushButton{\n"
                                    "border:1px solid transparent;\n"
                                    "\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    " background-color: rgb(85, 170, 255);\n"
                                    "    background-color: rgb(255, 75, 39);\n"
                                    "\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed{\n"
                                    "background-color:#d5d1d3;\n"
                                    "\n"
                                    "\n"
                                    "}")
        self.closebtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/icons8-multiply-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closebtn.setIcon(icon7)
        self.closebtn.setIconSize(QtCore.QSize(24, 24))
        self.closebtn.setCheckable(False)
        self.closebtn.setObjectName("closebtn")
        self.minimezebtn = QtWidgets.QPushButton(self.head)
        self.minimezebtn.setGeometry(QtCore.QRect(201, 0, 30, 30))
        self.minimezebtn.setMinimumSize(QtCore.QSize(30, 30))
        self.minimezebtn.setMaximumSize(QtCore.QSize(30, 30))
        self.minimezebtn.setStyleSheet("QPushButton{\n"
                                       "border:1px solid transparent;\n"
                                       "\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       " background-color: rgb(85, 170, 255);\n"
                                       "\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "background-color:#d5d1d3;\n"
                                       "\n"
                                       "\n"
                                       "}")
        self.minimezebtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimezebtn.setIcon(icon8)
        self.minimezebtn.setIconSize(QtCore.QSize(24, 24))
        self.minimezebtn.setCheckable(False)
        self.minimezebtn.setObjectName("minimezebtn")
        self.musicname = QtWidgets.QLabel(self.head)
        self.musicname.setGeometry(QtCore.QRect(31, 0, 171, 31))
        self.musicname.setObjectName("musicname")
        self.musicname.setStyleSheet("QLabel{color:white;}")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.musicname.setText(_translate("Form", "Şarkıların Konum: Bilgisayar/music"))


class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()


class ChildMainWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowModality(Qt.NonModal)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.closebtn.clicked.connect(self.closeevent)
        self.ui.list.clicked.connect(self.moreclck)
        self.ui.minimezebtn.clicked.connect(lambda: self.showMinimized())
        pixmap = QtGui.QPixmap("icons/tarayicilogo4.png")

        self.ui.muzikimg.setPixmap(pixmap.scaled(110, 110))

        ###

        self.morwidget = QtWidgets.QWidget(self.ui.main)
        self.morwidget.setGeometry(QtCore.QRect(0, 0, 261, 241))
        self.morwidget.setStyleSheet(
            "QWidget#morwidget{background-color:rgba(0,0,0,0.1);\n"
            ";}")

        self.morwidget.setObjectName("morwidget")
        self.morwidget.hide()
        self.listwidget = QtWidgets.QListView(self.morwidget)
        self.listwidget.setGeometry(QtCore.QRect(0, 0, 261, 241))
        self.listwidget.setAcceptDrops(True)
        self.listwidget.setProperty("showDropIndicator", True)
        self.listwidget.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.listwidget.setAlternatingRowColors(False)
        self.listwidget.setUniformItemSizes(True)
        self.listwidget.setFrameShape(False)

        self.listwidget.setStyleSheet("background-color:transparent;color:white;")
        self.listwidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listwidget.setObjectName("listwidget")

        ####
        self.player = QMediaPlayer()
        self.player.play()

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.player.error.connect(self.erroralert)

        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        self.ui.palybtn.pressed.connect(self.playpause)
        self.player.setVolume(50)
        self.ui.musicvalue.valueChanged.connect(self.player.setVolume)

        self.ui.backbtn.pressed.connect(self.playlist.previous)
        self.ui.forwardbtn.pressed.connect(self.playlist.next)

        self.model = PlaylistModel(self.playlist)
        self.listwidget.setModel(self.model)
        self.playlist.currentIndexChanged.connect(self.playlist_position_changed)

        selection_model = self.listwidget.selectionModel()
        selection_model.selectionChanged.connect(self.playlist_selection_changed)

        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.ui.filetime.valueChanged.connect(self.player.setPosition)
        self.ui.valuebtn.clicked.connect(self.valuechange)
        self.ui.repeatbtn.clicked.connect(self.repeat)
        self.ui.srufflebtn.clicked.connect(self.random)

        ####Muzikleri Çekme
        self.open_file()

        self.windowFX = WindowEffect()
        self.windowFX.setAeroEffect(self.winId())

        self.setStyleSheet("QMenu {border-radius:25px;}")
        self.setAcceptDrops(True)
        self.show()

        def moveWindow(e):

            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.musicname.mouseMoveEvent = moveWindow
        self.ui.muzikimg.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def closeevent(self):
        self.player.stop()
        self.close()

    def playpause(self):
        try:
            if self.ui.palybtn.isChecked():
                icon6 = QtGui.QIcon()
                icon6.addPixmap(
                    QtGui.QPixmap("icons/icons8-play-48.png"),
                    QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ui.palybtn.setIcon(icon6)
                self.player.pause()
            else:
                if self.ui.repeatbtn.isChecked():
                    print("bbbb")

                else:
                    pass
                icon6 = QtGui.QIcon()
                icon6.addPixmap(
                    QtGui.QPixmap("icons/icons8-pause-48.png"),
                    QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ui.palybtn.setIcon(icon6)
                self.player.play()
        except:
            return

    def repeat(self):
        if self.ui.repeatbtn.isChecked():
            self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        else:
            self.playlist.setPlaybackMode(QMediaPlaylist.Sequential)
            self.random()

    def random(self):
        if self.ui.srufflebtn.isChecked():
            if self.ui.repeatbtn.isChecked():
                return
            else:
                self.playlist.setPlaybackMode(QMediaPlaylist.Random)
        else:
            self.playlist.setPlaybackMode(QMediaPlaylist.Sequential)

    def valuechange(self):
        value = self.ui.musicvalue.value()
        if 0 <= value <= 24:
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("icons/volume (1).png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.valuebtn.setIcon(icon6)
            self.ui.musicvalue.setValue(25)
        elif 25 <= value <= 49:
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("icons/volume.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.valuebtn.setIcon(icon6)
            self.ui.musicvalue.setValue(50)
        elif 50 <= value <= 74:
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("icons/volume.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.valuebtn.setIcon(icon6)
            self.ui.musicvalue.setValue(75)
        elif 75 <= value <= 90:
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("icons/volume.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.valuebtn.setIcon(icon6)
            self.ui.musicvalue.setValue(100)
        elif 91 <= value <= 100:
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("icons/mute (1).png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.valuebtn.setIcon(icon6)
            self.ui.musicvalue.setValue(0)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.playlist.addMedia(
                QMediaContent(url)
            )

        self.model.layoutChanged.emit()

        if self.player.state() != QMediaPlayer.PlayingState:
            i = self.playlist.mediaCount() - len(e.mimeData().urls())
            self.playlist.setCurrentIndex(i)
            self.player.play()

    def open_file(self):
        import glob
        for file in glob.glob(f"C:/Users/{os.getlogin()}/music/*.mp3"):
            self.playlist.addMedia(
                QMediaContent(
                    QUrl.fromLocalFile(file)
                )
            )

        self.model.layoutChanged.emit()

    def update_duration(self, duration):
        self.ui.filetime.setMaximum(duration)

        if duration >= 0:
            self.ui.endtime.setText(time.strftime('%M:%S', time.localtime(self.player.duration() / 1000)))

    def update_position(self, position):
        if position >= 0:
            self.ui.nowtime.setText(time.strftime('%M:%S', time.localtime(self.player.position() / 1000)))

        self.ui.filetime.blockSignals(True)
        self.ui.filetime.setValue(position)
        self.ui.filetime.blockSignals(False)

    def moreclck(self):
        if self.ui.list.isChecked():
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("icons/back.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.list.setIcon(icon6)
            self.morwidget.show()
        else:
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("icons/icons8-menu-24.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.list.setIcon(icon6)
            self.morwidget.hide()

    def playlist_selection_changed(self, ix):
        i = ix.indexes()[0].row()

        self.playlist.setCurrentIndex(i)
        if not self.ui.palybtn.isChecked():
            self.player.play()

    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.listwidget.setCurrentIndex(ix)
            self.ui.musicname.setText(self.listwidget.currentIndex().data())

    def erroralert(self, *args):
        print(args)




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = ChildMainWindow()
    window.show()
    sys.exit(app.exec_())
