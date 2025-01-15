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
        self.exitAction = QAction(MainWindow)
        self.exitAction.setObjectName(u"exitAction")
        icon = QIcon(QIcon.fromTheme(u"application-exit"))
        self.exitAction.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabPnl = QWidget()
        self.tabPnl.setObjectName(u"tabPnl")
        self.horizontalLayout_3 = QHBoxLayout(self.tabPnl)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.pnlLongFrame = QFrame(self.tabPnl)
        self.pnlLongFrame.setObjectName(u"pnlLongFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pnlLongFrame.sizePolicy().hasHeightForWidth())
        self.pnlLongFrame.setSizePolicy(sizePolicy)
        self.pnlLongFrame.setStyleSheet(u"background-color: rgb(46, 194, 126);")
        self.pnlLongFrame.setFrameShape(QFrame.StyledPanel)
        self.pnlLongFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.pnlLongFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.pnlLongFrame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.pnlLongFrame)

        self.pnlShortFrame = QFrame(self.tabPnl)
        self.pnlShortFrame.setObjectName(u"pnlShortFrame")
        sizePolicy.setHeightForWidth(self.pnlShortFrame.sizePolicy().hasHeightForWidth())
        self.pnlShortFrame.setSizePolicy(sizePolicy)
        self.pnlShortFrame.setStyleSheet(u"background-color: rgb(42, 42, 42);")
        self.pnlShortFrame.setFrameShape(QFrame.StyledPanel)
        self.pnlShortFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.pnlShortFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.pnlShortFrame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.pnlShortFrame)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(self.tabPnl)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.tabPnl)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.pnlLeverageSlider = QSlider(self.tabPnl)
        self.pnlLeverageSlider.setObjectName(u"pnlLeverageSlider")
        self.pnlLeverageSlider.setAcceptDrops(True)
        self.pnlLeverageSlider.setMinimum(1)
        self.pnlLeverageSlider.setMaximum(125)
        self.pnlLeverageSlider.setOrientation(Qt.Horizontal)
        self.pnlLeverageSlider.setTickPosition(QSlider.TicksAbove)
        self.pnlLeverageSlider.setTickInterval(25)

        self.horizontalLayout_2.addWidget(self.pnlLeverageSlider)

        self.label_5 = QLabel(self.tabPnl)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAcceptDrops(False)

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(self.tabPnl)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_6 = QLabel(self.tabPnl)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.pnlEntryPrice = QLineEdit(self.tabPnl)
        self.pnlEntryPrice.setObjectName(u"pnlEntryPrice")
        self.pnlEntryPrice.setAcceptDrops(True)
        self.pnlEntryPrice.setToolTipDuration(0)
        self.pnlEntryPrice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pnlEntryPrice)

        self.label_7 = QLabel(self.tabPnl)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.pnlExitPrice = QLineEdit(self.tabPnl)
        self.pnlExitPrice.setObjectName(u"pnlExitPrice")
        self.pnlExitPrice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pnlExitPrice)

        self.label_8 = QLabel(self.tabPnl)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.tabPnl)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.pnlQuantity = QLineEdit(self.tabPnl)
        self.pnlQuantity.setObjectName(u"pnlQuantity")
        self.pnlQuantity.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pnlQuantity)

        self.pnlLeverage = QLineEdit(self.tabPnl)
        self.pnlLeverage.setObjectName(u"pnlLeverage")
        self.pnlLeverage.setLayoutDirection(Qt.LeftToRight)
        self.pnlLeverage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pnlLeverage)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.line_3 = QFrame(self.tabPnl)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.pnlCalculateBtn = QPushButton(self.tabPnl)
        self.pnlCalculateBtn.setObjectName(u"pnlCalculateBtn")
        self.pnlCalculateBtn.setStyleSheet(u"background-color: rgb(229, 165, 10);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.pnlCalculateBtn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.line_4 = QFrame(self.tabPnl)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.tabPnl)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_10)

        self.line_5 = QFrame(self.tabPnl)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_5)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_11 = QLabel(self.tabPnl)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.tabPnl)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.label_13 = QLabel(self.tabPnl)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.pnlInitialMargin = QLineEdit(self.tabPnl)
        self.pnlInitialMargin.setObjectName(u"pnlInitialMargin")
        self.pnlInitialMargin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pnlInitialMargin.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.pnlInitialMargin)

        self.pnlPnl = QLineEdit(self.tabPnl)
        self.pnlPnl.setObjectName(u"pnlPnl")
        self.pnlPnl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pnlPnl.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.pnlPnl)

        self.pnlRoi = QLineEdit(self.tabPnl)
        self.pnlRoi.setObjectName(u"pnlRoi")
        self.pnlRoi.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pnlRoi.setReadOnly(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.pnlRoi)


        self.verticalLayout_5.addLayout(self.formLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.tabWidget.addTab(self.tabPnl, "")
        self.tabLiquidationPrice = QWidget()
        self.tabLiquidationPrice.setObjectName(u"tabLiquidationPrice")
        self.horizontalLayout_6 = QHBoxLayout(self.tabLiquidationPrice)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.liqLongFrame = QFrame(self.tabLiquidationPrice)
        self.liqLongFrame.setObjectName(u"liqLongFrame")
        sizePolicy.setHeightForWidth(self.liqLongFrame.sizePolicy().hasHeightForWidth())
        self.liqLongFrame.setSizePolicy(sizePolicy)
        self.liqLongFrame.setStyleSheet(u"background-color: rgb(46, 194, 126);")
        self.liqLongFrame.setFrameShape(QFrame.StyledPanel)
        self.liqLongFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.liqLongFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.liqLongFrame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)


        self.horizontalLayout_4.addWidget(self.liqLongFrame)

        self.liqShortFrame = QFrame(self.tabLiquidationPrice)
        self.liqShortFrame.setObjectName(u"liqShortFrame")
        sizePolicy.setHeightForWidth(self.liqShortFrame.sizePolicy().hasHeightForWidth())
        self.liqShortFrame.setSizePolicy(sizePolicy)
        self.liqShortFrame.setStyleSheet(u"background-color: rgb(42, 42, 42);")
        self.liqShortFrame.setFrameShape(QFrame.StyledPanel)
        self.liqShortFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.liqShortFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_14 = QLabel(self.liqShortFrame)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_14)


        self.horizontalLayout_4.addWidget(self.liqShortFrame)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.line_6 = QFrame(self.tabLiquidationPrice)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_15 = QLabel(self.tabLiquidationPrice)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_15)

        self.liqLeverageSlider = QSlider(self.tabLiquidationPrice)
        self.liqLeverageSlider.setObjectName(u"liqLeverageSlider")
        self.liqLeverageSlider.setMinimum(1)
        self.liqLeverageSlider.setMaximum(125)
        self.liqLeverageSlider.setOrientation(Qt.Horizontal)
        self.liqLeverageSlider.setTickPosition(QSlider.TicksAbove)
        self.liqLeverageSlider.setTickInterval(25)

        self.horizontalLayout_5.addWidget(self.liqLeverageSlider)

        self.label_16 = QLabel(self.tabLiquidationPrice)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_16)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.line_7 = QFrame(self.tabLiquidationPrice)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_7)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_17 = QLabel(self.tabLiquidationPrice)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_17)

        self.label_18 = QLabel(self.tabLiquidationPrice)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_18)

        self.label_19 = QLabel(self.tabLiquidationPrice)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_19)

        self.label_20 = QLabel(self.tabLiquidationPrice)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_20)

        self.liqEntryPrice = QLineEdit(self.tabLiquidationPrice)
        self.liqEntryPrice.setObjectName(u"liqEntryPrice")
        self.liqEntryPrice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.liqEntryPrice)

        self.liqQuantity = QLineEdit(self.tabLiquidationPrice)
        self.liqQuantity.setObjectName(u"liqQuantity")
        self.liqQuantity.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.liqQuantity)

        self.liqLeverage = QLineEdit(self.tabLiquidationPrice)
        self.liqLeverage.setObjectName(u"liqLeverage")
        self.liqLeverage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.liqLeverage)

        self.lilqBalance = QLineEdit(self.tabLiquidationPrice)
        self.lilqBalance.setObjectName(u"lilqBalance")
        self.lilqBalance.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lilqBalance)


        self.verticalLayout_8.addLayout(self.formLayout_3)

        self.line_8 = QFrame(self.tabLiquidationPrice)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_8)

        self.liqCalculateBtn = QPushButton(self.tabLiquidationPrice)
        self.liqCalculateBtn.setObjectName(u"liqCalculateBtn")
        self.liqCalculateBtn.setStyleSheet(u"background-color: rgb(229, 165, 10);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.liqCalculateBtn)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.line_9 = QFrame(self.tabLiquidationPrice)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_9)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_21 = QLabel(self.tabLiquidationPrice)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_21)

        self.line_10 = QFrame(self.tabLiquidationPrice)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_10)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_22 = QLabel(self.tabLiquidationPrice)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_22)

        self.liqLiquidationPrice = QLineEdit(self.tabLiquidationPrice)
        self.liqLiquidationPrice.setObjectName(u"liqLiquidationPrice")
        self.liqLiquidationPrice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.liqLiquidationPrice.setReadOnly(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.liqLiquidationPrice)


        self.verticalLayout_9.addLayout(self.formLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)

        self.tabWidget.addTab(self.tabLiquidationPrice, "")
        self.tabTargetPrice = QWidget()
        self.tabTargetPrice.setObjectName(u"tabTargetPrice")
        self.horizontalLayout_9 = QHBoxLayout(self.tabTargetPrice)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetMinimumSize)
        self.targetLongFrame = QFrame(self.tabTargetPrice)
        self.targetLongFrame.setObjectName(u"targetLongFrame")
        sizePolicy.setHeightForWidth(self.targetLongFrame.sizePolicy().hasHeightForWidth())
        self.targetLongFrame.setSizePolicy(sizePolicy)
        self.targetLongFrame.setStyleSheet(u"background-color: rgb(46, 194, 126);")
        self.targetLongFrame.setFrameShape(QFrame.StyledPanel)
        self.targetLongFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.targetLongFrame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_23 = QLabel(self.targetLongFrame)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_23)


        self.horizontalLayout_7.addWidget(self.targetLongFrame)

        self.targetShortFrame = QFrame(self.tabTargetPrice)
        self.targetShortFrame.setObjectName(u"targetShortFrame")
        sizePolicy.setHeightForWidth(self.targetShortFrame.sizePolicy().hasHeightForWidth())
        self.targetShortFrame.setSizePolicy(sizePolicy)
        self.targetShortFrame.setStyleSheet(u"background-color: rgb(42, 42, 42);")
        self.targetShortFrame.setFrameShape(QFrame.StyledPanel)
        self.targetShortFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.targetShortFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_24 = QLabel(self.targetShortFrame)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_24)


        self.horizontalLayout_7.addWidget(self.targetShortFrame)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.line_11 = QFrame(self.tabTargetPrice)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_11)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_25 = QLabel(self.tabTargetPrice)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_25)

        self.horizontalSlider = QSlider(self.tabTargetPrice)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(125)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(25)

        self.horizontalLayout_8.addWidget(self.horizontalSlider)

        self.label_26 = QLabel(self.tabTargetPrice)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_26)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.line_12 = QFrame(self.tabTargetPrice)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_12)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_27 = QLabel(self.tabTargetPrice)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_27)

        self.targetEntryPrice = QLineEdit(self.tabTargetPrice)
        self.targetEntryPrice.setObjectName(u"targetEntryPrice")
        self.targetEntryPrice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.targetEntryPrice)

        self.label_28 = QLabel(self.tabTargetPrice)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_28)

        self.targetLeverage = QLineEdit(self.tabTargetPrice)
        self.targetLeverage.setObjectName(u"targetLeverage")
        self.targetLeverage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.targetLeverage)

        self.label_29 = QLabel(self.tabTargetPrice)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_29)

        self.targetRoi = QLineEdit(self.tabTargetPrice)
        self.targetRoi.setObjectName(u"targetRoi")
        self.targetRoi.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.targetRoi)


        self.verticalLayout_10.addLayout(self.formLayout_5)

        self.line_13 = QFrame(self.tabTargetPrice)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_13)

        self.pushButton = QPushButton(self.tabTargetPrice)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(229, 165, 10);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_10.addWidget(self.pushButton)


        self.horizontalLayout_9.addLayout(self.verticalLayout_10)

        self.line_14 = QFrame(self.tabTargetPrice)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.line_14)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_30 = QLabel(self.tabTargetPrice)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_30)

        self.line_15 = QFrame(self.tabTargetPrice)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_15)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_31 = QLabel(self.tabTargetPrice)
        self.label_31.setObjectName(u"label_31")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_31)

        self.targetTargetPrice = QLineEdit(self.tabTargetPrice)
        self.targetTargetPrice.setObjectName(u"targetTargetPrice")
        self.targetTargetPrice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.targetTargetPrice)


        self.verticalLayout_14.addLayout(self.formLayout_6)


        self.horizontalLayout_9.addLayout(self.verticalLayout_14)

        self.tabWidget.addTab(self.tabTargetPrice, "")
        self.tabTpSl = QWidget()
        self.tabTpSl.setObjectName(u"tabTpSl")
        self.horizontalLayout_12 = QHBoxLayout(self.tabTpSl)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetMinimumSize)
        self.tpslLongFrame = QFrame(self.tabTpSl)
        self.tpslLongFrame.setObjectName(u"tpslLongFrame")
        sizePolicy.setHeightForWidth(self.tpslLongFrame.sizePolicy().hasHeightForWidth())
        self.tpslLongFrame.setSizePolicy(sizePolicy)
        self.tpslLongFrame.setStyleSheet(u"background-color: rgb(46, 194, 126);")
        self.tpslLongFrame.setFrameShape(QFrame.StyledPanel)
        self.tpslLongFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.tpslLongFrame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_32 = QLabel(self.tpslLongFrame)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_32)


        self.horizontalLayout_10.addWidget(self.tpslLongFrame)

        self.tpslShortFrame = QFrame(self.tabTpSl)
        self.tpslShortFrame.setObjectName(u"tpslShortFrame")
        sizePolicy.setHeightForWidth(self.tpslShortFrame.sizePolicy().hasHeightForWidth())
        self.tpslShortFrame.setSizePolicy(sizePolicy)
        self.tpslShortFrame.setStyleSheet(u"background-color: rgb(42, 42, 42);")
        self.tpslShortFrame.setFrameShape(QFrame.StyledPanel)
        self.tpslShortFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.tpslShortFrame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_33 = QLabel(self.tpslShortFrame)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_33)


        self.horizontalLayout_10.addWidget(self.tpslShortFrame)


        self.verticalLayout_15.addLayout(self.horizontalLayout_10)

        self.line_16 = QFrame(self.tabTpSl)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_16)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_34 = QLabel(self.tabTpSl)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.label_34)

        self.tpslLeverageSlider = QSlider(self.tabTpSl)
        self.tpslLeverageSlider.setObjectName(u"tpslLeverageSlider")
        self.tpslLeverageSlider.setMinimum(1)
        self.tpslLeverageSlider.setMaximum(125)
        self.tpslLeverageSlider.setOrientation(Qt.Horizontal)
        self.tpslLeverageSlider.setTickPosition(QSlider.TicksAbove)
        self.tpslLeverageSlider.setTickInterval(25)

        self.horizontalLayout_11.addWidget(self.tpslLeverageSlider)

        self.label_35 = QLabel(self.tabTpSl)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.label_35)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.line_17 = QFrame(self.tabTpSl)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_17)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_36 = QLabel(self.tabTpSl)
        self.label_36.setObjectName(u"label_36")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_36)

        self.label_37 = QLabel(self.tabTpSl)
        self.label_37.setObjectName(u"label_37")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_37)

        self.label_38 = QLabel(self.tabTpSl)
        self.label_38.setObjectName(u"label_38")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.label_38)

        self.label_39 = QLabel(self.tabTpSl)
        self.label_39.setObjectName(u"label_39")

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.label_39)

        self.tpslEntryPrice = QLineEdit(self.tabTpSl)
        self.tpslEntryPrice.setObjectName(u"tpslEntryPrice")
        self.tpslEntryPrice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.tpslEntryPrice)

        self.tpslLeverage = QLineEdit(self.tabTpSl)
        self.tpslLeverage.setObjectName(u"tpslLeverage")
        self.tpslLeverage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.tpslLeverage)

        self.tpslTakeProfit = QLineEdit(self.tabTpSl)
        self.tpslTakeProfit.setObjectName(u"tpslTakeProfit")
        self.tpslTakeProfit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.tpslTakeProfit)

        self.tpslStopLoss = QLineEdit(self.tabTpSl)
        self.tpslStopLoss.setObjectName(u"tpslStopLoss")
        self.tpslStopLoss.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.tpslStopLoss)


        self.verticalLayout_15.addLayout(self.formLayout_7)

        self.line_18 = QFrame(self.tabTpSl)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_18)

        self.tpslCalculateBtn = QPushButton(self.tabTpSl)
        self.tpslCalculateBtn.setObjectName(u"tpslCalculateBtn")
        self.tpslCalculateBtn.setStyleSheet(u"background-color: rgb(229, 165, 10);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_15.addWidget(self.tpslCalculateBtn)


        self.horizontalLayout_12.addLayout(self.verticalLayout_15)

        self.line_19 = QFrame(self.tabTpSl)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.VLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_19)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_40 = QLabel(self.tabTpSl)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_40)

        self.line_20 = QFrame(self.tabTpSl)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.line_20)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_41 = QLabel(self.tabTpSl)
        self.label_41.setObjectName(u"label_41")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_41)

        self.tpslTakeProfitPrice = QLineEdit(self.tabTpSl)
        self.tpslTakeProfitPrice.setObjectName(u"tpslTakeProfitPrice")
        self.tpslTakeProfitPrice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tpslTakeProfitPrice.setReadOnly(True)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.tpslTakeProfitPrice)

        self.label_42 = QLabel(self.tabTpSl)
        self.label_42.setObjectName(u"label_42")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_42)

        self.tpslStopLossPrice = QLineEdit(self.tabTpSl)
        self.tpslStopLossPrice.setObjectName(u"tpslStopLossPrice")
        self.tpslStopLossPrice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tpslStopLossPrice.setReadOnly(True)

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.tpslStopLossPrice)


        self.verticalLayout_18.addLayout(self.formLayout_8)


        self.horizontalLayout_12.addLayout(self.verticalLayout_18)

        self.tabWidget.addTab(self.tabTpSl, "")

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
        self.menuFile.addAction(self.exitAction)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Futures Calculator", None))
        self.exitAction.setText(QCoreApplication.translate("MainWindow", u"Exit                             Ctrl+Q", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Short", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPnl), QCoreApplication.translate("MainWindow", u"PNL", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"125", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Entry Price", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Quantity (USDT)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Leverage", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Balance (USDT)", None))
        self.liqLeverage.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.liqCalculateBtn.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Liquidation Price", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLiquidationPrice), QCoreApplication.translate("MainWindow", u"Liquidation Price", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"125", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Entry Price", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Leverage", None))
        self.targetLeverage.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"ROI (%)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Target Price", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTargetPrice), QCoreApplication.translate("MainWindow", u"Target Price", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"125", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Entry Price", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Leverage", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Take Profit (%)", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Stop Loss (%)", None))
        self.tpslLeverage.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.tpslCalculateBtn.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Take Profit Price", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Stop Loss Price", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTpSl), QCoreApplication.translate("MainWindow", u"Take Profit / Stop Loss", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

