import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import unittest
from io import StringIO

from ui.menu import mostrar_menu


class TestMenu(unittest.TestCase):

    def test_mostrar_menu(self):
        # Capturar lo que se imprime
        captured_output = StringIO()
        sys.stdout = captured_output

        mostrar_menu()

        # Restaurar stdout
        sys.stdout = sys.__stdout__

        salida = captured_output.getvalue()

        # Verificaciones
        self.assertIn("CALCULADORA DE PROPINA", salida)
        self.assertIn("1. Calcular propina por porcentaje", salida)
        self.assertIn("2. Calcular propina con monto fijo", salida)
        self.assertIn("3. Salir", salida)
        self.assertIn("===================================", salida)


if __name__ == "__main__":
    unittest.main()
