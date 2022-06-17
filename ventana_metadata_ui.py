# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_metadata.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(592, 376)
        Dialog.setMinimumSize(QtCore.QSize(592, 376))
        Dialog.setMaximumSize(QtCore.QSize(592, 376))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("minilogo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(" background-color: rgb(49, 58, 67);")
        self.lbl_ordenar = QtWidgets.QLabel(Dialog)
        self.lbl_ordenar.setGeometry(QtCore.QRect(20, 23, 81, 16))
        self.lbl_ordenar.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.lbl_ordenar.setObjectName("lbl_ordenar")
        self.pbtn_ordenar = QtWidgets.QPushButton(Dialog)
        self.pbtn_ordenar.setGeometry(QtCore.QRect(300, 16, 121, 31))
        self.pbtn_ordenar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pbtn_ordenar.setStyleSheet("QPushButton {\n"
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
        self.pbtn_ordenar.setObjectName("pbtn_ordenar")
        self.scllarea = QtWidgets.QScrollArea(Dialog)
        self.scllarea.setGeometry(QtCore.QRect(10, 60, 571, 301))
        self.scllarea.setStyleSheet("QScrollBar:vertical {\n"
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
"}")
        self.scllarea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scllarea.setWidgetResizable(True)
        self.scllarea.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.scllarea.setObjectName("scllarea")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 571, 55))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_5.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_5.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.layout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layout.setContentsMargins(-1, -1, -1, 0)
        self.layout.setObjectName("layout")
        self.lbl_cpu = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_cpu.sizePolicy().hasHeightForWidth())
        self.lbl_cpu.setSizePolicy(sizePolicy)
        self.lbl_cpu.setMinimumSize(QtCore.QSize(90, 0))
        self.lbl_cpu.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border: 2px solid;\n"
"border-color:rgb(85,170,255);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.lbl_cpu.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_cpu.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_cpu.setIndent(4)
        self.lbl_cpu.setObjectName("lbl_cpu")
        self.layout.addWidget(self.lbl_cpu, 0, 1, 1, 1)
        self.lbl_tiempo = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_tiempo.sizePolicy().hasHeightForWidth())
        self.lbl_tiempo.setSizePolicy(sizePolicy)
        self.lbl_tiempo.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_tiempo.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border: 2px solid;\n"
"border-color:rgb(85,170,255);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.lbl_tiempo.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_tiempo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tiempo.setIndent(4)
        self.lbl_tiempo.setObjectName("lbl_tiempo")
        self.layout.addWidget(self.lbl_tiempo, 0, 3, 1, 1)
        self.lbl_ram = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_ram.sizePolicy().hasHeightForWidth())
        self.lbl_ram.setSizePolicy(sizePolicy)
        self.lbl_ram.setMinimumSize(QtCore.QSize(120, 40))
        self.lbl_ram.setMaximumSize(QtCore.QSize(90, 40))
        self.lbl_ram.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border: 2px solid;\n"
"border-color:rgb(85,170,255);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_ram.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_ram.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ram.setIndent(4)
        self.lbl_ram.setObjectName("lbl_ram")
        self.layout.addWidget(self.lbl_ram, 0, 2, 1, 1)
        self.lbl_algoritmo = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_algoritmo.sizePolicy().hasHeightForWidth())
        self.lbl_algoritmo.setSizePolicy(sizePolicy)
        self.lbl_algoritmo.setMinimumSize(QtCore.QSize(220, 0))
        self.lbl_algoritmo.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border: 2px solid;\n"
"border-color:rgb(85,170,255);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"")
        self.lbl_algoritmo.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_algoritmo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_algoritmo.setIndent(0)
        self.lbl_algoritmo.setObjectName("lbl_algoritmo")
        self.layout.addWidget(self.lbl_algoritmo, 0, 0, 1, 1)
        self.scllarea.setWidget(self.scrollAreaWidgetContents_5)
        self.cbx_ordenar = QtWidgets.QComboBox(Dialog)
        self.cbx_ordenar.setGeometry(QtCore.QRect(100, 20, 181, 22))
        self.cbx_ordenar.setStyleSheet("QComboBox {\n"
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
        self.cbx_ordenar.setObjectName("cbx_ordenar")
        self.cbx_ordenar.addItem("")
        self.cbx_ordenar.addItem("")
        self.cbx_ordenar.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Rendimiento computacional"))
        self.lbl_ordenar.setText(_translate("Dialog", "Ordenar por:"))
        self.pbtn_ordenar.setText(_translate("Dialog", "Menor a mayor ↓"))
        self.lbl_cpu.setText(_translate("Dialog", "Uso de CPU\n"
"(%)"))
        self.lbl_tiempo.setText(_translate("Dialog", "Tiempo de\n"
"búsqueda (s)"))
        self.lbl_ram.setToolTip(_translate("Dialog", "<html><head/><body><p>Memoria RAM empleada.</p></body></html>"))
        self.lbl_ram.setText(_translate("Dialog", "Memoria máxima\n"
"utilizada (MiB)"))
        self.lbl_algoritmo.setText(_translate("Dialog", "Algoritmo"))
        self.cbx_ordenar.setItemText(0, _translate("Dialog", "Uso de CPU"))
        self.cbx_ordenar.setItemText(1, _translate("Dialog", "Memoria máxima utilizada"))
        self.cbx_ordenar.setItemText(2, _translate("Dialog", "Tiempo de búsqueda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

