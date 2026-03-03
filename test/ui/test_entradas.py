import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import unittest
from unittest.mock import patch
from io import StringIO

from ui.entradas import obtener_float, obtener_int, mostrar_menu


class TestEntradas(unittest.TestCase):

    # -------------------------
    # Tests obtener_float
    # -------------------------

    @patch("builtins.input", return_value="10.5")
    def test_obtener_float_valido(self, mock_input):
        resultado = obtener_float("Ingrese un número: ")
        self.assertEqual(resultado, 10.5)

    @patch("builtins.input", return_value="abc")
    def test_obtener_float_invalido(self, mock_input):
        with self.assertRaises(ValueError):
            obtener_float("Ingrese un número: ")

    # -------------------------
    # Tests obtener_int
    # -------------------------

    @patch("builtins.input", return_value="5")
    def test_obtener_int_valido(self, mock_input):
        resultado = obtener_int("Ingrese un entero: ")
        self.assertEqual(resultado, 5)

    @patch("builtins.input", return_value="3.5")
    def test_obtener_int_invalido(self, mock_input):
        with self.assertRaises(ValueError):
            obtener_int("Ingrese un entero: ")

    # -------------------------
    # Tests mostrar_menu
    # -------------------------

    def test_mostrar_menu(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        mostrar_menu()

        sys.stdout = sys.__stdout__

        salida = captured_output.getvalue()

        self.assertIn("CALCULADORA DE PROPINA", salida)
        self.assertIn("1. Calcular propina por porcentaje", salida)
        self.assertIn("2. Calcular propina con monto fijo", salida)
        self.assertIn("3. Salir", salida)


if __name__ == "__main__":
    unittest.main()
