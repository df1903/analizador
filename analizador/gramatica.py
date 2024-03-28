class Gramatica:

  def __init__(self, terminales: [str], no_terminales: [str]):
    self.__terminales = terminales
    self.__no_terminales = no_terminales
    self.__simbolo_inicial = None
    self.__producciones = {}


  def get_simbolo_inicial(self):
    return self.__simbolo_inicial

  def get_no_terminales(self):
    return self.__no_terminales

  def get_terminales(self):
    return self.__terminales

  def get_producciones(self):
    return self.__producciones

  def agregar_simbolo_inicial(self, simbolo_inicial: str) -> bool:
    """
    Agrega el simbolo inicial de la gramatica si no tiene simbolo inicial
    :param simbolo_inicial:
    :return: bool
    """
    if self.__simbolo_inicial is not None:
      raise ValueError("La gramatica ya tiene un simbolo inicial")

    if simbolo_inicial in self.__no_terminales:
      self.__simbolo_inicial = simbolo_inicial
      return True
    else:
      return False

  
  def agregar_produccion(self, no_terminal: str, produccion: [str]) -> bool:
    """
    Agrega una produccion a un no terminal
    :param no_terminal:
    :param produccion:
    :return: bool
    """
    if no_terminal not in self.__no_terminales:
      return False

    # se verifica que la produccion tenga simbolos que pertenezcan a la gramatica
    for simbolo in produccion:
      if (simbolo not in self.__terminales) and (simbolo not in self.__no_terminales):
        return False

    if no_terminal not in self.__producciones:
      self.__producciones[no_terminal] = []

    self.__producciones[no_terminal].append(produccion)

    return True