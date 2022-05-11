import grafoGeoSimple 
import grafoGilbert
import grafoMalla 
import grafoErdos 
import grafoBarabasi
import grafoDorogovtsev 

from grafo import Grafo 

def dijkstra(grafoFuente, s, t):
        """
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
                    try:
                        alt = dist[u] + diccionarioAristas['{} -- {}'.format(u,v.id)].atributos["Peso"]
                    except: 
                        alt = dist[u] + diccionarioAristas['{} -- {}'.format(v.id,u)].atributos["Peso"]
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
  


    

    