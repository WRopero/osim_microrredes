import sys
from  graficos_ces import *;
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sqlite3, datetime
import time



import os
import graficos_ce as gr



class Principal_g(QtWidgets.QMainWindow):
    def __init__(self, parent=None, dir_xlsx = None): 
        from PyQt5 import QtWidgets
        QtWidgets.QMainWindow.__init__(self,parent);
        self.ui = Ui_MainWindow();
        self.ui.setupUi(self);

        #Coloco color blanco de fondo a la APP
        self.palette = QtGui.QPalette();
#        self.palette.setColor(QtGui.QPalette.Background,QtCore.Qt.white);
        self.setPalette(self.palette);
        self.setWindowTitle("Study Case")
        #self.setWindowIcon(QtGui.QIcon('log.png'))
        
       #self.ui.clip = QtWidgets.QApplication.clipboard()
       # #Botones para abrir las ventanas de las otras funciones        
        self.ui.pushButton.clicked.connect(self.graficar)
       #self.ui.pushButton_4.clicked.connect(self.battery_bank)
       #self.ui.pushButton_2.clicked.connect(self.diesel_gen)
       #self.ui.pushButton_5.clicked.connect(self.project_data)
       #self.ui.pushButton_6.clicked.connect(self.optimizador)
       #self.ui.pushButton_3.clicked.connect(self.getxlsx)   
    


    def graficar(self):
        self.ui.pushButton.setEnabled(0);
        self.ui.pushButton.setText("Loading...");      
        self.repaint();
        try:
            rute_xlsx = self.ui.label.text()
            print(type(rute_xlsx),rute_xlsx) 
            fig = gr.graficos(rute_xlsx)
            self.ui.webEngineView.setHtml(fig[0].to_html(include_plotlyjs='cdn'))
            self.ui.webEngineView_2.setHtml(fig[1].to_html(include_plotlyjs='cdn'))
            self.ui.webEngineView_3.setHtml(fig[2].to_html(include_plotlyjs='cdn'))
            self.ui.webEngineView_4.setHtml(fig[3].to_html(include_plotlyjs='cdn'))
            self.ui.webEngineView_5.setHtml(fig[4].to_html(include_plotlyjs='cdn'))
            self.ui.webEngineView_6.setHtml(fig[5].to_html(include_plotlyjs='cdn'))
            
        except:
            print("Error") 



        self.ui.pushButton.setEnabled(1);
        self.ui.pushButton.setText("Plot");      
        self.repaint();  

    
def main():
    from PyQt5 import QtWidgets
    app=QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    ventana=Principal_g()
    ventana.show()
    sys.exit(app.exec_())
    
    
if __name__=='__main__':
    main(); 
   