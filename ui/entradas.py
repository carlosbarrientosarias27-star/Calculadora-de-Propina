# ui/entradas.py

def obtener_float(mensaje: str) -> float:
    return float(input(mensaje))


def obtener_int(mensaje: str) -> int:
    return int(input(mensaje))
def mostrar_menu() -> None:
    print("\n===== CALCULADORA DE PROPINA =====")
    print("1. Calcular propina por porcentaje")
    print("2. Calcular propina con monto fijo")
    print("3. Salir")
    print("===================================")