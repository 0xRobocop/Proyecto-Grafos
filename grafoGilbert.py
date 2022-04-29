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




