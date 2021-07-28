import pandas as pd

def leer_datos(ruta):

    df = pd.read_excel(ruta)

    return df
