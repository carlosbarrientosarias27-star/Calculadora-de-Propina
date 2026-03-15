# 🧾 Calculadora de Propina

Aplicación de escritorio para calcular propinas de forma rápida y sencilla, con lógica de negocio desacoplada, interfaz de usuario dedicada y cobertura de tests completa.

---

# 📁 Estructura del Proyecto

```
Calculadora_Propina/
├── app/
│   ├── __init__.py
│   ├── logic.py          # Lógica de cálculo de propinas
│   ├── ui.py             # Interfaz de usuario
│   └── utils.py          # Utilidades y helpers
├── docs/
│   ├── asistencia_ia.md  # Documentación de asistencia IA
│   └── Casos Edge.md     # Casos límite documentados
├── test/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── test_logic.py  # Tests de lógica
│   │   ├── test_ui.py     # Tests de interfaz
│   │   └── test_utils.py  # Tests de utilidades
│   ├── __init__.py
│   └── test_main.py       # Tests del punto de entrada
├── __init__.py
├── .gitignore
├── LICENSE
├── main.py                # Punto de entrada de la aplicación
├── README.md
└── requirements.txt
```

---

# 🚀 Instalación y Uso

## Requisitos previos

- Python 3.14

## Instalación

```
# Clonar el repositorio
git clone https://github.com/tu-usuario/calculadora-propina.git
cd calculadora-propina

```

## Ejecutar la aplicación

```
python main.py
```

## Ejecutar los tests

```
python -m pytest test/
```

---

## 🧩 Módulos Principales

| Módulo | Descripción |
|---|---|
| `app/logic.py` | Contiene la lógica de cálculo: porcentaje de propina, división entre comensales, totales |
| `app/ui.py` | Gestiona la interfaz de usuario y la interacción con el usuario |
| `app/utils.py` | Funciones auxiliares de validación y formateo |
| `main.py` | Punto de entrada que inicializa y arranca la aplicación |

---

## 🧪 Tests

La suite de tests cubre los tres módulos principales de la aplicación:

- **`test_logic.py`** — Verifica los cálculos de propina, redondeos y casos edge
- **`test_ui.py`** — Comprueba el comportamiento de la interfaz
- **`test_utils.py`** — Valida las funciones utilitarias
- **`test_main.py`** — Prueba el flujo de arranque de la aplicación

Los casos límite están documentados en [`docs/Casos Edge.md`](docs/Casos%20Edge.md).

---

# 📦 Proyecto de Prueba

Versión simplificada y autocontenida de la calculadora, pensada para pruebas rápidas o integración en otros proyectos.

## Estructura

```
Proyecto_de_Prueba/
├── __init__.py
├── calculadora_propina.py   # Lógica completa en un único archivo
└── Readme.md
```

## Uso rápido

```python
from calculadora_propina import calcular_propina

total = 45.00
porcentaje = 15
propina, total_con_propina = calcular_propina(total, porcentaje)

print(f"Propina: {propina:.2f} €")
print(f"Total:   {total_con_propina:.2f} €")
```

---

# 📄 Licencia

Este proyecto está bajo la licencia incluida en el archivo [LICENSE](LICENSE MIT).

---

# 🤖 Asistencia IA

Este proyecto contó con apoyo de inteligencia artificial durante su desarrollo. Consulta [`docs/asistencia_ia.md`](docs/asistencia_ia.md) para más detalles.