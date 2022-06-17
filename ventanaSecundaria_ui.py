# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaSecundaria.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1006, 690)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1006, 690))
        Dialog.setMaximumSize(QtCore.QSize(1006, 690))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("minilogo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(" background-color: rgb(49, 58, 67);")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.scllarea_master = QtWidgets.QScrollArea(Dialog)
        self.scllarea_master.setGeometry(QtCore.QRect(0, 0, 1006, 690))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scllarea_master.sizePolicy().hasHeightForWidth())
        self.scllarea_master.setSizePolicy(sizePolicy)
        self.scllarea_master.setMinimumSize(QtCore.QSize(1006, 690))
        self.scllarea_master.setMaximumSize(QtCore.QSize(1006, 690))
        self.scllarea_master.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scllarea_master.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scllarea_master.setLineWidth(0)
        self.scllarea_master.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scllarea_master.setWidgetResizable(True)
        self.scllarea_master.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scllarea_master.setObjectName("scllarea_master")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 1006, 690))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_7.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_7.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_7.setMinimumSize(QtCore.QSize(1006, 690))
        self.scrollAreaWidgetContents_7.setMaximumSize(QtCore.QSize(1006, 690))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.layout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_7)
        self.layout_2.setContentsMargins(2, 2, 0, 0)
        self.layout_2.setObjectName("layout_2")
        self.gpbx_master = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpbx_master.sizePolicy().hasHeightForWidth())
        self.gpbx_master.setSizePolicy(sizePolicy)
        self.gpbx_master.setMinimumSize(QtCore.QSize(1006, 690))
        self.gpbx_master.setMaximumSize(QtCore.QSize(1006, 690))
        self.gpbx_master.setAutoFillBackground(False)
        self.gpbx_master.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(49, 58, 67);\n"
"    border: 0px solid;\n"
"    border-color:rgb(85,170,255);\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}")
        self.gpbx_master.setTitle("")
        self.gpbx_master.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gpbx_master.setFlat(True)
        self.gpbx_master.setObjectName("gpbx_master")
        self.gpbx_stubs = QtWidgets.QGroupBox(self.gpbx_master)
        self.gpbx_stubs.setGeometry(QtCore.QRect(600, 140, 391, 491))
        self.gpbx_stubs.setStyleSheet("QGroupBox {\n"
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
"}\n"
"")
        self.gpbx_stubs.setObjectName("gpbx_stubs")
        self.spnbx_parametrosstubs = QtWidgets.QSpinBox(self.gpbx_stubs)
        self.spnbx_parametrosstubs.setGeometry(QtCore.QRect(310, 70, 51, 22))
        self.spnbx_parametrosstubs.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spnbx_parametrosstubs.setStyleSheet("QSpinBox {\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 0px;\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-color: rgb(49, 58, 67);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    /*border-image: url(uparrow.png) 1;*/\n"
"    width: 20px; \n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    /*border-image: url(downarrow.png) 1;*/\n"
"    width: 20px; \n"
"}")
        self.spnbx_parametrosstubs.setSpecialValueText("")
        self.spnbx_parametrosstubs.setMinimum(1)
        self.spnbx_parametrosstubs.setProperty("value", 1)
        self.spnbx_parametrosstubs.setObjectName("spnbx_parametrosstubs")
        self.lbl_Nstubs = QtWidgets.QLabel(self.gpbx_stubs)
        self.lbl_Nstubs.setGeometry(QtCore.QRect(196, 70, 111, 20))
        self.lbl_Nstubs.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_Nstubs.setObjectName("lbl_Nstubs")
        self.scllarea_stubs = QtWidgets.QScrollArea(self.gpbx_stubs)
        self.scllarea_stubs.setGeometry(QtCore.QRect(10, 110, 361, 371))
        self.scllarea_stubs.setStyleSheet("QScrollBar:vertical {\n"
"   /* border: 2px solid black;*/\n"
"    background: rgb(49, 58, 67);\n"
"    width: 5px;\n"
"    margin: 20px 0 20px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(85,170,255);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px black;\n"
"    background: black;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 1px black;\n"
"    background: black;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical {\n"
"    background: rgb(79, 93, 108);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"    background: rgb(79, 93, 108);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"   /* border: 2px solid black;*/\n"
"    background: rgb(49, 58, 67);\n"
"    height: 5px;\n"
"    margin:0px 20px 0px 20px;\n"
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
        self.scllarea_stubs.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scllarea_stubs.setWidgetResizable(True)
        self.scllarea_stubs.setObjectName("scllarea_stubs")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 361, 64))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_5.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_5.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.layout_parametrosstubs = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.layout_parametrosstubs.setContentsMargins(-1, -1, -1, 9)
        self.layout_parametrosstubs.setObjectName("layout_parametrosstubs")
        self.linedit_d1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.linedit_d1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linedit_d1.sizePolicy().hasHeightForWidth())
        self.linedit_d1.setSizePolicy(sizePolicy)
        self.linedit_d1.setMinimumSize(QtCore.QSize(60, 0))
        self.linedit_d1.setMaximumSize(QtCore.QSize(60, 16777215))
        self.linedit_d1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.linedit_d1.setStyleSheet("QLineEdit{\n"
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
        self.linedit_d1.setObjectName("linedit_d1")
        self.layout_parametrosstubs.addWidget(self.linedit_d1, 0, 2, 1, 1)
        self.lbl_d1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_d1.sizePolicy().hasHeightForWidth())
        self.lbl_d1.setSizePolicy(sizePolicy)
        self.lbl_d1.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_d1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_d1.setObjectName("lbl_d1")
        self.layout_parametrosstubs.addWidget(self.lbl_d1, 0, 1, 1, 1)
        self.lbl_stub1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_stub1.sizePolicy().hasHeightForWidth())
        self.lbl_stub1.setSizePolicy(sizePolicy)
        self.lbl_stub1.setMinimumSize(QtCore.QSize(69, 0))
        self.lbl_stub1.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border: 2px solid;\n"
