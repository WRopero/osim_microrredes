import sys
from interface.main import *;
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sqlite3, datetime
import Lanzador_pv as pv
import Lanzador_diesel as dg
import Lanzador_battery as bat
import Lanzador_project as proj
import Lanzador_optimizer as op    
import Lanzador_graficos_ce as gr 

import os
import funcion_tabla as ft

class Principal_c(QtWidgets.QMainWindow):
    def __init__(self, parent=None): 
        from PyQt5 import QtWidgets
        QtWidgets.QMainWindow.__init__(self,parent);
        self.ui = Ui_MainWindow();
        self.ui.setupUi(self);

        #Coloco color blanco de fondo a la APP
        self.palette = QtGui.QPalette();
#        self.palette.setColor(QtGui.QPalette.Background,QtCore.Qt.white);
        self.setPalette(self.palette);
        self.setWindowTitle("optimal Sizing Islanded Microgrids")
        #self.setWindowIcon(QtGui.QIcon('log.png'))
        
        self.ui.clip = QtWidgets.QApplication.clipboard()
         #Botones para abrir las ventanas de las otras funciones        
        self.ui.pushButton.clicked.connect(self.pv_array)
        self.ui.pushButton_4.clicked.connect(self.battery_bank)
        self.ui.pushButton_2.clicked.connect(self.diesel_gen)
        self.ui.pushButton_5.clicked.connect(self.project_data)
        self.ui.pushButton_6.clicked.connect(self.optimizador)
        self.ui.pushButton_3.clicked.connect(self.getxlsx)   

    def getxlsx(self):
        self.ui.pushButton_3.setEnabled(0);
        self.ui.pushButton_3.setText("Loading...");      
        self.repaint()        
        import os
        import pandas as pd
        
        self.filename=QtWidgets.QFileDialog.getOpenFileName(self,"Seleccionar Documento",os.getcwd(),"Files (*.xlsx);;Files (*.TIF);;Files (*.Docx);;Files (*.Pdf);;Files (*.Doc);;All Files (*.*)")
        if self.filename !=0:
                
            try:
                self.ui.lineEdit.setText(self.filename[0])

                self.SW=gr.Principal_g()
                self.SW.ui.label.setText(self.filename[0])
                self.SW.show()
                print(self.filename[0])
                #self.datos=pd.ExcelFile(str(self.filename[0]))
                #self.ui.comboBox.addItems(list(self.datos.sheet_names))
            except (ValueError,KeyError,FileNotFoundError):
                pass
        elif self.filename ==0:
            print("Cargue archivo")
            
        self.ui.pushButton_3.setEnabled(1) 
        self.ui.pushButton_3.setText("Load Data");          
        self.repaint()
 
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


    def pv_array(self):
        self.SW=pv.PV()
        self.SW.show() 
    
    def diesel_gen(self):
        self.SW=dg.Diesel()
        self.SW.show() 
                    
    def battery_bank(self):
        self.SW=bat.Battery()
        self.SW.show() 

    def project_data(self):
        self.SW=proj.Project()
        self.SW.show() 

    def optimizador(self):
        self.SW=op.Optimizer()
        self.SW.show() 


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
    ventana=Principal_c()
    ventana.show()
    sys.exit(app.exec_())
    
    
if __name__=='__main__':
    main(); 
   