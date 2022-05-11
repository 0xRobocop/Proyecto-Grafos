from grafo import Grafo
import random

def grafoMalla(m, n, dirigido=False):
  # m es el numero de filas 
  # n es el numero de columnas

  m = max(2,m)
  n = max(2,n)

  g = Grafo()

  for fila in range(m):

    for columna in range(n):
      g.agregarNodo(str(fila * n + columna))
    
      if columna < (n-1):
        peso = (random.random()*100)/10
        g.agregarArista('{} -- {}'.format(fila * n + columna, fila * n + columna + 1), str(fila * n + columna), str(fila * n + columna + 1),peso)
      if fila < (m-1):
        peso2 = (random.random()*100)/10
        g.agregarArista('{} -- {}'.format(fila * n + columna, (fila+1)* n + columna), str(fila * n + columna), str((fila+1)* n + columna),peso2)
    
  return g


