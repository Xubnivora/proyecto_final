import numpy as npy
import matplotlib.pyplot as plt


size_gen = 100
data_a = []
data_b = []
data_y = []
error = []
gradiente_m = []
gradiente_b = []

m=2
b=1
error_promedio=0
gb_prom=0
gm_prom=0



def generar_listado_a():
    return list(npy.random.randint(low = 25,high=500,size=size_gen))

def generar_listado_b():
    return list(npy.random.poisson(52, size_gen))



def generar_listado_y_hat(data_a):
    for n in data_a:     
        data_y.append(n*m+b)              
    return data_y
     
def generar_listado_error(data_b,data_y):
    for n in range(size_gen):         
        error.append(((data_y[n]-data_b[n])**2)/2)            
    return error


def generar_listado_gradiente_m(data_a,data_b,data_y):
    for n in range(size_gen):         
        gradiente_m.append((data_y[n]-data_b[n])*data_a[n])            
    return gradiente_m

def generar_listado_gradiente_b(data_b,data_y):
    for n in range(size_gen):         
        gradiente_b.append((data_y[n]-data_b[n]))            
    return gradiente_b     



def listado():
  function=[]  
  
  
  
  #data_a=npy.array(generar_listado_a())
  #data_b=npy.array(generar_listado_b())
  
  npy.save('A', npy.array(generar_listado_a()))
  npy.save('B', npy.array(generar_listado_b()))
  
  data_a=npy.load('A.npy')
  data_b=npy.load('B.npy')
  
  data_y=generar_listado_y_hat(data_a)
  generar_listado_error(data_b,data_y) 
  error_promedio = npy.mean(error)
  
  gradiente_m = generar_listado_gradiente_m(data_a,data_b,data_y)
  gradiente_b = generar_listado_gradiente_b(data_b,data_y)
  
  
  gb_prom=npy.mean(gradiente_b)
  gm_prom=npy.mean(gradiente_m)
  print(gb_prom)
  print(gm_prom)
  for x in range(10): 
      x*gm_prom+gb_prom
      function.append(x*gm_prom+gb_prom)
      
  plt.plot(function)    
  return function



  
print(listado())




