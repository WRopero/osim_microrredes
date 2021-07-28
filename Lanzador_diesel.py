import sys
from interface.diesel import *;
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sqlite3, datetime

import os
import interface.funcion_tabla as ft

class Diesel(QtWidgets.QDialog):
    def __init__(self, parent=None): 
        from PyQt5 import QtWidgets
        QtWidgets.QDialog.__init__(self,parent);
        self.ui = Ui_Dialog();
        self.ui.setupUi(self);

        #Coloco color blanco de fondo a la APP
        self.palette = QtGui.QPalette();
#        self.palette.setColor(QtGui.QPalette.Background,QtCore.Qt.white);
        self.setPalette(self.palette);
        self.setWindowTitle("Diesel Generator")
        
        #self.setWindowIcon(QtGui.QIcon('log.png'))
        #
        self.ui.clip = QtWidgets.QApplication.clipboard()
        #
        conn = sqlite3.connect("config.db")          
        sql = "select * from diesel;"        
        df = pd.read_sql_query(sql, conn)

        conn.close()
        self.ui.doubleSpinBox_4.setValue(df.loc[0,'cki_dg'])  
        self.ui.doubleSpinBox.setValue(df.loc[0,'pdg_min'])  
        self.ui.doubleSpinBox_3.setValue(df.loc[0,'n_dg'])     
        self.ui.doubleSpinBox_5.setValue(df.loc[0,'cdg'])   
        self.ui.doubleSpinBox_6.setValue(df.loc[0,'factor_ini_inv'])   
        self.ui.doubleSpinBox_7.setValue(df.loc[0,'cec'])   
        self.ui.doubleSpinBox_8.setValue(df.loc[0,'cel'])   
        self.ui.doubleSpinBox_9.setValue(df.loc[0,'lifecycle'])
        self.ui.doubleSpinBox_10.setValue(df.loc[0,'alc'])   
        self.ui.doubleSpinBox_11.setValue(df.loc[0,'afc'])  

        self.ui.pushButton_2.clicked.connect(self.guardar)        
        
    def keyPressEvent(self, e):
        if (e.modifiers() & QtCore.Qt.ControlModifier):
            selected = self.ui.tableWidget.selectedRanges()

            if e.key() == QtCore.Qt.Key_C: #copy
                s = '\t'+"\t".join([str(self.ui.tableWidget.horizontalHeaderItem(i).text()) for i in range(selected[0].leftColumn(), selected[0].rightColumn()+1)])
                s = s + '\n'
                s = "";
                for r in range(selected[0].topRow(), selected[0].bottomRow()+1):
                    try:
                        s += self.ui.tableWidget.verticalHeaderItem(r).text() + '\t'
                    except AttributeError:
                            s += "\t"
                    for c in range(selected[0].leftColumn(), selected[0].rightColumn()+1):
                        try:
                            s += str(self.ui.tableWidget.item(r,c).text()) + "\t"
                        except AttributeError:
                            s += "\t"
                    s = s[:-1] + "\n" #eliminate last '\t'
                self.ui.clip.setText(s)
                
    def guardar(self):
        
        try:
            cki_dg = float(self.ui.doubleSpinBox_4.text())  
            pdg_min = float(self.ui.doubleSpinBox.text()) 
            n_dg = float( self.ui.doubleSpinBox_3.text())   
            cdg = float( self.ui.doubleSpinBox_5.text()) 
            factor_ini_inv= float( self.ui.doubleSpinBox_6.text())
            cec = float(self.ui.doubleSpinBox_7.text())  
            cel = float(self.ui.doubleSpinBox_8.text()) 
            lifecycle = float(self.ui.doubleSpinBox_9.text())
            alc = float(self.ui.doubleSpinBox_10.text())   
            afc = float(self.ui.doubleSpinBox_11.text())             

            
            conn = sqlite3.connect("config.db")
            sql = f"""UPDATE diesel SET 
            cki_dg = {cki_dg}, 
            pdg_min = {pdg_min},
            n_dg = {n_dg},
            cdg = {cdg},
            factor_ini_inv = {factor_ini_inv},
            cec = {cec},
            cel = {cel},
            lifecycle = {lifecycle},
            alc = {alc},
            afc = {afc};"""

            try:
                conn.execute(sql)
                conn.commit()
                conn.close()
            except:
                from PyQt5 import  QtWidgets                
                msg=QtWidgets.QMessageBox()
                msg.about(self, "Error", "Ha ocurrido un error al guardar los datos.")
            from PyQt5 import  QtWidgets
            msg=QtWidgets.QMessageBox()
            msg.about(self, "Ok", "The data have been updated")
       
        
        except:
            import traceback
            tb = sys.exc_info()[2]
            tbinfo = traceback.format_tb(tb)[0]
            pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
            from PyQt5 import  QtWidgets
            msg=QtWidgets.QMessageBox()
            msg.about(self, "Error", "Error en consulta. "+ pymsg) 
            self.ui.label_15.setText('<html><head/><body><p align="center"><span style=" font-size:10pt; color:#37a651;">%s</span></p></body></html>'%("ERROR"))
                
            
    def borrar_id(self):
        print("Hola")
        
    #    conn = sqlite3.connect("BD_COMPRAS.sqlite3")
    #    cur = conn.cursor()
    #    
    #    try:
    #        values = (int(self.ui.lineEdit_13.text()), )
    #        cur.execute("delete from CONTACTOS_GENERAL where Codigo=?", values)
    #        conn.commit()
    #        self.ui.label_18.setText('<html><head/><body><p align="center"><span style=" font-size:10pt; color:#ff0000;">%s</span></p></body></html>'%("BORRADO - "+self.ui.lineEdit_13.text()))
    #    except:
    #        import traceback
    #        tb = sys.exc_info()[2]
    #        tbinfo = traceback.format_tb(tb)[0]
    #        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    #        from PyQt5 import  QtWidgets
    #        msg=QtWidgets.QMessageBox()
    #        msg.about(self, "Error", "Error en consulta. "+ pymsg)
    #        
    #    conn.close()        
        
        
def main():
    from PyQt5 import QtWidgets
    app=QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    ventana=Diesel()
    ventana.show()
    sys.exit(app.exec_())
    
    
if __name__=='__main__':
    main(); 
   