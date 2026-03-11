import sys
import os
import io 
import unittest
from unittest.mock import patch
# Añadimos la raíz del proyecto (dos niveles arriba de este archivo) al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# ... el resto de tus imports y código ...
from app.ui import menu_interactivo

class TestUI(unittest.TestCase):

    @patch('builtins.input', side_effect=['100', '1', '10', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_interactivo_porcentaje_exito(self, mock_stdout, mock_input):
        """
        Simula: Cuenta 100, Opción 1 (Porcentaje), 10%, entre 2 personas.
        Resultado esperado: 110 total / 2 = 55 por persona.
        """
        menu_interactivo()
        
        output = mock_stdout.getvalue()
        
        # Verificamos que los datos clave aparezcan en el resumen final
        self.assertIn("Subtotal:", output)
        self.assertIn("Propina:", output)
        # Dependiendo de cómo funcione formatear_moneda, buscamos el valor
        self.assertIn("55", output) 

    @patch('builtins.input', side_effect=['200', '2', '20', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_interactivo_monto_fijo_exito(self, mock_stdout, mock_input):
        """
        Simula: Cuenta 200, Opción 2 (Fijo), 20 de propina, entre 4 personas.
        Resultado esperado: 220 total / 4 = 55 por persona.
        """
        menu_interactivo()
        
        output = mock_stdout.getvalue()
        self.assertIn("Total General:", output)
        self.assertIn("55", output)

    @patch('builtins.input', side_effect=['abc']) # Entrada inválida (no es número)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_interactivo_error_entrada(self, mock_stdout, mock_input):
        """
        Verifica que el programa maneje errores de tipo de dato (ValueError).
        """
        menu_interactivo()
        
        output = mock_stdout.getvalue()
        self.assertIn("❌ Error de entrada", output)

if __name__ == '__main__':
    unittest.main()