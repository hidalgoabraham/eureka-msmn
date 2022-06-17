# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_linea.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 370)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(341, 370))
        MainWindow.setMaximumSize(QtCore.QSize(341, 370))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("minilogo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(" background-color: rgb(49, 58, 67);")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gpbx_linea = QtWidgets.QGroupBox(self.centralwidget)
        self.gpbx_linea.setGeometry(QtCore.QRect(10, 10, 321, 331))
        self.gpbx_linea.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(49, 58, 67);\n"
"    border: 2px solid;\n"
"    border-color:rgb(85,170,255);\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QGroupBox::title {\n"
"color:rgb(238, 238, 238);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.gpbx_linea.setObjectName("gpbx_linea")
        self.pbtn_ok = QtWidgets.QPushButton(self.gpbx_linea)
        self.pbtn_ok.setGeometry(QtCore.QRect(220, 290, 84, 25))
        self.pbtn_ok.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(238, 238, 238);\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    color:rgb(238, 238, 238);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85,170,255);\n"
"    color:black;\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.pbtn_ok.setObjectName("pbtn_ok")
        self.lbl_modolinea = QtWidgets.QLabel(self.gpbx_linea)
        self.lbl_modolinea.setGeometry(QtCore.QRect(30, 70, 41, 20))
        self.lbl_modolinea.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.lbl_modolinea.setObjectName("lbl_modolinea")
        self.lbl_perdidaslinea = QtWidgets.QLabel(self.gpbx_linea)
        self.lbl_perdidaslinea.setGeometry(QtCore.QRect(65, 40, 61, 20))
        self.lbl_perdidaslinea.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.lbl_perdidaslinea.setObjectName("lbl_perdidaslinea")
        self.cbx_perdidaslinea = QtWidgets.QComboBox(self.gpbx_linea)
        self.cbx_perdidaslinea.setGeometry(QtCore.QRect(124, 40, 141, 20))
        self.cbx_perdidaslinea.setStyleSheet("QComboBox {\n"
"    border:1px solid rgb(0, 0, 0);\n"
"       border-radius: 10px;\n"
"    color:rgb(238, 238, 238);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(49, 58, 67);\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QComboBox::drop-down {    \n"
"    border-left-width: 0px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"    width:0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(85,170,255);\n"
"    selection-color: black;\n"
"    color: rgb(238, 238, 238);\n"
"    background-color: rgb(79, 93, 108);\n"
"}")
        self.cbx_perdidaslinea.setObjectName("cbx_perdidaslinea")
        self.cbx_perdidaslinea.addItem("")
        self.cbx_perdidaslinea.addItem("")
        self.cbx_modolinea = QtWidgets.QComboBox(self.gpbx_linea)
        self.cbx_modolinea.setGeometry(QtCore.QRect(75, 70, 191, 20))
        self.cbx_modolinea.setStyleSheet("QComboBox {\n"
"    border:1px solid rgb(0, 0, 0);\n"
"       border-radius: 10px;\n"
"    color:rgb(238, 238, 238);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(49, 58, 67);\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QComboBox::drop-down {    \n"
"    border-left-width: 0px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"    width:0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(85,170,255);\n"
"    selection-color: black;\n"
"    color: rgb(238, 238, 238);\n"
"    background-color: rgb(79, 93, 108);\n"
"}")
        self.cbx_modolinea.setObjectName("cbx_modolinea")
        self.cbx_modolinea.addItem("")
        self.cbx_modolinea.addItem("")
        self.gpbx_parametroslinea = QtWidgets.QGroupBox(self.gpbx_linea)
        self.gpbx_parametroslinea.setGeometry(QtCore.QRect(55, 90, 211, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpbx_parametroslinea.sizePolicy().hasHeightForWidth())
        self.gpbx_parametroslinea.setSizePolicy(sizePolicy)
        self.gpbx_parametroslinea.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(49, 58, 67);\n"
"    border: 0px solid;\n"
"    border-color:rgb(85,170,255);\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QGroupBox::title {\n"
"color:rgb(238, 238, 238);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.gpbx_parametroslinea.setTitle("")
        self.gpbx_parametroslinea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gpbx_parametroslinea.setObjectName("gpbx_parametroslinea")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gpbx_parametroslinea)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scllarea_parametroslinea = QtWidgets.QScrollArea(self.gpbx_parametroslinea)
        self.scllarea_parametroslinea.setStyleSheet("QScrollBar:horizontal {\n"
"   /* border: 2px solid black;*/\n"
"    background: rgb(49, 58, 67);\n"
"    height: 5px;\n"
"    margin: 0px 20px 0 20px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85,170,255);\n"
"    min-width: 10px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px black;\n"
"    background: black;\n"
"    width: 0px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 1px black;\n"
"    background: black;\n"
"    width: 0px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: rgb(79, 93, 108);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal {\n"
"    background: rgb(79, 93, 108);\n"
"}")
        self.scllarea_parametroslinea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scllarea_parametroslinea.setWidgetResizable(True)
        self.scllarea_parametroslinea.setObjectName("scllarea_parametroslinea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 193, 130))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.layout_parametroslinea = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.layout_parametroslinea.setObjectName("layout_parametroslinea")
        self.lbl_Ro = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.lbl_Ro.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_Ro.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Ro.setObjectName("lbl_Ro")
        self.layout_parametroslinea.addWidget(self.lbl_Ro, 0, 0, 1, 1)
        self.linedit_Ro = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linedit_Ro.sizePolicy().hasHeightForWidth())
        self.linedit_Ro.setSizePolicy(sizePolicy)
        self.linedit_Ro.setStyleSheet("QLineEdit{\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-color: rgb(49, 58, 67);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid rgb(85,170,255);\n"
"background-color:rgb(79, 93, 108);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 1px solid rgb(85,170,255);\n"
"background-color:rgb(79, 93, 108);\n"
"}\n"
"")
        self.linedit_Ro.setObjectName("linedit_Ro")
        self.layout_parametroslinea.addWidget(self.linedit_Ro, 0, 1, 1, 1)
        self.lbl_coero = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.lbl_coero.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_coero.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_coero.setObjectName("lbl_coero")
        self.layout_parametroslinea.addWidget(self.lbl_coero, 1, 0, 1, 1)
        self.linedit_coero = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linedit_coero.sizePolicy().hasHeightForWidth())
        self.linedit_coero.setSizePolicy(sizePolicy)
        self.linedit_coero.setStyleSheet("QLineEdit{\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-color: rgb(49, 58, 67);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid rgb(85,170,255);\n"
"background-color:rgb(79, 93, 108);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 1px solid rgb(85,170,255);\n"
"background-color:rgb(79, 93, 108);\n"
"}\n"
"")
        self.linedit_coero.setObjectName("linedit_coero")
        self.layout_parametroslinea.addWidget(self.linedit_coero, 1, 1, 1, 1)
        self.scllarea_parametroslinea.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_5.addWidget(self.scllarea_parametroslinea, 0, 0, 1, 1)
        self.cbx_tipocoero = QtWidgets.QComboBox(self.gpbx_linea)
        self.cbx_tipocoero.setGeometry(QtCore.QRect(65, 70, 201, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_tipocoero.sizePolicy().hasHeightForWidth())
        self.cbx_tipocoero.setSizePolicy(sizePolicy)
        self.cbx_tipocoero.setMinimumSize(QtCore.QSize(201, 0))
        self.cbx_tipocoero.setMaximumSize(QtCore.QSize(201, 16777215))
        self.cbx_tipocoero.setStyleSheet("QComboBox {\n"
"    border:1px solid rgb(0, 0, 0);\n"
"       border-radius: 10px;\n"
"    color:rgb(238, 238, 238);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(49, 58, 67);\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QComboBox::drop-down {    \n"
"    border-left-width: 0px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"    width:0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(85,170,255);\n"
"    selection-color: black;\n"
"    color: rgb(238, 238, 238);\n"
"    background-color: rgb(79, 93, 108);\n"
"}")
        self.cbx_tipocoero.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cbx_tipocoero.setObjectName("cbx_tipocoero")
        self.cbx_tipocoero.addItem("")
        self.cbx_tipocoero.addItem("")
        self.cbx_tipocoero.addItem("")
        self.linedit_DCA = QtWidgets.QLineEdit(self.gpbx_linea)
        self.linedit_DCA.setEnabled(True)
        self.linedit_DCA.setGeometry(QtCore.QRect(55, 260, 91, 20))
        self.linedit_DCA.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.linedit_DCA.setStyleSheet("QLineEdit{\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-color: rgb(49, 58, 67);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid rgb(85,170,255);\n"
"background-color:rgb(79, 93, 108);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 1px solid rgb(85,170,255);\n"
"background-color:rgb(79, 93, 108);\n"
"}\n"
"")
        self.linedit_DCA.setObjectName("linedit_DCA")
        self.lbl_DGA = QtWidgets.QLabel(self.gpbx_linea)
        self.lbl_DGA.setGeometry(QtCore.QRect(20, 230, 31, 20))
        self.lbl_DGA.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_DGA.setObjectName("lbl_DGA")
        self.cbx_DGA = QtWidgets.QComboBox(self.gpbx_linea)
        self.cbx_DGA.setGeometry(QtCore.QRect(150, 230, 35, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_DGA.sizePolicy().hasHeightForWidth())
        self.cbx_DGA.setSizePolicy(sizePolicy)
        self.cbx_DGA.setMinimumSize(QtCore.QSize(30, 0))
        self.cbx_DGA.setMaximumSize(QtCore.QSize(81, 20))
        self.cbx_DGA.setStyleSheet("QComboBox {\n"
"    border:1px solid rgb(0, 0, 0);\n"
"       border-radius: 10px;\n"
"    color:rgb(238, 238, 238);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(49, 58, 67);\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QComboBox::drop-down {    \n"
"    border-left-width: 0px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"    width:0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(85,170,255);\n"
"    selection-color: black;\n"
"    color: rgb(238, 238, 238);\n"
"    background-color: rgb(79, 93, 108);\n"
"}")
        self.cbx_DGA.setIconSize(QtCore.QSize(0, 0))
        self.cbx_DGA.setObjectName("cbx_DGA")
        self.cbx_DGA.addItem("")
        self.cbx_DGA.addItem("")
        self.cbx_DGA.addItem("")
        self.linedit_DGA = QtWidgets.QLineEdit(self.gpbx_linea)
        self.linedit_DGA.setGeometry(QtCore.QRect(55, 230, 91, 20))
        self.linedit_DGA.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.linedit_DGA.setStyleSheet("QLineEdit{\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-color: rgb(49, 58, 67);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid rgb(85,170,255);\n"
"background-color:rgb(79, 93, 108);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 1px solid rgb(85,170,255);\n"
"background-color:rgb(79, 93, 108);\n"
"}\n"
"")
        self.linedit_DGA.setObjectName("linedit_DGA")
        self.cbx_Pmax = QtWidgets.QComboBox(self.gpbx_linea)
        self.cbx_Pmax.setGeometry(QtCore.QRect(150, 290, 40, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_Pmax.sizePolicy().hasHeightForWidth())
        self.cbx_Pmax.setSizePolicy(sizePolicy)
        self.cbx_Pmax.setMinimumSize(QtCore.QSize(30, 0))
        self.cbx_Pmax.setMaximumSize(QtCore.QSize(81, 20))
        self.cbx_Pmax.setStyleSheet("QComboBox {\n"
"    border:1px solid rgb(0, 0, 0);\n"
"       border-radius: 10px;\n"
"    color:rgb(238, 238, 238);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(49, 58, 67);\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QComboBox::drop-down {    \n"
"    border-left-width: 0px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"    width:0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(85,170,255);\n"
"    selection-color: black;\n"
"    color: rgb(238, 238, 238);\n"
"    background-color: rgb(79, 93, 108);\n"
"}")
        self.cbx_Pmax.setIconSize(QtCore.QSize(0, 0))
        self.cbx_Pmax.setObjectName("cbx_Pmax")
        self.cbx_Pmax.addItem("")
        self.cbx_Pmax.addItem("")
        self.cbx_Pmax.addItem("")
        self.lbl_Pmax = QtWidgets.QLabel(self.gpbx_linea)
        self.lbl_Pmax.setGeometry(QtCore.QRect(15, 290, 41, 20))
        self.lbl_Pmax.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_Pmax.setObjectName("lbl_Pmax")
        self.linedit_Pmax = QtWidgets.QLineEdit(self.gpbx_linea)
        self.linedit_Pmax.setGeometry(QtCore.QRect(55, 290, 91, 20))
        self.linedit_Pmax.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.linedit_Pmax.setStyleSheet("QLineEdit{\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-color: rgb(49, 58, 67);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid rgb(85,170,255);\n"
"background-color:rgb(79, 93, 108);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 1px solid rgb(85,170,255);\n"
"background-color:rgb(79, 93, 108);\n"
"}\n"
"")
        self.linedit_Pmax.setObjectName("linedit_Pmax")
        self.cbx_DCA = QtWidgets.QComboBox(self.gpbx_linea)
        self.cbx_DCA.setEnabled(True)
        self.cbx_DCA.setGeometry(QtCore.QRect(150, 260, 35, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_DCA.sizePolicy().hasHeightForWidth())
        self.cbx_DCA.setSizePolicy(sizePolicy)
        self.cbx_DCA.setMinimumSize(QtCore.QSize(30, 0))
        self.cbx_DCA.setMaximumSize(QtCore.QSize(81, 20))
        self.cbx_DCA.setStyleSheet("QComboBox {\n"
"    border:1px solid rgb(0, 0, 0);\n"
"       border-radius: 10px;\n"
"    color:rgb(238, 238, 238);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(49, 58, 67);\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QComboBox::drop-down {    \n"
"    border-left-width: 0px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"    width:0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(85,170,255);\n"
"    selection-color: black;\n"
"    color: rgb(238, 238, 238);\n"
"    background-color: rgb(79, 93, 108);\n"
"}")
        self.cbx_DCA.setIconSize(QtCore.QSize(0, 0))
        self.cbx_DCA.setObjectName("cbx_DCA")
        self.cbx_DCA.addItem("")
        self.cbx_DCA.addItem("")
        self.cbx_DCA.addItem("")
        self.lbl_DCA = QtWidgets.QLabel(self.gpbx_linea)
        self.lbl_DCA.setGeometry(QtCore.QRect(20, 260, 31, 20))
        self.lbl_DCA.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_DCA.setObjectName("lbl_DCA")
        self.cbx_modolinea.raise_()
        self.gpbx_parametroslinea.raise_()
        self.pbtn_ok.raise_()
        self.lbl_perdidaslinea.raise_()
        self.cbx_perdidaslinea.raise_()
        self.lbl_modolinea.raise_()
        self.linedit_DCA.raise_()
        self.lbl_DGA.raise_()
        self.cbx_DGA.raise_()
        self.linedit_DGA.raise_()
        self.cbx_Pmax.raise_()
        self.lbl_Pmax.raise_()
        self.linedit_Pmax.raise_()
        self.cbx_DCA.raise_()
        self.lbl_DCA.raise_()
        self.cbx_tipocoero.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 341, 22))
        self.menuBar.setStyleSheet("QMenuBar {\n"
"    background-color:(49, 58, 67);\n"
"    spacing: 3px; /* spacing between menu bar items */\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    color:rgb(238, 238, 238);\n"
"    padding: 1px 4px;\n"
"    background: transparent;\n"
"    border: 2px solid rgb(238, 238, 238);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"    background: transparent;\n"
"    border: 2px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    color: black;\n"
"    background-color:rgb(85,170,255);\n"
"}")
        self.menuBar.setObjectName("menuBar")
        self.menuProyecto = QtWidgets.QMenu(self.menuBar)
        self.menuProyecto.setStyleSheet("QMenu::item {\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    color:rgb(238, 238, 238);\n"
"    background-color:rgb(79, 93, 108);\n"
"}\n"
"\n"
"QMenu::item:selected { /* when selected using mouse or keyboard */\n"
"    /*background:rgb(28, 33, 39);*/\n"
"    border: 1px solid rgb(85,170,255);\n"
"}\n"
"\n"
"QMenu::item:pressed {\n"
"    background-color:rgb(85,170,255);\n"
"    color:black;\n"
"}")
        self.menuProyecto.setObjectName("menuProyecto")
        MainWindow.setMenuBar(self.menuBar)
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionReiniciar = QtWidgets.QAction(MainWindow)
        self.actionReiniciar.setObjectName("actionReiniciar")
        self.actionManual_de_usuario = QtWidgets.QAction(MainWindow)
        self.actionManual_de_usuario.setObjectName("actionManual_de_usuario")
        self.actionArchivo_load = QtWidgets.QAction(MainWindow)
        self.actionArchivo_load.setObjectName("actionArchivo_load")
        self.actionArchivo_imp = QtWidgets.QAction(MainWindow)
        self.actionArchivo_imp.setObjectName("actionArchivo_imp")
        self.actionCargar = QtWidgets.QAction(MainWindow)
        self.actionCargar.setObjectName("actionCargar")
        self.menuProyecto.addAction(self.actionCargar)
        self.menuProyecto.addAction(self.actionGuardar)
        self.menuProyecto.addAction(self.actionReiniciar)
        self.menuBar.addAction(self.menuProyecto.menuAction())

        self.retranslateUi(MainWindow)
        self.cbx_DGA.setCurrentIndex(2)
        self.cbx_Pmax.setCurrentIndex(1)
        self.cbx_DCA.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Línea de transmisión"))
        self.gpbx_linea.setTitle(_translate("MainWindow", "Parámetros de línea de transmisión"))
        self.pbtn_ok.setText(_translate("MainWindow", "Ok"))
        self.lbl_modolinea.setText(_translate("MainWindow", " Modo:"))
        self.lbl_perdidaslinea.setText(_translate("MainWindow", "Pérdidas:"))
        self.cbx_perdidaslinea.setItemText(0, _translate("MainWindow", "Sin pérdidas"))
        self.cbx_perdidaslinea.setItemText(1, _translate("MainWindow", "Pérdidas generales"))
        self.cbx_modolinea.setItemText(0, _translate("MainWindow", "Parámetros rlgc"))
        self.cbx_modolinea.setItemText(1, _translate("MainWindow", "Tipo de línea de transmisión"))
        self.lbl_Ro.setToolTip(_translate("MainWindow", "<html><head/><body><p>Resistencia característica de la línea de transmisión.</p></body></html>"))
        self.lbl_Ro.setText(_translate("MainWindow", "Ro (Ω):"))
        self.lbl_coero.setToolTip(_translate("MainWindow", "<html><head/><body><p>Capacitancia distribuida de la línea de transmisión.</p></body></html>"))
        self.lbl_coero.setText(_translate("MainWindow", "c (pF/m):"))
        self.cbx_tipocoero.setItemText(0, _translate("MainWindow", "Capacitancia distribuida (pF/m)"))
        self.cbx_tipocoero.setItemText(1, _translate("MainWindow", "Constante dieléctrica relativa"))
        self.cbx_tipocoero.setItemText(2, _translate("MainWindow", "Velocidad de propagación (%)"))
        self.lbl_DGA.setToolTip(_translate("MainWindow", "<html><head/><body><p>Distancia entre el generador y el adaptador MSMN.</p></body></html>"))
        self.lbl_DGA.setText(_translate("MainWindow", "DGA:"))
        self.cbx_DGA.setItemText(0, _translate("MainWindow", "m"))
        self.cbx_DGA.setItemText(1, _translate("MainWindow", "cm"))
        self.cbx_DGA.setItemText(2, _translate("MainWindow", "mm"))
        self.cbx_Pmax.setItemText(0, _translate("MainWindow", "kW"))
        self.cbx_Pmax.setItemText(1, _translate("MainWindow", "W"))
        self.cbx_Pmax.setItemText(2, _translate("MainWindow", "mW"))
        self.lbl_Pmax.setToolTip(_translate("MainWindow", "<html><head/><body><p>Máxima potencia promedio soportada por la línea de transmisión.</p></body></html>"))
        self.lbl_Pmax.setText(_translate("MainWindow", "Pmax:"))
        self.cbx_DCA.setItemText(0, _translate("MainWindow", "m"))
        self.cbx_DCA.setItemText(1, _translate("MainWindow", "cm"))
        self.cbx_DCA.setItemText(2, _translate("MainWindow", "mm"))
        self.lbl_DCA.setToolTip(_translate("MainWindow", "<html><head/><body><p>Distancia entre la impedancia de carga y el adaptador MSMN.</p></body></html>"))
        self.lbl_DCA.setText(_translate("MainWindow", "DCA:"))
        self.menuProyecto.setTitle(_translate("MainWindow", "Archivo"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionReiniciar.setText(_translate("MainWindow", "Reiniciar"))
        self.actionManual_de_usuario.setText(_translate("MainWindow", "Manual de usuario"))
        self.actionArchivo_load.setText(_translate("MainWindow", "archivo .load"))
        self.actionArchivo_imp.setText(_translate("MainWindow", "archivo .imp"))
        self.actionCargar.setText(_translate("MainWindow", "Cargar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

