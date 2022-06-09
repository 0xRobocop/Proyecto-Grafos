import random 
import math 
import numpy as np
import pygame

from grafoDorogovtsev import grafoDorogovtsev
from grafoGeoSimple import grafoGeo
from grafoBarabasi import grafoBarabasi
from grafoErdos import grafoErdos
from grafoGilbert import grafoGilbert
from grafoMalla import grafoMalla

# LINK VIDEOS https://onering.mypinata.cloud/ipfs/QmbENxDij96GHGLAMTcDXifNjnRdStqSdc1PjkVdmDHM2Z

def distanciaEntrePuntos(a,b,c,d):
  """ puntos (a,b) y (c,d) """

  return math.sqrt( (a-c)**2 + (b-d)**2)

g = grafoMalla(25,20)
nodos = g.nodos.keys()
ventana = pygame.display.set_mode((500,500))
color = (200, 0, 0)

for nodo in nodos:
  objetoNodo = g.dameNodo(nodo)
  if objetoNodo.x == 0 and objetoNodo.y == 0:
    objetoNodo.x = random.random() * 500
    objetoNodo.y = random.random() * 500

c1 = 55
c2 = 0.35
active=True 
radio = 3 


def proyecta(g):

  nodos = g.nodos.keys()
  nodos = list(nodos)

  aristas = g.aristas.keys()
  aristas = list(aristas)

  for nodoID in nodos:
    objetoNodo = g.dameNodo(nodoID)
    x = objetoNodo.x
    y = objetoNodo.y 
    coordenadas = np.array([x,y])
    vecinos = objetoNodo.atributos['Vecinos']
    s = np.zeros(2)

    for vecinoID in vecinos:
      objetoVecino = g.dameNodo(vecinoID.id)
      x1 = objetoVecino.x 
      y1 = objetoVecino.y
      d = distanciaEntrePuntos(x,y,x1,y1)
      ga = c2*math.log(d/c1)
      vVecino = np.array([x1,y1])
      #nombreArista = '{} -- {}'.format(nodoID, vecinoID)

      vF = vVecino - coordenadas
      normalizar = np.linalg.norm(vF)
      vF = vF/normalizar 
      vF = ga * vF
      s += vF

    coordenadas += s 
    nx = coordenadas[0]
    ny = coordenadas[1]
    objetoNodo.gx = nx 
    objetoNodo.gy = ny 
    
  for nodoID in nodos:
    objetoNodo = g.dameNodo(nodoID)
    objetoNodo.x = objetoNodo.gx
    objetoNodo.y = objetoNodo.gy
  
  for arista in aristas:
    objetoArista = g.aristas[arista]
    nodo0 = objetoArista.n0
    nodo1 = objetoArista.n1 
    x1 = nodo0.x 
    y1 = nodo0.y
    x2 = nodo1.x 
    y2 = nodo1.y

    d = distanciaEntrePuntos(x1,y1,x2,y2)

    
    pygame.draw.circle(ventana,color,(int(x1),int(y1)),radio)
    pygame.draw.circle(ventana,color,(int(x2),int(y2)),radio)
    pygame.draw.line(ventana, 'white', (int(x1), int(y1)), (int(x2), int(y2)), 1)

while active:
  
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      active = False 
  
  proyecta(g)

  pygame.display.update()
  ventana.fill('blue')


