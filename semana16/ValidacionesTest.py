import unittest
import Validaciones

class OperacionesTest(unittest.TestCase):
    # def test_RUC_valido(self):
    #     self.assertEqual(Validaciones.validarRUC('20467534026'), True)

    # def test_RUC_no_valido1(self):
    #     self.assertEqual(Validaciones.validarRUC('20467534025'), False)

    # def test_RUC_no_valido2(self):
    #     self.assertNotEqual(Validaciones.validarRUC('20467534025'), True)

    # def test_RUC_exception(self):
    #     self.assertRaises(TypeError, Validaciones.validarRUC, 20467534026)
           
    def test_positive(self):
        #ruc 10465988458  
        #otro_ruc 20336951527
        self.assertTrue( Validaciones.validarRUC('20512333797') is True)

    def test_ruc_numeros_caracteres(self):
        self.assertEqual(Validaciones.validarRUC("203938"), False)

    def test_ruc_primeros_caracteres(self):
        self.assertEqual(Validaciones.validarRUC("30512333797"), False)
        
 
if __name__ == '__main__':
    unittest.main()

# Comandos para calcular coverage
# 1) Calcular coverage, se ejecuta luego de agregar un nuevo test o por primera vez cuando se realiza el primer cálculo de coverage
# coverage run -m unittest EjerciciosTest.py
# EjerciciosTest.py es la clase que contiene los unittest
# 2) Visualizar el resultado de coverage
# coverage report -m
# Enlace para la documentación: https://coverage.readthedocs.io/en/6.3.1/