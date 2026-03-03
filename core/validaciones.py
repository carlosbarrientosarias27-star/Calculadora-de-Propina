# core/validaciones.py

def validar_total(total: float) -> None:
    if total <= 0:
        raise ValueError("El total de la cuenta debe ser un número positivo.")


def validar_personas(personas: int) -> None:
    if not isinstance(personas, int) or personas <= 0:
        raise ValueError("La cantidad de personas debe ser un entero positivo.")


def validar_porcentaje(porcentaje: float) -> None:
    if porcentaje <= 0:
        raise ValueError("El porcentaje debe ser mayor que 0.")


def validar_propina_fija(monto: float) -> None:
    if monto < 0:
        raise ValueError("La propina no puede ser negativa.")