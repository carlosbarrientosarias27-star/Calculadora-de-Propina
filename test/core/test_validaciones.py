import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from core.validaciones import (
    validar_total,
    validar_personas,
    validar_porcentaje,
    validar_propina_fija
)


class TestValidaciones(unittest.TestCase):

    # -------------------------
    # validar_total
    # -------------------------

    def test_validar_total_valido(self):
        # No debe lanzar excepción
        validar_total(100)

    def test_validar_total_cero(self):
        with self.assertRaises(ValueError):
            validar_total(0)

    def test_validar_total_negativo(self):
        with self.assertRaises(ValueError):
            validar_total(-50)

    # -------------------------
    # validar_personas
    # -------------------------

    def test_validar_personas_valido(self):
        validar_personas(3)

    def test_validar_personas_cero(self):
        with self.assertRaises(ValueError):
            validar_personas(0)

    def test_validar_personas_negativo(self):
        with self.assertRaises(ValueError):
            validar_personas(-2)

    def test_validar_personas_no_entero(self):
        with self.assertRaises(ValueError):
            validar_personas(2.5)

    # -------------------------
    # validar_porcentaje
    # -------------------------

    def test_validar_porcentaje_valido(self):
        validar_porcentaje(10)

    def test_validar_porcentaje_cero(self):
        with self.assertRaises(ValueError):
            validar_porcentaje(0)

    def test_validar_porcentaje_negativo(self):
        with self.assertRaises(ValueError):
            validar_porcentaje(-5)

    # -------------------------
    # validar_propina_fija
    # -------------------------

    def test_validar_propina_fija_valida(self):
        validar_propina_fija(0)
        validar_propina_fija(15)

    def test_validar_propina_fija_negativa(self):
        with self.assertRaises(ValueError):
            validar_propina_fija(-10)


if __name__ == "__main__":
    unittest.main()