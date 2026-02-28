"""
Calculadora de Propina

Descripción:
Programa interactivo que permite calcular la propina de una cuenta
por porcentaje o monto fijo y dividir el total entre varias personas.

Requisitos:
- Python 3.x

Autor: [Tu nombre]
Versión: 2.0
"""

from typing import Tuple 


# ==============================
# VALIDACIONES
# ==============================

def validar_total(total: float) -> None:
    if total <= 0:
        raise ValueError("El total de la cuenta debe ser un número positivo.")


def validar_personas(personas: int) -> None:
    if not isinstance(personas, int) or personas <= 0:
        raise ValueError("La cantidad de personas debe ser un entero positivo.")


# ==============================
# LÓGICA DE NEGOCIO
# ==============================

def calcular_propina_porcentaje(total: float, porcentaje: float) -> float:
    validar_total(total)

    if porcentaje <= 0:
        raise ValueError("El porcentaje debe ser mayor que 0.")

    return total * (porcentaje / 100)


def calcular_propina_fija(total: float, monto_propina: float) -> float:
    validar_total(total)

    if monto_propina < 0:
        raise ValueError("La propina no puede ser negativa.")

    return monto_propina


def dividir_cuenta(total: float, propina: float, personas: int) -> Tuple[float, float]:
    validar_personas(personas)

    total_final = total + propina
    monto_por_persona = total_final / personas

    return total_final, monto_por_persona


# ==============================
# INTERFAZ
# ==============================

def mostrar_menu() -> None:
    print("\n===== CALCULADORA DE PROPINA =====")
    print("1. Calcular propina por porcentaje")
    print("2. Calcular propina con monto fijo")
    print("3. Salir")
    print("===================================")


def obtener_float(mensaje: str) -> float:
    return float(input(mensaje))


def obtener_int(mensaje: str) -> int:
    return int(input(mensaje))


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

def main() -> None:
    while True:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opción (1-3): ")

            if opcion == "3":
                print("Gracias por usar la calculadora. ¡Hasta luego!")
                break

            total = obtener_float("Ingrese el total de la cuenta: ")
            personas = obtener_int("Ingrese la cantidad de personas: ")

            if opcion == "1":
                porcentaje = obtener_float("Ingrese el porcentaje de propina: ")
                propina = calcular_propina_porcentaje(total, porcentaje)

            elif opcion == "2":
                monto = obtener_float("Ingrese el monto fijo de propina: ")
                propina = calcular_propina_fija(total, monto)

            else:
                print("Opción inválida. Intente nuevamente.")
                continue

            total_final, por_persona = dividir_cuenta(total, propina, personas)

            print("\n----- RESULTADOS -----")
            print(f"Propina: ${propina:.2f}")
            print(f"Total a pagar: ${total_final:.2f}")
            print(f"Monto por persona: ${por_persona:.2f}")
            print("----------------------")

        except ValueError as e:
            print("Error:", e)

        except Exception as e:
            print("Ocurrió un error inesperado:", e)


if __name__ == "__main__":
    main()