from grafo import Grafo
import random

def grafoGilbert(n, probabilidad):

  g = Grafo()


  for i in range(n):
    g.agregarNodo(str(i))

  for i in range(n):
    for j in range(n):
      if random.random() < probabilidad:
        if (j != i):
          g.agregarArista('{} -- {}'.format(str(i), str(j)),str(i),str(j))
 
  return g

tareaGrafos = {1:(30,0.02), 2: (100,0.02), 3: (500,0.02)}

for i in range(1,4):
  nodosAgenerar = tareaGrafos[i][0]
  probabilidad = tareaGrafos[i][1]

  grafoGilbert_ = grafoGilbert(nodosAgenerar,probabilidad)

  grafoGilbert_.generarArchivoGV('{} {}'.format('Gilbert',str(i)))
  


