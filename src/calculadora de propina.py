def calcular_propina(total_cuenta):
    """
    Calcula el 10% de propina sobre el total de la cuenta.
    """
    propina = total_cuenta * 0.10
    return propina 


# Prueba manual
total = 1000
resultado = calcular_propina(total)

print("Total de la cuenta:", total)
print("Propina (10%):", resultado)
print("Total a pagar:", total + resultado)