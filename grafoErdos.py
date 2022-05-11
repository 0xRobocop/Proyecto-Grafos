from grafo import Grafo
import random

def grafoErdos(n,m, dirigido=False, auto=False):

  g = Grafo()

  for i in range(n):
    g.agregarNodo(str(i))

  for i in range(m):
    u = random.randint(0, n-1)
    v = random.randint(0, n-1)

    if u != v:
      peso = (random.random()*100)/10
      g.agregarArista('{} -- {}'.format(str(u), str(v)),str(u),str(v),peso)


  return g


