import grafoGeoSimple 
import grafoGilbert
import grafoMalla 
import grafoErdos 
import grafoBarabasi
import grafoDorogovtsev 

from grafo import Grafo 

def BFS(grafoGenerado, nodoFuente):
  
  '''
    Funcion para generar un arbol BFS dado un grafo : grafoGenerado
    y un nodo inicio : nodoFuente

    Utilizamos el array visitado por que nodos hemos pasado
    BFS utiliza una cola para recorrer el grafo Last in Last Out
  '''

  arbolBFS = Grafo()

  visitado = [nodoFuente]
  cola = [nodoFuente]
  diccionarioNodos = grafoGenerado.nodos

  while cola:
    m = cola.pop(0)

    for nodoAdjacente in diccionarioNodos[m].atributos['Vecinos']:
      if nodoAdjacente.id not in visitado:
        visitado.append(nodoAdjacente.id)
        cola.append(nodoAdjacente.id)
        arbolBFS.agregarArista('{} -- {}'.format(str(m), str(nodoAdjacente.id)),str(m),str(nodoAdjacente.id))     
  

  return arbolBFS
  
if __name__ == "__main__":

  diccionarioGrafoGeo = {1:(30,0.3), 2: (100,0.3), 3: (500,0.3)}
  diccionarioGrafoBarabasi = {1:(30,9), 2: (100,9), 3: (500,9)}
  diccionarioGrafoDorogovtsev = {1:30, 2: 100, 3: 500}
  diccionarioGrafoErdos = {1:(30,200), 2: (100,1000), 3: (500,5000)}
  diccionarioGrafoGilbert = {1:(30,0.02), 2: (100,0.02), 3: (500,0.02)}
  diccionarioGrafoMalla = {1:(6,5), 2: (20,5), 3: (20,25)}

  for i in range(1,4):
    nodosGeoSimple = diccionarioGrafoGeo[i][0]
    nodosBarabasi = diccionarioGrafoBarabasi[i][0]
    nodosDorogovtsev = diccionarioGrafoDorogovtsev[i]
    nodosErdos = diccionarioGrafoErdos[i][0]
    nodosGilbert = diccionarioGrafoGilbert[i][0]
    baseMalla = diccionarioGrafoMalla[i][0]
    baseAltura = diccionarioGrafoMalla[i][1]

    rGeo = diccionarioGrafoGeo[i][1]
    aristasBarabasi = diccionarioGrafoBarabasi[i][1]
    numeroParesErdos = diccionarioGrafoErdos[i][1]
    probabilidadGilbert = diccionarioGrafoGilbert[i][1]

    grafoGeo_ = grafoGeoSimple.grafoGeo(nodosGeoSimple,rGeo)
    grafoBarabasi_ = grafoBarabasi.grafoBarabasi(nodosBarabasi,aristasBarabasi)
    grafoDorogovtsev_ = grafoDorogovtsev.grafoDorogovtsev(nodosDorogovtsev)
    grafoErdos_ = grafoErdos.grafoErdos(nodosErdos,numeroParesErdos)
    grafoGilbert_ = grafoGilbert.grafoGilbert(nodosGilbert,probabilidadGilbert)
    grafoMalla_ = grafoMalla.grafoMalla(baseMalla,baseAltura)

    primerNodoGeo = list(grafoGeo_.nodos.keys())[0]
    primerNodoBarabasi = list(grafoBarabasi_.nodos.keys())[0]
    primerNodoDorogovtsev = list(grafoDorogovtsev_.nodos.keys())[0]
    primerNodoErdos = list(grafoErdos_.nodos.keys())[0]
    primerNodoGilbert = list(grafoGilbert_.nodos.keys())[0]
    primerNodoMalla = list(grafoMalla_.nodos.keys())[0]

    arbolGeo = BFS(grafoGeo_, primerNodoMalla)
    arbolBarabasi = BFS(grafoBarabasi_, primerNodoMalla)
    arbolDorogovtsev = BFS(grafoDorogovtsev_, primerNodoMalla)
    arbolErdos = BFS(grafoErdos_, primerNodoMalla)
    arbolGilbert = BFS(grafoGilbert_, primerNodoMalla)
    arbolMalla = BFS(grafoMalla_, primerNodoMalla)

    arbolGeo.generarArchivoGV('{} # nodos {}'.format('BFSGeo',str(nodosGeoSimple)))
    arbolBarabasi.generarArchivoGV('{} # nodos {}'.format('BFSBarabasi',str(nodosBarabasi)))
    arbolDorogovtsev.generarArchivoGV('{} # nodos {}'.format('BFSDorogovtsev',str(nodosDorogovtsev)))
    arbolErdos.generarArchivoGV('{} # nodos {}'.format('BFSErdos',str(nodosErdos)))
    arbolGilbert.generarArchivoGV('{} # nodos {}'.format('BFSGilbert',str(nodosGilbert)))
    arbolMalla.generarArchivoGV('{} # nodos {}'.format('BFSMalla',str(baseMalla*baseAltura)))

  


