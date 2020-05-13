
import numpy as np

def op_or(var1, var2):
	return np.logica_or(var1, var2)

def op_and(var1, var2):
	return np.logical_and(var1,var2)

def op_condicional(var1, var2):	
	return (negar(var1) | var2)

def op_bicondicional(var1, var2):
	return negar(np.logical_xor(var1,var2))

def negar(var):
	return np.logical_not(var)

def evaluar(exp):
	
	