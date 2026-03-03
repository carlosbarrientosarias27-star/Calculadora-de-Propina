# core/calculos.py

from typing import Tuple
from core.validaciones import (
    validar_total,
    validar_personas,
    validar_porcentaje,
    validar_propina_fija
)


def calcular_propina_porcentaje(total: float, porcentaje: float) -> float:
    validar_total(total)
    validar_porcentaje(porcentaje)
    return total * (porcentaje / 100)


def calcular_propina_fija(total: float, monto_propina: float) -> float:
    validar_total(total)
    validar_propina_fija(monto_propina)
    return monto_propina


def dividir_cuenta(total: float, propina: float, personas: int) -> Tuple[float, float]:
    validar_personas(personas)

    total_final = total + propina
    monto_por_persona = total_final / personas

    return total_final, monto_por_persona