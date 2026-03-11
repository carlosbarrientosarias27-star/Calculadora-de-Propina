import sys
import os
import unittest
import runpy  # Librería estándar para ejecutar módulos
from unittest.mock import patch

# Ajuste de ruta para subir a la raíz del proyecto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

class TestMain(unittest.TestCase):

    def test_main_ejecuta_menu(self):
        """
        Verifica que al ejecutar main.py, se llame a menu_interactivo.
        """
        # Limpiamos el caché por seguridad
        if 'main' in sys.modules:
            del sys.modules['main']

        # Parchamos la función en el paquete original
        with patch('app.ui.menu_interactivo') as mock_menu:
            # run_path simula la ejecución del script desde la terminal
            # Esto garantiza que el bloque 'if __name__ == "__main__":' se ejecute
            runpy.run_path(os.path.join(BASE_DIR, 'main.py'), run_name="__main__")
            
            # Verificamos si la función fue llamada
            self.assertTrue(mock_menu.called, "menu_interactivo() no fue llamada al ejecutar main.py")

if __name__ == '__main__':
    unittest.main()