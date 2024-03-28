from unittest import TestCase
from analizador.gramatica import Gramatica


class TestGramatica(TestCase):

    def test_agregar_simbolo_inicial(self):
        # datos de la gramatica
        terminales: [str] = ["m", "a", "b", "d", "r"]
        no_terminales: [str] = ["T", "U", "P", "X", "D", "R"]
        simbolo_inicial: str = "T"  

        # se crea la gramatica y se agrega el simbolo inicial
        gramatica = Gramatica(terminales, no_terminales)
        resultado: bool = gramatica.agregar_simbolo_inicial(simbolo_inicial)

        # se verifica que el simbolo inicial se haya agregado correctamente
        self.assertTrue(resultado)
        self.assertEqual(gramatica.get_simbolo_inicial(), simbolo_inicial)
    
    def test_agregar_simbolo_inicial_error(self):
        # datos de la gramatica
        terminales: [str] = ["m", "a", "b", "d", "r"]
        no_terminales: [str] = ["T", "U", "P", "X", "D", "R"]
        simbolo_inicial: str = "T"  

        # se crea la gramatica y se agrega el simbolo inicial
        gramatica = Gramatica(terminales, no_terminales)
        gramatica.agregar_simbolo_inicial(simbolo_inicial)

        # se verifica que el simbolo inicial no se pueda agregar dos veces
        with self.assertRaises(ValueError):
            gramatica.agregar_simbolo_inicial("U")

    def test_agregar_simbolo_inicial_error_no_terminales(self):
        # datos de la gramatica
        terminales: [str] = ["m", "a", "b", "d", "r"]
        no_terminales: [str] = ["T", "U", "P", "X", "D", "R"]
        simbolo_inicial: str = "Z"

        # se crea la gramatica y se agrega el simbolo inicial
        gramatica = Gramatica(terminales, no_terminales)

        # se verifica que el simbolo inicial no se pueda agregar si no es un no terminal
        resultado: bool = gramatica.agregar_simbolo_inicial(simbolo_inicial)
        self.assertFalse(resultado)
        self.assertIsNone(gramatica.get_simbolo_inicial())
    
    def test_agregar_produccion(self):
        # datos de la gramatica
        terminales: [str] = ["m", "a", "b", "d", "r"]
        no_terminales: [str] = ["T", "U", "P", "X", "D", "R"]
        simbolo_inicial: str = "T"  

        # se crea la gramatica y se agrega el simbolo inicial
        gramatica = Gramatica(terminales, no_terminales)
        gramatica.agregar_simbolo_inicial(simbolo_inicial)

        # se agrega una produccion a un no terminal
        no_terminal: str = "T"
        produccion: [str] = "PmU"
        resultado: bool = gramatica.agregar_produccion(no_terminal, produccion)

        # se verifica que la produccion se haya agregado correctamente
        self.assertTrue(resultado)
        self.assertEqual(gramatica.get_producciones(), {no_terminal: [produccion]})
    
    def test_agregar_produccion_error_no_terminal(self):
        # datos de la gramatica
        terminales: [str] = ["m", "a", "b", "d", "r"]
        no_terminales: [str] = ["T", "U", "P", "X", "D", "R"]
        simbolo_inicial: str = "T"  

        # se crea la gramatica y se agrega el simbolo inicial
        gramatica = Gramatica(terminales, no_terminales)
        gramatica.agregar_simbolo_inicial(simbolo_inicial)

        # se agrega una produccion a un no terminal
        no_terminal: str = "Z"
        produccion: [str] = "PmU"
        resultado: bool = gramatica.agregar_produccion(no_terminal, produccion)

        # se verifica que la produccion no se pueda agregar si no es un no terminal
        self.assertFalse(resultado)
        self.assertEqual(gramatica.get_producciones(), {})
    
    def test_agregar_produccion_error_simbolos(self):
        # datos de la gramatica
        terminales: [str] = ["m", "a", "b", "d", "r"]
        no_terminales: [str] = ["T", "U", "P", "X", "D", "R"]
        simbolo_inicial: str = "T"  

        # se crea la gramatica y se agrega el simbolo inicial
        gramatica = Gramatica(terminales, no_terminales)
        gramatica.agregar_simbolo_inicial(simbolo_inicial)

        # se agrega una produccion a un no terminal
        no_terminal: str = "T"
        produccion: [str] = "PmZ"
        resultado: bool = gramatica.agregar_produccion(no_terminal, produccion)

        # se verifica que la produccion no se pueda agregar si tiene simbolos que no pertenecen a la gramatica
        self.assertFalse(resultado)
        self.assertEqual(gramatica.get_producciones(), {})
