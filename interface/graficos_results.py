
import pandas as pd
import sqlite3
import numpy as np
import os
import plotly.express as px
import plotly.graph_objects as go

def _graficos_resultados():
    def conexion_bd(sql=None, update=True):
        
        sqlite3.register_adapter(np.int64, lambda val: int(val))
        sqlite3.register_adapter(np.int32, lambda val: int(val))

        con = sqlite3.connect(os.getcwd() + os.sep+"database\\result_op.db")
        
        try:
            if update == True:
                cur = con.cursor()
                cur.execute(sql)
                con.commit()
                df=None
            else:
                df= pd.read_sql_query(sql, con=con)
        except:
            print(sql)
            df=None
        con.close()    
        return df

    tabla_resultados = conexion_bd(sql="select*from resultados where id_simulacion=5000", update=False)
    parametros = conexion_bd(sql="select*from parametros where id_simulacion=5000 and optimizacion='optimal' ", update=False)
    parametros_ = parametros.T.reset_index()
    parametros_.columns = ["Variable", "Value"]


    bd = pd.read_excel(r"C:\Users\Luis Fdo Baquero B\Documents\GitHub\osim_microrredes\data\datos_microrred_islote.xlsx")

    tabla_resultados[['date', 'hora', 'dia', 'mes']] = bd[['date', 'hora', 'dia', 'mes']]
    tabla_resultados["date"]=tabla_resultados["date"].apply(pd.to_datetime)
    tabla_resultados["Month"] = tabla_resultados["date"].dt.month_name()
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
    tabla_resultados["Month"] = tabla_resultados["Month"].apply(lambda x: dic_fecha[x])
    tabla_resultados["hora"]=tabla_resultados["hora"].apply(lambda x: x+1)

    #print(parametros)


    def graficar(tipo, lista_campos, titulo,df):
        if tipo == 'bar':
            fig = px.bar(df,
                        y=lista_campos,
                        
                        template="xgridoff",
                        title=titulo)
        elif tipo == 'linea':
            fig = px.line(df,
                        y=lista_campos,
                        x='hour',
                        template="xgridoff",
                        title=titulo,
                        category_orders={"State": lista_campos}
                )
        fig.update_yaxes(nticks=10)
        fig.update_xaxes(nticks=15)
        fig.update_xaxes(title_text='Time (hour)')
        fig.update_yaxes(title_text='Energy [kWh]')
        fig.update_yaxes(showline=True, linecolor='black')
        fig.update_xaxes(showline=False, linecolor='black')
        if 'SOC(t)_bateria' in lista_campos or 'SoC(t)' in lista_campos:
            fig.add_shape(  # add a horizontal "target" line
                type="line",
                line_color="gray",
                line_width=2,
                opacity=1,
                line_dash="dot",
                x0=0,
                x1=1,
                xref="paper",
                y0=parametros['p_bat']*0.5,
                y1=parametros['p_bat']*0.5,
                yref="y")
            fig.add_shape(  # add a horizontal "target" line
                type="line",
                line_color="gray",
                line_width=2,
                opacity=1,
                line_dash="dot",
                x0=0,
                x1=1,
                xref="paper",
                y0=parametros['p_bat'],
                y1=parametros['p_bat'],
                yref="y")
        fig.update_layout(
        font_family="Times New Roman",
        title_font_family="Times New Roman",
        font_size=14
        ,
        font_color="black",
            legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
            font_size=14)

    )

        return fig

    def _fig1():
        labels = ['PV Energy','PENS Energy','Diesel Energy', 'Battery Bank Energy']
        values = [round(tabla_resultados['energia_PV'].sum(),1), 
                round(tabla_resultados['energia_ENS'].sum(),1),
                round(tabla_resultados['energia_Dg'].sum(),1),           
                round(tabla_resultados['energia_descarga_bateria'].sum(),1)]

        colors = ['orange', 'firebrick', 'seagreen', 'royalBlue']

        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',textposition='outside', pull=[0, 0.2,0, 0], hole = .4,
                                    #title = 'Supply Load'
                                )])



        fig.update_xaxes(title_text='Time (hour)')
        fig.update_yaxes(title_text='Energy Supply Load (kWh)')
        fig.update_xaxes(showline=True, linecolor='black')
        fig.layout.update(showlegend=False) 
        fig.update_yaxes(showline=True, linecolor='black')


        fig.update_layout(
            margin=dict(l=1, r=5, t=5, b=5),
            
            font_family="Times New Roman",
            title_font_family="Times New Roman",
            font_size=14
            ,
            font_color="black",
                legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
                font_size=14)

        )

        fig.update_traces(  marker=dict(colors=colors))

        return fig

    def _fig2():
        soc = tabla_resultados.groupby(["hora"])['SOC(t)_bateria','energia_descarga_bateria','energia_carga_bateria'].mean().reset_index()
        soc.columns=['hour', 'SoC(t)', 'Discharging', 'Charging']
        fig=graficar(tipo='linea',
                lista_campos=['SoC(t)', 'Discharging', 'Charging'],
                titulo="",
                df=soc)
        return fig


    def _fig3():
        pv_disp = tabla_resultados.groupby(["hora"])['energia_carga_bateria','p_bat_pv',
                                                'p_bat_dg'].mean().reset_index()


        pv_disp.columns=['hour','Charging', 'PV Energy',  'Diesel Energy']

        fig = graficar(tipo='linea',
                lista_campos=['Charging','PV Energy',  'Diesel Energy'],
                titulo="",
                df = pv_disp )
        return fig

    def _fig4():
        #Sol disponible
        pv_disps = tabla_resultados[['recurso_pv_dis','p_bat_pv','energia_PV']]


        pv_disp = tabla_resultados.groupby(["hora"])['recurso_pv_dis','p_bat_pv','energia_PV'].mean().reset_index()


        pv_disp.columns=['hour','Available PV Energy', 'PV Energy to Battery Bank',  'PV Energy to Load']

        fig = graficar(tipo='linea',
                lista_campos=['Available PV Energy', 'PV Energy to Battery Bank',  'PV Energy to Load'],
                titulo="",
                df = pv_disp )
        return fig

    def _fig5():
        bat_c = tabla_resultados.head(23)[['energia_carga_bateria','energia_descarga_bateria']]
        bat_c['energia_descarga_bateria'] = bat_c['energia_descarga_bateria']*-1

        bat_c.columns = ['Charging','Discharging']

        fig = graficar(tipo='bar',
                lista_campos=['Charging','Discharging'],
                titulo="",
                df = bat_c)
        return fig

    def _fig6():
        energy_to_load = tabla_resultados.tail(120)[['energia_descarga_bateria','energia_PV','energia_Dg','energia_ENS']].head(24).reset_index(drop=True)

        energy_to_load.columns = ['Battery Bank Energy','PV Energy','Diesel Energy','PENS Energy']

        fig = graficar(tipo='bar',
                lista_campos=['Battery Bank Energy','PV Energy','Diesel Energy','PENS Energy'],
                titulo="",
                df = energy_to_load)
        return fig

    def _fig7():
        dg_disp = tabla_resultados.groupby(["hora"])['energia_Dg','p_bat_dg'].mean().reset_index()
        dg_disp.columns = ['hora','Diesel Energy to Load','Diesel Energy to Charging the Battery Bank']
        fig = graficar(tipo='bar',
                lista_campos=['Diesel Energy to Load','Diesel Energy to Charging the Battery Bank'],
                titulo="",
                df = dg_disp )
        return fig

    def _fig8():

        fig = go.Figure(go.Bar(
                    x=[ round(tabla_resultados['p_bat_pv'].sum(),1),
                        round(tabla_resultados['p_bat_dg'].sum(),1),
                        round(tabla_resultados['energia_PV'].sum(),1), 
                        round(tabla_resultados['energia_ENS'].sum(),1),
                        round(tabla_resultados['energia_Dg'].sum(),1),           
                        round(tabla_resultados['energia_descarga_bateria'].sum(),1)              
                    ],
                    y=['PV Energy to Battery','Diesel Energy to Battery',
                    'PV Energy to Load','ENS Energy to Load',
                    'Diesel Energy to Load', 
                    'Battery Energy to Load'],
                    orientation='h'))
        colors = ['orange', 'seagreen', 'orange',  'firebrick','seagreen','royalBlue']
        fig.update_traces(  marker=dict(color=colors))
        return fig

    def _fig9():
        labels = ['PV Energy','Diesel Energy']
        values = [round(tabla_resultados['p_bat_pv'].sum(),1), 
                round(tabla_resultados['p_bat_dg'].sum(),1)]

        colors = ['orange', 'seagreen']

        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent', hole = .4,
                                    title = 'Supply Battery Bank'
                                )])

        fig.update_layout(
            font_family="Times New Roman",
            title_font_family="Times New Roman",
            font_size=14
            ,
            font_color="black",
                legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
                font_size=14)

        )

        fig.update_traces(  marker=dict(colors=colors))
    



        return fig

    fig1=_fig1()
    fig2=_fig2()
    fig3=_fig3()
    fig4=_fig4()
    fig5=_fig5()
    fig6=_fig6()
    fig7=_fig7()
    fig8=_fig8()
    fig9=_fig9()

    return fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9,tabla_resultados,parametros_