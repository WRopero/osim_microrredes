from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import plotly.express as px
import pandas as pd


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QtWidgets.QPushButton('Plot', self)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)

        vlayout = QtWidgets.QVBoxLayout(self)
        vlayout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
        vlayout.addWidget(self.browser)

        self.button.clicked.connect(self.show_graph)
        self.resize(1000,800)

    def show_graph(self):
        #df = px.data.tips()
        #fig = px.box(df, x="day", y="total_bill", color="smoker")
        #fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
        #self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

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
        fig = px.bar(demanda,
            y='power Impute medida2 KWh',
            x='hora',
            template="ygridoff",
            #color='Month',
            category_orders={
                "Month": [
                    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                    "Sep", "Oct", "Nov", "Dec"                  ]
            },
            #title="Load Profile 2019",
            )

        fig.update_yaxes(nticks=10)
        fig.update_xaxes(nticks=24)
        fig.update_xaxes(title_text='Time (hour)')
        fig.update_yaxes(title_text='Load demand (kWh)')
        fig.update_xaxes(showline=True, linecolor='black')
        fig.layout.update(showlegend=False) 
        fig.update_yaxes(showline=True, linecolor='black')

        fig.update_layout(
                font_family="Times New Roman",
                title_font_family="Times New Roman",
                font_size=14
                ,
                font_color="black",
            )

        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Widget()
    widget.show()
    app.exec()