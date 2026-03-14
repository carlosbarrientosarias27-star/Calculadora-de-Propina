# 🧾 Calculadora de Propina

Repositorio que contiene la aplicación **Calculadora_Propina** junto con su **Proyecto de Prueba** de integración.

---

## 📁 Estructura del Repositorio

```
├── Calculadora_Propina/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── logic.py          # Lógica de negocio (cálculo de propina)
│   │   ├── ui.py             # Interfaz de usuario
│   │   └── utils.py          # Utilidades auxiliares
│   ├── docs/
│   │   ├── asistencia_ia.md  # Documentación de asistencia con IA
│   │   └── Casos Edge.md     # Casos borde documentados
│   ├── test/
│   │   └── app/
│   │       ├── __init__.py
│   │       ├── test_logic.py # Tests de lógica
│   │       ├── test_ui.py    # Tests de interfaz
│   │       └── test_utils.py # Tests de utilidades
│   ├── __init__.py
│   ├── .gitignore
│   ├── LICENSE
│   ├── main.py               # Punto de entrada principal
│   ├── README.md
│   ├── requirements.txt
│   └── test_main.py
│
└── Proyecto de Prueba/
    ├── __init__.py
    ├── calculadora_propina.py # Script de integración/prueba
    └── Readme.md
```

---

## 📦 Calculadora_Propina

Aplicación principal para calcular propinas de forma sencilla e intuitiva.

### Descripción

La app permite al usuario introducir el importe de una factura y calcular automáticamente la propina según el porcentaje deseado, con distintas opciones de reparto entre comensales.

### Módulos principales

| Módulo | Descripción |
|--------|-------------|
| `app/logic.py` | Cálculo del importe de la propina y reparto por persona |
| `app/ui.py` | Gestión de la interfaz de usuario (entrada/salida) |
| `app/utils.py` | Funciones auxiliares reutilizables |
| `main.py` | Punto de entrada de la aplicación |

### Instalación

```bash
# Clona el repositorio
git clone <url-del-repositorio>
cd Calculadora_Propina

# Instala las dependencias
pip install -r requirements.txt
```

### Uso

```bash
python main.py
```

### Tests

```bash
# Ejecutar todos los tests
python -m pytest test/

# Ejecutar un módulo de test específico
python -m pytest test/app/test_logic.py
```

---

## 🧪 Proyecto de Prueba

Proyecto auxiliar que contiene un script de integración para validar el comportamiento de la `Calculadora_Propina` en un entorno externo.

### Descripción

Simula el uso de la calculadora como si fuera un módulo importado, permitiendo verificar su funcionamiento de forma aislada e independiente del proyecto principal.

### Archivo principal

| Archivo | Descripción |
|---------|-------------|
| `calculadora_propina.py` | Script que importa y prueba la lógica de la calculadora |

### Uso

```bash
cd "Proyecto de Prueba"
python calculadora_propina.py
```

---

## 📄 Documentación adicional

- [`docs/asistencia_ia.md`](Calculadora_Propina/docs/asistencia_ia.md) — Registro del uso de IA como asistencia en el desarrollo.
- [`docs/Casos Edge.md`](Calculadora_Propina/docs/Casos%20Edge.md) — Casos borde identificados y cómo se gestionan.

---

## 🛠️ Requisitos

- Python 3.8+
- Dependencias listadas en `requirements.txt`

---

## 📝 Licencia

Distribuido bajo los términos descritos en el archivo [`LICENSE`](Calculadora_Propina/LICENSE).
