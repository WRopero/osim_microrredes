def graficos(dir_xlsx=None):
    import pandas as pd
    import plotly.express as px


    df = pd.read_excel(dir_xlsx)
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

    demanda_2 = df.groupby(["hora","Month"])['power Impute medida2 KWh'].mean().reset_index()
    demanda_3 = df.groupby(["Month"])['power Impute medida2 KWh'].sum().reset_index()
    demanda_3['power Impute medida2 KWh'] = demanda_3['power Impute medida2 KWh']/1000
    radiacion = df.groupby(["hora","Month"])['Solar Radiation Impute'].mean().reset_index()
    radiacion_2 = df.groupby(["hora","Month"])['Solar Radiation Impute'].mean().reset_index()
    radiacion_2['Solar Radiation Impute'] = radiacion_2['Solar Radiation Impute']/1000
    temperatura = df.groupby(["hora","Month"])['Outside Temperature Impute C'].mean().reset_index()


    fig1 = px.bar(demanda,
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
    fig1.update_yaxes(nticks=10)
    fig1.update_xaxes(nticks=24)
    fig1.update_xaxes(title_text='Time (hour)')
    fig1.update_yaxes(title_text='Load demand (kWh)')
    fig1.update_xaxes(showline=True, linecolor='black')
    fig1.layout.update(showlegend=False) 
    fig1.update_yaxes(showline=True, linecolor='black')

    fig1.update_layout(
        font_family="Times New Roman",
        title_font_family="Times New Roman",
        font_size=14
        ,
        font_color="black",
    )



    fig2 = px.box(demanda_2,
                y='power Impute medida2 KWh',
                x='Month',
                template="ygridoff",

                category_orders={
                    "Month": [
                        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                        "Sep", "Oct", "Nov", "Dec"                  ]
                },
                #title="Load Profile 2019",
                
                )
    fig2.update_yaxes(nticks=10)
    fig2.update_xaxes(nticks=24)
    fig2.update_xaxes(title_text='Month')
    fig2.update_yaxes(title_text='Load demand (kWh)')
    fig2.layout.update(showlegend=False) 
    fig2.update_yaxes(showline=True, linecolor='black')
    fig2.update_xaxes(showline=True, linecolor='black')

    fig2.update_layout(
        font_family="Times New Roman",
        title_font_family="Times New Roman",
        font_size=14
        ,
        font_color="black",
    )



    fig3 = px.bar(demanda_3,
                y='power Impute medida2 KWh',
                x='Month',
                template="ygridoff",

                category_orders={
                    "Month": [
                        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                        "Sep", "Oct", "Nov", "Dec"                  ]
                },
                #title="Load Profile 2019",
                
                )
    fig3.update_yaxes(nticks=10)
    fig3.update_xaxes(nticks=24)
    fig3.update_xaxes(title_text='Month')
    fig3.update_yaxes(title_text='Load demand (MWh/m)')
    fig3.update_xaxes(showline=True, linecolor='black')
    fig3.update_yaxes(showline=True, linecolor='black')


    fig3.update_layout(
        font_family="Times New Roman",
        title_font_family="Times New Roman",
        font_size=14
        ,
        font_color="black",
    )



    fig4 = px.line(temperatura,
                y='Outside Temperature Impute C',
                x='hora',
                template="xgridoff",
                color='Month',
                category_orders={
                    "Month": [
                        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                        "Sep", "Oct", "Nov", "Dec"                  ]
                },
                #title="Load Profile 2019",
                
                )
    fig4.update_yaxes(nticks=10)
    fig4.update_xaxes(nticks=15)
    fig4.update_xaxes(title_text='Time (hour)')
    fig4.update_yaxes(title_text='Temperature (°C)')
    
    fig4.update_yaxes(showline=True, linecolor='black')
    fig4.update_xaxes(showline=True, linecolor='black')

    fig4.update_layout(
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
            font_size=14
        
    )
    )


    fig5 = px.line(radiacion,
                y='Solar Radiation Impute',
                x='hora',
                template="xgridoff",
                color='Month',
                category_orders={
                    "Month": [
                        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                        "Sep", "Oct", "Nov", "Dec"                  ]
                },
                #title="Load Profile 2019",
                
                )
    fig5.update_yaxes(nticks=10)
    fig5.update_xaxes(nticks=15)
    fig5.update_xaxes(title_text='Time (hour)')
    fig5.update_yaxes(title_text='Solar radiation (Wh/m2)')
    #fig.layout.update(showlegend=False) 
    fig5.update_yaxes(showline=True, linecolor='black')
    fig5.update_xaxes(showline=True, linecolor='black')

    fig5.update_layout(
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
            font_size=14       
    )
    )


    fig6 = px.bar(radiacion_2,
                y='Solar Radiation Impute',
                x='Month',
                template="xgridoff",
                
                category_orders={
                    "Month": [
                        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                        "Sep", "Oct", "Nov", "Dec"                  ]
                },
                #title="Load Profile 2019",
                
                )
    fig6.update_yaxes(nticks=10)
    fig6.update_xaxes(nticks=15)
    fig6.update_xaxes(title_text='Month')
    fig6.update_yaxes(title_text='Solar radiation (kWh/m2)')
    #fig.layout.update(showlegend=False) 
    fig6.update_yaxes(showline=True, linecolor='black')
    fig6.update_xaxes(showline=True, linecolor='black')

    fig6.update_layout(
        font_family="Times New Roman",
        title_font_family="Times New Roman",
        font_size=14
        ,
        font_color="black",
    )

    return fig1, fig2, fig3, fig4, fig5, fig6