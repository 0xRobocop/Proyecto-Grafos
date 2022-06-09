import sys
import grafoGeoSimple 
import grafoGilbert
import grafoMalla 
import grafoErdos 
import grafoBarabasi
import grafoDorogovtsev 

from grafo import Grafo 
from BFS import BFS

def KruskalInverso(grafoFuente):
       
        g = clone(grafoFuente)
    
        q = sorted(grafoFuente.aristas.items(), key=lambda e: e[1].atributos["Peso"],
                   reverse=True)
        for e in q:
            g2 = clone(g)
        
            g2.aristas.pop(e[0])
         
            arbolBFS = BFS(g2,'0')
           
            if len(g2.nodos) != len(arbolBFS.nodos):
              g2 = clone(g)
            else:
              nombreArista = e[0]
              nombreNodoOrigen = e[1].n0.id
              nombreNodoDestino = e[1].n1.id
              peso = e[1].atributos['Peso']
              g.agregarArista(nombreArista,nombreNodoOrigen,nombreNodoDestino,peso)
        return g

    

def clone(grafoCopiar):

    id = grafoCopiar.id
    nodos = grafoCopiar.nodos.copy()
    aristas = grafoCopiar.aristas.copy()
    
    g = Grafo()
    g.id = id
    g.nodos = nodos 
    g.aristas = aristas
       
    return g

def KruskalD(grafoFuente):
       
        g = Grafo()

        # Create set for each v of V[G]
        parent = []
        rank = []
        diccionarioNodos = grafoFuente.nodos
        diccionarioAristas = grafoFuente.aristas
        for v in diccionarioNodos:
            parent.append(v)
            rank.append(0)

        # Sort edges by weight
        q = sorted(diccionarioAristas.items(), key=lambda e: e[1].atributos["Peso"])
        for e in q:
          u = e[1].n0.id 
          v = e[1].n1.id
          
          v1 = encuentraConjunto(parent, u)
          v2 = encuentraConjunto(parent, v)
          if v1 != v2:
            g.agregarArista('{} -- {}'.format(str(u), str(v)),str(u),str(v), e[1].atributos["Peso"])
            
            if rank[int(v1)] < rank[int(v2)]:
              parent[int(v1)] = v2
              rank[int(v2)] += 1
            else:
              parent[int(v2)] = v1
              rank[int(v1)] += 1
        
        return g

        

def encuentraConjunto(fuente, i):

  if fuente[int(i)] == i:
    return i

  return encuentraConjunto(fuente, fuente[int(i)])

def Prim(grafoFuente):
        
        g = Grafo()
        diccionarioNodos = grafoFuente.nodos
        diccionarioAristas = grafoFuente.aristas

        distance = [sys.maxsize] * len(diccionarioNodos)
        parent = [None] * len(diccionarioNodos)
        set = [False] * len(diccionarioNodos)

        distance[0] = 0
      
        for i in diccionarioNodos:
            min_index = 0
            min = sys.maxsize
            for v in diccionarioNodos:
                if distance[int(v)] < min and set[int(v)] is False:
                    min = distance[int(v)]
                    min_index = int(v)
            u = min_index

            set[u] = True
            g.agregarNodo(u)

            for v in diccionarioNodos[str(u)].atributos["Vecinos"]:

                try:

                  if set[int(v.id)] is False and distance[int(v.id)] > diccionarioAristas['{} -- {}'.format(str(u), str(v.id))].atributos["Peso"]:
                      distance[int(v.id)] = diccionarioAristas['{} -- {}'.format(str(u), str(v.id))].atributos["Peso"]
                    
                      parent[int(v.id)] = u
                
                except:
                  if set[int(v.id)] is False and distance[int(v.id)] > diccionarioAristas['{} -- {}'.format(str(v.id), str(u))].atributos["Peso"]:
                      distance[int(v.id)] = diccionarioAristas['{} -- {}'.format(str(v.id), str(u))].atributos["Peso"]
                    
                      parent[int(v.id)] = u

        for i in diccionarioNodos:
            if i == 0:
                continue
            if parent[int(i)] is not None:
              try:
                  g.agregarArista('{} -- {}'.format(str(parent[int(i)]), str(i)),str(parent[int(i)]),str(i), diccionarioAristas['{} -- {}'.format(str(parent[int(i)]), str(i))].atributos["Peso"])
              except:
                 g.agregarArista('{} -- {}'.format(str(parent[int(i)]), str(i)),str(parent[int(i)]),str(i), diccionarioAristas['{} -- {}'.format(str(i),str(parent[int(i)]))].atributos["Peso"])
        return g


