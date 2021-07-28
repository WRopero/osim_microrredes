import sys
from interface.results import *;
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sqlite3, datetime


import os
import interface.funcion_tabla as ft
import interface.graficos_results as gre

class Principal_r(QtWidgets.QMainWindow):
    def __init__(self, parent=None): 
        from PyQt5 import QtWidgets
        QtWidgets.QMainWindow.__init__(self,parent);
        self.ui = Ui_MainWindow();
        self.ui.setupUi(self);

        #Coloco color blanco de fondo a la APP
        self.palette = QtGui.QPalette();
#        self.palette.setColor(QtGui.QPalette.Background,QtCore.Qt.white);
        self.setPalette(self.palette);
        self.setWindowTitle("Result Data")
        #self.setWindowIcon(QtGui.QIcon('log.png'))
        self.ui.lineEdit.setText("10")
        self.ui.lineEdit_4.setText("10")
        self.ui.lineEdit_7.setText("10")
        
        self.ui.clip = QtWidgets.QApplication.clipboard()
        
        fig =gre._graficos_resultados()
        self.ui.webEngineView_6.setHtml(fig[0].to_html(include_plotlyjs='cdn'))
        self.ui.webEngineView_5.setHtml(fig[5].to_html(include_plotlyjs='cdn'))
        self.ui.webEngineView_7.setHtml(fig[7].to_html(include_plotlyjs='cdn'))
        self.ui.webEngineView_8.setHtml(fig[8].to_html(include_plotlyjs='cdn'))
        self.ui.webEngineView_20.setHtml(fig[4].to_html(include_plotlyjs='cdn'))
        self.ui.webEngineView_17.setHtml(fig[1].to_html(include_plotlyjs='cdn'))
        self.ui.webEngineView_18.setHtml(fig[6].to_html(include_plotlyjs='cdn'))
        self.ui.webEngineView_19.setHtml(fig[2].to_html(include_plotlyjs='cdn'))
        self.ui.webEngineView_10.setHtml(fig[3].to_html(include_plotlyjs='cdn'))

        ft.tabla(fig[9],self)
        ft.tabla2(fig[10],self)
        #self.ui.pushButton_2.clicked.connect(self.graficar1)
        
        #self.ui.pushButton_7.clicked.connect(self.graficar2)
        
        #self.ui.pushButton_4.clicked.connect(self.graficar3)
         #Botones para abrir las ventanas de las otras funciones        
        #self.ui.pushButton.clicked.connect(self.pv_array)
    
    def graficar1(self):
        self.ui.pushButton_2.setEnabled(0);
        self.ui.pushButton_2.setText("Loading...");      
        self.repaint();
        try:
            
            
            fig =gre._graficos_resultados()
            self.ui.webEngineView_6.setHtml(fig[0].to_html(include_plotlyjs='cdn'))
            self.ui.webEngineView_5.setHtml(fig[1].to_html(include_plotlyjs='cdn'))
            self.ui.webEngineView_7.setHtml(fig[2].to_html(include_plotlyjs='cdn'))
            self.ui.webEngineView_8.setHtml(fig[3].to_html(include_plotlyjs='cdn'))
            
        except:
            print("Error") 



        self.ui.pushButton_2.setEnabled(1);
        self.ui.pushButton_2.setText("Plot");      
        self.repaint();  

    def graficar2(self):
        self.ui.pushButton_7.setEnabled(0);
        self.ui.pushButton_7.setText("Loading...");      
        self.repaint();
        try:
            
             
            fig =gre._graficos_resultados()
            self.ui.webEngineView_10.setHtml(fig[4].to_html(include_plotlyjs='cdn'))
            self.ui.webEngineView_9.setHtml(fig[5].to_html(include_plotlyjs='cdn'))
            self.ui.webEngineView_12.setHtml(fig[6].to_html(include_plotlyjs='cdn'))
            self.ui.webEngineView_11.setHtml(fig[7].to_html(include_plotlyjs='cdn'))
            
        except:
            print("Error") 



        self.ui.pushButton_7.setEnabled(1);
        self.ui.pushButton_7.setText("Plot");      
        self.repaint();  
    
    def graficar3(self):
        self.ui.pushButton_4.setEnabled(0);
        self.ui.pushButton_4.setText("Loading...");      
        self.repaint();
        try:
            
            
            fig =gre._graficos_resultados()

            self.ui.webEngineView_10.setHtml(fig[8].to_html(include_plotlyjs='cdn'))
            #self.ui.webEngineView_9.setHtml(fig[9].to_html(include_plotlyjs='cdn'))
            
        except:
            print("Error") 



        self.ui.pushButton_4.setEnabled(1);
        self.ui.pushButton_4.setText("Plot");      
        self.repaint();  
        #         
def main():
    from PyQt5 import QtWidgets
    app=QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    ventana=Principal_r()
    ventana.show()
    sys.exit(app.exec_())
    
    
if __name__=='__main__':
    main(); 
   