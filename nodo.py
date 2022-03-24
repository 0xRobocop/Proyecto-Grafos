ATRIBUTO_ARISTAS = 'Aristas'
ATRIBUTO_VECINOS = 'Vecinos'
ATRIBUTO_POS = 'Posicion'

import random
import numpy 
class Nodo:

  """
  !param id: Identificador unico del nodo
  """
  def __init__(self, id):
    self.id = id
    self.atributos = {
      ATRIBUTO_ARISTAS: [],
      ATRIBUTO_VECINOS: [],
      ATRIBUTO_POS: numpy.array([random.random(),random.random()])
    }
