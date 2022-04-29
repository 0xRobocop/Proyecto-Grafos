from grafo import Grafo
import random

ATRIBUTO_ARISTAS = 'Aristas'
ATRIBUTO_VECINOS = 'Vecinos'

def grafoBarabasi(n,d):

  """
  Generación aleatoria de grafos utilizando el modelo de Barabasi-Albert
  n: número de nodos
  d: nuevos nodos    
  return: grafo aleatorio generado
  """
  g = Grafo()

  for i in range(n):
    g.agregarNodo(str(i))

  for i in range(1, n):
    nodosRandom = randomArray(i)
    for j in range(i):
      grado = g.dameGradoNodo(str(nodosRandom[j]))
      p = 1 - grado / d 
      if random.random() < p:
        if nodosRandom[j] != i:
          g.agregarArista('{} -- {}'.format(str(i),str(nodosRandom[j])), str(i), str(nodosRandom[j]))
       
  
  return g


def randomArray(size):

  k = size
  numeros = []
  resultado = []

  for i in range(size):
    numeros.append(i)

  for i in range(size):
    numeroAleatorio = random.randint(0,k-1)
    resultado.append(numeros[numeroAleatorio])
    numeros.pop(numeroAleatorio)
    k = k - 1

  return resultado
  
