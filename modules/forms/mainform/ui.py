# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created: Sat Jun 14 20:21:53 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 543)
        Form.setMaximumSize(QtCore.QSize(850, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 215, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 215, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 215, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 215, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Icons/music.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_5 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(242, 240))
        self.tabWidget.setMaximumSize(QtCore.QSize(242, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.userTab = QtGui.QWidget()
        self.userTab.setObjectName("userTab")
        self.verticalLayout = QtGui.QVBoxLayout(self.userTab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.userList = QtGui.QListWidget(self.userTab)
        self.userList.setFrameShape(QtGui.QFrame.NoFrame)
        self.userList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.userList.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.userList.setIconSize(QtCore.QSize(50, 50))
        self.userList.setTextElideMode(QtCore.Qt.ElideLeft)
        self.userList.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.userList.setObjectName("userList")
        self.verticalLayout.addWidget(self.userList)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Icons/meicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.userTab, icon1, "")
        self.friendsTab = QtGui.QWidget()
        self.friendsTab.setObjectName("friendsTab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.friendsTab)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 6, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.friendsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(31, 31))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Icons/findicon.ico"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.friendsTab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.friendsSearchEdit = QtGui.QLineEdit(self.friendsTab)
        self.friendsSearchEdit.setObjectName("friendsSearchEdit")
        self.horizontalLayout.addWidget(self.friendsSearchEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.friendsLoadPBar = QtGui.QProgressBar(self.friendsTab)
        self.friendsLoadPBar.setMaximumSize(QtCore.QSize(5, 16777215))
        self.friendsLoadPBar.setAutoFillBackground(False)
        self.friendsLoadPBar.setStyleSheet("QProgressBar {\n"
"text-align: top;\n"
"padding: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"background: rgb(255, 255, 255)\n"
"}\n"
"QProgressBar::chunk {\n"
"background: rgb(193, 196, 255);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"")
        self.friendsLoadPBar.setProperty("value", 0)
        self.friendsLoadPBar.setTextVisible(False)
        self.friendsLoadPBar.setOrientation(QtCore.Qt.Vertical)
        self.friendsLoadPBar.setInvertedAppearance(True)
        self.friendsLoadPBar.setObjectName("friendsLoadPBar")
        self.horizontalLayout_2.addWidget(self.friendsLoadPBar)
        self.friendsList = QtGui.QListWidget(self.friendsTab)
        self.friendsList.setFrameShape(QtGui.QFrame.NoFrame)
        self.friendsList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.friendsList.setIconSize(QtCore.QSize(50, 50))
        self.friendsList.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.friendsList.setObjectName("friendsList")
        self.horizontalLayout_2.addWidget(self.friendsList)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Icons/friendsicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.friendsTab, icon2, "")
        self.groupsTab = QtGui.QWidget()
        self.groupsTab.setObjectName("groupsTab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupsTab)
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 6, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtGui.QLabel(self.groupsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(31, 31))
        self.label_2.setBaseSize(QtCore.QSize(0, 0))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/Icons/findicon.ico"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(self.groupsTab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.groupsSearchEdit = QtGui.QLineEdit(self.groupsTab)
        self.groupsSearchEdit.setObjectName("groupsSearchEdit")
        self.horizontalLayout_4.addWidget(self.groupsSearchEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupsLoadPBar = QtGui.QProgressBar(self.groupsTab)
        self.groupsLoadPBar.setMaximumSize(QtCore.QSize(5, 16777215))
        self.groupsLoadPBar.setAutoFillBackground(False)
        self.groupsLoadPBar.setStyleSheet("QProgressBar {\n"
"text-align: top;\n"
"padding: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"background: rgb(255, 255, 255)\n"
"}\n"
"QProgressBar::chunk {\n"
"background: rgb(193, 196, 255);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"")
        self.groupsLoadPBar.setProperty("value", 0)
        self.groupsLoadPBar.setTextVisible(False)
        self.groupsLoadPBar.setOrientation(QtCore.Qt.Vertical)
        self.groupsLoadPBar.setInvertedAppearance(True)
        self.groupsLoadPBar.setObjectName("groupsLoadPBar")
        self.horizontalLayout_3.addWidget(self.groupsLoadPBar)
        self.groupsList = QtGui.QListWidget(self.groupsTab)
        self.groupsList.setFrameShape(QtGui.QFrame.NoFrame)
        self.groupsList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.groupsList.setIconSize(QtCore.QSize(50, 50))
        self.groupsList.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.groupsList.setViewMode(QtGui.QListView.ListMode)
        self.groupsList.setObjectName("groupsList")
        self.horizontalLayout_3.addWidget(self.groupsList)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Icons/neticon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.groupsTab, icon3, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.countLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.countLabel.setFont(font)
        self.countLabel.setObjectName("countLabel")
        self.horizontalLayout_6.addWidget(self.countLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.audioList = QtGui.QListWidget(Form)
        self.audioList.setMinimumSize(QtCore.QSize(350, 0))
        self.audioList.setMaximumSize(QtCore.QSize(550, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(236, 238, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 238, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 215, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.audioList.setPalette(palette)
        self.audioList.setObjectName("audioList")
        self.verticalLayout_4.addWidget(self.audioList)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.downloadButton = QtGui.QPushButton(Form)
        self.downloadButton.setCheckable(False)
        self.downloadButton.setObjectName("downloadButton")
        self.horizontalLayout_7.addWidget(self.downloadButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setMaximumSize(QtCore.QSize(25, 25))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/Icons/helpicon.ico"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.volumeSlider = phonon.Phonon.VolumeSlider(Form)
        self.volumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.volumeSlider.setTracking(True)
        self.volumeSlider.setMuteVisible(True)
        self.volumeSlider.setIconSize(QtCore.QSize(16, 16))
        self.volumeSlider.setObjectName("volumeSlider")
        self.verticalLayout_5.addWidget(self.volumeSlider)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.userTab), QtGui.QApplication.translate("Form", "Я", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Поиск:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.friendsTab), QtGui.QApplication.translate("Form", "Друзья", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Поиск:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.groupsTab), QtGui.QApplication.translate("Form", "Сообщества", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Музыка", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Аудиозаписей: ", None, QtGui.QApplication.UnicodeUTF8))
        self.countLabel.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadButton.setText(QtGui.QApplication.translate("Form", "Ожидают загрузки: 0 ", None, QtGui.QApplication.UnicodeUTF8))

from PySide import phonon
import resourses.resourses_rc