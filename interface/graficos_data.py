import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
import pandas as pd

class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(3, 3), dpi=200)
        super().__init__(fig)
        self.setParent(parent)
        df = pd.read_excel(r'C:\Users\Luis Fdo Baquero B\Documents\GitHub\dimensionamiento_microrred\data\datos_microrred_horario_ano_sede_oriente.xlsx')
        df["date"]=df["date"].apply(pd.to_datetime)
        df["Month"] = df["date"].dt.month_name()
        
        dic_fecha = {
        'January' :'Jan',
            'February':'Feb',
            'March':'Mar',
            'April':'Apr',
            'May':'May',
            'June':'Jun',
            'July':'Jul',
            'August':'Aug',
            'September':'Sep',
            'October':'Oct',
            'November':'Nov',
            'December':'Dec'
        }
        df["Month"] = df["Month"].apply(lambda x: dic_fecha[x])
        df["hora"]=df["hora"].apply(lambda x: x+1)
        demanda = df.groupby(["hora"])['power Impute medida2 KWh'].mean().reset_index()

        x = demanda['hora']
        y = demanda['power Impute medida2 KWh']
        
        self.ax.bar(x, y)

        self.ax.set(xlabel='Time (h)', ylabel='load kWh',
            title='Load')
        self.ax.grid()


class AppDemo(QWidget)      :
    def __init__(self):
        super().__init__()
        self.resize(1000, 800)

        chart = Canvas(self)

app = QApplication(sys.argv)        
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
        