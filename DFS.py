import grafoGeoSimple 
import grafoGeoSimple 
import grafoGilbert
import grafoMalla 
import grafoErdos 
import grafoBarabasi
import grafoDorogovtsev 

from grafo import Grafo 

def DFSR(grafoGenerado, nodoFuente, visitados, grafoDFSR):

  diccionarioNodos = grafoGenerado.nodos
  visitados.append(nodoFuente)
  
  for nodoAdjacente in diccionarioNodos[nodoFuente].atributos['Vecinos']:
    if nodoAdjacente.id not in visitados:
      grafoDFSR.agregarArista('{} -- {}'.format(str(nodoFuente), str(nodoAdjacente.id)),str(nodoFuente),str(nodoAdjacente.id))     
      grafoDFSR = DFSR(grafoGenerado, nodoAdjacente.id, visitados, grafoDFSR)

  return grafoDFSR


def DFSI(grafoGenerado, nodoFuente):

  '''
    Funcion para generar un arbol DFS dado un grafo : grafoGenerado
    y un nodo inicio : nodoFuente

    Utilizamos el array visitados por que nodos hemos pasado
    DFS utiliza una pila para recorrer el grafo Last in First Out
  '''

  arbolDFS = Grafo()
  diccionarioNodos = grafoGenerado.nodos 
  visitados = [nodoFuente]
  pila = [nodoFuente]

  while pila:

    m = pila.pop()
    if m not in visitados:
      visitados.append(m)
    
    for nodoAdjacente in diccionarioNodos[m].atributos['Vecinos']:
      if nodoAdjacente.id not in visitados:
        if nodoAdjacente.id not in pila:
            pila.append(nodoAdjacente.id)
 
    if pila:
      ultimoNodo = pila[-1]
      arbolDFS.agregarArista('{} -- {}'.format(str(m), str(ultimoNodo)),str(m),str(ultimoNodo))

  return arbolDFS

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

    emptyGraph1 = Grafo()
    emptyGraph2 = Grafo()
    emptyGraph3 = Grafo()
    emptyGraph4 = Grafo()
    emptyGraph5 = Grafo()
    emptyGraph6 = Grafo()

    arbolGeo = DFSR(grafoGeo_, primerNodoMalla,[],emptyGraph1)
    arbolBarabasi = DFSR(grafoBarabasi_, primerNodoMalla,[],emptyGraph2)
    arbolDorogovtsev = DFSR(grafoDorogovtsev_, primerNodoMalla,[],emptyGraph3)
    arbolErdos = DFSR(grafoErdos_, primerNodoMalla,[],emptyGraph4)
    arbolGilbert = DFSR(grafoGilbert_, primerNodoMalla,[],emptyGraph5)
    arbolMalla = DFSR(grafoMalla_, primerNodoMalla,[],emptyGraph6)

    arbolGeo.generarArchivoGV('{} # nodos {}'.format('DFSRGeo',str(nodosGeoSimple)))
    arbolBarabasi.generarArchivoGV('{} # nodos {}'.format('DFSRBarabasi',str(nodosBarabasi)))
    arbolDorogovtsev.generarArchivoGV('{} # nodos {}'.format('DFSRDorogovtsev',str(nodosDorogovtsev)))
    arbolErdos.generarArchivoGV('{} # nodos {}'.format('DFSRErdos',str(nodosErdos)))
    arbolGilbert.generarArchivoGV('{} # nodos {}'.format('DFSRGilbert',str(nodosGilbert)))
    arbolMalla.generarArchivoGV('{} # nodos {}'.format('DFSRMalla',str(baseMalla*baseAltura)))