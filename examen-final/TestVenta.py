import unittest
from Venta import Venta 
from DetalleVenta import DetalleVenta

class TestVenta(unittest.TestCase):

    def test_venta_efectivo(self):
        v = Venta("Christian", "Efectivo")
        v.agregar_detalle("arroz", 10, 3)
        v.calcular_total()
        self.assertEqual(v.total, 22.5)

    def test_venta_tarjeta(self):
        v = Venta("Christian", "Tarjeta")
        v.agregar_detalle("aceite", 5, 14)
        v.calcular_recargo()
        v.calcular_total()
        self.assertEqual(v.total, 55.125)

if __name__ == '__main__':
    unittest.main()