# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon = QIcon(QIcon.fromTheme(u"application-exit"))
        self.actionExit.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.pnlLongFrame = QFrame(self.tab)
        self.pnlLongFrame.setObjectName(u"pnlLongFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pnlLongFrame.sizePolicy().hasHeightForWidth())
        self.pnlLongFrame.setSizePolicy(sizePolicy)
        self.pnlLongFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.pnlLongFrame.setStyleSheet(u"background-color: rgb(46, 194, 126);")
        self.pnlLongFrame.setFrameShape(QFrame.StyledPanel)
        self.pnlLongFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.pnlLongFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.pnlLongFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.pnlLongFrame)

        self.pnlShortFrame = QFrame(self.tab)
        self.pnlShortFrame.setObjectName(u"pnlShortFrame")
        sizePolicy.setHeightForWidth(self.pnlShortFrame.sizePolicy().hasHeightForWidth())
        self.pnlShortFrame.setSizePolicy(sizePolicy)
        self.pnlShortFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.pnlShortFrame.setFrameShape(QFrame.StyledPanel)
        self.pnlShortFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.pnlShortFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.pnlShortFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.pnlShortFrame)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.pnlLeverageSlider = QSlider(self.tab)
        self.pnlLeverageSlider.setObjectName(u"pnlLeverageSlider")
        self.pnlLeverageSlider.setAcceptDrops(True)
        self.pnlLeverageSlider.setMinimum(1)
        self.pnlLeverageSlider.setMaximum(125)
        self.pnlLeverageSlider.setOrientation(Qt.Horizontal)
        self.pnlLeverageSlider.setTickPosition(QSlider.TicksAbove)
        self.pnlLeverageSlider.setTickInterval(25)

        self.horizontalLayout_2.addWidget(self.pnlLeverageSlider)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAcceptDrops(False)

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.pnlEntryPrice = QLineEdit(self.tab)
        self.pnlEntryPrice.setObjectName(u"pnlEntryPrice")
        self.pnlEntryPrice.setAcceptDrops(True)
        self.pnlEntryPrice.setToolTipDuration(0)
        self.pnlEntryPrice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pnlEntryPrice)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.pnlExitPrice = QLineEdit(self.tab)
        self.pnlExitPrice.setObjectName(u"pnlExitPrice")
        self.pnlExitPrice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pnlExitPrice)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.pnlQuantity = QLineEdit(self.tab)
        self.pnlQuantity.setObjectName(u"pnlQuantity")
        self.pnlQuantity.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pnlQuantity)

        self.pnlLeverage = QLineEdit(self.tab)
        self.pnlLeverage.setObjectName(u"pnlLeverage")
        self.pnlLeverage.setLayoutDirection(Qt.LeftToRight)
        self.pnlLeverage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pnlLeverage)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.pnlCalculateBtn = QPushButton(self.tab)
        self.pnlCalculateBtn.setObjectName(u"pnlCalculateBtn")
        self.pnlCalculateBtn.setStyleSheet(u"background-color: rgb(229, 165, 10);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.pnlCalculateBtn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.line_4 = QFrame(self.tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_10)

        self.line_5 = QFrame(self.tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_5)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.pnlInitialMargin = QLineEdit(self.tab)
        self.pnlInitialMargin.setObjectName(u"pnlInitialMargin")
        self.pnlInitialMargin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pnlInitialMargin.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.pnlInitialMargin)

        self.pnlPnl = QLineEdit(self.tab)
        self.pnlPnl.setObjectName(u"pnlPnl")
        self.pnlPnl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pnlPnl.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.pnlPnl)

        self.pnlRoi = QLineEdit(self.tab)
        self.pnlRoi.setObjectName(u"pnlRoi")
        self.pnlRoi.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pnlRoi.setReadOnly(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.pnlRoi)


        self.verticalLayout_5.addLayout(self.formLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Futures Calculator", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit                             Ctrl+Q", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Short", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"125", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Entry Price", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Exit Price", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Quantity (USDT)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Leverage", None))
        self.pnlLeverage.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pnlCalculateBtn.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Initial Margin", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"PNL", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ROI", None))
        self.pnlInitialMargin.setText("")
        self.pnlPnl.setText("")
        self.pnlRoi.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"PNL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Liquidation Price", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Target Price", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Take Profit / Stop Loss", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

