import pandas as pd
import sqlite3
import numpy as np
import os

def guardar_bd(tabla_resultados, par_in, term_cond):

    sqlite3.register_adapter(np.int64, lambda val: int(val))
    sqlite3.register_adapter(np.int32, lambda val: int(val))
    con = sqlite3.connect(os.getcwd() + os.sep + "result_op.db")
    if term_cond =='optimal':
        tabla_resultados.to_sql("resultados", con, index=False,if_exists='append')

    par_in.to_sql("parametros", con,  index=False, if_exists='append')
    con.close()