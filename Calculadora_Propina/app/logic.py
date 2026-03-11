# app/logic.py

def calcular_propina_porcentaje(monto_cuenta, porcentaje):
    """
    Calcula el monto de la propina basado en un porcentaje del total.

    Args:
        monto_cuenta (float): El valor total de la factura.
        porcentaje (float): El porcentaje de propina a aplicar (ej. 15).

    Returns:
        float: El monto calculado de la propina.

    Raises:
        ValueError: Si el monto o el porcentaje son negativos.
    """
    if monto_cuenta < 0 or porcentaje < 0:
        raise ValueError("El monto y el porcentaje deben ser positivos.")
    return monto_cuenta * (porcentaje / 100)

def calcular_propina_fija(monto_cuenta, monto_propina):
    """
    Valida y retorna un monto de propina fijo predefinido.

    Args:
        monto_cuenta (float): El valor total de la factura.
        monto_propina (float): El monto fijo que se desea dejar.

    Returns:
        float: El monto de la propina validado.

    Raises:
        ValueError: Si la cuenta o la propina son valores negativos.
    """
    if monto_cuenta < 0 or monto_propina < 0:
        raise ValueError("Los montos deben ser positivos.")
    return monto_propina

def dividir_cuenta(monto_total, num_personas):
    """
    Divide el costo total entre el número de comensales.

    Args:
        monto_total (float): La suma de la cuenta más la propina.
        num_personas (int): Número de personas que pagarán.

    Returns:
        float: El monto que debe pagar cada persona redondeado a 4 decimales.

    Raises:
        ValueError: Si el número de personas es menor o igual a cero.
    """
    if num_personas <= 0:
        raise ValueError("El número de personas debe ser al menos 1.")
    
    monto_por_persona = monto_total / num_personas
    return round(monto_por_persona, 4)
