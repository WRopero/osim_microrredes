import plotly.express as px
import pandas as pd
import os
import numpy as np
import plotly.graph_objects as go


def graficos(bd, tabla_resultados, i, parametros):

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
    supply_load = tabla_resultados.groupby(["hora"])['energia_PV','energia_ENS','energia_Dg','energia_descarga_bateria'].mean().reset_index()
    supply_load_2 = tabla_resultados.groupby(["hora","Month"])['energia_PV','energia_ENS','energia_Dg','energia_descarga_bateria'].mean().reset_index()
    supply_load_3 = tabla_resultados.groupby(["Month"])['energia_PV','energia_ENS','energia_Dg','energia_descarga_bateria'].sum().reset_index()

    fig = px.bar(supply_load,
                  y=['energia_descarga_bateria','energia_PV','energia_Dg','energia_ENS'],
                  x='hora',
                  template="xgridoff",
                  #color='Month',
                  category_orders={
                      "Month": [
                          "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                          "Sep", "Oct", "Nov", "Dec"                  ]
                  },
                  #title="Energy Supply to Load 2019",
                  width=520,
                  height=400)
    fig.update_yaxes(nticks=10)
    fig.update_xaxes(nticks=24)
    fig.update_xaxes(title_text='Time (hour)')
    fig.update_yaxes(title_text='Energy Supply Load (kWh)')
    fig.update_xaxes(showline=True, linecolor='black')
    fig.layout.update(showlegend=True) 
    fig.update_yaxes(showline=True, linecolor='black')

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

    
    fig.write_image(os.getcwd()+os.sep+"graficos"+os.sep+
                    str(i)+os.sep+"energy_supply_load_bar.svg")


    fig = px.line(supply_load,
                  y=['energia_descarga_bateria','energia_PV','energia_Dg','energia_ENS'],
                  x='hora',
                  template="xgridoff",
                  #color='Month',
                  category_orders={
                      "Month": [
                          "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                          "Sep", "Oct", "Nov", "Dec"                  ]
                  },
                  #title="Energy Supply to Load 2019",
                  width=520,
                  height=400)
    fig.update_yaxes(nticks=10)
    fig.update_xaxes(nticks=24)
    fig.update_xaxes(title_text='Time (hour)')
    fig.update_yaxes(title_text='Energy Supply Load (kWh)')
    fig.update_xaxes(showline=True, linecolor='black')
    fig.layout.update(showlegend=True) 
    fig.update_yaxes(showline=True, linecolor='black')

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

    
    fig.write_image(os.getcwd()+os.sep+"graficos"+os.sep+
                    str(i)+os.sep+"energy_supply_load_lines.svg")


    fig = go.Figure(go.Bar(
                x=[ round(tabla_resultados['p_bat_pv'].sum(),1),
                    
                    round(tabla_resultados['energia_PV'].sum(),1), 
                    round(tabla_resultados['energia_ENS'].sum(),1),
                    round(tabla_resultados['energia_Dg'].sum(),1),           
                    round(tabla_resultados['energia_descarga_bateria'].sum(),1)              
                  ],
                y=['PV Energy to Battery',
                   'PV Energy to Load','ENS Energy to Load',
                   'Diesel Energy to Load', 
                   'Battery Energy to Load'],
                orientation='h'))
    colors = ['orange', 'seagreen', 'orange',  'firebrick','seagreen','royalBlue']
    fig.update_traces(  marker=dict(color=colors))




    fig.update_layout(title='Energy Used in Microgrid')
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
            font_size=14))
    
    fig.write_image(os.getcwd()+os.sep+"graficos"+os.sep+str(i)+os.sep+"bar_energy.svg")

    labels = ['PV Energy']
    values = [round(tabla_resultados['p_bat_pv'].sum(),1)]

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
   
    fig.write_image(os.getcwd()+os.sep+"graficos"+os.sep+
                    str(i)+os.sep+"energy_supply_battery.svg")

    labels = ['PV Energy','ENS Energy','Diesel Energy', 'Battery Energy']
    values = [round(tabla_resultados['energia_PV'].sum(),1), 
              round(tabla_resultados['energia_ENS'].sum(),1),
              round(tabla_resultados['energia_Dg'].sum(),1),           
              round(tabla_resultados['energia_descarga_bateria'].sum(),1)]

    colors = ['orange', 'firebrick', 'seagreen', 'royalBlue']

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent', pull=[0, 0.2,0, 0], hole = .4,
                                 title = 'Supply Load'
                               )])



    fig.update_xaxes(title_text='Time (hour)')
    fig.update_yaxes(title_text='Energy Supply Load (kWh)')
    fig.update_xaxes(showline=True, linecolor='black')
    fig.layout.update(showlegend=False) 
    fig.update_yaxes(showline=True, linecolor='black')


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
    
    fig.write_image(os.getcwd()+os.sep+"graficos"+os.sep+str(i)+os.sep+"energy_supply_load.svg")


    def graficar(tipo, lista_campos, titulo,df):
        if tipo == 'bar':
            fig = px.bar(df,
                         y=lista_campos,
                         template="xgridoff",
                         title=titulo,
                  width=520,
                  height=400)
        elif tipo == 'linea':
            fig = px.line(df,
                          y=lista_campos,
                          template="xgridoff",
                          title=titulo,
                  width=520,
                  height=400)
        fig.update_yaxes(nticks=20)
        fig.update_xaxes(nticks=30)
        fig.update_xaxes(title_text='Hora')
        fig.update_yaxes(title_text='Energía kWh')
        if 'SOC(t)_bateria' in lista_campos:
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
        
        fig.write_image(os.getcwd()+os.sep+"graficos"+os.sep+
                        str(i)+os.sep+"graficos%s.svg"%(lista_campos[0]+tipo))

    soc = tabla_resultados.groupby(["hora"])['SOC(t)_bateria','energia_descarga_bateria','energia_carga_bateria'].mean().reset_index()

    graficar(tipo='linea',
             lista_campos=['SOC(t)_bateria','energia_descarga_bateria','energia_carga_bateria'],
             titulo="",
            df=soc)

    bat_c = tabla_resultados.groupby(["hora"])['energia_descarga_bateria','energia_carga_bateria'].mean().reset_index()
    bat_c['energia_descarga_bateria'] = bat_c['energia_descarga_bateria']*-1

    graficar(tipo='bar',
             lista_campos=['energia_descarga_bateria','energia_carga_bateria'],
             titulo="",
            df = bat_c)

    pv_disp = tabla_resultados.groupby(["hora"])['p_bat_pv','energia_carga_bateria'].mean().reset_index()

    graficar(tipo='linea',
             lista_campos=['p_bat_pv','energia_carga_bateria'],
             titulo="",
            df = pv_disp )

    dg_disp = tabla_resultados.groupby(["hora"])['energia_Dg'].mean().reset_index()

    graficar(tipo='bar',
             lista_campos=['energia_Dg'],
             titulo="",
            df = dg_disp )
    print("Terminado - Guardado de gráficos")