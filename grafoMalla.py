from grafo import Grafo
import numpy

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
        g.agregarArista('{} -- {}'.format(fila * n + columna, fila * n + columna + 1), str(fila * n + columna), str(fila * n + columna + 1))
      if fila < (m-1):
        g.agregarArista('{} -- {}'.format(fila * n + columna, (fila+1)* n + columna), str(fila * n + columna), str((fila+1)* n + columna))
    
  return g

tareaGrafos = {1:(6,5), 2: (20,5), 3: (20,25)}

for i in range(1,4):
  base = tareaGrafos[i][0]
  altura = tareaGrafos[i][1]

  grafoMalla_ = grafoMalla(base,altura)

  grafoMalla_.generarArchivoGV('{} {}'.format('Malla',str(i)))
