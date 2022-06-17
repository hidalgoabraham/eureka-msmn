# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'linea_plana.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(460, 321)
        Dialog.setMinimumSize(QtCore.QSize(460, 321))
        Dialog.setMaximumSize(QtCore.QSize(460, 321))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("minilogo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(1.0)
        Dialog.setStyleSheet(" background-color: rgb(49, 58, 67);")
        Dialog.setModal(False)
        self.pbtn = QtWidgets.QPushButton(Dialog)
        self.pbtn.setGeometry(QtCore.QRect(350, 280, 84, 31))
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
        self.gpbx_conductores = QtWidgets.QGroupBox(Dialog)
        self.gpbx_conductores.setGeometry(QtCore.QRect(290, 10, 161, 81))
        self.gpbx_conductores.setStyleSheet("QGroupBox {\n"
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
        self.gpbx_conductores.setObjectName("gpbx_conductores")
        self.lbl_urc = QtWidgets.QLabel(self.gpbx_conductores)
        self.lbl_urc.setGeometry(QtCore.QRect(52, 20, 31, 21))
        self.lbl_urc.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_urc.setObjectName("lbl_urc")
        self.lbl_Dc = QtWidgets.QLabel(self.gpbx_conductores)
        self.lbl_Dc.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.lbl_Dc.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_Dc.setObjectName("lbl_Dc")
        self.linedit_urc = QtWidgets.QLineEdit(self.gpbx_conductores)
        self.linedit_urc.setGeometry(QtCore.QRect(80, 20, 61, 20))
        self.linedit_urc.setStyleSheet("QLineEdit{\n"
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
        self.linedit_urc.setObjectName("linedit_urc")
        self.linedit_Dc = QtWidgets.QLineEdit(self.gpbx_conductores)
        self.linedit_Dc.setGeometry(QtCore.QRect(80, 50, 61, 20))
        self.linedit_Dc.setStyleSheet("QLineEdit{\n"
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
        self.linedit_Dc.setObjectName("linedit_Dc")
        self.gpbx_dielectrico = QtWidgets.QGroupBox(Dialog)
        self.gpbx_dielectrico.setGeometry(QtCore.QRect(290, 100, 161, 111))
        self.gpbx_dielectrico.setStyleSheet("QGroupBox {\n"
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
        self.gpbx_dielectrico.setObjectName("gpbx_dielectrico")
        self.lbl_Dd = QtWidgets.QLabel(self.gpbx_dielectrico)
        self.lbl_Dd.setGeometry(QtCore.QRect(12, 80, 61, 16))
        self.lbl_Dd.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_Dd.setObjectName("lbl_Dd")
        self.lbl_urd = QtWidgets.QLabel(self.gpbx_dielectrico)
        self.lbl_urd.setGeometry(QtCore.QRect(52, 20, 31, 16))
        self.lbl_urd.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_urd.setObjectName("lbl_urd")
        self.lbl_erd = QtWidgets.QLabel(self.gpbx_dielectrico)
        self.lbl_erd.setGeometry(QtCore.QRect(52, 50, 21, 20))
        self.lbl_erd.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_erd.setObjectName("lbl_erd")
        self.linedit_urd = QtWidgets.QLineEdit(self.gpbx_dielectrico)
        self.linedit_urd.setGeometry(QtCore.QRect(80, 20, 61, 20))
        self.linedit_urd.setStyleSheet("QLineEdit{\n"
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
        self.linedit_urd.setObjectName("linedit_urd")
        self.linedit_erd = QtWidgets.QLineEdit(self.gpbx_dielectrico)
        self.linedit_erd.setGeometry(QtCore.QRect(80, 50, 61, 20))
        self.linedit_erd.setStyleSheet("QLineEdit{\n"
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
        self.linedit_erd.setObjectName("linedit_erd")
        self.linedit_Dd = QtWidgets.QLineEdit(self.gpbx_dielectrico)
        self.linedit_Dd.setGeometry(QtCore.QRect(80, 80, 61, 20))
        self.linedit_Dd.setStyleSheet("QLineEdit{\n"
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
        self.linedit_Dd.setObjectName("linedit_Dd")
        self.lbl_imagen = QtWidgets.QLabel(Dialog)
        self.lbl_imagen.setGeometry(QtCore.QRect(20, 80, 251, 131))
        self.lbl_imagen.setText("")
        self.lbl_imagen.setPixmap(QtGui.QPixmap("lineaplana.png"))
        self.lbl_imagen.setScaledContents(True)
        self.lbl_imagen.setObjectName("lbl_imagen")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 271, 301))
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
        self.linedit_dim2 = QtWidgets.QLineEdit(Dialog)
        self.linedit_dim2.setGeometry(QtCore.QRect(330, 250, 61, 20))
        self.linedit_dim2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.linedit_dim2.setStyleSheet("QLineEdit{\n"
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
        self.linedit_dim2.setObjectName("linedit_dim2")
        self.linedit_dim1 = QtWidgets.QLineEdit(Dialog)
        self.linedit_dim1.setGeometry(QtCore.QRect(330, 220, 61, 20))
        self.linedit_dim1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.linedit_dim1.setStyleSheet("QLineEdit{\n"
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
        self.linedit_dim1.setObjectName("linedit_dim1")
        self.lbl_dim1 = QtWidgets.QLabel(Dialog)
        self.lbl_dim1.setGeometry(QtCore.QRect(310, 220, 16, 20))
        self.lbl_dim1.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_dim1.setObjectName("lbl_dim1")
        self.cbx_dim1 = QtWidgets.QComboBox(Dialog)
        self.cbx_dim1.setGeometry(QtCore.QRect(395, 220, 35, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_dim1.sizePolicy().hasHeightForWidth())
        self.cbx_dim1.setSizePolicy(sizePolicy)
        self.cbx_dim1.setMinimumSize(QtCore.QSize(30, 0))
        self.cbx_dim1.setMaximumSize(QtCore.QSize(81, 20))
        self.cbx_dim1.setStyleSheet("QComboBox {\n"
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
        self.cbx_dim1.setIconSize(QtCore.QSize(0, 0))
        self.cbx_dim1.setObjectName("cbx_dim1")
        self.cbx_dim1.addItem("")
        self.cbx_dim1.addItem("")
        self.cbx_dim1.addItem("")
        self.cbx_dim2 = QtWidgets.QComboBox(Dialog)
        self.cbx_dim2.setGeometry(QtCore.QRect(395, 250, 35, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_dim2.sizePolicy().hasHeightForWidth())
        self.cbx_dim2.setSizePolicy(sizePolicy)
        self.cbx_dim2.setMinimumSize(QtCore.QSize(30, 0))
        self.cbx_dim2.setMaximumSize(QtCore.QSize(81, 20))
        self.cbx_dim2.setStyleSheet("QComboBox {\n"
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
        self.cbx_dim2.setIconSize(QtCore.QSize(0, 0))
        self.cbx_dim2.setObjectName("cbx_dim2")
        self.cbx_dim2.addItem("")
        self.cbx_dim2.addItem("")
        self.cbx_dim2.addItem("")
        self.lbl_dim2 = QtWidgets.QLabel(Dialog)
        self.lbl_dim2.setGeometry(QtCore.QRect(310, 250, 16, 20))
        self.lbl_dim2.setStyleSheet("QLabel{\n"
"color:rgb(238, 238, 238);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolTip{ \n"
"background-color: rgb(79, 93, 108); \n"
"color: rgb(238, 238, 238); \n"
"border: black solid 2px;\n"
"}")
        self.lbl_dim2.setObjectName("lbl_dim2")
        self.groupBox.raise_()
        self.pbtn.raise_()
        self.gpbx_conductores.raise_()
        self.gpbx_dielectrico.raise_()
        self.lbl_imagen.raise_()
        self.linedit_dim2.raise_()
        self.linedit_dim1.raise_()
        self.lbl_dim1.raise_()
        self.cbx_dim1.raise_()
        self.cbx_dim2.raise_()
        self.lbl_dim2.raise_()

        self.retranslateUi(Dialog)
        self.cbx_dim1.setCurrentIndex(2)
        self.cbx_dim2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Linea plana"))
        self.pbtn.setText(_translate("Dialog", "Ok"))
        self.gpbx_conductores.setTitle(_translate("Dialog", "Conductores"))
        self.lbl_urc.setToolTip(_translate("Dialog", "<html><head/><body><p>Permeabilidad magnética relativa de los conductores.</p></body></html>"))
        self.lbl_urc.setText(_translate("Dialog", "μᵣ :"))
        self.lbl_Dc.setToolTip(_translate("Dialog", "<html><head/><body><p>Conductividad de los conductores.</p></body></html>"))
        self.lbl_Dc.setText(_translate("Dialog", "σ (MS/m):"))
        self.gpbx_dielectrico.setTitle(_translate("Dialog", "Dieléctrico"))
        self.lbl_Dd.setToolTip(_translate("Dialog", "<html><head/><body><p>Conductividad del dieléctrico.</p></body></html>"))
        self.lbl_Dd.setText(_translate("Dialog", "σ (pS/m):"))
        self.lbl_urd.setToolTip(_translate("Dialog", "<html><head/><body><p>Permeabilidad magnética relativa del dieléctrico.</p></body></html>"))
        self.lbl_urd.setText(_translate("Dialog", "μᵣ :"))
        self.lbl_erd.setToolTip(_translate("Dialog", "<html><head/><body><p>Permitividad eléctrica relativa del dieléctrico.</p></body></html>"))
        self.lbl_erd.setText(_translate("Dialog", "εᵣ :"))
        self.lbl_dim1.setToolTip(_translate("Dialog", "<html><head/><body><p>Separación entre los conductores.</p></body></html>"))
        self.lbl_dim1.setText(_translate("Dialog", "d:"))
        self.cbx_dim1.setCurrentText(_translate("Dialog", "mm"))
        self.cbx_dim1.setItemText(0, _translate("Dialog", "in"))
        self.cbx_dim1.setItemText(1, _translate("Dialog", "cm"))
        self.cbx_dim1.setItemText(2, _translate("Dialog", "mm"))
        self.cbx_dim2.setCurrentText(_translate("Dialog", "mm"))
        self.cbx_dim2.setItemText(0, _translate("Dialog", "in"))
        self.cbx_dim2.setItemText(1, _translate("Dialog", "cm"))
        self.cbx_dim2.setItemText(2, _translate("Dialog", "mm"))
        self.lbl_dim2.setToolTip(_translate("Dialog", "<html><head/><body><p>Ancho de los conductores.</p></body></html>"))
        self.lbl_dim2.setText(_translate("Dialog", "w:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

