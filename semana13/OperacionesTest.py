import unittest
import Operaciones

class OperacionesTest(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(Operaciones.sumar(4,6), 10)

    def test_suma_no_valida(self):
        self.assertNotEqual(Operaciones.sumar(4,7), 10)

    def test_suma_excepcion(self):
        self.assertRaises(TypeError, Operaciones.sumar, "4", 5)

    def test_division_cero(self):
        self.assertRaises(ZeroDivisionError, Operaciones.dividir, 10, 0)

    def test_operar_suma(self):
        operacion = "+"
        a = 10
        b = 4
        self.assertEqual(Operaciones.operar(operacion, a, b), 14)

    def test_operar_resta(self):
        operacion = "-"
        a = 10
        b = 5
        self.assertEqual(Operaciones.operar(operacion, a, b), 5)

    def test_operacion_division(self):
        operacion = "/"
        a = 10
        b = 5
        self.assertEqual(Operaciones.operar(operacion, a, b), 2)

    def test_operacion_desconocida(self):
        operacion = "*"
        a = 10
        b = 5
        self.assertEqual(Operaciones.operar(operacion, a, b), -1)



if __name__ == "__main__":
    unittest.main()