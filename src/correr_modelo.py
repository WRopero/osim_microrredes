import gurobipy
import warnings
import pyomo.environ as pyo
from pyomo.opt import *
import sys
warnings.filterwarnings("ignore")
from time import time
import os


def correr_modelo(model=None, gap=None, time_limit=None, experimento=None):
    """Correr el modelo"""
    solver = solvers.SolverFactory("gurobi", solver_io="python")
    solver.options['mipgap'] = gap
    if time_limit != None:
        solver.options['TimeLimit'] = time_limit
    results = solver.solve(model, tee=True, keepfiles=True, 
                           logfile = os.getcwd()+os.sep+"src\log_opt"+os.sep+"%s.txt"%(experimento))
    term_cond = results.solver.termination_condition
    print(f"El programa '{model.name}' es: ", term_cond)
    
    return results, term_cond