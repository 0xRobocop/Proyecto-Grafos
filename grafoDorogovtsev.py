from grafo import Grafo
import random


def grafoDorogovtsev(numeroNodos):

  """
  Generación de grafos utilizando el modelo de Dorogovtsev-Mendes.
  numeroNodos: número de nodos.    
  """

  g = Grafo()

  g.agregarArista('0 -- 1', str(0), str(1))
  g.agregarArista('0 -- 2', str(0), str(2))
  g.agregarArista('1 -- 2', str(1), str(2))

  for nodoAdicional in range(3, numeroNodos-2):
    cantidadAristas = len(g.aristas)
    aristaRandom = random.randint(1,cantidadAristas-1)
    listaAristas = list(g.aristas.keys())
    aristaSeleccionada = listaAristas[aristaRandom]
    nodoInicio = g.aristas[aristaSeleccionada].n0.id
    nodoFinal = g.aristas[aristaSeleccionada].n1.id
    
    g.agregarArista('{} -- {}'.format(str(nodoAdicional), str(nodoInicio)), str(nodoAdicional), str(nodoInicio))
    g.agregarArista(str('{} -- {}'.format(str(nodoAdicional), str(nodoFinal))), str(nodoAdicional), str(nodoFinal))




  return g

tareaGrafos = {1:30, 2: 100, 3: 500}

for i in range(1,4):
  nodosAgenerar = tareaGrafos[i]

  grafoDorogovtsev_ = grafoDorogovtsev(nodosAgenerar)

  grafoDorogovtsev_.generarArchivoGV('{} {}'.format('Dorogovtsev',str(i)))


