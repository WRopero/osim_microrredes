# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graficos_ce.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 816)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.webEngineView_4 = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView_4.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView_4.setObjectName("webEngineView_4")
        self.gridLayout_2.addWidget(self.webEngineView_4, 1, 0, 1, 1)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.gridLayout_2.addWidget(self.webEngineView, 0, 0, 1, 1)
        self.webEngineView_2 = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView_2.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView_2.setObjectName("webEngineView_2")
        self.gridLayout_2.addWidget(self.webEngineView_2, 0, 1, 1, 1)
        self.webEngineView_3 = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView_3.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView_3.setObjectName("webEngineView_3")
        self.gridLayout_2.addWidget(self.webEngineView_3, 1, 1, 1, 1)
        self.webEngineView_5 = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView_5.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView_5.setObjectName("webEngineView_5")
        self.gridLayout_2.addWidget(self.webEngineView_5, 2, 0, 1, 1)
        self.webEngineView_6 = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView_6.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView_6.setObjectName("webEngineView_6")
        self.gridLayout_2.addWidget(self.webEngineView_6, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 2, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1070, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Plot"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">xlsx</p></body></html>"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
