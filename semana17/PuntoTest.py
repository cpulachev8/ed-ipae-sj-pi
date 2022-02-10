# Given-When-Then (GWT) is a semi-structured way to write down test cases

import unittest

from Punto import Punto

class PuntoTest(unittest.TestCase):

    def test_cuadrante_I(self):
        p1 = Punto(2,3)
        self.assertEqual(p1.pertenece_al_cuadrante(), "CUADRANTE I")

    def test_cuadrante_II(self):
        p1 = Punto(-2,3)
        self.assertEqual(p1.pertenece_al_cuadrante(), "CUADRANTE II")
    
    def test_cuadrante_III(self):
        p1 = Punto(-2,-3)
        self.assertEqual(p1.pertenece_al_cuadrante(), "CUADRANTE III")

    def test_cuadrante_IV(self):
        p1 = Punto(2,-3)
        self.assertEqual(p1.pertenece_al_cuadrante(), "CUADRANTE IV")

    def test_cuadrante_no_definido(self):
        p1 = Punto(0,-3)
        self.assertEqual(p1.pertenece_al_cuadrante(), "CUADRANTE NO DEFINIDO")

    def test_datos_incorrectos(self):
        p1 = Punto("0", "")
        self.assertEqual(p1.pertenece_al_cuadrante(), "CUADRANTE NO DEFINIDO")

if __name__ == '__main__':
    unittest.main()