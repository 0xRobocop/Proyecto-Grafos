import grafoGeoSimple 
import grafoGilbert
import grafoMalla 
import grafoErdos 
import grafoBarabasi
import grafoDorogovtsev 

from grafo import Grafo 

def dijkstra(grafoFuente, s, t):
        """
        dijkstra es un algoritmo para encontrar el camino más corto entre nodos en un grafo.
        :param grafoFuente: el grafo original
        :param s: node fuente
        :param t: node objetivo
        :return g un grafo del nodo fuente al nodo objetivo
        """
        l = []
        dist = {}
        prev = {}
        descubierto = {}
        diccionarioNodos = grafoFuente.nodos
        diccionarioAristas = grafoFuente.aristas
        for v in diccionarioNodos:
            dist[v] = float('inf')
            prev[v] = None
            descubierto[v] = False
        dist[s] = 0
        l.append((s, dist[s]))
        while len(l) != 0:
            u = min(l, key=lambda x: x[1])
            l.remove(u)
            u = u[0]
            descubierto[u] = True
            if u == t:
                break
            for v in diccionarioNodos[u].atributos['Vecinos']:
                if not descubierto[v.id]:
                    alt = dist[u] + diccionarioAristas['{} -- {}'.format(u,v.id)].atributos["Peso"]
                    if alt < dist[v.id]:
                        dist[v.id] = alt
                        prev[v.id] = u
                        l.append((v.id, dist[v.id]))
      
        u = t
        g = Grafo()
        while u is not None:
            nodoU = g.agregarNodo(u)
            nodoU.atributos['Dijkstra'] = dist[u]
            if prev[u] is not None:
                nodoPrevioU = g.agregarNodo(prev[u])
                nodoPrevioU.atributos['Dijkstra'] = dist[prev[u]]
                g.agregarArista('{} -- {}'.format(prev[u],u),prev[u],u)
                u = prev[u]
            else:
                break
        return g

def agregarNodo(self, nombre):

    """
    Si el nodo no existe, lo crea
    """
    nodo_ = self.nodos.get(nombre)

    if nodo_ is None:
      nodo_ = Nodo(nombre)
      self.nodos[nombre] = nodo_

    
    return nodo_        

if __name__ == "__main__":

  diccionarioGrafoGeo = {1: (500,0.3)}
  
  for i in range(1,2):
    nodosGeoSimple = diccionarioGrafoGeo[i][0]
    
    rGeo = diccionarioGrafoGeo[i][1]
    
    grafoGeo_ = grafoGeoSimple.grafoGeo(nodosGeoSimple,rGeo)
    
    primerNodoGeo = list(grafoGeo_.nodos.keys())[0]
    segundoNodoGeo = list(grafoGeo_.nodos.keys())[75]
    
    print('PrimerNodo: ', primerNodoGeo)
    print('SegundoNodo: ', segundoNodoGeo)
    grafoDijkstra = dijkstra(grafoGeo_,primerNodoGeo,segundoNodoGeo)
  
    grafoDijkstra.generarArchivoGVDjisktra('{} # nodos {}'.format('DijkstraGeo',str(nodosGeoSimple)))
    