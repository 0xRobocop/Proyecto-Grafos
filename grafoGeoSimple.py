from grafo import Grafo 
import random 
from math import sqrt

def distancia(NodoInicio, NodoFinal):

  """
  Calcula la distancia entre dos puntos
  """
  x1 = NodoInicio.atributos['cX']
  y1 = NodoInicio.atributos['cY']
  x2 = NodoFinal.atributos['cX']
  y2 = NodoFinal.atributos['cY']

  _distancia = sqrt((x1-x2)**2 + (y1-y2)**2)
  return _distancia


def grafoGeo(n,r):

  """
  Grafo geográfico simple
  Retorna grafo generado
  """
  g = Grafo()

  for i in range(n):
    nodo_ = g.agregarNodo(str(i))
    nodo_.atributos['cX'] = 2*random.random()
    nodo_.atributos['cY'] = 2*random.random()
  

  for i in range(n):
    for j in range(n):
      if i != j:
        nodoI = g.dameNodo(str(i))
        nodoF = g.dameNodo(str(j))
        _distancia = distancia(nodoI,nodoF)

        if _distancia < r:
          g.agregarArista('{} -- {}'.format(str(i), str(j)),str(i),str(j))
 
  return g

tareaGrafos = {1:(30,0.3), 2: (100,0.3), 3: (500,0.3)}

for i in range(1,4):
  nodosAgenerar = tareaGrafos[i][0]
  r = tareaGrafos[i][1]

  grafoGeo_ = grafoGeo(nodosAgenerar,r)

  grafoGeo_.generarArchivoGV('{} {}'.format('GeoSimple',str(i)))


