#Gerekli Olan Modüller ve dosyalar projeye ekleniyor
import sys
import os

from PyQt5.QtCore import QPropertyAnimation,QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from star6t import *
from PyQt5.QtWebEngineWidgets import *
import os.path
import datetime
import pymysql
import hesapmakinesi
import msc
import notepad




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #Tasarımların oldugu dosyayı self ui ye atayarak özellikleri çekiyorum
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #Penceren Çerceçe özelliklerini atandıgı kısım
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(Qt.NonModal)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #star6t dosyaysında oluşturulan görünümdeki butonların click eventlerine bağlama
        # Main Pencere Kapatma butonu
        self.ui.appclosebtn.clicked.connect(self.closeevent)
        #Altta atma butonu
        self.ui.simgelestir.clicked.connect(lambda: self.showMinimized())
        #Hızlı erişim panelindeki more(üç nokta kısmının butonu)
        self.ui.morebtn.clicked.connect(self.morefunction)
        #Hızlı Erişimdeki whatsapp butonu
        self.ui.whatsapp.clicked.connect(self.whatsappweb)
        # Hızlı Erişimdeki instagram butonu
        self.ui.instagram.clicked.connect(self.instagramweb)
        # Hızlı Erişimdeki discord butonu
        self.ui.discord.clicked.connect(self.discordweb)
        # Hızlı Erişimdeki youtube butonu
        self.ui.youtube.clicked.connect(self.youtubeweb)
        # Hızlı Erişimdeki hesap makinesi butonu
        self.ui.calc.clicked.connect(self.calc)
        # Hızlı Erişimdeki not defteri butonu
        self.ui.notepad.clicked.connect(self.notepad)
        # Hızlı Erişimdeki muzik botu butonu
        self.ui.music.clicked.connect(self.musicbot)

        #Bu kısımda instagram ve whatsapp butonun penceresinde kullanılan Qwebengine itemine bir page özelliği atayarak
        #sayfanın hangi sürümde açılacağını belirtiyoruz
        #Bu kısmı manuel atamasssam Sitelere giriş yapmıyor hata alıyorum
        self.profile = QWebEngineProfile()
        self.profile.setHttpUserAgent(
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82  Safari/537.36")
        self.page = QWebEnginePage(self.profile, self.ui.ksayolgovde)
        self.ui.ksayolgovde.setPage(self.page)

        #Bu kısımda yukardaki gibi  youtube için page yapılandırması atıyorum
        #Normalde uRLLERİNİ butoonların bağlandıgı fonksiyonada yönlendiriyordum ancak youtube hızlı erişimi alta atınca,
        # şarkı çalmaya devam etsin diye yönlendrimeye init fonksiyonunda yapıyorum
        self.yprofile = QWebEngineProfile()
        self.yprofile.setHttpUserAgent(
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82  Safari/537.36")
        self.ypage = QWebEnginePage(self.yprofile, self.ui.ksayolgovde2Y)
        self.ui.ksayolgovde2Y.setPage(self.ypage)
        self.ui.ksayolgovde2Y.setUrl(QUrl("https://youtube.com/"))

        #Hızlı erişim butonlarına basılınca açılan widget ın sayfayı yenilemek için oluşturulan butonların görevlendirlmesi yapılması
        self.ui.yenilebtn4Y.clicked.connect(self.ui.ksayolgovde2Y.reload)
        self.ui.yenilebtn4.clicked.connect(self.ui.ksayolgovde2.reload)
        self.ui.yenilebtn_3.clicked.connect(self.ui.ksayolgovde.reload)
        self.ui.yenilebtn4D.clicked.connect(self.ui.ksayolgovde2D.reload)

        ############Kısayol close Widget#################
        #Bu kısımda hzılı erişim kısmından bir uygulamaya tıklandıgında hızlı erişim çerçevenin dışında bir yere tıklandığında
        #Hızlı erişim penceresini kapatmak için oluşturulan Click eventi için kullanılacak widget ın eklenmesi
        self.passwidget = QtWidgets.QWidget(self.ui.centralwidget)
        self.passwidget.setGeometry(QtCore.QRect(839, 116, 0, 788))
        self.passwidget.setStyleSheet("background-color: transparent;")
        self.passwidget.setObjectName("passwidget")

        #Logo Butonuna tıklandıgında açılan menunun özellikelrini ve bağlantı yerlerinin atanması
        self.menu = QMenu()
        self.menu.addAction("Yeni Sekme", self.addtabbtn)
        self.menu.addAction("İndirilenler", self.indirlenlerpage)
        self.menu.addAction("Geçmiş", self.gecmispage)
        self.ui.log.setMenu(self.menu)

        #Bu kısımda star6t dosyasında olusturulan indirme yapıldıgında altta gözüken küçük dikdörtgen pencerin oluşumunu çağırma
        #Ve click eventlerinin atanması
        self.ui.Downloadreq()
        self.ui.downloadreqclsbtn.clicked.connect(self.dwnloadwdgtclose)
        self.ui.tumunugosterbtn.clicked.connect(self.tumunugosterbtn)

        # Bu Kısımda ileri ,geri, yenile , url bar, hesap ,vs gibi butonların tasarımalarının oldugu fonksiyonu init içerisine çağırma
        self.tabcrnchng()
        #Tarayıcı özelliği atamak için Qwebengine mettodunun uyglumaya eklenmesi ve özellikelrinin atanması
        self.browser = QWebEngineView()

        #Tarayıcı metodu eklendikten soran Tab bar olarak tasarlanan tarayıcı tab widget ilk sekmesi olarak atama

        self.ui.tabWidget.addTab(self.browser, "Hızlı Erişim")
        self.browser.setContentsMargins(0, 58, 0, 0)
        #Tarayıcı pencersi için oluşturulan bi page sınıfı ekleme
        self.page = QWebEnginePage(self.profile, self.browser)
        self.browser.setPage(self.page)
        #İlk sayfaının bağlantı urlsini atama
        self.ui.tabWidget.currentWidget().load(QUrl('http://localhost/anasayfa/hew.html'))
        #Tarayıcın Java vs. gibi eklentilerin eklendiği kısım
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        #Cookie özellikleriin sadece gerekli  olanların kabulu diğerlerin reddi şeklinde özellik atama
        self.page.profile().setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        #Cookie lerin dosya halinde kaydedilmesi
        self.defaultProfile = QWebEngineProfile.defaultProfile()
        self.defaultProfile.setCachePath("yourfolder")
        self.defaultProfile.setPersistentStoragePath("yourfolder")

        #Url barı güncellemek için  kullanılan bir çağrım
        i = self.ui.tabWidget.addTab(self.browser, self.ui.tabWidget.tabText(0))
        self.browser.urlChanged.connect(lambda qurl, browser=self.browser:
                                        self.update_urlbar(qurl, browser))
        #Tab kısmında girdiği sitenin title çekip tab widget barına atandıgı kısım
        self.browser.loadFinished.connect(lambda _, i=i, browser=self.browser:
                                          self.ui.tabWidget.setTabText(i, browser.page().title()))

        # İndirme Taleplerin iletilceği fonksiyonu belirtme
        self.browser.page().profile().downloadRequested.connect(self.on_downloadRequested)

        # self.ui.menuaramacubu.returnPressed.connect(self.loadUrlMain)
        #Bu kısımda tarayıca ileri , geri yenile, anasayfa vs gibi self.tabcrnchng() çağrılan butonların click işlevlerinin atanması
        self.geribtn_2.clicked.connect(lambda: self.ui.tabWidget.currentWidget().back())
        self.ileribtn_2.clicked.connect(lambda: self.ui.tabWidget.currentWidget().forward())
        self.yenilebtn_2.clicked.connect(lambda: self.ui.tabWidget.currentWidget().reload())
        self.anasayfabtn_2.clicked.connect(self.home)
        self.camerabtn.clicked.connect(self.screenshoot)
        self.aramacubuedit_2.returnPressed.connect(self.load_url)
        #Tab widget için oluşturulan ekle ve kapat tuslarının yönlendrimeleri
        self.ui.addtabbtn.clicked.connect(self.addtabbtn)
        self.ui.tabWidget.tabCloseRequested.connect(self.closecurrent_tab)
        self.ui.tabWidget.currentChanged.connect(self.currenttab_changed)
        #Url bar değiştiğinde geçmiş database kaydetmek için oluşturulan fonksyiona yönlendirme
        self.aramacubuedit_2.textChanged.connect(self.historysave)
        #Kullanıcı için oluştuurlan kullanıcı giriş sayfasına yölnedirildiği fonksyona bağlama
        self.hesapbtn.clicked.connect(self.hesapcontent)

        #Bu kısımda tarayıcın ses görüntü paylaşımı taleplerini mesaj kutusnda gösterildiği ve
        # evet hayır durumuna göre izin veren fonksyiona bağlandıgı kısım
        # self.browser.page().featurePermissionRequested.connect(self.popupmicandcam)

        #Url Bar ilk tıklandıgında barın içerisindeki metinin hepsini şemek için kullandıgım fonksiyon
        #Hemen altında url bar bu fonksiyona yönlendiriliyor(self.aramacubuedit_2)
        def selectlinedit(y):
            if y.button() == Qt.LeftButton:
                if self.aramacubuedit_2.selectionLength() == 0:
                    self.aramacubuedit_2.selectAll()
                else:
                    self.aramacubuedit_2.deselect()

            else:
                pass

        self.aramacubuedit_2.mousePressEvent = selectlinedit

        #Bu kısımda hzılı erişim kısmındaki butonları tıklandıgında yeniden tarayıcıya basıp kapatmak için
        # arkada transparent şeklinde oluşan widget ın genişliğinin duruma göre ayarlanması için oluşturudgum fonksiyon
        #Eğer click eventine girdiyse hızlı erişim widgetlarının yeniden geometrisini atıyor ve passwidget iteminin genişliğini sıfırlıyor

        def pageclick(s):
            if s.button() == Qt.LeftButton:
                self.ui.ksayol.setGeometry(QtCore.QRect(39, 7, 0, 902))
                self.ui.ksayol2.setGeometry(QtCore.QRect(39, 7, 0, 902))
                self.ui.ksayol2Y.setGeometry(QtCore.QRect(39, 7, 0, 902))
                self.ui.ksayol2D.setGeometry(QtCore.QRect(39, 7, 0, 902))
                passwidgtwdht = self.passwidget.width()
                if passwidgtwdht == 1431:
                    self.passwidget.setGeometry(QtCore.QRect(0, 60, 0, 784))
                else:
                    self.passwidget.setGeometry(QtCore.QRect(0, 60, 0, 784))

            else:
                pass

        # self.ui.aramaubcuguwdgt.mousePressEvent = pageclick
        self.passwidget.mousePressEvent = pageclick

        #Çerçevesiz ekran modeli kullandıgım için ekranın sağa sola taşınmıyor
        #Bu alttaki moveWindow foksiyonuyla uygulamanın üst ve sol kısmındaki bosluklara widget atayarak
        #TAŞınmasını sağlıyorum
        def moveWindow(e):

            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        #Bu kısımda sagdan ve ussten ayrıdıgım widgetları fonksiyona göderiyorum
        #Click eventi gerçekleşip taşınmaya çalışıldıgında
        # movePressevent fonksiyonunda gelen clickPositon global konuma göre yeniden konumlandırıyor
        self.ui.titleheader.mouseMoveEvent = moveWindow
        self.ui.movebar.mouseMoveEvent = moveWindow
        #Pencere görünür yapıyor
        self.show()

    def calc(self):
        #Hızlı erişim kısmından hesapmakinesi butonuna tıklandıgında çağrılan foksiyon
        self.window1 = hesapmakinesi.ChildMainWindow() #Hesap Makinesi için oluşturulan Dosyayı self.window1 'e atıyor
        self.window1.show()  #Uygulanmayı görünür kılıyor.

    def notepad(self):
        # Hızlı erişim kısmından not defteri butonuna tıklandıgında çağrılan foksiyon
        self.notpadw = notepad.ChildMainWindow() #Not defteri için oluşturulan Dosyayı self.window1 'e atıyor
        self.notpadw.show() #Uygulanmayı görünür kılıyor.

    def musicbot(self):
        # Hızlı erişim kısmından müzik butonuna tıklandıgında çağrılan foksiyon
        self.muscwnd = msc.ChildMainWindow()  #Müzik botu için oluşturulan Dosyayı self.window1 'e atıyor
        self.muscwnd.show() #Uygulanmayı görünür kılıyor.


    def hesapcontent(self,qurl=None, label="Hesap"):
        #tabcrnchng fonksiyonunda oluşturlan hesap butonuna tıklandıgında bağlanılıyor
        #
        #url yönlendirme yoksa google yönlendriyor
        if qurl is None:
            qurl = QUrl("https://google.com/")

        #Bir tarayıcı objesi atanıyor ve verilen aralıga oturtmak için content marginleri atanıyor
        browser = QWebEngineView()
        browser.setContentsMargins(0, 58, 0, 0)
        #Page init de oluşturaln profil atanıyor
        #page objesi browserin içine yollanıyor
        page = QWebEnginePage(self.profile, browser)
        browser.setPage(page)

        #Tabwidget itemine yeni bir sayfa ekleniyor içine browser(tarayıcı objesi ekleniyor)
        i = self.ui.tabWidget.addTab(browser, label)
        #Tab widget son eklenen yani bu sayfaya geçiş yapıyor
        self.ui.tabWidget.setCurrentIndex(i)
        #Kullanıcı için oluşturulan giriş sayfasına yönlendiriliyor
        self.ui.tabWidget.currentWidget().load(QUrl('http://localhost/login/login.php'))

        #Tab widget köşe kısmında marginlerle sola çektiğim ekle butonunu anlık konumu çekip tab bar genişkliğini çıkarıyor
        # ve yeni sayfa eklendiğinde tab bar ile ekle butonu iç içe geçmiyor
        marginright = self.ui.cornerwidget.contentsMargins().right()
        self.ui.cornerwidget.setContentsMargins(0, 0, marginright - 154, 6)

        #Browserin urlsini güncellemek için update_urlbar fonksiyonuna yolluyor
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        #Tab bar kısmının textini sayfadan alınan title içerisinden çekerek tab barı güncelliyor
        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.ui.tabWidget.setTabText(i, browser.page().title()))

    """def girispage(self):
        
        self.addtabbtn()
        count = self.ui.tabWidget.count()
        self.ui.tabWidget.setCurrentIndex(count - 1)
        #
        self.ui.tabWidget.currentWidget().load(QUrl('http://localhost/login/mctas.php?yenile=03781c4d8f9fb327'))
"""
    def gecmispage(self):
        # Logo kısmında menuden geçmiş butonuna tılandıgında çağrılan addtabbtn fonksiyonuyla yeni bir tarayıcı sekmesi açıyor
        self.addtabbtn()
        # Son eklenen sayfayı geçmek için count sayısını çekip indexler sıfırdan başladıgı için bir küçügünü alıp buluna n indexi değiştiriyor
        count = self.ui.tabWidget.count()
        self.ui.tabWidget.setCurrentIndex(count - 1)
        #Bu kısımda geçmişi gösteremek için oluşturulan web site urlsine yönlendirilyor
        self.ui.tabWidget.currentWidget().load(QUrl('http://localhost/history/data.php'))

    def indirlenlerpage(self):
        # Logo kısmında menuden indirlenler butonuna tılandıgında çağrılan addtabbtn fonksiyonuyla yeni bir tarayıcı sekmesi açıyor
        self.addtabbtn()
        # Son eklenen sayfayı geçmek için count sayısını çekip indexler sıfırdan başladıgı için bir küçügünü alıp buluna n indexi değiştiriyor
        count = self.ui.tabWidget.count()
        self.ui.tabWidget.setCurrentIndex(count - 1)
        # Bu kısımda indirlenleri gösteremek için oluşturulan web site urlsine yönlendirilyor
        self.ui.tabWidget.currentWidget().load(QUrl('http://localhost/download/download.php'))


    def historysave(self):
        #Url bar text değişince yönlendilen bir fonksiyon
        #Fonksiyonun amacı gezidğin siteleri geçmişe kaydetme
        #Öncelikle database bağlantısı kurluyor
        try:
            db = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='',
                                 db='web',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
            baglanti = db.cursor()
            #Tarihi eklemek için datetime modülündne format değiştirek çekiliyor
            htarih = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

            #Bu if else döngüleri eğer url boş , geçmiş , veya giriş sayfası tasarımı gibi sitelerin urlleri dönüyorsa kayıt yapmadan return ediyor
            #Geriye kalan siteler else  içerisinde database den execute ile kaydı yapılıyor
            if self.ui.tabWidget.currentWidget().url().toString() == '':
                return
            elif self.ui.tabWidget.currentWidget().url().toString() == f'http://localhost/download/download.php':
                return
            elif self.ui.tabWidget.currentWidget().url().toString() == 'http://localhost/anasayfa/hew.html':
                return
            elif self.ui.tabWidget.currentWidget().url().toString() == f'http://localhost/yun/data.php':
                return
            elif self.ui.tabWidget.currentWidget().url().toString() == f'https://www.google.com/':
                return
            else:
                baglanti.execute(
                    f"INSERT INTO history (HTarih,HPage) VALUES ('{htarih}','{self.ui.tabWidget.currentWidget().url().toString()}')")
                db.commit()
        except:
            pass

    def tabcrnchng(self):
        #Tarayıcının ileri, geri, url bar vs gibi butonların oluşturuldgu kısım
        #Genel hepsini kapsayan widget bu kısımda oluşturulan objelere bunun içine veya altındaki objelerde yer alıyor
        aramaubcuguwdgt = QtWidgets.QWidget(self.ui.browserwidget)
        aramaubcuguwdgt.setGeometry(QtCore.QRect(0, 34, 1431, 60))
        aramaubcuguwdgt.setStyleSheet("/*background-color: rgb(43, 43, 43);\n"
                                      "\n"
                                      "*/\n"
                                      "background-color: rgb(17, 17, 17);")
        aramaubcuguwdgt.setObjectName("aramaubcuguwdgt")

        #Geri Butonun ve özeliklerinin atanması
        self.geribtn_2 = QtWidgets.QPushButton(aramaubcuguwdgt)
        self.geribtn_2.setGeometry(QtCore.QRect(0, 0, 31, 30))
        self.geribtn_2.setStyleSheet("QPushButton{background-color: rgb(17, 17,17);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border: 2px solid rgb(17,17,17);\n"
                                     "border-radius: 15px;}\n"
                                     "QPushButton:pressed{ background-color: black; }\n"
                                     "QPushButton:focus:pressed{ background-color: black; }\n"
                                     "\n"
                                     "\n"
                                     "QPushButton:hover{ background-color:rgb(78,78,78);\n"
                                     "border: 2px solid rgb(78,78,78);\n"
                                     "border-radius: 15px;\n"
                                     " }\n"
                                     "\n"
                                     "/*rgb(54 ,54 ,54)*/")
        self.geribtn_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.geribtn_2.setIcon(icon)
        self.geribtn_2.setIconSize(QtCore.QSize(32, 32))
        self.geribtn_2.setObjectName("geribtn_2")

        #İleri Butonun ve özeliklerinin atanması
        self.ileribtn_2 = QtWidgets.QPushButton(aramaubcuguwdgt)
        self.ileribtn_2.setGeometry(QtCore.QRect(30, 0, 31, 30))
        self.ileribtn_2.setStyleSheet("QPushButton{background-color: rgb(17, 17,17);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border: 2px solid rgb(17,17,17);\n"
                                      "border-radius: 15px;}\n"
                                      "QPushButton:pressed{ background-color: black; }\n"
                                      "QPushButton:focus:pressed{ background-color: black; }\n"
                                      "\n"
                                      "\n"
                                      "QPushButton:hover{ background-color:rgb(78,78,78);\n"
                                      "border: 2px solid rgb(78,78,78);\n"
                                      "border-radius: 15px;\n"
                                      " }\n"
                                      "")
        self.ileribtn_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ileribtn_2.setIcon(icon1)
        self.ileribtn_2.setIconSize(QtCore.QSize(32, 32))
        self.ileribtn_2.setObjectName("ileribtn_2")

        #Yenile Butonun ve özeliklerinin atanması
        self.yenilebtn_2 = QtWidgets.QPushButton(aramaubcuguwdgt)
        self.yenilebtn_2.setGeometry(QtCore.QRect(60, 0, 31, 30))
        self.yenilebtn_2.setStyleSheet("QPushButton{background-color: rgb(17, 17,17);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border: 2px solid rgb(17,17,17);\n"
                                       "border-radius: 15px;}\n"
                                       "QPushButton:pressed{ background-color: black; }\n"
                                       "QPushButton:focus:pressed{ background-color: black; }\n"
                                       "\n"
                                       "\n"
                                       "QPushButton:hover{ background-color:rgb(78,78,78);\n"
                                       "border: 2px solid rgb(78,78,78);\n"
                                       "border-radius: 15px;\n"
                                       " }\n"
                                       "\n"
                                       "")
        self.yenilebtn_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yenilebtn_2.setIcon(icon2)
        self.yenilebtn_2.setIconSize(QtCore.QSize(19, 19))
        self.yenilebtn_2.setCheckable(False)
        self.yenilebtn_2.setChecked(False)
        self.yenilebtn_2.setAutoRepeat(False)
        self.yenilebtn_2.setObjectName("yenilebtn_2")


        #Url bar kısımın atanması ve özeliklerinin verilmesi
        self.aramacubuedit_2 = QtWidgets.QLineEdit(aramaubcuguwdgt)
        self.aramacubuedit_2.setGeometry(QtCore.QRect(90, 0, 1271, 30))
        self.aramacubuedit_2.setStyleSheet("QLineEdit{\n"
                                           "border: 2px solid gray;\n"
                                           "border-radius: 15px;\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "padding-left:20px;\n"
                                           "}\n"
                                           "QLineEdit:hover{\n"
                                           "background-color:rgb(38,38,38);\n"
                                           "padding-left:30px;\n"
                                           "}")
        self.aramacubuedit_2.setObjectName("aramacubuedit_2")
        #Screenshot(Kamera)  butonunun eklenmsi için açılan widget
        songibi_2 = QtWidgets.QWidget(aramaubcuguwdgt)
        songibi_2.setGeometry(QtCore.QRect(1310, 4, 41, 21))
        songibi_2.setStyleSheet("background-color: rgb(17, 17, 17);")
        songibi_2.setObjectName("songibi_2")
        #Screenshot(Kamera) botunun widget içine horizontal şeklinde biçimlendirme
        horizontalLayout_3 = QtWidgets.QHBoxLayout(songibi_2)
        horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_3.setSpacing(0)
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        #Screenshot(Kamera) butoun ve özeliklerinin atanması
        self.camerabtn = QtWidgets.QPushButton(songibi_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camerabtn.sizePolicy().hasHeightForWidth())
        self.camerabtn.setSizePolicy(sizePolicy)
        self.camerabtn.setMaximumSize(QtCore.QSize(20, 20))
        self.camerabtn.setStyleSheet("QPushButton{background-color: rgb(17, 17, 17);\n"
                                     "border:1px solid rgb(17,17,17);\n"
                                     "}\n"
                                     "QPushButton:disabled{ background-color: yellow; }\n"
                                     "QPushButton:pressed{ background-color: rgb(17, 17, 17); }\n"
                                     "QPushButton:focus:pressed{ background-color: gray; }\n"
                                     "QPushButton:focus{ background-color: rgb(17, 17, 17); }\n"
                                     "QPushButton:hover{ background-color: rgb(78 ,78 ,78); }\n"
                                     "QPushButton:checked{ background-color: pink; }\n"
                                     "\n"
                                     "\n"
                                     "")
        self.camerabtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/icons8-camera-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camerabtn.setIcon(icon3)
        self.camerabtn.setIconSize(QtCore.QSize(19, 19))
        self.camerabtn.setObjectName("camerabtn")
        #Horizontal widget içine kamera butonun eklenmesi
        horizontalLayout_3.addWidget(self.camerabtn)
        #Favoriler butounun atanması ve özelliklerin verilmesi
        self.kaydetbtn_3 = QtWidgets.QPushButton(songibi_2)
        self.kaydetbtn_3.setMaximumSize(QtCore.QSize(20, 20))
        self.kaydetbtn_3.setStyleSheet("QPushButton{background-color: rgb(17, 17, 17);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border:1px solid rgb(17,17,17);\n"
                                       "\n"
                                       "}\n"
                                       "QPushButton:disabled{ background-color: yellow; }\n"
                                       "QPushButton:pressed{ background-color:rgb(17,17,17); }\n"
                                       "QPushButton:focus:pressed{ background-color:gray; }\n"
                                       "QPushButton:focus{ background-color:rgb(17,17,17); }\n"
                                       "QPushButton:hover{ background-color:rgb(78,78,78); }\n"
                                       "QPushButton:checked{ background-color: pink; }\n"
                                       "")
        self.kaydetbtn_3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kaydetbtn_3.setIcon(icon4)
        self.kaydetbtn_3.setIconSize(QtCore.QSize(19, 18))
        self.kaydetbtn_3.setObjectName("kaydetbtn_3")
        #Kamera butouyla aynı horzontal widget içine ekleme
        horizontalLayout_3.addWidget(self.kaydetbtn_3)
        #Hesap ve anasayfa butonu oluşturuldugunda içinde gözükçeği gorzontal widgetın atanması
        horizontalLayoutWidgetah = QtWidgets.QWidget(aramaubcuguwdgt)
        horizontalLayoutWidgetah.setGeometry(QtCore.QRect(1362, 0, 62, 30))
        horizontalLayoutWidgetah.setObjectName("horizontalLayoutWidgetah")
        horizontalLayoutah = QtWidgets.QHBoxLayout(horizontalLayoutWidgetah)
        horizontalLayoutah.setContentsMargins(0, 0, 0, 0)
        horizontalLayoutah.setSpacing(0)
        horizontalLayoutah.setObjectName("horizontalLayoutah")
        horizontalLayoutah.setAlignment(Qt.AlignLeft)
        #Hesap butonu ve özeliklerin atanması
        self.hesapbtn = QtWidgets.QPushButton(aramaubcuguwdgt)
        self.hesapbtn.setGeometry(QtCore.QRect(1393, 0, 31, 30))
        self.hesapbtn.setStyleSheet("QPushButton{background-color: rgb(17, 17,17);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 2px solid rgb(17,17,17);\n"
                                         "border-radius: 3px;}\n"
                                         "QPushButton:pressed{ background-color: black; }\n"
                                         "QPushButton:focus:pressed{ background-color: black; }\n"
                                         "\n"
                                         "\n"
                                         "QPushButton:hover{ background-color:rgb(78,78,78);\n"
                                         "border: 2px solid rgb(78,78,78);\n"
                                         "border-radius: 3px;\n"
                                         " }\n"
                                    "")
        self.hesapbtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/icons8-account-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hesapbtn.setIcon(icon5)
        self.hesapbtn.setIconSize(QtCore.QSize(23, 23))
        self.hesapbtn.setObjectName("hesapbtn")
        #Anasayfa butounu ve özelliklerin atanması
        self.anasayfabtn_2 = QtWidgets.QPushButton(aramaubcuguwdgt)
        self.anasayfabtn_2.setGeometry(QtCore.QRect(1361, 0, 31, 30))
        self.anasayfabtn_2.setStyleSheet(
                                         "QPushButton{background-color: rgb(17, 17,17);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 2px solid rgb(17,17,17);\n"
                                         "border-radius: 3px;}\n"
                                         "QPushButton:pressed{ background-color: black; }\n"
                                         "QPushButton:focus:pressed{ background-color: black; }\n"
                                         "\n"
                                         "\n"
                                         "QPushButton:hover{ background-color:rgb(78,78,78);\n"
                                         "border: 2px solid rgb(78,78,78);\n"
                                         "border-radius: 3px;\n"
                                         " }\n"
                                         "")
        self.anasayfabtn_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.anasayfabtn_2.setIcon(icon6)
        self.anasayfabtn_2.setIconSize(QtCore.QSize(23, 23))
        self.anasayfabtn_2.setObjectName("anasayfabtn_2")
        #Anasayfa ve hesap butonu için oluşturulan widget içine butonların eklenmesi
        horizontalLayoutah.addWidget(self.anasayfabtn_2)
        horizontalLayoutah.addWidget(self.hesapbtn)

    def addtabbtn(self, qurl=None, label="Hızlı Erişim"):
        #Tarayıcıda bir sekme eklenmsi gerektiinde gerek butonlardan gerek ekle butonun atıklandıgında bağlanılan fonksiyon

        if qurl is None:
            qurl = QUrl("https://google.com/")
        #Bir browser objesi içine owebengine objesi çağrılır
        browser = QWebEngineView()
        #Pencereyi tab widgeta oturtmak için margin veriliyor
        browser.setContentsMargins(0, 58, 0, 0)
        #Sayfanın progil özelliklerimi initte oluşturlan profili ekleyerk page objesine atanıyor
        page = QWebEnginePage(self.profile, browser)
        # Ve browserın page modulu ile page ekleniyor
        browser.setPage(page)

        #Tab widget addtabb modulu ile oluşturulan browser ve yukardan çekilen label ile oluşturuluyor
        i = self.ui.tabWidget.addTab(browser, label)
        #Mevcut Konumu son ekşlenen sekmeye alıyor
        self.ui.tabWidget.setCurrentIndex(i)
        #Eğer sonradan url verilmediyse anasayda tasırımına yönlendirilyor
        self.ui.tabWidget.currentWidget().load(QUrl('http://localhost/anasayfa/hew.html'))

        #Ekle butonunun mevcut marginini çekiyor ve tab bar genmişliği çıkarılıyor ki iç içe geçmesin buton ile tab bar
        marginright = self.ui.cornerwidget.contentsMargins().right()
        self.ui.cornerwidget.setContentsMargins(0, 0, marginright - 154, 6)

        #Bu  updateurlbar fonksiyonun a gönderilyor
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))
        #Sayfanın url yuklemsi bittiginde sayfanın title olarak atanan textini tab widgetın bar textine atıyor
        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.ui.tabWidget.setTabText(i, browser.page().title()))


    def closecurrent_tab(self, i):
        #Tab ar tasarımında ekjlediğim kapatılabilir modulu sayesinde close url bar da close işareti oluyor
        #Sekme Kapatma butouna tıklandıgında Eğer bir tane sekme var ise anasayda tasırımına yönlendiriliyor
        count = self.ui.tabWidget.count()
        if count == 1:
            return self.ui.tabWidget.currentWidget().load(QUrl('http://localhost/anasayfa/hew.html'))

        #Tılandıgı indexi page sayfasını çekiyor
        page = self.ui.tabWidget.widget(i)
        #tabwidge objesinin removetab modulu ile sekmeyi siliyor
        self.ui.tabWidget.removeTab(i)
        #Sekme için atanan sayfa(page) objesini siliyor
        page.deleteLater()
        #Ekle butonun sekme silindiğinde sağda kalmasın diye sola doğru margin veirliyor
        # (Mevcut konumu çektikten sonra tab bar genişliği ekleniyor)
        marginright = self.ui.cornerwidget.contentsMargins().right()
        self.ui.cornerwidget.setContentsMargins(0, 0, marginright + 154, 6)

    def home(self):
        #Anasayfa butonuna tılandıgında url yi google olarak günceliyor
        self.ui.tabWidget.currentWidget().setUrl(QUrl("https://google.com/"))

    def update_urlbar(self, q, browser=None):
        #Bu fonksiyon url veya sekme değiştiginde url barı güncellemek için yönledirilen fonksiyon
        #Browser objesi current widgeta eşit değil ise return yollanıyor
        if browser != self.ui.tabWidget.currentWidget():
            return
        #Return edilmesse arama cubugunun(urlbarın) textini yönlendirilirken gelen q objesini (url) text oalrak atıyor
        self.aramacubuedit_2.setText(q.toString())
        self.aramacubuedit_2.setCursorPosition(0)


    def currenttab_changed(self):
        #Sekme değiştiginde güncel sekmedeki urlyi çekip updateurlbar(urlbar teextini güncellemke için) fonksiyonuna yollanıyor
        #Sekme değişince fonksiyona geliyor
        qurl = self.ui.tabWidget.currentWidget().url()
        self.aramacubuedit_2.setText(qurl.toString())
        self.update_urlbar(qurl, self.ui.tabWidget.currentWidget())

    def load_url(self):
        #Url bardan elle yazılan metin ifadesinin eğer bir https sunucusu bağlantısı ise direk açaması
        # değil ise googledan metinin aratılması için bir döngüye sokuyor ve urlyi güncelliyor
        q = self.aramacubuedit_2.text()
        if 'https://' in q:
            self.ui.tabWidget.currentWidget().load(QUrl(q))
        else:
            url = self.aramacubuedit_2.text()
            qurls = f"https://www.google.com/search?q={url}"
            self.ui.tabWidget.currentWidget().load(QUrl(qurls))

    def mousePressEvent(self, event):
        #moveWindow fonksiyonun(Pencereyi taşımak için oluşturulan foksiyon) tıklandıgı kısmın conumunu atıyor
        # ve yukarıdan çekiliyor
        self.clickPosition = event.globalPos()

    def closeevent(self):
        #Uygulamıın kapatma tusuna bastıgında clse modulu ile uygulamayı katıyor
        self.close()
        app2 = QApplication(sys.argv)
        app2.exec_()



    def instagramweb(self):
        #Hızlı erişimdeki instagram butonuna tıklandıgında çağrılna foksiyon

        #Passwidget(ekranan tıklayarak kapatmak için oluşturulan widget) objesiin mevcut gernişligini atıyor ve kontrol ediyor
        #Eger sıfır ise yuksekliği uygulama ile aynı yapıyor
        passwidgtwdht = self.passwidget.width()
        if passwidgtwdht == 0:
            self.passwidget.setGeometry(QtCore.QRect(839, 116, 632, 788))
        else:
            pass

        #Eger instagram harcinde discord vs gibi hızlı erişim objeleri açık ise genişliğini sıfırlıyor instagram gövde tasarımını animasyon ile buyultuyor
        self.ui.ksayol2Y.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ui.ksayol.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ui.ksayol2D.setGeometry(QtCore.QRect(39, 7, 0, 902))
        #star6t da tasarlanan instagram baslık atıyor
        self.ui.baslkksyol2.setText("İnstagram")
        #Url yönlediriyor
        self.ui.ksayolgovde2.setUrl(QUrl("https://www.instagram.com/"))
        widht = self.ui.ksayol2.width()
        #instagram gövdesinin uzunlugunu çekiyor 0 ise animasyon ile 800 ekliyor görininr bi hal alıyor değil ise sıfırlıyor hata oluşmasın diye
        if widht == 0:
            self.animation = QPropertyAnimation(self.ui.ksayol2, b"geometry")
            self.animation.setDuration(700)
            self.animation.setStartValue(QtCore.QRect(self.ui.ksayol2.geometry()))
            self.animation.setEndValue(QtCore.QRect(self.ui.ksayol2.geometry().adjusted(0, 0, 800, 0)))
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
        else:
            self.ui.ksayol2.setGeometry(QtCore.QRect(39, 7, 0, 902))

    def whatsappweb(self):
        # Hızlı erişim kısmındaki Whatsapp butouna tıklandıgında bağlanılıyor
        #  instagramweb fonksiyonunda açılanna aynı şeyleri yapıyor sadece whatsappa yönlendiriyor
        passwidgtwdht = self.passwidget.width()
        if passwidgtwdht == 0:
            self.passwidget.setGeometry(QtCore.QRect(839, 116, 632, 788))
        else:
            pass

        self.ui.ksayol2Y.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ui.ksayol2.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ui.ksayol2D.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ui.baslkksyol.setText("Whatsapp")
        self.ui.ksayolgovde.setUrl(QUrl("https://web.whatsapp.com/"))
        widht = self.ui.ksayol.width()

        if widht == 0:
            self.animation = QPropertyAnimation(self.ui.ksayol, b"geometry")
            self.animation.setDuration(700)
            self.animation.setStartValue(QtCore.QRect(self.ui.ksayol.geometry()))
            self.animation.setEndValue(QtCore.QRect(self.ui.ksayol.geometry().adjusted(0, 0, 800, 0)))
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

        else:
            self.ui.ksayol.setGeometry(QtCore.QRect(39, 7, 0, 902))

    def youtubeweb(self):
        #Hızlı erişimdeki youtube butonuna tıkladıgında bağlanılıyor
        #instagramweb fonksiyonunda açıklanna aynı şeyleri yapıuyor ancak youtube için ayarlanan ksımı gösteriyor
        passwidgtwdht = self.passwidget.width()
        if passwidgtwdht == 0:
            self.passwidget.setGeometry(QtCore.QRect(839, 116, 632, 788))
        else:
            pass

        self.ui.ksayol.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ui.ksayol2.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ui.ksayol2D.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ui.baslkksyol2Y.setText("Youtube")
        widht = self.ui.ksayol2Y.width()

        if widht == 0:
            self.animation = QPropertyAnimation(self.ui.ksayol2Y, b"geometry")
            self.animation.setDuration(700)
            self.animation.setStartValue(QtCore.QRect(self.ui.ksayol2Y.geometry()))
            self.animation.setEndValue(QtCore.QRect(self.ui.ksayol2Y.geometry().adjusted(0, 0, 800, 0)))
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

        else:
            self.ui.ksayol2Y.setGeometry(QtCore.QRect(39, 7, 0, 902))

    def discordweb(self):
        # Hızlı erişim kısmındaki Discord butouna tıklandıgında bağlanılıyor
        #  instagramweb fonksiyonunda açılanna aynı şeyleri yapıyor sadece whatsappa yönlendiriyor
        passwidgtwdht = self.passwidget.width()
        if passwidgtwdht == 0:
            self.passwidget.setGeometry(QtCore.QRect(839, 116, 632, 788))
        else:
            pass
        self.ui.ksayol2Y.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ui.ksayol.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ui.ksayol2.setGeometry(QtCore.QRect(39, 7, 0, 902))
        self.ui.baslkksyol2D.setText("Discord")
        #Ses kullanım request talbinde bağlanılcak fonksiyona yönlendiriyor
        self.ui.ksayolgovde2D.page().featurePermissionRequested.connect(self.onFeaturePermissionRequested)

        self.ui.ksayolgovde2D.setUrl(QUrl("https://discord.com"))
        widht = self.ui.ksayol2D.width()

        if widht == 0:
            self.animation = QPropertyAnimation(self.ui.ksayol2D, b"geometry")
            self.animation.setDuration(700)
            self.animation.setStartValue(QtCore.QRect(self.ui.ksayol2D.geometry()))
            self.animation.setEndValue(QtCore.QRect(self.ui.ksayol2D.geometry().adjusted(0, 0, 800, 0)))
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

        else:
            self.ui.ksayol2D.setGeometry(QtCore.QRect(39, 7, 0, 902))

    def onFeaturePermissionRequested(self, url, feature):
        # Hızlı erişim kısımında discord tusuna basıldıgında ses ve görüntü kullanım izni vermek için oluşturulan bir fonksiyon
        # feature discord kısmından talep edilen özellige göre(ses, görüntü veya ikiside) discord kısımı kulanılırıken oluşturulan page objesie özellikler tanımlanıyor

        if feature in (QWebEnginePage.MediaAudioCapture,
                       QWebEnginePage.MediaVideoCapture,
                       QWebEnginePage.MediaAudioVideoCapture):
            self.ui.ksayolgovde2D.page().setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)
        else:
            self.ui.ksayolgovde2D.page().setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)

    def screenshoot(self):
        # Arama widget içinde bulunan kamera butonu(screenshott butonu) kayıt edilmesi için oluşturulan fonksiyon
        # Kamera butonuna tıklandıgında öncelikle os modulu ile path yolundaki dosya kontrol ediliyor varsa geçiyor yoksa dosyayı oluşturuyor

        paths = f"C:/Users/{os.getlogin()}/Documents/ScreenShootPy"
        try:
            os.mkdir(paths)

        except:
            pass
        # Dosyanın adını aynı kaydedim üzerine yazılmasını önlemek için tarihi isme ekleniyor ve x değişkenine atanıyor
        x = f"{datetime.datetime.now().strftime('%d_%m_%y-%H_%M_%S')}"
        # Pixmap modulu p değerine atanıyor ve bulundugu sekmenin ekran görüntüsünü .grap ile hafızada tutuyor
        p = QPixmap()
        p = self.ui.tabWidget.currentWidget().grab()
        # hafızada tutulan resmi path yoluna kaydediliyor
        p.save(f"C:/Users/{os.getlogin()}/Documents/ScreenShootPy/Screenshot{x}.png", "PNG")

    def morefunction(self):
        # Hızlı erişim kısmının çok uzun olmasın diye not defteri , müzik,hesap makinesi eklentilerini gizlenmiş sekilde dururken,
        # more(üç nokta butonu) tıklandıgında bu foknksiyona yönlendiriyor
        #Tasarımda hesap makine müzik ve not defteri butonun oldugu kısmı görünür hale getirdikten
        # sonra baslangıcta yuksekligi sıfır olan morewidget(hesap makine müzik ve not defteri butonlarının bulundugu widget) animasyon ile yuksekligini genişletiyor
        #Eger yuksekligi sıfır değilse sıfıra eşitliyor ve widgetı gizliyor
        self.ui.morewidget.show()
        if self.ui.morebtn.isChecked():

            self.animation = QPropertyAnimation(self.ui.morewidget, b"geometry")
            self.animation.setDuration(700)
            self.animation.setStartValue(QtCore.QRect(self.ui.morewidget.geometry()))
            self.animation.setEndValue(QtCore.QRect(self.ui.morewidget.geometry().adjusted(0, 0, 0, 120)))
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
        else:
            self.ui.morewidget.hide()
            self.ui.morewidget.setGeometry(QtCore.QRect(0, 350, 41, 0))

    """def loadUrlMain(self):
        #
        url = self.ui.menuaramacubu.text()
        qurl = f"https://www.google.com/search?q={url}"
        self.ui.tabWidget.currentWidget().load(QUrl(qurl))
        self.ui.menuaramacubu.setText("")"""

    def on_downloadRequested(self, download):
        #indirme taleplerinin yönlendirldiği kısım
        #Bu kısımda dosyanın indirlceği kısım directory değerine atanıyor
        directory = "C:/Users/Yunn/Downloads/"
        #Bu kısımda İndirlenler sayfası için database eklenmesi için indirilen dosyanın ismini self.filename'e atananıyor
        self.filename = QtCore.QFileInfo(download.path()).fileName()
        #download talebinin indirleceği konum ve indirlen dosyanın ismi atanıyor ve indirme kabul ediliyor
        download.setPath(QtCore.QDir(directory).filePath(self.filename))
        download.accept()

        #Database bağlantısı indirilenler için olan kısma bağlanılıyor
        db = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='web',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )
        baglanti = db.cursor()
        #İndirme tarihini eklemek için tarih formatlı bir şekilde dtarih değerine atanıyor
        dtarih = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        #Execute ile database sorgusu ekleniyor commit ifadesi ile yollanıyor
        baglanti.execute(
            f"INSERT INTO download (DTarih,DName) VALUES ('{dtarih}','{self.filename}')")
        db.commit()

        #star6t dosyasında tasarlanan downlaodreq içerisindne indirlenleri ayrıntılı göstermek için altta oluşan widgetın konumu çağrılıyor
        y = self.ui.downloadreqwdgt.y()
        #Eğer konum belirtilenden farklı ise animasyonla yukarıya doğru çekiliyor
        #Değil ise eski konumuna çekiliyor
        if y == 880:
            self.ui.downloadreqwdgt.show()
            self.animation = QPropertyAnimation(self.ui.downloadreqwdgt, b"geometry")
            self.animation.setDuration(700)
            self.animation.setStartValue(QtCore.QRect(self.ui.downloadreqwdgt.geometry()))
            self.animation.setEndValue(QtCore.QRect(self.ui.downloadreqwdgt.geometry().adjusted(0, -45, 0, 0)))
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

        else:
            self.ui.downloadreqwdgt.setGeometry(QtCore.QRect(0, 835, 1431, 45))
        #İndirilen dosyanın ismini ve konumu aç, iptal ve aç foksiyonların bulundugu fonksiyon çağrılıyor
        self.Downloadconnct()

    """def hesapcontexmenu(self, point):
        self.menu.exec_(self.hesapbtn.mapToGlobal(point))"""

    def popupmicandcam(self, url, feature):
        #Bu kısımda Ses, Video gibi taleplerin izin verilip verilmemesi için bir popup tasarımı çağrıyor
        #Talebe göre bir messagebox kutusu oluşturularak kullanıcıya bir evet hayır popup ı yolluyor
        #Evet cevabı verilir ise eklenti izin veriliyor Hayır verilir ise hiç birşey yapmıyor
        if feature == QWebEnginePage.MediaAudioCapture:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Ses kullanımı izin ?.\n\t")
            msgBox.setWindowFlags(Qt.FramelessWindowHint)
            msgBox.setStyleSheet("background-color:rgb(47,47,47);border:1px solid rgb(47,47,47);border-radius:10px;")
            msgBox.setWindowIcon(QtGui.QIcon("icons/icons8-google-48.png"))
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            buttony = msgBox.button(QMessageBox.Yes)
            buttony.setText("İzin Ver")
            buttonN = msgBox.button(QMessageBox.No)
            buttonN.setText("İzin verme")
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Yes:
                self.ui.tabWidget.currentWidget().page().setFeaturePermission(url, feature,
                                                                              QWebEnginePage.PermissionGrantedByUser)
        elif feature in QWebEnginePage.MediaVideoCapture:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Video cam kullanımı izin ?.\n\t")
            msgBox.setWindowFlags(Qt.FramelessWindowHint)
            msgBox.setWindowIcon(QtGui.QIcon("icons/icons8-google-48.png"))
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            buttony = msgBox.button(QMessageBox.Yes)
            buttony.setText("İzin Ver")
            buttonN = msgBox.button(QMessageBox.No)
            buttonN.setText("İzin verme")
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Yes:
                self.ui.tabWidget.currentWidget().page().setFeaturePermission(url, feature,
                                                                              QWebEnginePage.PermissionDeniedByUser)

        elif feature in QWebEnginePage.MediaAudioVideoCapture:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Ses ve video kullanımı izin ?.\n\t")
            msgBox.setWindowFlags(Qt.FramelessWindowHint)
            msgBox.setWindowIcon(QtGui.QIcon("icons/icons8-google-48.png"))
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            buttony = msgBox.button(QMessageBox.Yes)
            buttony.setText("İzin Ver")
            buttonN = msgBox.button(QMessageBox.No)
            buttonN.setText("İzin verme")
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Yes:
                self.ui.tabWidget.currentWidget().page().setFeaturePermission(url, feature,
                                                                              QWebEnginePage.PermissionGrantedByUser)

    def Downloadconnct(self):
        #İndirmeler talebinde en son çağrılan kısım
        #star6t da olusturulan tasarım fonksiyonu buraya çağrılıyor ve görünür hale getiriliyor
        self.ui.downloadwdgts()
        self.ui.dwidgt.show()
        #Tasarımda dlbl(indirilen dosyanın gösterilece label) dosyanın adı atanıyor
        self.ui.dlbl.setText(self.filename)
        #Bu kısımda tasarımda bulunan menu tuusnua basılınca açılır menu ekleniyor ve click fonksiyonalrı yönlendiriliyor
        self.dmenu = QtWidgets.QMenu()
        self.dmenu.addAction("Aç", self.fopen)
        self.dmenu.addAction("Klasörde Göster", self.dmenushowfile)
        self.dmenu.addAction("İptal")
        self.ui.dmenubtn.setMenu(self.dmenu)

    @staticmethod
    def dmenushowfile():
        #Bu ksımda Downloadconnct kısmında oluşturulan Klasörde göster kısmına tıklandığında bağlanılıyor
        #Kullanıcının download yolu atanıyor ve os modülü ile dosya yolu açılıyor
        #Sadece klasör yolu verildiği için klasörü açıyor
        # QFileDialog.getOpenFileName(f'C:\Users\{os.getlogin()}\Downloads')
        path = f'C:/Users/{os.getlogin()}/Downloads'
        path = os.path.realpath(path)
        os.startfile(path)

    def fopen(self):
        # Bu ksımda Downloadconnct kısmında oluşturulan Aç kısmına tıklandığında bağlanılıyor
        # Kullanıcının download yolu atanıyor ve os modülü ile dosya yolu açılıyor
        # İndirilen dosyanın da adı verildiği için dosyayı başlatıyor
        path = f'C:/Users/{os.getlogin()}/Downloads/{self.filename}'
        path = os.path.realpath(path)
        os.startfile(path)

    def dwnloadwdgtclose(self):
        #Downlaodreq fonksiyonunda tasarlanan kapat butonuna tıklandığında bağlanılan foksiyon
        #Her indirme için downloadconnect kısmına bağlandıgından sağa doğru eklenen dosya isimleri ve menuleri oluyor
        #Bu menuleri for döngüsü ile kapat tusuna basıldıgında siliniyor
        # bir daha fonksiyon çağrıldıgında önceki indirmeleri gözükmesin veya iç içe geçmesin diye
        #En sonda downlaodrewdgt (indirilenler bağlanılınca altta gözüken çubuk) yüksekliği bir daha atanıyor ki görünmez hale gelsin
        for i in reversed(range(self.ui.horizontalLayout_2.count())):
            self.ui.horizontalLayout_2.itemAt(i).widget().deleteLater()
        self.ui.downloadreqwdgt.setGeometry(QtCore.QRect(0, 880, 1431, 45))

    def tumunugosterbtn(self):
        #star6t da oluşturulan downloadreq fonksiyonundaki tümünü göster butonuna tıklandıgında çağrılan foksiyon
        #Bu kısımda addtabbtn foknsiyonu çağrılarak yeni bir tab widget sekmesi ekleniyor
        #Son sekmeye geçtikten sonra indirlenleri görüntülemek için oluşturulan siteye yönlendiriliyor
        self.addtabbtn()
        count = self.ui.tabWidget.count()
        self.ui.tabWidget.setCurrentIndex(count - 1)
        self.ui.tabWidget.currentWidget().load(QUrl("http://localhost/download/download.php"))
        #Yönelendirme bittikten sonra altta gözüken downloadwdgt içinde bulunan widgetları silerek içerisini temizliyor
        for i in reversed(range(self.ui.horizontalLayout_2.count())):
            self.ui.horizontalLayout_2.itemAt(i).widget().deleteLater()
        #indirme kutusunu kapatmak için oluşturlan fonksiyon çağrılarak widget görünmez ve sıfır haline geri geliyor
        self.dwnloadwdgtclose()
        return self.aramacubuedit_2.setText("")


#Bu kısımda MainWindwo klası window objesine atarak gösteriliyor ve sistem kapatma ve aplikasyon argümanları atanıyor
try:
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec_())
    else:
        print(__name__, "hh")
except KeyboardInterrupt as e:
    print(e)
