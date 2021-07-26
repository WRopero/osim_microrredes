#modelo paneles

def panel(irradiance, Npv, temperatura):
    """
    función que cálcula la producción del panel
    """
    p_pv_stc = 300
    G_stc = 1000
    alpha_p = -0.39
    t_cell = temperatura*irradiance*((45-20)/800)
    t_1 = 1 + (alpha_p/100)*(t_cell-25)
    fpv = 0.85
    Ppv = Npv*p_pv_stc*(irradiance/G_stc)*t_1*fpv

    return abs(Ppv/1000)

def diesel(eficiencia, potencia, Ndg):
    """
    función que cálcula la producción del 
    generador diésel
    """
    Pdg = round(eficiencia*potencia*Ndg,4)
    
    return Pdg

def bateria(pcell_nom, vdc_sist, vdc_bc, nbat_p):
    """
    Para calcular la potencia de la batería
    vdc_sist: Usually is 12, 24 or 48 V for
              large sistems.    
    """
    
    nbat_s = vdc_sist/vdc_bc    
    Pbat_nom = round(nbat_p*nbat_s*pcell_nom,2)
    
    nbat = nbat_s*nbat_p
    
    return Pbat_nom, nbat
