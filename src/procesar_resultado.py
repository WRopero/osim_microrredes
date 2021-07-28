import pandas as pd
import sys
import numpy as np


def procesar(model, load, dates, results):
    
    
    #Listas para guardar los valores
    pv_result = []
    dg_result = []
    #Ebat_c_result = []
    #Ebat_d_result = []
    p_gf_result = []
    LPSP_result = []
    SOC_result = []

    #Ciclo que obtiene el valor de cada resultado enlas iteraciones del modelo
    for v in model.var_reales.items():
        uni = v[0][0]
        if uni == 'Pv':
            pv_result.append(v[1].value)
        elif uni == 'Dg':
            dg_result.append(v[1].value)
      #  elif uni == 'Ebat_c':
      #      Ebat_c_result.append(v[1].value)
      #  elif uni == 'Ebat_d':
      #      Ebat_d_result.append(v[1].value)
        elif uni == 'P_gf':
            p_gf_result.append(v[1].value)    
        else:
            print("Pass")
    else:
        print('Ciclo términado otros')
        
    for x in model.soc_t.items():        
        SOC_result.append(x[1].value)   

    else:
        print('Ciclo términado batería')

    #concateno para mostrar en DataFrame
    modelo_result = pd.concat([pd.DataFrame(pv_result), 
                               pd.DataFrame(dg_result), 
                               pd.DataFrame(Ebat_c_result),
                               pd.DataFrame(Ebat_d_result),
                               pd.DataFrame(p_gf_result),
                               pd.DataFrame(SOC_result),
                               pd.DataFrame([load]).T], axis = 1)
    
    #Renombro las columnas del DataFrame
    modelo_result.columns = ['energy_Pv', 'energy_Dg', 
                             'energy_Bat_C','energy_Bat_D',
                             'energy_Pgf','energy_SOC_t',  
                             'Load']


    modelo_result = pd.concat([modelo_result, dates],axis=1) #Agregar fechas
    modelo_result["e_recursos_nf"] = modelo_result[['energy_Pv', 'energy_Dg', 'energy_Bat_D']].sum(axis=1)

    modelo_result[['energy_Pv', 'energy_Dg', 
                   'energy_Bat_C','energy_Bat_D',
                   'energy_Pgf','energy_SOC_t', 
                   'Load',"e_recursos_nf"]].describe()

    modelo_result[modelo_result['energy_Dg']>0].min()

    # Agrupación por hora.
    result_hour = modelo_result.groupby(['Hour']).mean().reset_index()


    DNA = modelo_result[modelo_result['energy_Pgf'] !=0]
    print("Tiempo con demanda no atendida (DNA): ", len(DNA),
          "-", round((len(DNA)/len(load))*100,2), "%")


    costo_not_clean = [i.replace("Upper bound","").replace(" ","").replace("\n","") for i in str(results.get('Problem')).split(':') if 'Upper bound' in i]
    print("Costo real: ", "${:,.2f}". format(float(costo_not_clean[0])-(modelo_result['energy_Pgf'].sum()*model.costos['P_gf'])),"\n")


    costo_DNA = float((modelo_result['energy_Pgf'].sum()*model.costos['P_gf']))
    print("Costo Pgf: ","${:,.2f}". format(costo_DNA),"\n")
    
    
    pd_var_ = pd.concat([
            pd.read_csv(r'data/g_panel.csv', squeeze=True, sep=','),
            pd.read_csv(r'data/g_diesel.csv', squeeze=True, sep=','),
            pd.read_csv(r'data/g_bateria.csv', squeeze=True, sep=','),
            pd.read_csv(r'data/demand.csv', squeeze=True, sep=',')
                ], axis = 1)
    
    pd_var_ = pd.concat([pd_var_, dates],axis=1)
    modelo_result['LPSP'] =  modelo_result['energy_Pgf']/modelo_result['Load']
    pd_var_.describe()
    
    return result_hour, pd_var_, modelo_result