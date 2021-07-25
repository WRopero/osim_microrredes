import sys
from pv import *;
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sqlite3, datetime

import os
import funcion_tabla as ft

class PV(QtWidgets.QDialog):
    def __init__(self, parent=None): 
        from PyQt5 import QtWidgets
        QtWidgets.QDialog.__init__(self,parent);
        self.ui = Ui_Dialog();
        self.ui.setupUi(self);

        #Coloco color blanco de fondo a la APP
        self.palette = QtGui.QPalette();
#        self.palette.setColor(QtGui.QPalette.Background,QtCore.Qt.white);
        self.setPalette(self.palette);
        self.setWindowTitle("PV")
        
        #self.setWindowIcon(QtGui.QIcon('log.png'))
        #
        #self.ui.clip = QtWidgets.QApplication.clipboard()
        #
        #self.ui.pushButton_6.clicked.connect(self.guardar_c)
        #
        #self.ui.pushButton.clicked.connect(self.conName)
        #self.ui.pushButton_2.clicked.connect(self.conEmpresa)
        #self.ui.pushButton_5.clicked.connect(self.conActividad)
        #self.ui.pushButton_7.clicked.connect(self.borrar_id)

        conn = sqlite3.connect("config.db")          
        sql = "select * from pv_cell;"        
        df = pd.read_sql_query(sql, conn)

        conn.close()

        self.ui.doubleSpinBox_2.setValue(df.loc[0,'ppvstc'])     
        self.ui.doubleSpinBox_4.setValue(df.loc[0,'npv'])   
        self.ui.doubleSpinBox.setValue(df.loc[0,'noct'])   
        self.ui.doubleSpinBox_3.setValue(df.loc[0,'cpv'])   
        self.ui.doubleSpinBox_5.setValue(df.loc[0,'fpv'])   
        self.ui.doubleSpinBox_6.setValue(df.loc[0,'oym_factor'])
        self.ui.doubleSpinBox_7.setValue(df.loc[0,'cki_pv'])   
        self.ui.doubleSpinBox_8.setValue(df.loc[0,'ptc_coef'])           

        self.ui.pushButton.clicked.connect(self.guardar) 
        

        
        
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
            ppvstc=float(self.ui.doubleSpinBox_2.text())     
            npv=float(self.ui.doubleSpinBox_4.text())   
            noct=float(self.ui.doubleSpinBox.text())   
            cpv=float(self.ui.doubleSpinBox_3.text())   
            fpv=float(self.ui.doubleSpinBox_5.text())   
            oym_factor=float(self.ui.doubleSpinBox_6.text())
            cki_pv=float(self.ui.doubleSpinBox_7.text())   
            ptc_coef=float(self.ui.doubleSpinBox_8.text())
            
            conn = sqlite3.connect("config.db")
            sql = f"""UPDATE pv_cell SET 
            ppvstc = {ppvstc}, 
            npv = {npv},
            noct = {noct},
            cpv = {cpv},
            fpv = {fpv},
            oym_factor = {oym_factor},
            cki_pv = {cki_pv},
            ptc_coef = {ptc_coef};"""

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
    ventana=PV()
    ventana.show()
    sys.exit(app.exec_())
    
    
if __name__=='__main__':
    main(); 
   