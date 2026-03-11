# app/utils.py

def formatear_moneda(cantidad):
    """
    Convierte un valor numérico a un string con formato de moneda.

    Args:
        cantidad (float): El número a formatear.

    Returns:
        str: El número formateado con símbolo de peso, separador de miles y 2 decimales.
        Ejemplo: 1250.5 -> "$1,250.50"
    """
    return f"${cantidad:,.2f}"