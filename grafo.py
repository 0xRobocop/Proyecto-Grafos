from nodo import Nodo 
from arista import Arista 

ATRIBUTO_ARISTAS = 'Aristas'
ATRIBUTO_VECINOS = 'Vecinos'
ATRIBUTO_DIJKSTRA = 'Dijkstra'
class Grafo():

  def __init__(self):
    self.id = 'grafo'
    self.nodos = {} 
    self.aristas = {}
    
  def agregarNodo(self, nombre):

    """
    Si el nodo no existe, lo crea
    """
    nodo_ = self.nodos.get(nombre)

    if nodo_ is None:
      nodo_ = Nodo(nombre)
      self.nodos[nombre] = nodo_

    
    return nodo_
  
  def agregarArista(self, nombreArista, nombreNodoOrigen, nombreNodoDestino, peso=0):
    """
    Agregar una arista al grafo 
    Se retorna la arista creada
    """

    arista_ = self.aristas.get(nombreArista)

    if arista_ is None:
      
      nodoOrigen = self.agregarNodo(nombreNodoOrigen)
      nodoDestino = self.agregarNodo(nombreNodoDestino)

      _arista = Arista(nombreArista,nodoOrigen,nodoDestino,peso) 
      self.aristas[nombreArista] = _arista

      nodoOrigen.atributos[ATRIBUTO_VECINOS].append(nodoDestino)
      nodoDestino.atributos[ATRIBUTO_VECINOS].append(nodoOrigen)

      nodoOrigen.atributos[ATRIBUTO_ARISTAS].append(_arista)
      nodoDestino.atributos[ATRIBUTO_ARISTAS].append(_arista)



  def dameGradoNodo(self, nombreNodo):
    if not nombreNodo in self.nodos:
      return 0

    else:
      _nodo = self.nodos[nombreNodo]
      grado = len(_nodo.atributos[ATRIBUTO_VECINOS])
      return grado

  def dameNodo(self, nombre):
    return self.nodos[nombre]

  def imprimirGrafo(self):
    for arista in self.aristas:
      objetoArista = self.aristas[arista]
      grafoInicial = objetoArista.inicio.id
      grafoFinal = objetoArista.final.id
      print('{} -- {}'.format(grafoInicial,grafoFinal))

  def generarArchivoGV(self, sufijo):
    file = open('{}{}.gv'.format(self.id, sufijo), 'w')
    file.write('graph #nombre {' + '\n')
    for arista in self.aristas:
      file.write('{};'.format(arista) + '\n')
    file.write('}')
    file.close()


  def generarArchivoGVDjisktra(self, sufijo):
    file = open('{}{}.gv'.format(self.id, sufijo), 'w')
    file.write('graph #nombre {' + '\n')
    for arista in self.aristas:
      file.write('{};'.format(arista) + '\n')
    for nodo in self.nodos:
      file.write('{} [label="{}"]'.format(nodo,self.nodos[nodo].atributos['Dijkstra']) + '\n')
    file.write('}')
    file.close()

  def generarArchivoGVKruskal(self, sufijo):
    file = open('{}{}.gv'.format(self.id, sufijo), 'w')
    file.write('graph #nombre {' + '\n')
    pesoFinal = 0
    for arista in self.aristas:
      peso = self.aristas[arista].atributos["Peso"]
      pesoFinal += int(peso)
      file.write('{} [label={}]'.format(arista, self.aristas[arista].atributos["Peso"]) + '\n')
    file.write(str(pesoFinal) + '\n')
    file.write('}')
    file.close()

