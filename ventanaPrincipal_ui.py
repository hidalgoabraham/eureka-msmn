# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1006, 690)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1006, 690))
        MainWindow.setMaximumSize(QtCore.QSize(1006, 690))
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
        self.scllarea_master = QtWidgets.QScrollArea(self.centralwidget)
        self.scllarea_master.setGeometry(QtCore.QRect(0, 0, 1006, 690))
        self.scllarea_master.setMinimumSize(QtCore.QSize(1006, 690))
        self.scllarea_master.setMaximumSize(QtCore.QSize(1006, 690))
        self.scllarea_master.setStyleSheet("")
        self.scllarea_master.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scllarea_master.setWidgetResizable(True)
        self.scllarea_master.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scllarea_master.setObjectName("scllarea_master")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 1006, 690))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_8.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_8.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_8.setMinimumSize(QtCore.QSize(1006, 690))
        self.scrollAreaWidgetContents_8.setMaximumSize(QtCore.QSize(1006, 690))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.layout_master = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_8)
        self.layout_master.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_master.setContentsMargins(2, 0, 0, 0)
        self.layout_master.setObjectName("layout_master")
        self.gpbx_master = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpbx_master.sizePolicy().hasHeightForWidth())
        self.gpbx_master.setSizePolicy(sizePolicy)
        self.gpbx_master.setMinimumSize(QtCore.QSize(1006, 690))
        self.gpbx_master.setMaximumSize(QtCore.QSize(1006, 690))
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
        self.gpbx_master.setFlat(True)
        self.gpbx_master.setObjectName("gpbx_master")
        self.gpbx_requerimientos = QtWidgets.QGroupBox(self.gpbx_master)
        self.gpbx_requerimientos.setGeometry(QtCore.QRect(10, 352, 671, 241))
        self.gpbx_requerimientos.setStyleSheet("QGroupBox {\n"
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
        self.gpbx_requerimientos.setObjectName("gpbx_requerimientos")
        self.lbl_funcionobjetivo = QtWidgets.QLabel(self.gpbx_requerimientos)
        self.lbl_funcionobjetivo.setGeometry(QtCore.QRect(95, 30, 321, 181))
        self.lbl_funcionobjetivo.setStyleSheet("QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_funcionobjetivo.setText("")
        self.lbl_funcionobjetivo.setPixmap(QtGui.QPixmap("funcionobjetivo.png"))
        self.lbl_funcionobjetivo.setScaledContents(True)
        self.lbl_funcionobjetivo.setObjectName("lbl_funcionobjetivo")
        self.lbl_req = QtWidgets.QLabel(self.gpbx_requerimientos)
        self.lbl_req.setGeometry(QtCore.QRect(10, 155, 61, 20))
        self.lbl_req.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_req.setObjectName("lbl_req")
        self.linedit_max = QtWidgets.QLineEdit(self.gpbx_requerimientos)
        self.linedit_max.setGeometry(QtCore.QRect(70, 155, 41, 20))
        self.linedit_max.setStyleSheet("QLineEdit{\n"
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
        self.linedit_max.setObjectName("linedit_max")
        self.lbl_fo = QtWidgets.QLabel(self.gpbx_requerimientos)
        self.lbl_fo.setGeometry(QtCore.QRect(220, 195, 21, 20))
        self.lbl_fo.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_fo.setObjectName("lbl_fo")
        self.linedit_fo = QtWidgets.QLineEdit(self.gpbx_requerimientos)
        self.linedit_fo.setGeometry(QtCore.QRect(240, 195, 71, 20))
        self.linedit_fo.setStyleSheet("QLineEdit{\n"
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
        self.linedit_fo.setObjectName("linedit_fo")
        self.lbl_bw = QtWidgets.QLabel(self.gpbx_requerimientos)
        self.lbl_bw.setGeometry(QtCore.QRect(205, 115, 31, 20))
        self.lbl_bw.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_bw.setObjectName("lbl_bw")
        self.linedit_bw = QtWidgets.QLineEdit(self.gpbx_requerimientos)
        self.linedit_bw.setGeometry(QtCore.QRect(238, 115, 61, 20))
        self.linedit_bw.setStyleSheet("QLineEdit{\n"
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
        self.linedit_bw.setObjectName("linedit_bw")
        self.lbl_algoritmos = QtWidgets.QLabel(self.gpbx_requerimientos)
        self.lbl_algoritmos.setGeometry(QtCore.QRect(410, 20, 221, 20))
        self.lbl_algoritmos.setToolTip("")
        self.lbl_algoritmos.setStyleSheet("QLabel{\n"
"color: rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_algoritmos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_algoritmos.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_algoritmos.setObjectName("lbl_algoritmos")
        self.chkbx_NM = QtWidgets.QCheckBox(self.gpbx_requerimientos)
        self.chkbx_NM.setGeometry(QtCore.QRect(420, 50, 245, 20))
        self.chkbx_NM.setMinimumSize(QtCore.QSize(245, 0))
        self.chkbx_NM.setMaximumSize(QtCore.QSize(251, 16777215))
        self.chkbx_NM.setToolTip("")
        self.chkbx_NM.setStyleSheet("QCheckBox{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}\n"
"")
        self.chkbx_NM.setObjectName("chkbx_NM")
        self.chkbx_DE = QtWidgets.QCheckBox(self.gpbx_requerimientos)
        self.chkbx_DE.setGeometry(QtCore.QRect(420, 70, 245, 20))
        self.chkbx_DE.setMinimumSize(QtCore.QSize(245, 0))
        self.chkbx_DE.setMaximumSize(QtCore.QSize(251, 16777215))
        self.chkbx_DE.setToolTip("")
        self.chkbx_DE.setStyleSheet("QCheckBox{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.chkbx_DE.setObjectName("chkbx_DE")
        self.chkbx_DA = QtWidgets.QCheckBox(self.gpbx_requerimientos)
        self.chkbx_DA.setGeometry(QtCore.QRect(420, 90, 245, 20))
        self.chkbx_DA.setMinimumSize(QtCore.QSize(245, 0))
        self.chkbx_DA.setMaximumSize(QtCore.QSize(251, 16777215))
        self.chkbx_DA.setToolTip("")
        self.chkbx_DA.setStyleSheet("QCheckBox{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.chkbx_DA.setObjectName("chkbx_DA")
        self.chkbx_BF = QtWidgets.QCheckBox(self.gpbx_requerimientos)
        self.chkbx_BF.setGeometry(QtCore.QRect(420, 110, 245, 20))
        self.chkbx_BF.setMinimumSize(QtCore.QSize(245, 0))
        self.chkbx_BF.setMaximumSize(QtCore.QSize(251, 16777215))
        self.chkbx_BF.setToolTip("")
        self.chkbx_BF.setStyleSheet("QCheckBox{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.chkbx_BF.setObjectName("chkbx_BF")
        self.chkbx_EO = QtWidgets.QCheckBox(self.gpbx_requerimientos)
        self.chkbx_EO.setGeometry(QtCore.QRect(420, 150, 245, 20))
        self.chkbx_EO.setMinimumSize(QtCore.QSize(245, 0))
        self.chkbx_EO.setMaximumSize(QtCore.QSize(251, 16777215))
        self.chkbx_EO.setToolTip("")
        self.chkbx_EO.setStyleSheet("QCheckBox{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.chkbx_EO.setObjectName("chkbx_EO")
        self.chkbx_HHO = QtWidgets.QCheckBox(self.gpbx_requerimientos)
        self.chkbx_HHO.setGeometry(QtCore.QRect(420, 170, 245, 20))
        self.chkbx_HHO.setMinimumSize(QtCore.QSize(245, 0))
        self.chkbx_HHO.setMaximumSize(QtCore.QSize(251, 16777215))
        self.chkbx_HHO.setToolTip("")
        self.chkbx_HHO.setStyleSheet("QCheckBox{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.chkbx_HHO.setObjectName("chkbx_HHO")
        self.chkbx_WOA = QtWidgets.QCheckBox(self.gpbx_requerimientos)
        self.chkbx_WOA.setGeometry(QtCore.QRect(420, 130, 245, 18))
        self.chkbx_WOA.setMinimumSize(QtCore.QSize(245, 0))
        self.chkbx_WOA.setMaximumSize(QtCore.QSize(251, 16777215))
        self.chkbx_WOA.setToolTip("")
        self.chkbx_WOA.setStyleSheet("QCheckBox{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.chkbx_WOA.setObjectName("chkbx_WOA")
        self.chkbx_VCS = QtWidgets.QCheckBox(self.gpbx_requerimientos)
        self.chkbx_VCS.setGeometry(QtCore.QRect(420, 190, 245, 20))
        self.chkbx_VCS.setMinimumSize(QtCore.QSize(245, 0))
        self.chkbx_VCS.setMaximumSize(QtCore.QSize(251, 16777215))
        self.chkbx_VCS.setToolTip("")
        self.chkbx_VCS.setStyleSheet("QCheckBox{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.chkbx_VCS.setObjectName("chkbx_VCS")
        self.chkbx_AEO = QtWidgets.QCheckBox(self.gpbx_requerimientos)
        self.chkbx_AEO.setGeometry(QtCore.QRect(420, 210, 245, 20))
        self.chkbx_AEO.setMinimumSize(QtCore.QSize(245, 0))
        self.chkbx_AEO.setMaximumSize(QtCore.QSize(251, 16777215))
        self.chkbx_AEO.setToolTip("")
        self.chkbx_AEO.setStyleSheet("QCheckBox{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.chkbx_AEO.setObjectName("chkbx_AEO")
        self.cbx_bw = QtWidgets.QComboBox(self.gpbx_requerimientos)
        self.cbx_bw.setGeometry(QtCore.QRect(303, 115, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_bw.sizePolicy().hasHeightForWidth())
        self.cbx_bw.setSizePolicy(sizePolicy)
        self.cbx_bw.setMinimumSize(QtCore.QSize(30, 0))
        self.cbx_bw.setMaximumSize(QtCore.QSize(81, 20))
        self.cbx_bw.setStyleSheet("QComboBox {\n"
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
        self.cbx_bw.setIconSize(QtCore.QSize(0, 0))
        self.cbx_bw.setObjectName("cbx_bw")
        self.cbx_bw.addItem("")
        self.cbx_bw.addItem("")
        self.cbx_bw.addItem("")
        self.cbx_fo = QtWidgets.QComboBox(self.gpbx_requerimientos)
        self.cbx_fo.setGeometry(QtCore.QRect(315, 195, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_fo.sizePolicy().hasHeightForWidth())
        self.cbx_fo.setSizePolicy(sizePolicy)
        self.cbx_fo.setMinimumSize(QtCore.QSize(30, 0))
        self.cbx_fo.setMaximumSize(QtCore.QSize(81, 20))
        self.cbx_fo.setStyleSheet("QComboBox {\n"
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
        self.cbx_fo.setIconSize(QtCore.QSize(0, 0))
        self.cbx_fo.setObjectName("cbx_fo")
        self.cbx_fo.addItem("")
        self.cbx_fo.addItem("")
        self.cbx_fo.addItem("")
        self.lbl_vswr = QtWidgets.QLabel(self.gpbx_requerimientos)
        self.lbl_vswr.setGeometry(QtCore.QRect(6, 130, 71, 20))
        self.lbl_vswr.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_vswr.setObjectName("lbl_vswr")
        self.linedit_vswr = QtWidgets.QLineEdit(self.gpbx_requerimientos)
        self.linedit_vswr.setGeometry(QtCore.QRect(77, 130, 33, 20))
        self.linedit_vswr.setStyleSheet("QLineEdit{\n"
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
        self.linedit_vswr.setObjectName("linedit_vswr")
        self.lbl_warning_algoritmos = QtWidgets.QLabel(self.gpbx_requerimientos)
        self.lbl_warning_algoritmos.setGeometry(QtCore.QRect(638, 13, 25, 25))
        self.lbl_warning_algoritmos.setStyleSheet("QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_warning_algoritmos.setText("")
        self.lbl_warning_algoritmos.setPixmap(QtGui.QPixmap("warning.png"))
        self.lbl_warning_algoritmos.setScaledContents(True)
        self.lbl_warning_algoritmos.setObjectName("lbl_warning_algoritmos")
        self.lbl_anuncio = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_anuncio.setGeometry(QtCore.QRect(690, 600, 311, 61))
        self.lbl_anuncio.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_anuncio.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_anuncio.setObjectName("lbl_anuncio")
        self.pbtn_buscar = QtWidgets.QPushButton(self.gpbx_master)
        self.pbtn_buscar.setGeometry(QtCore.QRect(20, 620, 121, 31))
        self.pbtn_buscar.setStyleSheet("QPushButton {\n"
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
        self.pbtn_buscar.setObjectName("pbtn_buscar")
        self.pbtn_graficar = QtWidgets.QPushButton(self.gpbx_master)
        self.pbtn_graficar.setGeometry(QtCore.QRect(160, 620, 84, 31))
        self.pbtn_graficar.setStyleSheet("QPushButton {\n"
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
        self.pbtn_graficar.setObjectName("pbtn_graficar")
        self.pbtn_cancelar = QtWidgets.QPushButton(self.gpbx_master)
        self.pbtn_cancelar.setGeometry(QtCore.QRect(20, 620, 131, 31))
        self.pbtn_cancelar.setStyleSheet("QPushButton {\n"
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
        self.pbtn_cancelar.setObjectName("pbtn_cancelar")
        self.scllarea = QtWidgets.QScrollArea(self.gpbx_master)
        self.scllarea.setGeometry(QtCore.QRect(690, 360, 301, 231))
        self.scllarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scllarea.setWidgetResizable(True)
        self.scllarea.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.scllarea.setObjectName("scllarea")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 299, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_6.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_6.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.layout_avisos = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.layout_avisos.setContentsMargins(-1, -1, -1, 0)
        self.layout_avisos.setObjectName("layout_avisos")
        self.scllarea.setWidget(self.scrollAreaWidgetContents_6)
        self.pbtn_metadata = QtWidgets.QPushButton(self.gpbx_master)
        self.pbtn_metadata.setGeometry(QtCore.QRect(480, 620, 201, 31))
        self.pbtn_metadata.setStyleSheet("QPushButton {\n"
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
        self.pbtn_metadata.setObjectName("pbtn_metadata")
        self.pbtn_resultados_msmn = QtWidgets.QPushButton(self.gpbx_master)
        self.pbtn_resultados_msmn.setGeometry(QtCore.QRect(270, 620, 201, 31))
        self.pbtn_resultados_msmn.setStyleSheet("QPushButton {\n"
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
        self.pbtn_resultados_msmn.setObjectName("pbtn_resultados_msmn")
        self.label = QtWidgets.QLabel(self.gpbx_master)
        self.label.setGeometry(QtCore.QRect(150, 50, 711, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("LTx_principal.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pbtn_configurar_carga = QtWidgets.QPushButton(self.gpbx_master)
        self.pbtn_configurar_carga.setGeometry(QtCore.QRect(890, 160, 84, 61))
        self.pbtn_configurar_carga.setStyleSheet("QPushButton {\n"
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
        self.pbtn_configurar_carga.setAutoDefault(False)
        self.pbtn_configurar_carga.setDefault(False)
        self.pbtn_configurar_carga.setFlat(False)
        self.pbtn_configurar_carga.setObjectName("pbtn_configurar_carga")
        self.pbtn_configurar_linea = QtWidgets.QPushButton(self.gpbx_master)
        self.pbtn_configurar_linea.setGeometry(QtCore.QRect(130, 40, 141, 51))
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
        self.pbtn_configurar_linea.setDefault(False)
        self.pbtn_configurar_linea.setFlat(False)
        self.pbtn_configurar_linea.setObjectName("pbtn_configurar_linea")
        self.pbtn_configurar_reqStubs = QtWidgets.QPushButton(self.gpbx_master)
        self.pbtn_configurar_reqStubs.setGeometry(QtCore.QRect(780, 50, 121, 31))
        self.pbtn_configurar_reqStubs.setStyleSheet("QPushButton {\n"
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
        self.pbtn_configurar_reqStubs.setAutoDefault(False)
        self.pbtn_configurar_reqStubs.setDefault(False)
        self.pbtn_configurar_reqStubs.setFlat(False)
        self.pbtn_configurar_reqStubs.setObjectName("pbtn_configurar_reqStubs")
        self.pbtn_configurar_generador = QtWidgets.QPushButton(self.gpbx_master)
        self.pbtn_configurar_generador.setGeometry(QtCore.QRect(30, 165, 91, 51))
        self.pbtn_configurar_generador.setStyleSheet("QPushButton {\n"
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
        self.pbtn_configurar_generador.setAutoDefault(False)
        self.pbtn_configurar_generador.setDefault(False)
        self.pbtn_configurar_generador.setFlat(False)
        self.pbtn_configurar_generador.setObjectName("pbtn_configurar_generador")
        self.lbl_DGA = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_DGA.setGeometry(QtCore.QRect(250, 250, 41, 21))
        self.lbl_DGA.setStyleSheet("QLabel{\n"
"background-color: rgba(0,0,0,0%)\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_DGA.setText("")
        self.lbl_DGA.setObjectName("lbl_DGA")
        self.lbl_DCA = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_DCA.setGeometry(QtCore.QRect(760, 250, 41, 21))
        self.lbl_DCA.setStyleSheet("QLabel{\n"
"background-color: rgba(0,0,0,0%)\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_DCA.setText("")
        self.lbl_DCA.setObjectName("lbl_DCA")
        self.lbl_MSMN = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_MSMN.setGeometry(QtCore.QRect(310, 60, 441, 251))
        self.lbl_MSMN.setStyleSheet("QLabel{\n"
"background-color: rgba(0,0,0,0%)\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_MSMN.setText("")
        self.lbl_MSMN.setObjectName("lbl_MSMN")
        self.lbl_D1 = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_D1.setGeometry(QtCore.QRect(670, 250, 81, 21))
        self.lbl_D1.setStyleSheet("QLabel{\n"
"background-color: rgba(0,0,0,0%)\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_D1.setText("")
        self.lbl_D1.setObjectName("lbl_D1")
        self.lbl_D2 = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_D2.setGeometry(QtCore.QRect(570, 250, 81, 21))
        self.lbl_D2.setStyleSheet("QLabel{\n"
"background-color: rgba(0,0,0,0%)\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_D2.setText("")
        self.lbl_D2.setObjectName("lbl_D2")
        self.lbl_DN = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_DN.setGeometry(QtCore.QRect(300, 250, 91, 21))
        self.lbl_DN.setStyleSheet("QLabel{\n"
"background-color: rgba(0,0,0,0%)\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_DN.setText("")
        self.lbl_DN.setObjectName("lbl_DN")
        self.lbl_L1 = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_L1.setGeometry(QtCore.QRect(650, 70, 51, 41))
        self.lbl_L1.setStyleSheet("QLabel{\n"
"background-color: rgba(0,0,0,0%)\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_L1.setText("")
        self.lbl_L1.setObjectName("lbl_L1")
        self.lbl_L2 = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_L2.setGeometry(QtCore.QRect(550, 70, 51, 41))
        self.lbl_L2.setStyleSheet("QLabel{\n"
"background-color: rgba(0,0,0,0%)\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_L2.setText("")
        self.lbl_L2.setObjectName("lbl_L2")
        self.lbl_LNm1 = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_LNm1.setGeometry(QtCore.QRect(380, 70, 51, 41))
        self.lbl_LNm1.setStyleSheet("QLabel{\n"
"background-color: rgba(0,0,0,0%)\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_LNm1.setText("")
        self.lbl_LNm1.setObjectName("lbl_LNm1")
        self.lbl_LN = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_LN.setGeometry(QtCore.QRect(290, 70, 51, 41))
        self.lbl_LN.setStyleSheet("QLabel{\n"
"background-color: rgba(0,0,0,0%)\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_LN.setText("")
        self.lbl_LN.setObjectName("lbl_LN")
        self.lbl_Zin = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_Zin.setGeometry(QtCore.QRect(280, 327, 71, 21))
        self.lbl_Zin.setStyleSheet("QLabel{\n"
"background-color: rgba(0,0,0,0%)\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_Zin.setText("")
        self.lbl_Zin.setObjectName("lbl_Zin")
        self.lbl_Zc = QtWidgets.QLabel(self.gpbx_master)
        self.lbl_Zc.setGeometry(QtCore.QRect(368, 323, 25, 25))
        self.lbl_Zc.setStyleSheet("QLabel{\n"
"background-color: rgba(0,0,0,0%)\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_Zc.setText("")
        self.lbl_Zc.setObjectName("lbl_Zc")
        self.label.raise_()
        self.pbtn_cancelar.raise_()
        self.pbtn_buscar.raise_()
        self.gpbx_requerimientos.raise_()
        self.pbtn_graficar.raise_()
        self.scllarea.raise_()
        self.pbtn_metadata.raise_()
        self.pbtn_resultados_msmn.raise_()
        self.pbtn_configurar_carga.raise_()
        self.pbtn_configurar_linea.raise_()
        self.pbtn_configurar_reqStubs.raise_()
        self.pbtn_configurar_generador.raise_()
        self.lbl_anuncio.raise_()
        self.lbl_MSMN.raise_()
        self.lbl_Zin.raise_()
        self.lbl_D1.raise_()
        self.lbl_D2.raise_()
        self.lbl_DN.raise_()
        self.lbl_DGA.raise_()
        self.lbl_DCA.raise_()
        self.lbl_L1.raise_()
        self.lbl_L2.raise_()
        self.lbl_LNm1.raise_()
        self.lbl_LN.raise_()
        self.lbl_Zc.raise_()
        self.layout_master.addWidget(self.gpbx_master, 0, 0, 1, 1)
        self.scllarea_master.setWidget(self.scrollAreaWidgetContents_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1006, 22))
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
        self.actionCargar = QtWidgets.QAction(MainWindow)
        self.actionCargar.setObjectName("actionCargar")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionReiniciar = QtWidgets.QAction(MainWindow)
        self.actionReiniciar.setObjectName("actionReiniciar")
        self.actionManual_de_usuario = QtWidgets.QAction(MainWindow)
        self.actionManual_de_usuario.setObjectName("actionManual_de_usuario")
        self.menuProyecto.addAction(self.actionCargar)
        self.menuProyecto.addAction(self.actionGuardar)
        self.menuProyecto.addAction(self.actionReiniciar)
        self.menuBar.addAction(self.menuProyecto.menuAction())

        self.retranslateUi(MainWindow)
        self.cbx_bw.setCurrentIndex(1)
        self.cbx_fo.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eureka MSMN"))
        self.gpbx_requerimientos.setTitle(_translate("MainWindow", "Requerimientos de adaptación de impedancia"))
        self.lbl_funcionobjetivo.setToolTip(_translate("MainWindow", "<html><head/><body><p>Valor del módulo del coeficiente de reflexión de voltaje que se requiere en el plano de adaptación d=d<span style=\" vertical-align:sub;\">A </span>.</p></body></html>"))
        self.lbl_req.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#eeeeee;\">Valor máximo permitido para el módulo del coeficiente de reflexión de voltaje en el ancho de banda de adaptación.</span></p></body></html>"))
        self.lbl_req.setText(_translate("MainWindow", "|Γ| Máx.:"))
        self.lbl_fo.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Frecuencia central.</span></p></body></html>"))
        self.lbl_fo.setText(_translate("MainWindow", "fo:"))
        self.lbl_bw.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:400;\">Ancho de banda de adaptación.</span></p></body></html>"))
        self.lbl_bw.setText(_translate("MainWindow", "ABA:"))
        self.lbl_algoritmos.setText(_translate("MainWindow", "Algoritmos heurísticos a implementar:"))
        self.chkbx_NM.setText(_translate("MainWindow", "Nelder-Mead"))
        self.chkbx_DE.setText(_translate("MainWindow", "Differential Evolution"))
        self.chkbx_DA.setText(_translate("MainWindow", "Dual Annealing"))
        self.chkbx_BF.setText(_translate("MainWindow", "Brute Force"))
        self.chkbx_EO.setText(_translate("MainWindow", "Equilibrium Optimizer"))
        self.chkbx_HHO.setText(_translate("MainWindow", "Harris Hawks Optimization"))
        self.chkbx_WOA.setText(_translate("MainWindow", "Whale Optimization Algorithm"))
        self.chkbx_VCS.setText(_translate("MainWindow", "Virus Colony Search"))
        self.chkbx_AEO.setText(_translate("MainWindow", "Artificial Ecosystem-Based Optimization"))
        self.cbx_bw.setItemText(0, _translate("MainWindow", "GHz"))
        self.cbx_bw.setItemText(1, _translate("MainWindow", "MHz"))
        self.cbx_bw.setItemText(2, _translate("MainWindow", "kHz"))
        self.cbx_fo.setItemText(0, _translate("MainWindow", "GHz"))
        self.cbx_fo.setItemText(1, _translate("MainWindow", "MHz"))
        self.cbx_fo.setItemText(2, _translate("MainWindow", "kHz"))
        self.lbl_vswr.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#eeeeee;\">Valor máximo permitido para la relación de onda estacionaria de voltaje en el ancho de banda de adaptación.</span></p></body></html>"))
        self.lbl_vswr.setText(_translate("MainWindow", "ROEV Máx.:"))
        self.lbl_warning_algoritmos.setToolTip(_translate("MainWindow", "<html><head/><body><p>Advertencia: Realizar una búsqueda con más de 4 algoritmos en simultáneo podría ralentizar considerablemente el funcionamiento del equipo.</p></body></html>"))
        self.lbl_anuncio.setText(_translate("MainWindow", "Los algoritmos de búsqueda han finalizado."))
        self.pbtn_buscar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Buscar las configuraciones de stubs mediante los algoritmos de optimizacion.</p></body></html>"))
        self.pbtn_buscar.setText(_translate("MainWindow", "Iniciar búsqueda"))
        self.pbtn_graficar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Obtener las gráficas de una configuración de stubs dada.</p></body></html>"))
        self.pbtn_graficar.setText(_translate("MainWindow", "Graficar"))
        self.pbtn_cancelar.setText(_translate("MainWindow", "Cancelar búsqueda"))
        self.pbtn_metadata.setText(_translate("MainWindow", "Ver rendimiento computacional"))
        self.pbtn_resultados_msmn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ver configuraciones de redes de adaptación de múltiples stubs encontradas por los algoritmos de optimización.</p></body></html>"))
        self.pbtn_resultados_msmn.setText(_translate("MainWindow", "Ver gráficas"))
        self.pbtn_configurar_carga.setText(_translate("MainWindow", "Configurar\n"
"impedancia\n"
"de carga"))
        self.pbtn_configurar_linea.setText(_translate("MainWindow", "Configurar\n"
"línea de transmisión"))
        self.pbtn_configurar_reqStubs.setText(_translate("MainWindow", "Configurar MSMN"))
        self.pbtn_configurar_generador.setText(_translate("MainWindow", "Configurar\n"
"generador"))
        self.lbl_DGA.setToolTip(_translate("MainWindow", "<html><head/><body><p>Distancia entre el generador y el adaptador MSMN.</p></body></html>"))
        self.lbl_DCA.setToolTip(_translate("MainWindow", "<html><head/><body><p>Distancia entre la impedancia de carga y el adaptador MSMN.</p></body></html>"))
        self.lbl_MSMN.setToolTip(_translate("MainWindow", "<html><head/><body><p>Multiple Stub Matching Network (Red de adaptación de múltiples stubs).</p></body></html>"))
        self.lbl_D1.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Distancia del stub número 1.</p></body></html>"))
        self.lbl_D2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Distancia del stub número 2.</p></body></html>"))
        self.lbl_DN.setToolTip(_translate("MainWindow", "<html><head/><body><p>Distancia del stub número N.</p></body></html>"))
        self.lbl_L1.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Longitud del stub número 1.</p></body></html>"))
        self.lbl_L2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Longitud del stub número 2.</p></body></html>"))
        self.lbl_LNm1.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Longitud del stub número N-1.</p></body></html>"))
        self.lbl_LN.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Longitud del stub número N.</p></body></html>"))
        self.lbl_Zin.setToolTip(_translate("MainWindow", "<html><head/><body><p>Impedancia vista desde el plano de adaptación d=d<span style=\" vertical-align:sub;\">A </span>.</p></body></html>"))
        self.lbl_Zc.setToolTip(_translate("MainWindow", "<html><head/><body><p>Impedancia característica de la línea de transmisión.</p></body></html>"))
        self.menuProyecto.setTitle(_translate("MainWindow", "Proyecto"))
        self.actionCargar.setText(_translate("MainWindow", "Cargar"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionReiniciar.setText(_translate("MainWindow", "Reiniciar"))
        self.actionManual_de_usuario.setText(_translate("MainWindow", "Manual de usuario"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

