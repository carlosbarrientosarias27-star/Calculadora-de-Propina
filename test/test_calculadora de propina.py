import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.calculadora_de_propina import (
    calcular_propina_porcentaje, 
    calcular_propina_fija, 
    dividir_cuenta, 
    validar_total,
    validar_personas
)


class TestCalculadoraPropina(unittest.TestCase):

    # ==========================
    # PRUEBAS validar_total
    # ==========================

    def test_validar_total_valido(self):
        validar_total(100)  # No debe lanzar excepción

    def test_validar_total_invalido(self):
        with self.assertRaises(ValueError):
            validar_total(0)

    # ==========================
    # PRUEBAS validar_personas
    # ==========================

    def test_validar_personas_valido(self):
        validar_personas(3)

    def test_validar_personas_invalido(self):
        with self.assertRaises(ValueError):
            validar_personas(0)

    # ==========================
    # PRUEBAS calcular_propina_porcentaje
    # ==========================

    def test_calcular_propina_porcentaje_correcto(self):
        resultado = calcular_propina_porcentaje(100, 10)
        self.assertEqual(resultado, 10)

    def test_calcular_propina_porcentaje_invalido(self):
        with self.assertRaises(ValueError):
            calcular_propina_porcentaje(100, 0)

    # ==========================
    # PRUEBAS calcular_propina_fija
    # ==========================

    def test_calcular_propina_fija_correcto(self):
        resultado = calcular_propina_fija(100, 15)
        self.assertEqual(resultado, 15)

    def test_calcular_propina_fija_negativa(self):
        with self.assertRaises(ValueError):
            calcular_propina_fija(100, -5)

    # ==========================
    # PRUEBAS dividir_cuenta
    # ==========================

    def test_dividir_cuenta_correcto(self):
        total_final, por_persona = dividir_cuenta(100, 20, 4)
        self.assertEqual(total_final, 120)
        self.assertEqual(por_persona, 30)

    def test_dividir_cuenta_personas_invalidas(self):
        with self.assertRaises(ValueError):
            dividir_cuenta(100, 20, 0)


if __name__ == "__main__":
    unittest.main()