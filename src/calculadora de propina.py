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

    print(f"Propina ({porcentaje}%): ${propina:.2f}")
    print(f"Total a pagar: ${total_con_propina:.2f}")
    print(f"Monto por persona: ${por_persona:.2f}")

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Ocurrió un error inesperado:", e)


"""
Calculadora de Propina

Este programa permite calcular la propina de una cuenta
ya sea por porcentaje o por monto fijo, además de dividir
el total entre varias personas.

Autor: [Tu nombre]
Fecha: [Fecha actual]
Versión: 1.0
"""


def calcular_propina_porcentaje(total_cuenta, porcentaje):
    """
    Calcula la propina basada en un porcentaje del total.

    Parámetros:
        total_cuenta (float): Total de la cuenta.
        porcentaje (float): Porcentaje de propina a aplicar.

    Retorna:
        float: Monto calculado de la propina.

    Lanza:
        ValueError: Si el total o el porcentaje son inválidos.
    """
    if total_cuenta <= 0:
        raise ValueError("El total de la cuenta debe ser positivo.")
    if porcentaje <= 0:
        raise ValueError("El porcentaje debe ser mayor que 0.")

    return total_cuenta * (porcentaje / 100)


def calcular_propina_fija(total_cuenta, monto_propina):
    """
    Devuelve un monto fijo como propina.

    Parámetros:
        total_cuenta (float): Total de la cuenta.
        monto_propina (float): Monto fijo de propina.

    Retorna:
        float: Monto de la propina.

    Lanza:
        ValueError: Si los valores son inválidos.
    """
    if total_cuenta <= 0:
        raise ValueError("El total de la cuenta debe ser positivo.")
    if monto_propina < 0:
        raise ValueError("La propina no puede ser negativa.")

    return monto_propina


def dividir_cuenta(total_cuenta, propina, personas):
    """
    Divide el total de la cuenta con propina entre varias personas.

    Parámetros:
        total_cuenta (float): Total original de la cuenta.
        propina (float): Monto de la propina.
        personas (int): Número de personas que pagan.

    Retorna:
        tuple:
            total_final (float): Total con propina incluida.
            monto_por_persona (float): Pago individual.

    Lanza:
        ValueError: Si la cantidad de personas es inválida.
    """
    if not isinstance(personas, int) or personas <= 0:
        raise ValueError("La cantidad de personas debe ser un entero positivo.")

    total_final = total_cuenta + propina
    monto_por_persona = total_final / personas

    return total_final, monto_por_persona


def mostrar_menu():
    """
    Muestra el menú principal del programa.
    """
    print("\n===== CALCULADORA DE PROPINA =====")
    print("1. Calcular propina por porcentaje")
    print("2. Calcular propina con monto fijo")
    print("3. Salir")
    print("===================================")


# Programa principal
def main():
    """
    Ejecuta el flujo principal del programa.
    Maneja la interacción con el usuario y el control de errores.
    """
    while True:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opción (1-3): ")

            if opcion == "3":
                print("Gracias por usar la calculadora. ¡Hasta luego!")
                break

            total = float(input("Ingrese el total de la cuenta: "))
            personas = int(input("Ingrese la cantidad de personas: "))

            if opcion == "1":
                porcentaje = float(input("Ingrese el porcentaje de propina: "))
                propina = calcular_propina_porcentaje(total, porcentaje)

            elif opcion == "2":
                monto_fijo = float(input("Ingrese el monto fijo de propina: "))
                propina = calcular_propina_fija(total, monto_fijo)

            else:
                print("Opción inválida. Intente nuevamente.")
                continue

            total_con_propina, por_persona = dividir_cuenta(
                total, propina, personas
            )

            print("\n----- RESULTADOS -----")
            print(f"Propina: ${propina:.2f}")
            print(f"Total a pagar: ${total_con_propina:.2f}")
            print(f"Monto por persona: ${por_persona:.2f}")
            print("----------------------")

        except ValueError as e:
            print("Error:", e)

        except Exception as e:
            print("Ocurrió un error inesperado:", e)


if __name__ == "__main__":
    main()





    




