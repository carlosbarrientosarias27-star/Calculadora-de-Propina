def calcular_propina(total_cuenta):
    """
    Calcula el 10% de propina sobre el total de la cuenta.
    """
    propina = total_cuenta * 0.10
    return propina 


def calcular_propina(total_cuenta, porcentaje):
    """
    Calcula la propina según el porcentaje indicado.
    Valida que el porcentaje sea positivo.
    """
    if porcentaje <= 0:
        raise ValueError("El porcentaje debe ser un número positivo mayor que 0.")
    
    propina = total_cuenta * (porcentaje / 100)
    return propina


# Prueba manual
total = 1000
porcentaje_propina = 10

resultado = calcular_propina(total, porcentaje_propina)

print("Total de la cuenta:", total)
print(f"Propina ({porcentaje_propina}%):", resultado)
print("Total a pagar:", total + resultado)

