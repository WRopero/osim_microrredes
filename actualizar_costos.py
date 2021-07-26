import pandas as pd
import numpy as np
import math
import sqlite3
import os

def conexion_bd(sql=None, update=True):
    
    sqlite3.register_adapter(np.int64, lambda val: int(val))
    sqlite3.register_adapter(np.int32, lambda val: int(val))

    con = sqlite3.connect(os.getcwd() + os.sep + "result_op.db")
    
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



def actualizar_costos(parametros=None, resultados=None, i=None):
    
    trm = 3736.91

    id_simulacion = parametros.loc[i,'id_simulacion']
    n_pv = parametros.loc[i,'n_pv']
    n_dg = parametros.loc[i,'n_dg']
    p_bat = parametros.loc[i,'p_bat']
    p_dg = parametros.loc[i,'p_dg']
    ens = parametros.loc[i,'ens_result']

    c_pv = parametros.loc[i,'cost_pv']
    c_bat = parametros.loc[i,'cost_bat']
    c_dg = parametros.loc[i,'cost_dg']
    
    lpsp = parametros.loc[i,'lpsp_result']
    
    if lpsp <=1.5:
        c_ens = 1532.53
    elif lpsp > 1.5 and lpsp <= 5:
        c_ens = 2778.13
    elif lpsp > 5 and lpsp < 90:
        c_ens = 4872.19
    else:
        c_ens = 0
        
        
    resultado_id = resultados[resultados['id_simulacion']==id_simulacion].reset_index(drop=True)

    resultado_id['total_dg'] = resultado_id['energia_Dg'] + resultado_id['p_bat_dg']
    resultado_id['total_pv'] = resultado_id['energia_PV'] + resultado_id['p_bat_pv']


    ei = round(resultado_id['total_dg'].sum(),2)
    et = round(resultado_id['total_dg'].sum(),2)

    et_pv = round(resultado_id['total_pv'].sum(),2)

    load = round(resultado_id['load'].sum(),2)

    et_bat = round(resultado_id['energia_descarga_bateria'].sum(),2)

    cost_e_dg = (et*c_dg)/trm
    cost_e_pv = (et_pv*c_pv)/trm
    cost_e_bat =( et_bat*c_bat)/trm
    cost_e_ens =( ens*c_ens)/trm

    financiero = {'R':20, 'ir':0.0808, 'cpv_ins' : 5605.365 ,'cbat_ins' : 539983.495,'cdg_ins' : 7627407.001,  'npv' : n_pv ,'ndg' : n_dg ,'ppv_stc': 300,'ebcell_nom': p_bat,
    'pdg_rate': p_dg, 'li_bat':10,'li_dg':10,'ybat': 0.7,'ydg': 0.7, 'ipp_o': 74.37,'ipp_actual' : 129.23, 'cec': 0.0974,'ei': ei,'et': et,'pami': 8789 ,
    'cel':0.0005,'plim':79900, 'p_load':load,'ens':ens, 'factor_pv':0.01,'factor_bat':0.02}


    R = financiero['R'] # the life time of the project
    ir = financiero['ir']  #  (i_n - i_f) / (1 + i_f) # Tomado de otro estudio

    crf = round(ir*((1+ir)**R) /((1+ir)**R - 1),2)  # The capital recovery factor is calculated by

    cpv_ins = financiero['cpv_ins'] # costo de PV kWh instalado
    cbat_ins = financiero['cbat_ins'] # costo Battery de kWh instalado
    cdg_ins = financiero['cdg_ins'] # costo diesel de kWh instalado

    npv = financiero['npv'] # Número de paneles fotovoltaicos
    ndg = financiero['ndg'] # Número planta diesel
    ppv_stc = financiero['ppv_stc']# Capacidad nominal paneles
    ebcell_nom = financiero['ebcell_nom'] # Capacidad de la batería
    pdg_rate = financiero['pdg_rate'] # Capacidad nominal diesel

    ccpv = round(cpv_ins*npv*ppv_stc,4)
    ccbat = round(cbat_ins*ebcell_nom,4)
    ccdg = round(cdg_ins*ndg*pdg_rate,4)

    def calcular_ki(R, li, ir):
        """
        Para cálcular single payment present worth
        """
        yi_replacements = math.floor(R/li)
        values_to_sum = []
        for i in range(1,yi_replacements+1):
            x = (1)/((1+ir)**(i*li))
            values_to_sum.append(x)

        return sum(values_to_sum)

    kbat = round(calcular_ki(R=financiero['R'], li=financiero['li_bat'], ir=financiero['ir']),4)  # single payment present worth battery
    kdg = round(calcular_ki(R=financiero['R'], li=financiero['li_dg'], ir=financiero['ir']),4) # single payment present worth diesel

    ybat = financiero['ybat'] #are de-rate factors of the initial capital cost invested 
    ydg = financiero['ydg'] #are de-rate factors of the initial capital cost invested

    rc_bat = round(ybat*ccbat*kbat,4)
    rc_dg = round(ydg*ccdg*kdg,4)

    factor_pv = financiero['factor_pv'] # Factor de la inversión inicial
    factor_bat = financiero['factor_bat'] # Factor de la inversión inicial

    oym_pv = factor_pv*ccpv 
    oym_bat = factor_bat*ccbat

    ipp_o = financiero['ipp_o']
    ipp_actual = financiero['ipp_actual']

    cec = financiero['cec'] #Consumo especifíco de combustible 0.0974 gal/kWh (capacidad <= 100 kW)
    ei = financiero['ei'] #Energía entregada al Sistema de Distribución por el generador i 
    et = financiero['et'] #Energía total entregada al Sistema de Distribución

    pami = financiero['pami'] #Precio promedio del combustible para la planta de abasto más cercana al generador i en el mes m ($/gal).
    tmi = pami*0.1
    calm = 82.14*(ipp_actual/ipp_o) # Costo de almacenamiento de combustible en el mes m ($/gal)
    pci = pami + tmi + calm  # Precio del galón  en el sitio para el generador i
    
    if et>0:
        cc = (1/et)*(cec*pci*ei) # Costo de Combustible (CC)
    else:
        cc=0

    cel = financiero['cel'] # Consumo Específico de Lubricante 0,00050 gal/kWh para plantas de capacidad <= 2.000 Kw
    plim = financiero['plim'] #Precio del Galón de lubricante en el sitio para el generador i en el mes m ($/gal). el precio del lubricante se determinará con base en los precios promedio del mercado.
    if et>0:
        cl = (1/et)*(cel*(plim+tmi)*ei)
    else:
        cl=0
    cam = 0.1*(cc+cl)

    oym_dg = (cam + cc + cl)*ei 
    incentivo = 0.9038
    asc = (((ccpv+ccbat+ccdg)+(rc_bat+rc_dg))*crf + (oym_dg + oym_pv + oym_bat))/trm
    asc_incentivo = ((((ccpv+ccbat)*incentivo+ccdg)+(rc_bat+rc_dg))*crf + (oym_dg + oym_pv + oym_bat))/trm

    p_load = financiero['p_load']
    ens = financiero['ens']
    lcoe = (asc/(p_load - ens))
    lcoe_incentivo = (asc_incentivo/(p_load - ens))

    sql_actualizar= """UPDATE parametros 
            SET  vida_proyecto = %s,
            ir = %s,
            crf= %s,
            cpv_ins= %s,
            cbat_ins= %s,
            cdg_ins= %s,
            capital_cpv= %s,
            capital_cbat= %s,
            capital_cdg= %s,
            kbat= %s,
            kdg= %s,
            ybat= %s,
            ydg= %s,
            rc_bat= %s,
            rc_dg= %s,
            factor_bat= %s,
            factor_pv= %s,
            oym_pv= %s,
            oym_bat= %s,
            ipp_actual= %s,
            trm= %s,
            pami = %s,
            plim = %s,
            oym_dg = %s,
            asc = %s,
            lcoe= %s,
            asc_incentivo=%s,
            lcoe_incentivo=%s,
            cost_e_dg=%s,
            cost_e_pv=%s,
            cost_e_bat=%s,
            cost_e_ens=%s        
            WHERE id_simulacion =%s"""%(R, 
                                        ir, 
                                        crf, 
                                        cpv_ins,
                                        cbat_ins, 
                                        cdg_ins, 
                                        ccpv ,
                                        ccbat,
                                        ccdg ,
                                        kbat, 
                                        kdg, 
                                        ybat, 
                                        ydg, 
                                        rc_bat, 
                                        rc_dg, 
                                        factor_bat,
                                        factor_pv, 
                                        round(oym_pv,2), 
                                        round(oym_bat,2), 
                                        round(ipp_actual,2), 
                                        round(trm,2), 
                                        round(pami,2), 
                                        round(plim,2),
                                        round(oym_dg,2), 
                                        round(asc,2), 
                                        round(lcoe,2), 
                                        round(asc_incentivo,2),
                                        round(lcoe_incentivo,2), 
                                        round(cost_e_dg,2),
                                        round(cost_e_pv,2) ,
                                        round(cost_e_bat,2),
                                        round(cost_e_ens,2),
                                        round(id_simulacion,2))



    conexion_bd(sql=sql_actualizar)

