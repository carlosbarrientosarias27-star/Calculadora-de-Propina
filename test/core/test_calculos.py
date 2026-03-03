import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from core.calculos import (
    calcular_propina_porcentaje,
    calcular_propina_fija,
    dividir_cuenta
)


class TestCalculos(unittest.TestCase):

    # -------------------------
    # Tests calcular_propina_porcentaje
    # -------------------------

    def test_propina_porcentaje_valido(self):
        resultado = calcular_propina_porcentaje(100, 10)
        self.assertEqual(resultado, 10)

    def test_propina_porcentaje_decimal(self):
        resultado = calcular_propina_porcentaje(200, 12.5)
        self.assertEqual(resultado, 25)

    def test_propina_porcentaje_total_invalido(self):
        with self.assertRaises(ValueError):
            calcular_propina_porcentaje(-100, 10)

    def test_propina_porcentaje_porcentaje_invalido(self):
        with self.assertRaises(ValueError):
            calcular_propina_porcentaje(100, -5)

    # -------------------------
    # Tests calcular_propina_fija
    # -------------------------

    def test_propina_fija_valida(self):
        resultado = calcular_propina_fija(100, 20)
        self.assertEqual(resultado, 20)

    def test_propina_fija_invalida(self):
        with self.assertRaises(ValueError):
            calcular_propina_fija(100, -10)

    # -------------------------
    # Tests dividir_cuenta
    # -------------------------

    def test_dividir_cuenta_valido(self):
        total_final, por_persona = dividir_cuenta(100, 10, 2)
        self.assertEqual(total_final, 110)
        self.assertEqual(por_persona, 55)

    def test_dividir_cuenta_una_persona(self):
        total_final, por_persona = dividir_cuenta(100, 20, 1)
        self.assertEqual(total_final, 120)
        self.assertEqual(por_persona, 120)

    def test_dividir_cuenta_personas_invalidas(self):
        with self.assertRaises(ValueError):
            dividir_cuenta(100, 10, 0)


if __name__ == "__main__":
    unittest.main()