"border-color:rgb(85,170,255);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.lbl_stub1.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_stub1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_stub1.setObjectName("lbl_stub1")
        self.layout_parametrosstubs.addWidget(self.lbl_stub1, 0, 0, 1, 1)
        self.slider_d1 = QtWidgets.QSlider(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_d1.sizePolicy().hasHeightForWidth())
        self.slider_d1.setSizePolicy(sizePolicy)
        self.slider_d1.setMinimumSize(QtCore.QSize(120, 20))
        self.slider_d1.setMaximumSize(QtCore.QSize(120, 20))
        self.slider_d1.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 2px solid black;\n"
"    border-radius: 0px;\n"
"    height: 7px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(79, 93, 108);\n"
"    border: 2px solid black;\n"
"    width: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background:rgb(79, 93, 108);\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(79, 93, 108);\n"
"}")
        self.slider_d1.setMaximum(100)
        self.slider_d1.setPageStep(1)
        self.slider_d1.setProperty("value", 50)
        self.slider_d1.setOrientation(QtCore.Qt.Horizontal)
        self.slider_d1.setInvertedAppearance(False)
        self.slider_d1.setObjectName("slider_d1")
        self.layout_parametrosstubs.addWidget(self.slider_d1, 0, 3, 1, 1)
        self.lbl_l1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_l1.sizePolicy().hasHeightForWidth())
        self.lbl_l1.setSizePolicy(sizePolicy)
        self.lbl_l1.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_l1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_l1.setObjectName("lbl_l1")
        self.layout_parametrosstubs.addWidget(self.lbl_l1, 1, 1, 1, 1)
        self.linedit_l1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linedit_l1.sizePolicy().hasHeightForWidth())
        self.linedit_l1.setSizePolicy(sizePolicy)
        self.linedit_l1.setMinimumSize(QtCore.QSize(60, 0))
        self.linedit_l1.setMaximumSize(QtCore.QSize(60, 16777215))
        self.linedit_l1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.linedit_l1.setStyleSheet("QLineEdit{\n"
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
        self.linedit_l1.setObjectName("linedit_l1")
        self.layout_parametrosstubs.addWidget(self.linedit_l1, 1, 2, 1, 1)
        self.slider_l1 = QtWidgets.QSlider(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_l1.sizePolicy().hasHeightForWidth())
        self.slider_l1.setSizePolicy(sizePolicy)
        self.slider_l1.setMinimumSize(QtCore.QSize(120, 20))
        self.slider_l1.setMaximumSize(QtCore.QSize(120, 20))
        self.slider_l1.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 2px solid black;\n"
"    border-radius: 0px;\n"
"    height: 7px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(79, 93, 108);\n"
"    border: 2px solid black;\n"
"    width: 5px;\n"
"    margin: -2px 0;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background:rgb(79, 93, 108);\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(79, 93, 108);\n"
"}")
        self.slider_l1.setMaximum(100)
        self.slider_l1.setPageStep(1)
        self.slider_l1.setProperty("value", 50)
        self.slider_l1.setOrientation(QtCore.Qt.Horizontal)
        self.slider_l1.setInvertedAppearance(False)
        self.slider_l1.setObjectName("slider_l1")
        self.layout_parametrosstubs.addWidget(self.slider_l1, 1, 3, 1, 1)
        self.scllarea_stubs.setWidget(self.scrollAreaWidgetContents_5)
        self.lbl_dipostubs = QtWidgets.QLabel(self.gpbx_stubs)
        self.lbl_dipostubs.setEnabled(False)
        self.lbl_dipostubs.setGeometry(QtCore.QRect(196, 20, 71, 21))
        self.lbl_dipostubs.setStyleSheet("color: rgba(0,0,0,0%);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.lbl_dipostubs.setObjectName("lbl_dipostubs")
        self.lbl_cargastubs = QtWidgets.QLabel(self.gpbx_stubs)
        self.lbl_cargastubs.setGeometry(QtCore.QRect(196, 35, 41, 21))
        self.lbl_cargastubs.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.lbl_cargastubs.setObjectName("lbl_cargastubs")
        self.cbx_cargastubs = QtWidgets.QComboBox(self.gpbx_stubs)
        self.cbx_cargastubs.setGeometry(QtCore.QRect(240, 35, 121, 20))
        self.cbx_cargastubs.setStyleSheet("QComboBox {\n"
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
        self.cbx_cargastubs.setObjectName("cbx_cargastubs")
        self.cbx_cargastubs.addItem("")
        self.cbx_cargastubs.addItem("")
        self.cbx_dispostubs = QtWidgets.QComboBox(self.gpbx_stubs)
        self.cbx_dispostubs.setEnabled(False)
        self.cbx_dispostubs.setGeometry(QtCore.QRect(270, 20, 91, 20))
        self.cbx_dispostubs.setStyleSheet("QComboBox {\n"
"    border:1px solid rgba(0,0,0,0%);\n"
"       border-radius: 10px;\n"
"    color:rgba(0,0,0,0%);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    background-color: rgba(0,0,0,0%);\n"
"    padding-left: 10px;\n"
"   /* min-width: 6em;*/\n"
"}\n"
"\n"
"QComboBox::drop-down {    \n"
"    border-left-width: 0px;\n"
"    border-left-color: rgba(0,0,0,0%);\n"
"    border-left-style: solid; \n"
"}\n"
"")
        self.cbx_dispostubs.setObjectName("cbx_dispostubs")
        self.cbx_dispostubs.addItem("")
        self.pbtn_reiniciarstubs = QtWidgets.QPushButton(self.gpbx_stubs)
        self.pbtn_reiniciarstubs.setGeometry(QtCore.QRect(20, 70, 151, 25))
        self.pbtn_reiniciarstubs.setStyleSheet("QPushButton {\n"
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
        self.pbtn_reiniciarstubs.setAutoDefault(False)
        self.pbtn_reiniciarstubs.setObjectName("pbtn_reiniciarstubs")
        self.pbtn_guardarstubs = QtWidgets.QPushButton(self.gpbx_stubs)
        self.pbtn_guardarstubs.setGeometry(QtCore.QRect(100, 30, 70, 25))
        self.pbtn_guardarstubs.setMinimumSize(QtCore.QSize(0, 0))
        self.pbtn_guardarstubs.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pbtn_guardarstubs.setStyleSheet("QPushButton {\n"
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
        self.pbtn_guardarstubs.setAutoDefault(False)
        self.pbtn_guardarstubs.setObjectName("pbtn_guardarstubs")
        self.pbtn_cargarstubs = QtWidgets.QPushButton(self.gpbx_stubs)
        self.pbtn_cargarstubs.setGeometry(QtCore.QRect(20, 30, 70, 25))
        self.pbtn_cargarstubs.setMinimumSize(QtCore.QSize(0, 0))
        self.pbtn_cargarstubs.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pbtn_cargarstubs.setStyleSheet("QPushButton {\n"
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
        self.pbtn_cargarstubs.setAutoDefault(False)
        self.pbtn_cargarstubs.setObjectName("pbtn_cargarstubs")
        self.gpbx_visualizacion = QtWidgets.QGroupBox(self.gpbx_master)
        self.gpbx_visualizacion.setGeometry(QtCore.QRect(10, 10, 581, 121))
        self.gpbx_visualizacion.setStyleSheet("QGroupBox {\n"
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
"}\n"
"")
        self.gpbx_visualizacion.setObjectName("gpbx_visualizacion")
        self.lbl_fsv = QtWidgets.QLabel(self.gpbx_visualizacion)
        self.lbl_fsv.setGeometry(QtCore.QRect(12, 55, 121, 20))
        self.lbl_fsv.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_fsv.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_fsv.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_fsv.setLineWidth(1)
        self.lbl_fsv.setMidLineWidth(0)
        self.lbl_fsv.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_fsv.setObjectName("lbl_fsv")
        self.lbl_tipografica = QtWidgets.QLabel(self.gpbx_visualizacion)
        self.lbl_tipografica.setGeometry(QtCore.QRect(300, 25, 91, 20))
        self.lbl_tipografica.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_tipografica.setObjectName("lbl_tipografica")
        self.lbl_fiv = QtWidgets.QLabel(self.gpbx_visualizacion)
        self.lbl_fiv.setGeometry(QtCore.QRect(20, 25, 111, 21))
        self.lbl_fiv.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_fiv.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_fiv.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_fiv.setLineWidth(1)
        self.lbl_fiv.setMidLineWidth(0)
        self.lbl_fiv.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_fiv.setObjectName("lbl_fiv")
        self.cbx_presentaciongrafica = QtWidgets.QComboBox(self.gpbx_visualizacion)
        self.cbx_presentaciongrafica.setGeometry(QtCore.QRect(450, 55, 121, 20))
        self.cbx_presentaciongrafica.setStyleSheet("QComboBox {\n"
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
        self.cbx_presentaciongrafica.setObjectName("cbx_presentaciongrafica")
        self.cbx_presentaciongrafica.addItem("")
        self.cbx_presentaciongrafica.addItem("")
        self.cbx_presentaciongrafica.addItem("")
        self.cbx_presentaciongrafica.addItem("")
        self.cbx_tipografica = QtWidgets.QComboBox(self.gpbx_visualizacion)
        self.cbx_tipografica.setGeometry(QtCore.QRect(400, 25, 171, 20))
        self.cbx_tipografica.setStyleSheet("QComboBox {\n"
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
        self.cbx_tipografica.setObjectName("cbx_tipografica")
        self.cbx_tipografica.addItem("")
        self.cbx_tipografica.addItem("")
        self.cbx_tipografica.addItem("")
        self.cbx_tipografica.addItem("")
        self.cbx_tipografica.addItem("")
        self.linedit_fiv = QtWidgets.QLineEdit(self.gpbx_visualizacion)
        self.linedit_fiv.setGeometry(QtCore.QRect(140, 25, 71, 21))
        self.linedit_fiv.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.linedit_fiv.setStyleSheet("QLineEdit{\n"
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
"}")
        self.linedit_fiv.setObjectName("linedit_fiv")
        self.lbl_presentaciongrafica = QtWidgets.QLabel(self.gpbx_visualizacion)
        self.lbl_presentaciongrafica.setGeometry(QtCore.QRect(365, 55, 81, 16))
        self.lbl_presentaciongrafica.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_presentaciongrafica.setObjectName("lbl_presentaciongrafica")
        self.linedit_fsv = QtWidgets.QLineEdit(self.gpbx_visualizacion)
        self.linedit_fsv.setGeometry(QtCore.QRect(140, 55, 71, 20))
        self.linedit_fsv.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.linedit_fsv.setStyleSheet("QLineEdit{\n"
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
"}")
        self.linedit_fsv.setObjectName("linedit_fsv")
        self.cbx_algoritmos = QtWidgets.QComboBox(self.gpbx_visualizacion)
        self.cbx_algoritmos.setGeometry(QtCore.QRect(360, 85, 211, 20))
        self.cbx_algoritmos.setStyleSheet("QComboBox {\n"
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
        self.cbx_algoritmos.setObjectName("cbx_algoritmos")
        self.lbl_algoritmos = QtWidgets.QLabel(self.gpbx_visualizacion)
        self.lbl_algoritmos.setGeometry(QtCore.QRect(292, 85, 61, 21))
        self.lbl_algoritmos.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_algoritmos.setObjectName("lbl_algoritmos")
        self.cbx_fiv = QtWidgets.QComboBox(self.gpbx_visualizacion)
        self.cbx_fiv.setGeometry(QtCore.QRect(220, 25, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_fiv.sizePolicy().hasHeightForWidth())
        self.cbx_fiv.setSizePolicy(sizePolicy)
        self.cbx_fiv.setMinimumSize(QtCore.QSize(30, 0))
        self.cbx_fiv.setMaximumSize(QtCore.QSize(81, 20))
        self.cbx_fiv.setStyleSheet("QComboBox {\n"
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
        self.cbx_fiv.setIconSize(QtCore.QSize(0, 0))
        self.cbx_fiv.setObjectName("cbx_fiv")
        self.cbx_fiv.addItem("")
        self.cbx_fiv.addItem("")
        self.cbx_fiv.addItem("")
        self.cbx_fsv = QtWidgets.QComboBox(self.gpbx_visualizacion)
        self.cbx_fsv.setGeometry(QtCore.QRect(220, 55, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_fsv.sizePolicy().hasHeightForWidth())
        self.cbx_fsv.setSizePolicy(sizePolicy)
        self.cbx_fsv.setMinimumSize(QtCore.QSize(30, 0))
        self.cbx_fsv.setMaximumSize(QtCore.QSize(81, 20))
        self.cbx_fsv.setStyleSheet("QComboBox {\n"
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
        self.cbx_fsv.setIconSize(QtCore.QSize(0, 0))
        self.cbx_fsv.setObjectName("cbx_fsv")
        self.cbx_fsv.addItem("")
        self.cbx_fsv.addItem("")
        self.cbx_fsv.addItem("")
        self.cbx_filtrar = QtWidgets.QComboBox(self.gpbx_visualizacion)
        self.cbx_filtrar.setGeometry(QtCore.QRect(140, 85, 121, 20))
        self.cbx_filtrar.setStyleSheet("QComboBox {\n"
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
        self.cbx_filtrar.setObjectName("cbx_filtrar")
        self.cbx_filtrar.addItem("")
        self.cbx_filtrar.addItem("")
        self.lbl_filtrar = QtWidgets.QLabel(self.gpbx_visualizacion)
        self.lbl_filtrar.setGeometry(QtCore.QRect(10, 85, 131, 21))
        self.lbl_filtrar.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_filtrar.setObjectName("lbl_filtrar")
        self.chkbx_Pmax = QtWidgets.QCheckBox(self.gpbx_visualizacion)
        self.chkbx_Pmax.setGeometry(QtCore.QRect(400, 55, 161, 20))
        self.chkbx_Pmax.setMinimumSize(QtCore.QSize(30, 0))
        self.chkbx_Pmax.setMaximumSize(QtCore.QSize(251, 16777215))
        self.chkbx_Pmax.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.chkbx_Pmax.setObjectName("chkbx_Pmax")
        self.lbl_filtrar.raise_()
        self.lbl_fsv.raise_()
        self.lbl_tipografica.raise_()
        self.lbl_fiv.raise_()
        self.cbx_presentaciongrafica.raise_()
        self.cbx_tipografica.raise_()
        self.linedit_fiv.raise_()
        self.lbl_presentaciongrafica.raise_()
        self.linedit_fsv.raise_()
        self.cbx_algoritmos.raise_()
        self.lbl_algoritmos.raise_()
        self.cbx_fiv.raise_()
        self.cbx_fsv.raise_()
        self.cbx_filtrar.raise_()
        self.chkbx_Pmax.raise_()
        self.slider = QtWidgets.QSlider(self.gpbx_master)
        self.slider.setGeometry(QtCore.QRect(20, 633, 561, 20))
        self.slider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 2px solid black;\n"
"    border-radius: 0px;\n"
"    height: 10px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(85,170,255);\n"
"    border: 2px solid black;\n"
"    width: 15px;\n"
"    margin: -2px 0;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background:rgb(85,170,255);\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(98, 115, 134);\n"
"}")
        self.slider.setPageStep(1)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setInvertedAppearance(True)
        self.slider.setObjectName("slider")
        self.lbl_alertastub = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_alertastub.setGeometry(QtCore.QRect(220, 656, 69, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_alertastub.sizePolicy().hasHeightForWidth())
        self.lbl_alertastub.setSizePolicy(sizePolicy)
        self.lbl_alertastub.setMinimumSize(QtCore.QSize(69, 0))
        self.lbl_alertastub.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border: 2px solid;\n"
"border-color:rgb(85,170,255);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.lbl_alertastub.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_alertastub.setText("")
        self.lbl_alertastub.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_alertastub.setObjectName("lbl_alertastub")
        self.lbl_d = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_d.setGeometry(QtCore.QRect(290, 656, 21, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_d.sizePolicy().hasHeightForWidth())
        self.lbl_d.setSizePolicy(sizePolicy)
        self.lbl_d.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_d.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_d.setObjectName("lbl_d")
        self.lbl_dn = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_dn.setGeometry(QtCore.QRect(312, 656, 141, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_dn.sizePolicy().hasHeightForWidth())
        self.lbl_dn.setSizePolicy(sizePolicy)
        self.lbl_dn.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_dn.setText("")
        self.lbl_dn.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_dn.setObjectName("lbl_dn")
        self.gpbx_grafica_1 = QtWidgets.QGroupBox(self.gpbx_master)
        self.gpbx_grafica_1.setGeometry(QtCore.QRect(10, 140, 581, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpbx_grafica_1.sizePolicy().hasHeightForWidth())
        self.gpbx_grafica_1.setSizePolicy(sizePolicy)
        self.gpbx_grafica_1.setStyleSheet("QGroupBox {\n"
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
"}\n"
"")
        self.gpbx_grafica_1.setTitle("")
        self.gpbx_grafica_1.setObjectName("gpbx_grafica_1")
        self.gpbx_grafica = QtWidgets.QGroupBox(self.gpbx_grafica_1)
        self.gpbx_grafica.setGeometry(QtCore.QRect(10, 10, 561, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpbx_grafica.sizePolicy().hasHeightForWidth())
        self.gpbx_grafica.setSizePolicy(sizePolicy)
        self.gpbx_grafica.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(49, 58, 67);\n"
"    border: 0px solid;\n"
"    border-color:rgb(85,170,255);\n"
"    border-radius: 0px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QGroupBox::title {\n"
"color:rgb(238, 238, 238);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.gpbx_grafica.setTitle("")
        self.gpbx_grafica.setObjectName("gpbx_grafica")
        self.pbtn_figuras_merito = QtWidgets.QPushButton(self.gpbx_master)
        self.pbtn_figuras_merito.setGeometry(QtCore.QRect(840, 640, 141, 31))
        self.pbtn_figuras_merito.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pbtn_figuras_merito.setStyleSheet("QPushButton {\n"
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
        self.pbtn_figuras_merito.setObjectName("pbtn_figuras_merito")
        self.pbtn_configurar_linea = QtWidgets.QPushButton(self.gpbx_master)
        self.pbtn_configurar_linea.setGeometry(QtCore.QRect(610, 640, 211, 31))
        self.pbtn_configurar_linea.setToolTip("")
        self.pbtn_configurar_linea.setToolTipDuration(-1)
        self.pbtn_configurar_linea.setStyleSheet("QPushButton {\n"
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
        self.pbtn_configurar_linea.setAutoDefault(False)
        self.pbtn_configurar_linea.setObjectName("pbtn_configurar_linea")
        self.lbl_entrada_msmn = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_entrada_msmn.setGeometry(QtCore.QRect(470, 656, 101, 21))
        self.lbl_entrada_msmn.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_entrada_msmn.setObjectName("lbl_entrada_msmn")
        self.gpbx_otros_ajustes = QtWidgets.QGroupBox(self.gpbx_master)
        self.gpbx_otros_ajustes.setGeometry(QtCore.QRect(600, 10, 391, 121))
        self.gpbx_otros_ajustes.setStyleSheet("QGroupBox {\n"
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
"}\n"
"")
        self.gpbx_otros_ajustes.setObjectName("gpbx_otros_ajustes")
        self.spnbx_celdas = QtWidgets.QSpinBox(self.gpbx_otros_ajustes)
        self.spnbx_celdas.setGeometry(QtCore.QRect(290, 35, 71, 22))
        self.spnbx_celdas.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spnbx_celdas.setStyleSheet("QSpinBox {\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 0px;\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-color: rgb(49, 58, 67);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    /*border-image: url(uparrow.png) 1;*/\n"
"    width: 20px; \n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    /*border-image: url(downarrow.png) 1;*/\n"
"    width: 20px; \n"
"}\n"
"\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.spnbx_celdas.setSpecialValueText("")
        self.spnbx_celdas.setMinimum(1)
        self.spnbx_celdas.setMaximum(5000)
        self.spnbx_celdas.setProperty("value", 5)
        self.spnbx_celdas.setObjectName("spnbx_celdas")
        self.lbl_celdas = QtWidgets.QLabel(self.gpbx_otros_ajustes)
        self.lbl_celdas.setGeometry(QtCore.QRect(20, 35, 261, 20))
        self.lbl_celdas.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_celdas.setObjectName("lbl_celdas")
        self.lbl_puntos_frecuencia = QtWidgets.QLabel(self.gpbx_otros_ajustes)
        self.lbl_puntos_frecuencia.setGeometry(QtCore.QRect(20, 70, 131, 20))
        self.lbl_puntos_frecuencia.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_puntos_frecuencia.setObjectName("lbl_puntos_frecuencia")
        self.spnbx_puntos_frecuencia = QtWidgets.QSpinBox(self.gpbx_otros_ajustes)
        self.spnbx_puntos_frecuencia.setGeometry(QtCore.QRect(150, 70, 71, 22))
        self.spnbx_puntos_frecuencia.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spnbx_puntos_frecuencia.setStyleSheet("QSpinBox {\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 0px;\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-color: rgb(49, 58, 67);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    /*border-image: url(uparrow.png) 1;*/\n"
"    width: 20px; \n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    /*border-image: url(downarrow.png) 1;*/\n"
"    width: 20px; \n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.spnbx_puntos_frecuencia.setSpecialValueText("")
        self.spnbx_puntos_frecuencia.setMinimum(3)
        self.spnbx_puntos_frecuencia.setMaximum(5001)
        self.spnbx_puntos_frecuencia.setProperty("value", 101)
        self.spnbx_puntos_frecuencia.setObjectName("spnbx_puntos_frecuencia")
        self.pbtn_aplicar = QtWidgets.QPushButton(self.gpbx_otros_ajustes)
        self.pbtn_aplicar.setGeometry(QtCore.QRect(290, 80, 70, 25))
        self.pbtn_aplicar.setMinimumSize(QtCore.QSize(0, 0))
        self.pbtn_aplicar.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pbtn_aplicar.setStyleSheet("QPushButton {\n"
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
"}\n"
"\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.pbtn_aplicar.setAutoDefault(False)
        self.pbtn_aplicar.setObjectName("pbtn_aplicar")
        self.lbl_celdas.raise_()
        self.lbl_puntos_frecuencia.raise_()
        self.spnbx_puntos_frecuencia.raise_()
        self.pbtn_aplicar.raise_()
        self.spnbx_celdas.raise_()
        self.lbl_todos_msmn = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_todos_msmn.setGeometry(QtCore.QRect(160, 650, 271, 21))
        self.lbl_todos_msmn.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_todos_msmn.setObjectName("lbl_todos_msmn")
        self.lbl_no_hay_algoritmos = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_no_hay_algoritmos.setGeometry(QtCore.QRect(170, 635, 231, 21))
        self.lbl_no_hay_algoritmos.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_no_hay_algoritmos.setObjectName("lbl_no_hay_algoritmos")
        self.lbl_revisar_parametros = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_revisar_parametros.setGeometry(QtCore.QRect(190, 660, 191, 21))
        self.lbl_revisar_parametros.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_revisar_parametros.setObjectName("lbl_revisar_parametros")
        self.layout_2.addWidget(self.gpbx_master, 0, 0, 1, 1)
        self.scllarea_master.setWidget(self.scrollAreaWidgetContents_7)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gráfica"))
        self.gpbx_stubs.setTitle(_translate("Dialog", "Configuración de MSMN"))
        self.lbl_Nstubs.setText(_translate("Dialog", "Cantidad de stubs:"))
        self.lbl_d1.setText(_translate("Dialog", " D1 (mm):"))
        self.lbl_stub1.setText(_translate("Dialog", "Stub 1:"))
        self.lbl_l1.setText(_translate("Dialog", "  L1 (mm):"))
        self.lbl_dipostubs.setText(_translate("Dialog", "Disposición:"))
        self.lbl_cargastubs.setText(_translate("Dialog", "Carga:"))
        self.cbx_cargastubs.setItemText(0, _translate("Dialog", "Corto circuito"))
        self.cbx_cargastubs.setItemText(1, _translate("Dialog", "Circuito abierto"))
        self.cbx_dispostubs.setItemText(0, _translate("Dialog", "Paralelo"))
        self.pbtn_reiniciarstubs.setText(_translate("Dialog", "Reiniciar"))
        self.pbtn_guardarstubs.setText(_translate("Dialog", "Guardar"))
        self.pbtn_cargarstubs.setText(_translate("Dialog", "Cargar"))
        self.gpbx_visualizacion.setTitle(_translate("Dialog", "Parámetros de visualización"))
        self.lbl_fsv.setText(_translate("Dialog", "Frecuencia superior:"))
        self.lbl_tipografica.setToolTip(_translate("Dialog", "<html><head/><body><p>La respuesta en frecuencia está definida como el voltaje a la entrada de la impedancia de carga dividido entre el voltaje de salida del generador.</p></body></html>"))
        self.lbl_tipografica.setText(_translate("Dialog", "Tipo de gráfica:"))
        self.lbl_fiv.setText(_translate("Dialog", "Frecuencia inferior:"))
        self.cbx_presentaciongrafica.setItemText(0, _translate("Dialog", "Magnitud"))
        self.cbx_presentaciongrafica.setItemText(1, _translate("Dialog", "Fase"))
        self.cbx_presentaciongrafica.setItemText(2, _translate("Dialog", "Parte real"))
        self.cbx_presentaciongrafica.setItemText(3, _translate("Dialog", "Parte imaginaria"))
        self.cbx_tipografica.setItemText(0, _translate("Dialog", "Coeficiente de reflexión"))
        self.cbx_tipografica.setItemText(1, _translate("Dialog", "Impedancia vista"))
        self.cbx_tipografica.setItemText(2, _translate("Dialog", "ROEV"))
        self.cbx_tipografica.setItemText(3, _translate("Dialog", "Potencia activa promedio"))
        self.cbx_tipografica.setItemText(4, _translate("Dialog", "Respuesta en frecuencia"))
        self.lbl_presentaciongrafica.setText(_translate("Dialog", "Presentación:"))
        self.lbl_algoritmos.setText(_translate("Dialog", "Algoritmo:"))
        self.cbx_fiv.setItemText(0, _translate("Dialog", "GHz"))
        self.cbx_fiv.setItemText(1, _translate("Dialog", "MHz"))
        self.cbx_fiv.setItemText(2, _translate("Dialog", "kHz"))
        self.cbx_fsv.setItemText(0, _translate("Dialog", "GHz"))
        self.cbx_fsv.setItemText(1, _translate("Dialog", "MHz"))
        self.cbx_fsv.setItemText(2, _translate("Dialog", "kHz"))
        self.cbx_filtrar.setItemText(0, _translate("Dialog", "Mejor esfuerzo"))
        self.cbx_filtrar.setItemText(1, _translate("Dialog", "Modo estricto"))
        self.lbl_filtrar.setToolTip(_translate("Dialog", "<html><head/><body><p>Modo estricto: Muestra sólo los algoritmos que hallaron una solución que satisface los requerimientos de adaptación.</p></body></html>"))
        self.lbl_filtrar.setText(_translate("Dialog", "Filtrar algoritmos por:"))
        self.chkbx_Pmax.setText(_translate("Dialog", "Graficar Pmax de la línea"))
        self.lbl_d.setText(_translate("Dialog", " d:"))
        self.pbtn_figuras_merito.setText(_translate("Dialog", "Ver figuras de mérito"))
        self.pbtn_configurar_linea.setText(_translate("Dialog", "Configurar línea de transmisión"))
        self.lbl_entrada_msmn.setText(_translate("Dialog", "Entrada a MSMN"))
        self.gpbx_otros_ajustes.setTitle(_translate("Dialog", "Otros ajustes"))
        self.spnbx_celdas.setToolTip(_translate("Dialog", "<html><head/><body><p>Advertencia: Mayor número de celdas implica mayor retardo al generar las gráficas.</p></body></html>"))
        self.lbl_celdas.setToolTip(_translate("Dialog", "<html><head/><body><p>Advertencia: Mayor número de celdas implica mayor retardo al generar las gráficas.</p></body></html>"))
        self.lbl_celdas.setText(_translate("Dialog", "Número de celdas por cada longitud de onda:"))
        self.lbl_puntos_frecuencia.setToolTip(_translate("Dialog", "<html><head/><body><p>Advertencia: Mayor número de puntos de frecuencia implica mayor retardo al generar las gráficas.</p></body></html>"))
        self.lbl_puntos_frecuencia.setText(_translate("Dialog", "Puntos de frecuencia:"))
        self.spnbx_puntos_frecuencia.setToolTip(_translate("Dialog", "<html><head/><body><p>Advertencia: Mayor número de puntos de frecuencia implica mayor retardo al generar las gráficas.</p></body></html>"))
        self.pbtn_aplicar.setToolTip(_translate("Dialog", "<html><head/><body><p>Advertencia: Mayor número de celdas y/o mayor número de puntos de frecuencia implica mayor retardo al generar las gráficas.</p></body></html>"))
        self.pbtn_aplicar.setText(_translate("Dialog", "Aplicar"))
        self.lbl_todos_msmn.setText(_translate("Dialog", "Gráficas en el plano de entrada a cada MSMN"))
        self.lbl_no_hay_algoritmos.setText(_translate("Dialog", "No hay soluciones para el modo estricto"))
        self.lbl_revisar_parametros.setText(_translate("Dialog", "Ingrese correctamente los datos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

