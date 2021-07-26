# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 08:52:01 2018

@author: WILMER ROPERO C
"""


def tabla(df2,self):
    df2=df2.fillna(value="")
            #        df1="lo que deberia quedar"
                
              
                #   CREANDO LA TABLA
    [dfy,dfx]=df2.shape
    
    data=[]
    for xx in range (dfx):
        a=list(df2.iloc[:,xx])
        data.append(a)
    
    listnameheaders=list(df2.iloc[:0])
    
    from PyQt5 import QtWidgets
    self.ui.tableWidget.setRowCount(0)
    self.ui.tableWidget.setColumnCount(0)
    
    ncolumn=len(data)
    nrow=len(data[0])
    
    self.ui.tableWidget.setRowCount(nrow)
    self.ui.tableWidget.setColumnCount(ncolumn)
    self.ui.tableWidget.setHorizontalHeaderLabels(listnameheaders)
    
    for ii in range(0, ncolumn):
        mainins =data[ii]
        for var in range(0, nrow):
            self.ui.tableWidget.setItem(var, ii, QtWidgets.QTableWidgetItem((str(mainins[var]))))      