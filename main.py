# main.py

from core.calculos import (
    calcular_propina_porcentaje,
    calcular_propina_fija,
    dividir_cuenta
)

from ui.menu import mostrar_menu
from ui.entradas import obtener_float, obtener_int


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