# 🧾 Calculadora de Propina

Programa interactivo en Python que permite calcular la propina de una cuenta —ya sea por porcentaje o monto fijo— y dividir el total entre varias personas.

---

## 📋 Descripción

La **Calculadora de Propina** es una herramienta de consola diseñada para facilitar el cálculo de propinas en restaurantes u otros servicios. Permite elegir entre dos métodos de cálculo y reparte automáticamente el monto total entre el número de comensales indicado.

---

## ✨ Funcionalidades

- **Propina por porcentaje:** Calcula la propina aplicando un porcentaje sobre el total de la cuenta.
- **Propina con monto fijo:** Permite ingresar directamente el monto de la propina.
- **División de cuenta:** Divide el total (cuenta + propina) entre el número de personas.
- **Validación de entradas:** Maneja errores de entrada inválida con mensajes claros.
- **Menú interactivo:** Interfaz de consola sencilla con opciones numeradas.

---

## 🚀 Requisitos

- Python 3.x

No requiere librerías externas.

---

## ▶️ Uso

```bash
python calculadora_de_propina.py
```

Al ejecutar el programa, se mostrará el siguiente menú:

```
===== CALCULADORA DE PROPINA =====
1. Calcular propina por porcentaje
2. Calcular propina con monto fijo
3. Salir
===================================
```

### Ejemplo de uso (opción 1 — porcentaje):

```
Seleccione una opción (1-3): 1
Ingrese el total de la cuenta: 500
Ingrese la cantidad de personas: 4
Ingrese el porcentaje de propina: 15

----- RESULTADOS -----
Propina: $75.00
Total a pagar: $575.00
Monto por persona: $143.75
----------------------
```

---

## 🗂️ Estructura del proyecto

```
calculadora_de_propina.py
│
├── Validaciones
│   ├── validar_total()
│   └── validar_personas()
│
├── Lógica de negocio
│   ├── calcular_propina_porcentaje()
│   ├── calcular_propina_fija()
│   └── dividir_cuenta()
│
└── Interfaz
    ├── mostrar_menu()
    ├── obtener_float()
    └── obtener_int()
```

---

## 👤 Autor

- **Autor:** [Tu nombre]
- **Versión:** 2.0

## 📄 Licencia

Este proyecto está bajo la licencia MIT especificada en el archivo [LICENSE](LICENSE).

---

*Desarrollado en Python*