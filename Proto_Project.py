import numpy as npy
import matplotlib.pyplot as plt
import statistics


data_a = []
data_b = []
data_y = []
error = []
m=0
b=0

def generar_listado_a():
    return list(npy.random.randint(low = 125,high=1000,size=100))

def generar_listado_b():
    return list(npy.random.poisson(89, 100))



def generar_listado_y_hat(data_a):
    for n in data_a:     
        data_y.append(n*m+b)              
    return data_y
     
def generar_listado_error(data_b,data_y):
    for n in range(100):         
        error.append(((data_y[n]-data_b[n])**2)/2)            
    return error

     

def listado():
  data_a=npy.array(generar_listado_a())
  data_b=npy.array(generar_listado_b())
  data_y=generar_listado_y_hat(data_a)
  generar_listado_error(data_b,data_y) 
  return statistics.mean(error)
  
  
print(listado())




