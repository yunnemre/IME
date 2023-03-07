from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1471, 902)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("/*#centralwidget{\n"
                                 "border-image:url(C:/Users/Yunn/Desktop/2109.jpg)\n"
                                 "}\n"
                                 "*/\n"
                                 "#centralwidget{background-color:#000000;\n"
                                 "}")  # 050505
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browserwidget = QtWidgets.QWidget(self.centralwidget)
        self.browserwidget.setGeometry(QtCore.QRect(40, 22, 1431, 880))
        self.tabWidget = QtWidgets.QTabWidget(self.browserwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1431, 880))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabWidget.setStyleSheet("QTabWidget QTabBar::tab{\n "
                                     "background-color: black;\n"
                                     "color: #e6e6e6;\n"
                                     "border:2px solid rgb(17,17,17);border-top-left-radius:15px;border-top-right-radius:15px;\n"
                                     "}                                 \n"
                                     "QTabWidget QTabBar::tab:selected{\n"
                                     "background-color: rgb(17 ,17 ,17);}\n"
                                     "\n"
                                     "QTabWidget QTabBar::tab:!selected:hover{\n"
                                     "background-color: rgb(54 ,54 ,54);\n"
                                     "border-color: rgb(54 ,54 ,54);\n"
                                     "}\n"
                                     "\n"
                                     "QTabWidget QTabBar::tab:selected:hover{\n"
                                     "background-color: rgb(54 ,54 ,54);\n"
                                     "border-color: rgb(54 ,54 ,54);\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "QTabWidget QTabBar::tab:!selected{background-color: black;border-color:black;}\n"
                                     "\n"
                                     "QTabBar::close-button { image: url(C:/Users/Yunn/PycharmProjects/pythonProject/IME/icons/icons8-multiply-24.png); \n"
                                     "border: 0px solid rgb(28 ,28 ,28);\n"
                                     "border-radius:5px;}\n"
                                     "\n"
                                     "QTabBar::close-button:selected{\n"
                                     "     image: url(C:/Users/Yunn/PycharmProjects/pythonProject/IME/icons/icons8-multiply-24.png);\n"
                                     "    border: 2px solid rgb(28 ,28 ,28);\n"
                                     "    background-color: rgb(28 ,28 ,28);\n"
                                     "    border-radius:5px;}\n"
                                     "\n"
                                     " QTabBar::close-button:hover {\n"
                                     "    image: url(C:/Users/Yunn/PycharmProjects/pythonProject/IME/icons/Close-256.ico);\n"
                                     "    background-color: gray;\n"
                                     "    border: 2px solid gray;\n"
                                     "    border-radius:5px;}\n"
                                     "\n"
                                     "QTabBar::close-button:selected:pressed {\n"
                                     "     image: url(C:/Users/Yunn/PycharmProjects/pythonProject/IME/icons/Close-256.ico);\n"
                                     "    background-color:rgb(28 ,28 ,28);\n"
                                     "    border: 2px solid rgb(28 ,28 ,28);\n"
                                     "    border-radius:5px;\n"
                                     " }\n"
                                     " QTabBar::close-button:pressed {\n"
                                     "    image: ur(lC:/Users/Yunn/PycharmProjects/pythonProject/IME/icons/Close-256.ico);\n"
                                     "    background-color:black;\n"
                                     "    border: 2px solid black;\n"
                                     "    border-radius:5px; }\n"
                                     "\n"
                                     "QTabBar::tab:!selected{margin-top: 2px;}                               \n"
                                     "\n"
                                     "QTabBar::tab { height: 30px; width: 150px; }")
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)

        self.cornerwidget = QtWidgets.QWidget()

        self.addtabbtn = QtWidgets.QPushButton()

        sizePolicy31 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy31.setHorizontalStretch(0)
        sizePolicy31.setVerticalStretch(0)
        sizePolicy31.setHeightForWidth(self.addtabbtn.sizePolicy().hasHeightForWidth())
        self.addtabbtn.setSizePolicy(sizePolicy31)
        self.addtabbtn.setMaximumSize(QtCore.QSize(20, 20))
        self.addtabbtn.setStyleSheet("QPushButton{background-color: black;\n"
                                     "border: 2px solid black;\n"
                                     "border-radius: 3px;\n"
                                     "}\n"
                                     "QPushButton:pressed{ background-color: black; }\n"
                                     "QPushButton:focus:pressed{ background-color: rgb(54,54,54);\n"
                                     "border-color:rgb(54,54,54);\n"
                                     "}\n"
                                     "QPushButton:hover{ background-color:rgb(28,28,28);\n"
                                     "border: 2px solid rgb(28,28,28);\n"
                                     "border-radius: 3px;\n"
                                     " }\n"

                                     "/*rgb(54 ,54 ,54)*/")

        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("icons/icons8-plus-math-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addtabbtn.setIcon(icon23)
        self.addtabbtn.setIconSize(QtCore.QSize(20, 20))
        self.addtabbtn.setObjectName("addtabbtn")
        self.vbox = QtWidgets.QHBoxLayout(self.cornerwidget)
        self.vbox.addWidget(self.addtabbtn)
        self.vbox.setSpacing(5)
        self.vbox.setContentsMargins(0, 10, 0, 0)
        self.cornerwidget.setContentsMargins(0, 0, 1254, 6)
        self.tabWidget.setCornerWidget(self.cornerwidget, Qt.TopRightCorner)

        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 80, 41, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.hzlerisimlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.hzlerisimlayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.hzlerisimlayout.setContentsMargins(0, 0, 0, 0)
        self.hzlerisimlayout.setSpacing(0)
        self.hzlerisimlayout.setObjectName("hzlerisimlayout")
        self.youtube = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.youtube.sizePolicy().hasHeightForWidth())
        self.youtube.setSizePolicy(sizePolicy)
        self.youtube.setMaximumSize(QtCore.QSize(40, 40))
        self.youtube.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);}\n"
                                   "QPushButton:disabled{ background-color: yellow; }\n"
                                   "QPushButton:pressed{ background-color: orange; }\n"
                                   "QPushButton:focus:pressed{ background-color: gray; }\n"
                                   "QPushButton:focus{ background-color:black; }\n"
                                   "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                                   "QPushButton:checked{ background-color: pink; }\n"
                                   "\n")
        self.youtube.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/youtube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.youtube.setIcon(icon7)
        self.youtube.setIconSize(QtCore.QSize(25, 25))
        self.youtube.setCheckable(False)
        self.youtube.setChecked(False)
        self.youtube.setAutoRepeat(False)
        self.youtube.setAutoDefault(False)
        self.youtube.setDefault(False)
        self.youtube.setFlat(False)
        self.youtube.setObjectName("youtube")
        self.hzlerisimlayout.addWidget(self.youtube)
        self.instagram = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instagram.sizePolicy().hasHeightForWidth())
        self.instagram.setSizePolicy(sizePolicy)
        self.instagram.setMaximumSize(QtCore.QSize(40, 40))
        self.instagram.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);}\n"
                                     "QPushButton:disabled{ background-color: yellow; }\n"
                                     "QPushButton:pressed{ background-color: orange; }\n"
                                     "QPushButton:focus:pressed{ background-color: gray; }\n"
                                     "QPushButton:focus{ background-color:black; }\n"
                                     "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                                     "QPushButton:checked{ background-color: pink; }\n"
                                     "\n")
        self.instagram.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/instagram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.instagram.setIcon(icon8)
        self.instagram.setIconSize(QtCore.QSize(25, 25))
        self.instagram.setObjectName("instagram")
        self.hzlerisimlayout.addWidget(self.instagram)
        self.whatsapp = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.whatsapp.sizePolicy().hasHeightForWidth())
        self.whatsapp.setSizePolicy(sizePolicy)
        self.whatsapp.setMaximumSize(QtCore.QSize(40, 40))
        self.whatsapp.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);}\n"
                                    "QPushButton:disabled{ background-color: yellow; }\n"
                                    "QPushButton:pressed{ background-color: orange; }\n"
                                    "QPushButton:focus:pressed{ background-color: gray; }\n"
                                    "QPushButton:focus{ background-color:black; }\n"
                                    "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                                    "QPushButton:checked{ background-color: pink; }\n"
                                    "\n")
        self.whatsapp.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.whatsapp.setIcon(icon9)
        self.whatsapp.setIconSize(QtCore.QSize(25, 25))
        self.whatsapp.setObjectName("whatsapp")
        self.hzlerisimlayout.addWidget(self.whatsapp)
        self.discord = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discord.sizePolicy().hasHeightForWidth())
        self.discord.setSizePolicy(sizePolicy)
        self.discord.setMaximumSize(QtCore.QSize(40, 40))
        self.discord.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);}\n"
                                   "QPushButton:disabled{ background-color: yellow; }\n"
                                   "QPushButton:pressed{ background-color: orange; }\n"
                                   "QPushButton:focus:pressed{ background-color: gray; }\n"
                                   "QPushButton:focus{ background-color:black; }\n"
                                   "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                                   "QPushButton:checked{ background-color: pink; }\n"
                                   "\n")
        self.discord.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/discord.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.discord.setIcon(icon10)
        self.discord.setIconSize(QtCore.QSize(29, 29))
        self.discord.setObjectName("discord")
        self.hzlerisimlayout.addWidget(self.discord)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setMaximumSize(QtCore.QSize(39, 3))
        self.line.setStyleSheet("background-color: rgb(107, 107, 107);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(-1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.hzlerisimlayout.addWidget(self.line)
        self.morebtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.morebtn.sizePolicy().hasHeightForWidth())
        self.morebtn.setSizePolicy(sizePolicy)
        self.morebtn.setMaximumSize(QtCore.QSize(40, 40))
        self.morebtn.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);}\n"
                                   "QPushButton:disabled{ background-color: yellow; }\n"
                                   "QPushButton:pressed{ background-color: orange; }\n"
                                   "QPushButton:focus:pressed{ background-color: gray; }\n"
                                   "QPushButton:focus{ background-color:black; }\n"
                                   "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                                   "QPushButton:!checked{ background-color:black; }\n"
                                   "QPushButton:!checked:hover{ background-color: rgb(54 ,54 ,54) }\n"
                                   "QPushButton:!checked:pressed{ background-color: gray; }\n"
                                   "QPushButton{\n"
                                   "    border: 2px solid black;\n"
                                   "    border-radius: 18px;      \n"
                                   "}\n"
                                   "QPushButton#evilButton:pressed {\n"
                                   "    background-color: rgb(224, 0, 0);\n"
                                   "    border-style: inset;\n"
                                   "}\n")
        self.morebtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/more2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap("icons/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.morebtn.setIcon(icon11)
        self.morebtn.setIconSize(QtCore.QSize(25, 25))
        self.morebtn.setCheckable(True)
        self.morebtn.setChecked(False)
        self.morebtn.setAutoDefault(False)
        self.morebtn.setFlat(False)
        self.morebtn.setObjectName("morebtn")
        self.hzlerisimlayout.addWidget(self.morebtn)
        self.titleheader = QtWidgets.QWidget(self.centralwidget)
        self.titleheader.setGeometry(QtCore.QRect(40, 0, 1401, 21))
        self.titleheader.setObjectName("titleheader")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1427, 0, 45, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.simgelestir = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simgelestir.sizePolicy().hasHeightForWidth())
        self.simgelestir.setSizePolicy(sizePolicy)
        self.simgelestir.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);}\n"
                                       "QPushButton:disabled{ background-color: yellow;}\n"
                                       "QPushButton:pressed{ background-color: orange; }\n"
                                       "QPushButton:focus:pressed{ background-color: gray; }\n"
                                       "QPushButton:focus{ background-color:black; }\n"
                                       "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                                       "QPushButton:checked{ background-color: pink; }\n"
                                       "\n")
        self.simgelestir.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.simgelestir.setIcon(icon12)
        self.simgelestir.setIconSize(QtCore.QSize(20, 20))
        self.simgelestir.setObjectName("simgelestir")
        self.horizontalLayout.addWidget(self.simgelestir)
        """self.bykckbtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bykckbtn.sizePolicy().hasHeightForWidth())
        self.bykckbtn.setSizePolicy(sizePolicy)
        self.bykckbtn.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);}\n"
                                    "QPushButton:disabled{ background-color: yellow; }\n"
                                    "QPushButton:pressed{ background-color: orange; }\n"
                                    "QPushButton:focus:pressed{ background-color: gray; }\n"
                                    "QPushButton:focus{ background-color:black; }\n"
                                    "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                                    "QPushButton:checked{ background-color: pink; }\n"
                                    "\n")
        self.bykckbtn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bykckbtn.setIcon(icon13)
        self.bykckbtn.setIconSize(QtCore.QSize(20, 20))
        self.bykckbtn.setObjectName("bykckbtn")
        self.horizontalLayout.addWidget(self.bykckbtn)"""
        self.appclosebtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.appclosebtn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appclosebtn.sizePolicy().hasHeightForWidth())
        self.appclosebtn.setSizePolicy(sizePolicy)
        self.appclosebtn.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);}\n"
                                       "QPushButton:disabled{ background-color: yellow; }\n"
                                       "QPushButton:pressed{ background-color: orange; }\n"
                                       "QPushButton:focus:pressed{ background-color: gray; }\n"
                                       "QPushButton:focus{ background-color:black; }\n"
                                       "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                                       "QPushButton:checked{ background-color: pink; }\n"
                                       "\n")
        self.appclosebtn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/icons8-close-50 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.appclosebtn.setIcon(icon14)
        self.appclosebtn.setIconSize(QtCore.QSize(20, 20))
        self.appclosebtn.setObjectName("appclosebtn")
        self.horizontalLayout.addWidget(self.appclosebtn)
        self.movebar = QtWidgets.QWidget(self.centralwidget)
        self.movebar.setGeometry(QtCore.QRect(0, 340, 41, 521))
        self.movebar.setObjectName("movebar")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 860, 41, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.settingslayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.settingslayout.setContentsMargins(0, 0, 0, 5)
        self.settingslayout.setSpacing(0)
        self.settingslayout.setObjectName("settingslayout")
        self.settings = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setMaximumSize(QtCore.QSize(40, 40))
        self.settings.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);}\n"
                                    "QPushButton:disabled{ background-color: yellow; }\n"
                                    "QPushButton:pressed{ background-color: orange; }\n"
                                    "QPushButton:focus:pressed{ background-color: gray; }\n"
                                    "QPushButton:focus{ background-color:black; }\n"
                                    "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                                    "QPushButton:checked{ background-color: pink; }\n"
                                    "\n")
        self.settings.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon15)
        self.settings.setIconSize(QtCore.QSize(25, 25))
        self.settings.setObjectName("settings")
        self.settingslayout.addWidget(self.settings)
        self.logo = QtWidgets.QFrame(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 41, 41))
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.log = QtWidgets.QPushButton(self.logo)
        self.log.setGeometry(QtCore.QRect(0, 0, 39, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        self.log.setMaximumSize(QtCore.QSize(40, 40))
        self.log.setStyleSheet("QPushButton::menu-indicator{width:0px;}QPushButton{;background-color: rgb(0, 0, 0);}\n"
                               "QPushButton:disabled{ background-color: yellow; }\n"
                               "QPushButton:pressed{ background-color: orange; }\n"
                               "QPushButton:focus:pressed{ background-color: gray; }\n"
                               "QPushButton:focus{ background-color:black; }\n"
                               "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                               "QPushButton:checked{ background-color: pink; }\n"
                               "\n")
        self.log.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/tarayicilogo4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.log.setIcon(icon16)
        self.log.setIconSize(QtCore.QSize(40, 40))
        self.log.setCheckable(False)
        self.log.setChecked(False)
        self.log.setAutoRepeat(False)
        self.log.setAutoDefault(False)
        self.log.setDefault(False)
        self.log.setFlat(False)
        self.log.setObjectName("log")
        self.morewidget = QtWidgets.QWidget(self.centralwidget)
        # self.morewidget.setGeometry(QtCore.QRect(0, 350, 41, 120))
        self.morewidget.setGeometry(QtCore.QRect(0, 350, 41, 0))
        self.morewidget.setStyleSheet("")
        self.morewidget.setObjectName("morewidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.morewidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.calc = QtWidgets.QPushButton(self.morewidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calc.sizePolicy().hasHeightForWidth())
        self.calc.setSizePolicy(sizePolicy)
        self.calc.setMaximumSize(QtCore.QSize(40, 40))
        self.calc.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);}\n"
                                "QPushButton:disabled{ background-color: yellow; }\n"
                                "QPushButton:pressed{ background-color: orange; }\n"
                                "QPushButton:focus:pressed{ background-color: gray; }\n"
                                "QPushButton:focus{ background-color:black; }\n"
                                "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                                "QPushButton:checked{ background-color: pink; }\n"
                                "\n")
        self.calc.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icons/icons8-calculator-66.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calc.setIcon(icon17)
        self.calc.setIconSize(QtCore.QSize(25, 25))
        self.calc.setObjectName("calc")
        self.verticalLayout_3.addWidget(self.calc)
        self.music = QtWidgets.QPushButton(self.morewidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.music.sizePolicy().hasHeightForWidth())
        self.music.setSizePolicy(sizePolicy)
        self.music.setMaximumSize(QtCore.QSize(40, 40))
        self.music.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);}\n"
                                 "QPushButton:disabled{ background-color: yellow; }\n"
                                 "QPushButton:pressed{ background-color: orange; }\n"
                                 "QPushButton:focus:pressed{ background-color: gray; }\n"
                                 "QPushButton:focus{ background-color:black; }\n"
                                 "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                                 "QPushButton:checked{ background-color: pink; }\n"
                                 "\n")
        self.music.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icons/itunes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.music.setIcon(icon18)
        self.music.setIconSize(QtCore.QSize(25, 25))
        self.music.setObjectName("music")
        self.verticalLayout_3.addWidget(self.music)
        self.notepad = QtWidgets.QPushButton(self.morewidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notepad.sizePolicy().hasHeightForWidth())
        self.notepad.setSizePolicy(sizePolicy)
        self.notepad.setMaximumSize(QtCore.QSize(40, 40))
        self.notepad.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);}\n"
                                   "QPushButton:disabled{ background-color: yellow; }\n"
                                   "QPushButton:pressed{ background-color: orange; }\n"
                                   "QPushButton:focus:pressed{ background-color: gray; }\n"
                                   "QPushButton:focus{ background-color:black; }\n"
                                   "QPushButton:hover{ background-color: rgb(54 ,54 ,54); }\n"
                                   "QPushButton:checked{ background-color: pink; }\n")
        self.notepad.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icons/icons8-notepad-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notepad.setIcon(icon19)
        self.notepad.setIconSize(QtCore.QSize(25, 25))
        self.notepad.setObjectName("notepad")
        self.verticalLayout_3.addWidget(self.notepad)
        self.ksayol = QtWidgets.QWidget(self.centralwidget)
        self.ksayol.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ksayol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ksayol.setObjectName("ksayol")
        self.ksayolcubuk = QtWidgets.QFrame(self.ksayol)
        self.ksayolcubuk.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.ksayolcubuk.setStyleSheet("background-color: rgb(37,37, 37);")
        self.ksayolcubuk.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ksayolcubuk.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ksayolcubuk.setObjectName("ksayolcubuk")
        self.yenilebtn_3 = QtWidgets.QPushButton(self.ksayolcubuk)
        self.yenilebtn_3.setGeometry(QtCore.QRect(20, 0, 21, 21))
        self.yenilebtn_3.setStyleSheet("QPushButton{background-color:rgb(37,37, 37);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border: 2px solid rgb(37,37, 37);\n"
                                       "border-radius: 10px;}\n"
                                       "QPushButton:pressed{ background-color: black;\n"
                                       "border: 2px solid black;\n"
                                       "border-radius: 10px;\n"
                                       " }\n"
                                       "QPushButton:focus:pressed{ background-color: black; \n"
                                       "border: 2px solid black;\n"
                                       "border-radius: 10px;\n"
                                       "}\n"
                                       "QPushButton:hover{ background-color:rgb(78,78,78);\n"
                                       "border: 2px solid rgb(78,78,78);\n"
                                       "border-radius: 10px;\n"
                                       " }\n"
                                       "\n")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yenilebtn_3.setText("")
        self.yenilebtn_3.setIcon(icon2)
        self.yenilebtn_3.setIconSize(QtCore.QSize(14, 14))
        self.yenilebtn_3.setCheckable(False)
        self.yenilebtn_3.setChecked(False)
        self.yenilebtn_3.setAutoRepeat(False)
        self.yenilebtn_3.setObjectName("yenilebtn_3")
        self.baslkksyol = QtWidgets.QLabel(self.ksayolcubuk)
        self.baslkksyol.setGeometry(QtCore.QRect(365, 0, 51, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.baslkksyol.setFont(font)
        self.baslkksyol.setStyleSheet("color: rgb(255, 255, 255);")
        self.baslkksyol.setObjectName("baslkksyol")
        self.ksayolgovde = QWebEngineView(self.ksayol)
        self.ksayolgovde.setGeometry(QtCore.QRect(0, 23, 801, 879))
        self.ksayolgovde.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.ksayolgovde.setObjectName("ksayolgovde")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1471, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        ######################İNSTAGRAM################################
        self.ksayol2 = QtWidgets.QWidget(self.centralwidget)
        self.ksayol2.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ksayol2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ksayol2.setObjectName("ksayol2")
        self.ksayolcubuk2 = QtWidgets.QFrame(self.ksayol2)
        self.ksayolcubuk2.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.ksayolcubuk2.setStyleSheet("background-color: rgb(37,37, 37);")
        self.ksayolcubuk2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ksayolcubuk2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ksayolcubuk2.setObjectName("ksayolcubuk2")
        self.yenilebtn4 = QtWidgets.QPushButton(self.ksayolcubuk2)
        self.yenilebtn4.setGeometry(QtCore.QRect(20, 0, 21, 21))
        self.yenilebtn4.setStyleSheet("QPushButton{background-color:rgb(37,37, 37);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border: 2px solid rgb(37,37, 37);\n"
                                      "border-radius: 10px;}\n"
                                      "QPushButton:pressed{ background-color: black;\n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 10px;\n"
                                      " }\n"
                                      "QPushButton:focus:pressed{ background-color: black; \n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 10px;\n"
                                      "}\n"
                                      "QPushButton:hover{ background-color:rgb(78,78,78);\n"
                                      "border: 2px solid rgb(78,78,78);\n"
                                      "border-radius: 10px;\n"
                                      " }\n"
                                      "\n")
        self.yenilebtn4.setText("")
        self.yenilebtn4.setIcon(icon2)
        self.yenilebtn4.setIconSize(QtCore.QSize(14, 14))
        self.yenilebtn4.setCheckable(False)
        self.yenilebtn4.setChecked(False)
        self.yenilebtn4.setAutoRepeat(False)
        self.yenilebtn4.setObjectName("yenilebtn4")
        self.baslkksyol2 = QtWidgets.QLabel(self.ksayolcubuk2)
        self.baslkksyol2.setGeometry(QtCore.QRect(365, 0, 51, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.baslkksyol2.setFont(font)
        self.baslkksyol2.setStyleSheet("color: rgb(255, 255, 255);")
        self.baslkksyol2.setObjectName("baslkksyol2")
        self.ksayolgovde2 = QWebEngineView(self.ksayol2)
        self.ksayolgovde2.setGeometry(QtCore.QRect(0, 23, 801, 879))
        self.ksayolgovde2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.ksayolgovde2.setObjectName("ksayolgovde2")

        ###########################YOUTUBE################################
        self.ksayol2Y = QtWidgets.QWidget(self.centralwidget)
        self.ksayol2Y.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ksayol2Y.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ksayol2Y.setObjectName("ksayol2Y")
        self.ksayolcubuk2Y = QtWidgets.QFrame(self.ksayol2Y)
        self.ksayolcubuk2Y.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.ksayolcubuk2Y.setStyleSheet("background-color: rgb(37,37, 37);")
        self.ksayolcubuk2Y.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ksayolcubuk2Y.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ksayolcubuk2Y.setObjectName("ksayolcubuk2Y")
        self.yenilebtn4Y = QtWidgets.QPushButton(self.ksayolcubuk2Y)
        self.yenilebtn4Y.setGeometry(QtCore.QRect(20, 0, 21, 21))
        self.yenilebtn4Y.setStyleSheet("QPushButton{background-color:rgb(37,37, 37);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border: 2px solid rgb(37,37, 37);\n"
                                       "border-radius: 10px;}\n"
                                       "QPushButton:pressed{ background-color: black;\n"
                                       "border: 2px solid black;\n"
                                       "border-radius: 10px;\n"
                                       " }\n"
                                       "QPushButton:focus:pressed{ background-color: black; \n"
                                       "border: 2px solid black;\n"
                                       "border-radius: 10px;\n"
                                       "}\n"
                                       "QPushButton:hover{ background-color:rgb(78,78,78);\n"
                                       "border: 2px solid rgb(78,78,78);\n"
                                       "border-radius: 10px;\n"
                                       " }\n"
                                       "\n"
                                       "")
        self.yenilebtn4Y.setText("")
        self.yenilebtn4Y.setIcon(icon2)
        self.yenilebtn4Y.setIconSize(QtCore.QSize(14, 14))
        self.yenilebtn4Y.setCheckable(False)
        self.yenilebtn4Y.setChecked(False)
        self.yenilebtn4Y.setAutoRepeat(False)
        self.yenilebtn4Y.setObjectName("yenilebtn4Y")
        self.baslkksyol2Y = QtWidgets.QLabel(self.ksayolcubuk2Y)
        self.baslkksyol2Y.setGeometry(QtCore.QRect(365, 0, 51, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.baslkksyol2Y.setFont(font)
        self.baslkksyol2Y.setStyleSheet("color: rgb(255, 255, 255);")
        self.baslkksyol2Y.setObjectName("baslkksyol2")
        self.ksayolgovde2Y = QWebEngineView(self.ksayol2Y)
        self.ksayolgovde2Y.setGeometry(QtCore.QRect(0, 23, 801, 879))
        self.ksayolgovde2Y.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.ksayolgovde2Y.setObjectName("ksayolgovde2Y")

        ###########################DİSCORD################################
        self.ksayol2D = QtWidgets.QWidget(self.centralwidget)
        self.ksayol2D.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ksayol2D.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ksayol2D.setObjectName("ksayol2D")
        self.ksayolcubuk2D = QtWidgets.QFrame(self.ksayol2D)
        self.ksayolcubuk2D.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.ksayolcubuk2D.setStyleSheet("background-color: rgb(37,37, 37);")
        self.ksayolcubuk2D.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ksayolcubuk2D.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ksayolcubuk2D.setObjectName("ksayolcubuk2D")
        self.yenilebtn4D = QtWidgets.QPushButton(self.ksayolcubuk2D)
        self.yenilebtn4D.setGeometry(QtCore.QRect(20, 0, 21, 21))
        self.yenilebtn4D.setStyleSheet("QPushButton{background-color:rgb(37,37, 37);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border: 2px solid rgb(37,37, 37);\n"
                                       "border-radius: 10px;}\n"
                                       "QPushButton:pressed{ background-color: black;\n"
                                       "border: 2px solid black;\n"
                                       "border-radius: 10px;\n"
                                       " }\n"
                                       "QPushButton:focus:pressed{ background-color: black; \n"
                                       "border: 2px solid black;\n"
                                       "border-radius: 10px;\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "QPushButton:hover{ background-color:rgb(78,78,78);\n"
                                       "border: 2px solid rgb(78,78,78);\n"
                                       "border-radius: 10px;\n"
                                       " }\n"
                                       "\n"
                                       "")
        self.yenilebtn4D.setText("")
        self.yenilebtn4D.setIcon(icon2)
        self.yenilebtn4D.setIconSize(QtCore.QSize(14, 14))
        self.yenilebtn4D.setCheckable(False)
        self.yenilebtn4D.setChecked(False)
        self.yenilebtn4D.setAutoRepeat(False)
        self.yenilebtn4D.setObjectName("yenilebtn4D")
        self.baslkksyol2D = QtWidgets.QLabel(self.ksayolcubuk2D)
        self.baslkksyol2D.setGeometry(QtCore.QRect(365, 0, 51, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.baslkksyol2D.setFont(font)
        self.baslkksyol2D.setStyleSheet("color: rgb(255, 255, 255);")
        self.baslkksyol2D.setObjectName("baslkksyol2D")
        self.ksayolgovde2D = QWebEngineView(self.ksayol2D)
        self.ksayolgovde2D.setGeometry(QtCore.QRect(0, 23, 801, 879))
        self.ksayolgovde2D.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.ksayolgovde2D.setObjectName("ksayolgovde2D")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.baslkksyol.setText(_translate("MainWindow", ""))



    def Downloadreq(self):
        #İndirme yapmadan önce indirme kısımın gözükceği widget'ın tasarımını init dosyasından çekmek için fonksiyon şeklince yazdım
        self.downloadreqwdgt = QtWidgets.QWidget(self.tabWidget)
        self.downloadreqwdgt.setGeometry(QtCore.QRect(0, 880, 1431, 45))
        self.downloadreqwdgt.setStyleSheet("QWidget{background-color: rgb(17, 17, 17);\n"
                                           "border:2px solid rgb(17, 17, 17);\n"
                                           "border-top-left-radius:8px;\n"
                                           "border-top-right-radius:8px;\n"
                                           "}")
        self.downloadreqwdgt.setObjectName("downloadreqwdgt")
        self.downloadreqclsbtn = QtWidgets.QPushButton(self.downloadreqwdgt)
        self.downloadreqclsbtn.setGeometry(QtCore.QRect(1400, 13, 20, 20))
        self.downloadreqclsbtn.setStyleSheet("QPushButton{background-color:rgb(17, 17, 17);\n"
                                             "border: 2px solid rgb(17, 17, 17);\n"
                                             "border-radius: 3px;}\n"

                                             "QPushButton:focus:pressed{ background-color: rgb(77, 77, 77); \n"
                                             "border: 2px solid rgb(77, 77, 77);\n"
                                             "border-radius: 3px;\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "QPushButton:hover{ background-color:rgb(47, 47, 47);\n"
                                             "border: 2px solid rgb(55,55,55);\n"
                                             "border-radius: 3px;\n"
                                             " }\n"
                                             "\n"
                                             "")
        self.downloadreqclsbtn.setObjectName("downloadreqclsbtn")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icons8-close-50 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadreqclsbtn.setIcon(icon)
        self.downloadreqclsbtn.setIconSize(QtCore.QSize(15, 15))
        self.downloadreqclsbtn.setAutoRepeat(False)
        self.downloadreqclsbtn.setText("")
        self.tumunugosterbtn = QtWidgets.QPushButton(self.downloadreqwdgt)
        self.tumunugosterbtn.setGeometry(QtCore.QRect(1280, 10, 100, 25))
        self.tumunugosterbtn.setStyleSheet("QPushButton{background-color:rgb(17, 17, 17);\n"
                                           "border: 1px solid rgb(155,155,155);\n"
                                           "border-radius: 5px;font-weight: normal;\n"
                                           "color:blue;\n"
                                           "}\n"
                                           "QPushButton:focus:pressed{ background-color: rgb(37, 37, 37); \n"
                                           "border: 1px solid rgb(155,155,155);\n"
                                           "border-radius: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "QPushButton:hover{ background-color:rgb(27, 27, 27);\n"
                                           "border: 1px solid rgb(155,155,155);\n"
                                           "border-radius: 5px;\n"

                                           " }\n"
                                           "\n"
                                           "")
        self.tumunugosterbtn.setObjectName("tumunugosterbtn")
        self.tumunugosterbtn.setText("Tümünü Göster")
        self.horizontalLayoutWidget1 = QtWidgets.QWidget(self.downloadreqwdgt)
        self.horizontalLayoutWidget1.setGeometry(QtCore.QRect(0, 0, 1200, 45))
        self.horizontalLayoutWidget1.setObjectName("horizontalLayoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setAlignment(Qt.AlignLeft)

    def downloadwdgts(self):
        #Bu kısımda indirme dosyamızın adı vs gibi özelliklerin eklendigi kısım indirme talebi kabul edilince bu dosyayı cagırıp
        #Dosyayının ismini vs özellikleri yazdırlan widget
        self.dwidgt = QtWidgets.QWidget(self.horizontalLayoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dwidgt.sizePolicy().hasHeightForWidth())
        self.dwidgt.setSizePolicy(sizePolicy)
        self.dwidgt.setMinimumSize(QtCore.QSize(200, 45))
        self.dwidgt.setStyleSheet("QWidget#dwidgt{background-color:rgb(17,17,17);\n"
                                  "border:1px solid rgb(17,17,17);\n"
                                  "border-top-left-radius:8px;\n"
                                  "border-top-right-radius:0px;\n"
                                  "} QWidget:hover#dwidgt{background-color:rgb(27,27,27);}")
        self.dwidgt.setObjectName("dwidgt")

        self.horizontalLayout_2.addWidget(self.dwidgt)


        self.dlbl = QtWidgets.QLabel(self.dwidgt)
        self.dlbl.setGeometry(QtCore.QRect(5, 13, 180, 20))
        self.dlbl.setStyleSheet(
            "QLabel{color:white;background-color:transparent;border:0px solid rgb(17,17,17);border-radius:2px;}")
        self.dlbl.setObjectName("dlbl")
        self.dlbl.setAlignment(Qt.AlignCenter)


        #BUkısımda indirilen dosyanın indirilince  aç ,klasörde göster, iptal menusunun olusturuldugu kısım

        self.dmenubtn = QtWidgets.QPushButton(self.dwidgt)
        self.dmenubtn.setGeometry(QtCore.QRect(175, 13, 20, 20))
        self.dmenubtn.setStyleSheet("QPushButton{background-color:transparent;\n"
                                    "border: 2px solid transparent;\n"
                                    "border-radius: 3px;}\n"

                                    "QPushButton:focus:pressed{ background-color: rgb(77, 77, 77); \n"
                                    "border: 2px solid rgb(77, 77, 77);\n"
                                    "border-radius: 3px;\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QPushButton:hover{ background-color:rgb(47, 47, 47);\n"
                                    "border: 2px solid rgb(55,55,55);\n"
                                    "border-radius: 3px;\n"
                                    " }\n"
                                    "\n"
                                    "")
        self.dmenubtn.setObjectName("dmenubtn")
        self.dmenubtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/downk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dmenubtn.setIcon(icon1)
        self.dmenubtn.setIconSize(QtCore.QSize(20, 20))
        self.dmenubtn.setAutoRepeat(False)
        self.dmenubtn.setCheckable(True)
        self.dmenubtn.setChecked(False)
        self.dmenubtn.setAutoDefault(False)
        self.dmenubtn.setFlat(False)


