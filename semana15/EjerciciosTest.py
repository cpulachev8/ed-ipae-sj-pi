import unittest
from ejercicio1 import es_potencia

class EjerciciosTest(unittest.TestCase):

    def test_ejercicio_uno_ok(self):
        es_potencia(8, 2)
    
    def test_ejercicio_uno_fail(self):
        es_potencia(7, 2)

if __name__ == '__main__':
    unittest.main()