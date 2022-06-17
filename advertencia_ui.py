# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advertencia.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(321, 164)
        Dialog.setMinimumSize(QtCore.QSize(321, 164))
        Dialog.setMaximumSize(QtCore.QSize(321, 164))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("warning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(" background-color: rgb(49, 58, 67);")
        self.lbl = QtWidgets.QLabel(Dialog)
        self.lbl.setGeometry(QtCore.QRect(20, 20, 281, 81))
        self.lbl.setStyleSheet("color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl.setText("")
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.pbtn = QtWidgets.QPushButton(Dialog)
        self.pbtn.setGeometry(QtCore.QRect(120, 110, 84, 31))
        self.pbtn.setStyleSheet("QPushButton {\n"
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
        self.pbtn.setAutoDefault(False)
        self.pbtn.setObjectName("pbtn")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 141))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    background-color: transparent;\n"
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
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox.raise_()
        self.lbl.raise_()
        self.pbtn.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "¡Error!"))
        self.pbtn.setText(_translate("Dialog", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

