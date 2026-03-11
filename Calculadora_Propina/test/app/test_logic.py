import sys
import os
import unittest

# Añade la carpeta raíz del proyecto al camino de búsqueda de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app.logic import calcular_propina_porcentaje, calcular_propina_fija, dividir_cuenta
# ... resto del código ...

class TestLogic(unittest.TestCase):

    # Pruebas para calcular_propina_porcentaje
    def test_calcular_propina_porcentaje_exito(self):
        self.assertEqual(calcular_propina_porcentaje(100, 15), 15.0)
        self.assertEqual(calcular_propina_porcentaje(200, 10), 20.0)

    def test_calcular_propina_porcentaje_error(self):
        with self.assertRaises(ValueError):
            calcular_propina_porcentaje(-100, 15)

    # Pruebas para calcular_propina_fija
    def test_calcular_propina_fija_exito(self):
        self.assertEqual(calcular_propina_fija(100, 20), 20)

    def test_calcular_propina_fija_error(self):
        with self.assertRaises(ValueError):
            calcular_propina_fija(100, -5)

    # Pruebas para dividir_cuenta
    def test_dividir_cuenta_exito(self):
        # 100 entre 4 personas = 25
        self.assertEqual(dividir_cuenta(100, 4), 25.0)
        # Probando el redondeo a 4 decimales que pusiste en tu código
        self.assertEqual(dividir_cuenta(100, 3), 33.3333)

    def test_dividir_cuenta_error_personas(self):
        with self.assertRaises(ValueError):
            dividir_cuenta(100, 0)

if __name__ == '__main__':
    unittest.main()