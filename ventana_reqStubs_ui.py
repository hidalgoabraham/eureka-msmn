# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_reqStubs.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(310, 280))
        MainWindow.setMaximumSize(QtCore.QSize(310, 280))
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
        self.gpbx_stubs = QtWidgets.QGroupBox(self.centralwidget)
        self.gpbx_stubs.setGeometry(QtCore.QRect(10, 0, 291, 251))
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
"}")
        self.gpbx_stubs.setObjectName("gpbx_stubs")
        self.cbx_dispostubs = QtWidgets.QComboBox(self.gpbx_stubs)
        self.cbx_dispostubs.setEnabled(False)
        self.cbx_dispostubs.setGeometry(QtCore.QRect(30, 180, 91, 20))
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
        self.lbl_cargastubs = QtWidgets.QLabel(self.gpbx_stubs)
        self.lbl_cargastubs.setGeometry(QtCore.QRect(100, 150, 41, 21))
        self.lbl_cargastubs.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_cargastubs.setObjectName("lbl_cargastubs")
        self.cbx_cargastubs = QtWidgets.QComboBox(self.gpbx_stubs)
        self.cbx_cargastubs.setGeometry(QtCore.QRect(143, 150, 121, 20))
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
        self.lbl_lmin = QtWidgets.QLabel(self.gpbx_stubs)
        self.lbl_lmin.setGeometry(QtCore.QRect(50, 80, 141, 16))
        self.lbl_lmin.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_lmin.setObjectName("lbl_lmin")
        self.linedit_lmin = QtWidgets.QLineEdit(self.gpbx_stubs)
        self.linedit_lmin.setGeometry(QtCore.QRect(193, 80, 71, 20))
        self.linedit_lmin.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.linedit_lmin.setStyleSheet("QLineEdit{\n"
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
        self.linedit_lmin.setObjectName("linedit_lmin")
        self.lbl_dmin = QtWidgets.QLabel(self.gpbx_stubs)
        self.lbl_dmin.setGeometry(QtCore.QRect(47, 115, 151, 16))
        self.lbl_dmin.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_dmin.setObjectName("lbl_dmin")
        self.linedit_dmin = QtWidgets.QLineEdit(self.gpbx_stubs)
        self.linedit_dmin.setGeometry(QtCore.QRect(193, 115, 71, 20))
        self.linedit_dmin.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.linedit_dmin.setStyleSheet("QLineEdit{\n"
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
        self.linedit_dmin.setObjectName("linedit_dmin")
        self.cbx_Nmax = QtWidgets.QComboBox(self.gpbx_stubs)
        self.cbx_Nmax.setGeometry(QtCore.QRect(15, 45, 191, 20))
        self.cbx_Nmax.setStyleSheet("QComboBox {\n"
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
        self.cbx_Nmax.setObjectName("cbx_Nmax")
        self.cbx_Nmax.addItem("")
        self.cbx_Nmax.addItem("")
        self.spnbx_Nmax = QtWidgets.QSpinBox(self.gpbx_stubs)
        self.spnbx_Nmax.setGeometry(QtCore.QRect(210, 45, 51, 21))
        self.spnbx_Nmax.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spnbx_Nmax.setStyleSheet("QSpinBox {\n"
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
"\n"
"\n"
"")
        self.spnbx_Nmax.setSpecialValueText("")
        self.spnbx_Nmax.setMinimum(1)
        self.spnbx_Nmax.setProperty("value", 1)
        self.spnbx_Nmax.setObjectName("spnbx_Nmax")
        self.pbtn_ok = QtWidgets.QPushButton(self.gpbx_stubs)
        self.pbtn_ok.setGeometry(QtCore.QRect(180, 195, 84, 25))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 310, 22))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MSMN"))
        self.gpbx_stubs.setTitle(_translate("MainWindow", "Parámetros de MSMN"))
        self.cbx_dispostubs.setItemText(0, _translate("MainWindow", "Paralelo"))
        self.lbl_cargastubs.setText(_translate("MainWindow", "Carga:"))
        self.cbx_cargastubs.setItemText(0, _translate("MainWindow", "Corto circuito"))
        self.cbx_cargastubs.setItemText(1, _translate("MainWindow", "Circuito abierto"))
        self.lbl_lmin.setText(_translate("MainWindow", "Longitud mínima  (mm):"))
        self.lbl_dmin.setText(_translate("MainWindow", "Distancia mínima  (mm):"))
        self.cbx_Nmax.setItemText(0, _translate("MainWindow", "Cantidad máxima de stubs:"))
        self.cbx_Nmax.setItemText(1, _translate("MainWindow", "Cantidad fija de stubs:"))
        self.pbtn_ok.setText(_translate("MainWindow", "Ok"))
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

