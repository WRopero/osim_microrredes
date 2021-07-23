import sys
from project import *;
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sqlite3, datetime

import os
import funcion_tabla as ft

class Project(QtWidgets.QDialog):
    def __init__(self, parent=None): 
        from PyQt5 import QtWidgets
        QtWidgets.QDialog.__init__(self,parent);
        self.ui = Ui_Dialog();
        self.ui.setupUi(self);

        #Coloco color blanco de fondo a la APP
        self.palette = QtGui.QPalette();
#        self.palette.setColor(QtGui.QPalette.Background,QtCore.Qt.white);
        self.setPalette(self.palette);
        self.setWindowTitle("Project and Economic Data")
        
        #self.setWindowIcon(QtGui.QIcon('log.png'))
        #
        self.ui.clip = QtWidgets.QApplication.clipboard()
        #
        #self.ui.pushButton_6.clicked.connect(self.guardar_c)
        #
        conn = sqlite3.connect("config.db")          
        sql = "select * from project;"        
        df = pd.read_sql_query(sql, conn)

        conn.close()

        self.ui.doubleSpinBox_2.setValue(df.loc[0,'life_time'])     
        self.ui.doubleSpinBox_4.setValue(df.loc[0,'lpsp_max'])   
        self.ui.doubleSpinBox.setValue(df.loc[0,'ir'])   
        self.ui.doubleSpinBox_3.setValue(df.loc[0,'cens'])   
        self.ui.doubleSpinBox_5.setValue(df.loc[0,'tax_reduction'])   
        self.ui.doubleSpinBox_6.setValue(df.loc[0,'T1'])
        self.ui.doubleSpinBox_7.setValue(df.loc[0,'T2'])   
        self.ui.doubleSpinBox_8.setValue(df.loc[0,'corporate_tax']) 
        

        
        
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
                
    def guardar_c(self):
        
        try:
            print("Hola")
        #    name = (self.ui.lineEdit_3.text()).upper()
        #    empresa = (self.ui.lineEdit_4.text()).upper()
        #    cargo = (self.ui.lineEdit_5.text()).capitalize()
        #    correo = (self.ui.lineEdit_7.text()).lower()
        #    celular = self.ui.lineEdit_9.text()   +" " + self.ui.lineEdit_6.text()  
        #    fijo = self.ui.lineEdit_10.text()   +" " +self.ui.lineEdit_8.text()
        #    ubica = (self.ui.lineEdit_11.text()).capitalize()
        #    pagina_web = (self.ui.lineEdit_12.text()).lower()
        #    servicio = (self.ui.textEdit.toPlainText()).capitalize()
        #    
        #    conn = sqlite3.connect("BD_COMPRAS.sqlite3")    
        #    
        #    argumentos = (name, empresa, cargo, correo,celular,fijo,ubica,pagina_web,servicio, datetime.date.today())
        #    sql = """INSERT INTO CONTACTOS_GENERAL (Nombre,Empresa,Cargo,correo,Tel_Celular,Tel_Fijo,Ubicacion,Pagina_web,Tipo_servicio,Fecha_ingreso)
        #    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        #    try:
        #        conn.execute(sql, argumentos)
        #        conn.commit()
        #        conn.close()
        #    except:
        #        from PyQt5 import  QtWidgets
        #        msg=QtWidgets.QMessageBox()
        #        msg.about(self, "Error", "Ha ocurrido un error al guardar los datos.")
        #        
        #    self.ui.label_15.setText('<html><head/><body><p align="center"><span style=" font-size:10pt; color:#37a651;">%s</span></p></body></html>'%("GUARDADO - "+ name))
        #    self.ui.lineEdit_3.clear()
        #    self.ui.lineEdit_4.clear()
        #    self.ui.lineEdit_5.clear()
        #    self.ui.lineEdit_7.clear()
        #    self.ui.lineEdit_6.clear()
        #    self.ui.lineEdit_8.clear()
        #    self.ui.lineEdit_11.clear()
        #    self.ui.lineEdit_12.clear()
        #    self.ui.textEdit.clear()
            
        
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
    ventana=Project()
    ventana.show()
    sys.exit(app.exec_())
    
    
if __name__=='__main__':
    main(); 
   