if __name__ == "__main__":

  diccionarioGrafoGeo = {1:(50,0.3),2: (100,0.3)}
  diccionarioGrafoBarabasi = {1:(50,9), 2: (100,9)}
  diccionarioGrafoDorogovtsev = {1:50, 2: 100}
  diccionarioGrafoErdos = {1:(50,200), 2: (100,1000)}
  diccionarioGrafoGilbert = {1:(50,0.02), 2: (100,0.02)}
 
  for i in range(1,3):
    nodosGeoSimple = diccionarioGrafoGeo[i][0]
    nodosBarabasi = diccionarioGrafoBarabasi[i][0]
    nodosDorogovtsev = diccionarioGrafoDorogovtsev[i]
    nodosErdos = diccionarioGrafoErdos[i][0]
    nodosGilbert = diccionarioGrafoGilbert[i][0]

    rGeo = diccionarioGrafoGeo[i][1]
    aristasBarabasi = diccionarioGrafoBarabasi[i][1]
    numeroParesErdos = diccionarioGrafoErdos[i][1]
    probabilidadGilbert = diccionarioGrafoGilbert[i][1]

    grafoGeo_ = grafoGeoSimple.grafoGeo(nodosGeoSimple,rGeo)
    grafoBarabasi_ = grafoBarabasi.grafoBarabasi(nodosBarabasi,aristasBarabasi)
    grafoDorogovtsev_ = grafoDorogovtsev.grafoDorogovtsev(nodosDorogovtsev)
    grafoErdos_ = grafoErdos.grafoErdos(nodosErdos,numeroParesErdos)
    grafoGilbert_ = grafoGilbert.grafoGilbert(nodosGilbert,probabilidadGilbert)

    grafoGeo_.generarArchivoGV('{} # nodos {}'.format('GrafoGeneradoGeo',str(nodosGeoSimple)))
    grafoBarabasi_.generarArchivoGV('{} # nodos {}'.format('GrafoGeneradoGeoBarabasi',str(nodosBarabasi)))
    grafoDorogovtsev_.generarArchivoGV('{} # nodos {}'.format('GrafoGeneradoGeoDorogovtsev',str(nodosDorogovtsev)))
    grafoErdos_.generarArchivoGV('{} # nodos {}'.format('GrafoGeneradoGeoErdos',str(nodosErdos)))
    grafoGilbert_.generarArchivoGV('{} # nodos {}'.format('GrafoGeneradoGeoGilbert',str(nodosGilbert)))
    
    kruskalGeo = KruskalD(grafoGeo_)
    kruskalBarabasi = KruskalD(grafoBarabasi_)
    kruskalDorogovtsev = KruskalD(grafoDorogovtsev_)
    kruskalErdos = KruskalD(grafoErdos_)
    kruskalGilbert = KruskalD(grafoGilbert_)

    kruskalInversoGeo = KruskalInverso(grafoGeo_)
    kruskalInversoBarabasi = KruskalInverso(grafoBarabasi_)
    kruskalInversoDorogovtsev = KruskalInverso(grafoDorogovtsev_)
    kruskalInversoErdos = KruskalInverso(grafoErdos_)
    kruskalInversoGilber = KruskalInverso(grafoGilbert_)

    kruskalInversoGeo.generarArchivoGVKruskal('{} # nodos {}'.format('KruskalIGeo', str(nodosGeoSimple)))
    kruskalInversoBarabasi.generarArchivoGVKruskal('{} # nodos {}'.format('KruskalIBarabasi', str(nodosBarabasi)))
    kruskalInversoDorogovtsev.generarArchivoGVKruskal('{} # nodos {}'.format('KruskalIDorogovtsev', str(nodosDorogovtsev)))
    kruskalInversoErdos.generarArchivoGVKruskal('{} # nodos {}'.format('KruskalIErdos', str(nodosErdos)))
    kruskalInversoGilber.generarArchivoGVKruskal('{} # nodos {}'.format('KruskalIGilbert', str(nodosGilbert)))

    PrimGeo = Prim(grafoGeo_)
    PrimBarabasi = Prim(grafoBarabasi_)
    PrimDorogovtsev = Prim(grafoDorogovtsev_)
    PrimErdos = Prim(grafoErdos_)
    PrimGilbert = Prim(grafoGilbert_)
  
     
    kruskalGeo.generarArchivoGVKruskal('{} # nodos {}'.format('KruskalGeo',str(nodosGeoSimple)))
    kruskalBarabasi.generarArchivoGVKruskal('{} # nodos {}'.format('KruskalBarabasi',str(nodosBarabasi)))
    kruskalDorogovtsev.generarArchivoGVKruskal('{} # nodos {}'.format('KruskalDorogovtsev',str(nodosDorogovtsev)))
    kruskalErdos.generarArchivoGVKruskal('{} # nodos {}'.format('KruskalErdos',str(nodosErdos)))
    kruskalGilbert.generarArchivoGVKruskal('{} # nodos {}'.format('KruskalGilbert',str(nodosGilbert)))

    PrimGeo.generarArchivoGVKruskal('{} # nodos {}'.format('PrimGeo',str(nodosGeoSimple)))
    PrimBarabasi.generarArchivoGVKruskal('{} # nodos {}'.format('PrimBarabasi',str(nodosBarabasi)))
    PrimDorogovtsev.generarArchivoGVKruskal('{} # nodos {}'.format('PrimDorogobtsev',str(nodosDorogovtsev)))
    PrimErdos.generarArchivoGVKruskal('{} # nodos {}'.format('PrimErdos',str(nodosErdos)))
    PrimGilbert.generarArchivoGVKruskal('{} # nodos {}'.format('PrimGilbert',str(nodosGilbert)))
  