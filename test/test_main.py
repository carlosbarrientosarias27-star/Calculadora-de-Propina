import sys
import os

# Agregamos la carpeta raíz al buscador de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from main import main  # Ahora sí lo encontrará

class TestMain(unittest.TestCase):

    @patch('main.mostrar_menu')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main_salir_inmediatamente(self, mock_print, mock_input, mock_menu):
        """Prueba que el programa termine cuando se elige la opción 3 (Salir)."""
        # Simulamos que el usuario presiona '3'
        mock_input.return_value = '3'
        
        main()
        
        # Verificamos que se mostró el mensaje de despedida
        mock_print.assert_any_call("Gracias por usar la calculadora. ¡Hasta luego!")

    @patch('main.obtener_float')
    @patch('main.obtener_int')
    @patch('main.calcular_propina_porcentaje')
    @patch('main.dividir_cuenta')
    @patch('builtins.input')
    @patch('main.mostrar_menu')
    def test_flujo_calculo_porcentaje(self, mock_menu, mock_input, mock_dividir, 
                                     mock_calc_propina, mock_int, mock_float):
        """Prueba el flujo completo de calcular propina por porcentaje."""
        
        # Secuencia de entradas: Opción 1 (Porcentaje), luego Opción 3 (Salir)
        mock_input.side_effect = ['1', '3']
        
        # Simulamos valores de retorno para las funciones de entrada y cálculo
        mock_float.side_effect = [100.0, 15.0] # Total cuenta y Porcentaje
        mock_int.return_value = 2              # Personas
        mock_calc_propina.return_value = 15.0
        mock_dividir.return_value = (115.0, 57.5) # total_final, por_persona

        with patch('builtins.print') as mock_print:
            main()
            
            # Verificamos que se llamaron a las funciones de cálculo correctamente
            mock_calc_propina.assert_called_with(100.0, 15.0)
            mock_dividir.assert_called_with(100.0, 15.0, 2)
            
            # Verificamos que se imprimieron los resultados formateados
            mock_print.assert_any_call("\n----- RESULTADOS -----")
            mock_print.assert_any_call("Monto por persona: $57.50")

    @patch('builtins.input')
    @patch('main.mostrar_menu')
    def test_opcion_invalida(self, mock_menu, mock_input):
        """Prueba el manejo de una opción de menú que no existe."""
        # Primero una opción inválida '9', luego '3' para salir
        mock_input.side_effect = ['9', '3']
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    unittest.main()