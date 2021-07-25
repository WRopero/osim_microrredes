import sys
from battery import *;
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sqlite3, datetime

import os
import funcion_tabla as ft

class Battery(QtWidgets.QDialog):
    def __init__(self, parent=None): 
        from PyQt5 import QtWidgets
        QtWidgets.QDialog.__init__(self,parent);
        self.ui = Ui_Dialog();
        self.ui.setupUi(self);

        #Coloco color blanco de fondo a la APP
        self.palette = QtGui.QPalette();
#        self.palette.setColor(QtGui.QPalette.Background,QtCore.Qt.white);
        self.setPalette(self.palette);
        self.setWindowTitle("Battery")
        
        #self.setWindowIcon(QtGui.QIcon('log.png'))
        #
        self.ui.clip = QtWidgets.QApplication.clipboard()
        #
        #self.ui.pushButton_6.clicked.connect(self.guardar_c)
        #
        conn = sqlite3.connect("config.db")          
        sql = "select * from battery;"        
        df = pd.read_sql_query(sql, conn)

        conn.close()

        self.ui.doubleSpinBox_18.setValue(df.loc[0,'mb'])     
        self.ui.doubleSpinBox_4.setValue(df.loc[0,'self_dis'])   
        self.ui.doubleSpinBox.setValue(df.loc[0,'c_rate'])   
        self.ui.doubleSpinBox_3.setValue(df.loc[0,'dod_max'])   
        self.ui.doubleSpinBox_5.setValue(df.loc[0,'cycles_max'])   
        self.ui.doubleSpinBox_6.setValue(df.loc[0,'cbat'])
        self.ui.doubleSpinBox_7.setValue(df.loc[0,'pbat_cell'])   
        self.ui.doubleSpinBox_8.setValue(df.loc[0,'vdc_sist']) 
        self.ui.doubleSpinBox_9.setValue(df.loc[0,'vdc_bc'])
        self.ui.doubleSpinBox_2.setValue(df.loc[0,'ninv'])
        self.ui.doubleSpinBox_11.setValue(df.loc[0,'oym_factor'])
        self.ui.doubleSpinBox_12.setValue(df.loc[0,'factor_ini_inv'])
        self.ui.doubleSpinBox_13.setValue(df.loc[0,'lifecycle'])
        self.ui.doubleSpinBox_14.setValue(df.loc[0,'cki_bat'])
        self.ui.doubleSpinBox_15.setValue(df.loc[0,'nd'])
        self.ui.doubleSpinBox_16.setValue(df.loc[0,'nc'])       
        
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
            mb=float(self.ui.doubleSpinBox_18.text())     
            self_dis =float(self.ui.doubleSpinBox_4.text())   
            c_rate=float(self.ui.doubleSpinBox.text())   
            dod_max=float(self.ui.doubleSpinBox_3.text())   
            cycles_max=float(self.ui.doubleSpinBox_5.text())   
            cbat=float(self.ui.doubleSpinBox_6.text())
            pbat_cell=float(self.ui.doubleSpinBox_7.text())   
            vdc_sist=float(self.ui.doubleSpinBox_8.text()) 
            vdc_bc=float(self.ui.doubleSpinBox_9.text())
            ninv=float(self.ui.doubleSpinBox_2.text())
            oym_factor=float(self.ui.doubleSpinBox_11.text())
            factor_ini_inv=float(self.ui.doubleSpinBox_12.text())
            lifecycle=float(self.ui.doubleSpinBox_13.text())
            cki_bat=float(self.ui.doubleSpinBox_14.text())
            nd=float(self.ui.doubleSpinBox_15.text())
            nc=float(self.ui.doubleSpinBox_16.text())          

            
            conn = sqlite3.connect("config.db")
            sql = f"""UPDATE battery SET 
            mb = {mb}, 
            self_dis = {self_dis},
            c_rate = {c_rate},
            dod_max = {dod_max},
            cycles_max = {cycles_max},
            cbat = {cbat},
            pbat_cell = {pbat_cell},
            vdc_bc = {vdc_bc},
            ninv = {ninv},
            oym_factor = {oym_factor},
            factor_ini_inv = {factor_ini_inv},
            lifecycle= {lifecycle},
            cki_bat = {cki_bat},
            nd = {nd},
            nc = {nc};"""

            
            conn.execute(sql)
            conn.commit()
            conn.close()

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
    ventana=Battery()
    ventana.show()
    sys.exit(app.exec_())
    
    
if __name__=='__main__':
    main(); 
   