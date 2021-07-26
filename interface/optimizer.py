# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optimizer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(364, 187)
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(30, 20, 301, 31))
        self.label_15.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.label_15.setObjectName("label_15")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 60, 301, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_3.setDecimals(4)
        self.doubleSpinBox_3.setMaximum(10000.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_2.addWidget(self.doubleSpinBox_3, 0, 1, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_4.setFont(font)
        self.doubleSpinBox_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_4.setDecimals(8)
        self.doubleSpinBox_4.setMaximum(10000.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_2.addWidget(self.doubleSpinBox_4, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Optimizer Gurobi</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "MIP GAP"))
        self.label_9.setText(_translate("Dialog", "Time Limit"))
        self.pushButton.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

