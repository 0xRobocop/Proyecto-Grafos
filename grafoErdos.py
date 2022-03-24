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
      g.agregarArista('{} -- {}'.format(str(u), str(v)),str(u),str(v))


  return g

tareaGrafos = {1:(30,200), 2: (100,1000), 3: (500,5000)}

for i in range(1,4):
  nodosAgenerar = tareaGrafos[i][0]
  numeroPares = tareaGrafos[i][1]

  grafoErdos_ = grafoErdos(nodosAgenerar,numeroPares)

  grafoErdos_.generarArchivoGV('{} {}'.format('Erdos',str(i)))

