import sys
import os
import unittest

# Añadimos la raíz del proyecto al path para evitar el ModuleNotFoundError
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app.utils import formatear_moneda

class TestUtils(unittest.TestCase):

    def test_formatear_moneda_entero(self):
        """Prueba que un entero se formatee con símbolo $ y dos decimales."""
        self.assertEqual(formatear_moneda(100), "$100.00")

    def test_formatear_moneda_decimales(self):
        """Prueba el redondeo o ajuste de decimales."""
        self.assertEqual(formatear_moneda(1250.5), "$1,250.50")

    def test_formatear_moneda_miles(self):
        """Prueba que se incluya la coma como separador de miles."""
        self.assertEqual(formatear_moneda(1000000), "$1,000,000.00")

    def test_formatear_moneda_cero(self):
        """Prueba el comportamiento con el valor cero."""
        self.assertEqual(formatear_moneda(0), "$0.00")

if __name__ == '__main__':
    unittest.main()