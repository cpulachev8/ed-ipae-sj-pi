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
