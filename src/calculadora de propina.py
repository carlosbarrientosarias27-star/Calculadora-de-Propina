def calcular_propina(total_cuenta):
    """
    Calcula el 10% de propina sobre el total de la cuenta.
    """
    propina = total_cuenta * 0.10
    return propina 


def calcular_propina(total_cuenta, porcentaje):
    """
    Calcula la propina según el porcentaje indicado.
    """
    if porcentaje <= 0:
        raise ValueError("El porcentaje debe ser un número positivo mayor que 0.")
    
    return total_cuenta * (porcentaje / 100)


def dividir_cuenta(total_cuenta, porcentaje_propina, personas):
    """
    Calcula:
    - Propina
    - Total con propina
    - Monto por persona
    """
    if personas <= 0:
        raise ValueError("La cantidad de personas debe ser mayor que 0.")
    
    propina = calcular_propina(total_cuenta, porcentaje_propina)
    total_final = total_cuenta + propina
    monto_por_persona = total_final / personas

    return propina, total_final, monto_por_persona


# Prueba manual
total = 1000
porcentaje = 10
personas = 4

propina, total_con_propina, por_persona = dividir_cuenta(total, porcentaje, personas)

print("Total de la cuenta:", total)
print(f"Propina ({porcentaje}%):", propina)
print("Total a pagar:", total_con_propina)
print("Monto por persona:", por_persona) 


def calcular_propina(total_cuenta, porcentaje):
    """
    Calcula la propina según el porcentaje indicado.
    """
    if total_cuenta <= 0:
        raise ValueError("El total de la cuenta debe ser un número positivo.")
    
    if porcentaje <= 0:
        raise ValueError("El porcentaje debe ser un número positivo mayor que 0.")
    
    return total_cuenta * (porcentaje / 100)


def dividir_cuenta(total_cuenta, porcentaje_propina, personas):
    """
    Calcula:
    - Propina
    - Total con propina
    - Monto por persona
    """
    if not isinstance(personas, int) or personas <= 0:
        raise ValueError("La cantidad de personas debe ser un entero positivo.")
    
    propina = calcular_propina(total_cuenta, porcentaje_propina)
    total_final = total_cuenta + propina
    monto_por_persona = total_final / personas

    return propina, total_final, monto_por_persona


# Programa principal con manejo de errores
try:
    total = float(input("Ingrese el total de la cuenta: "))
    porcentaje = float(input("Ingrese el porcentaje de propina: "))
    personas = int(input("Ingrese la cantidad de personas: "))

    propina, total_con_propina, por_persona = dividir_cuenta(
        total, porcentaje, personas
    )

    print("\n--- RESULTADOS ---")
    print(f"Propina ({porcentaje}%): {propina:.2f}")
    print(f"Total a pagar: {total_con_propina:.2f}")
    print(f"Monto por persona: {por_persona:.2f}")

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Ocurrió un error inesperado:", e)




