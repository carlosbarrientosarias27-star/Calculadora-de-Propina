# 🧾 Calculadora de Propina

Una aplicación de escritorio desarrollada en Python que permite calcular propinas de forma rápida, sencilla e intuitiva. Ideal para dividir cuentas en restaurantes y gestionar pagos en grupo.

---

# 📋 Descripción

**Calculadora de Propina** es una herramienta con interfaz gráfica que facilita el cálculo del monto de propina a dejar según el total de la cuenta, el porcentaje deseado y el número de comensales. Incluye lógica de negocio bien estructurada, utilidades de apoyo y una suite de pruebas automatizadas.

---

# 🗂️ Estructura del Proyecto

```
Calculadora_Propina/
├── app/
│   ├── __init__.py
│   ├── logic.py         # Lógica principal de cálculo
│   ├── ui.py            # Interfaz gráfica de usuario
│   └── utils.py         # Funciones utilitarias
├── docs/
│   ├── asistencia_ia.md # Documentación de asistencia con IA
│   └── Casos Edge.md    # Casos de prueba extremos
├── test/
│   ├── app/
│   │   ├── test_logic.py   # Tests unitarios de lógica
│   │   ├── test_ui.py      # Tests de la interfaz
│   │   └── test_utils.py   # Tests de utilidades
│   └── test_main.py        # Tests de integración
├── main.py              # Punto de entrada de la aplicación
├── requirements.txt     # Dependencias del proyecto
├── .gitignore
└── LICENSE
```

---

# ✨ Funcionalidades

- Cálculo automático del monto de propina según porcentaje personalizable
- División equitativa de la cuenta entre varios comensales
- Interfaz gráfica clara e intuitiva
- Validación de entradas del usuario
- Cobertura de casos extremos (montos cero, porcentajes negativos, etc.)

---

# 🚀 Instalación y uso

## Requisitos previos

- Python 3.8 o superior
- pip

## Instalación

```
# Clonar el repositorio
git clone https://github.com/tu-usuario/Calculadora_Propina.git
cd Calculadora_Propina

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecutar la aplicación

```
python main.py
```

---

## 🧪 Pruebas

El proyecto cuenta con una suite completa de pruebas unitarias e integración:

```
# Ejecutar todos los tests
python -m pytest test/

# Ejecutar tests con detalle
python -m pytest test/ -v
```

---

## 📖 Documentación

Consulta la carpeta `docs/` para información adicional:

- **`asistencia_ia.md`** — Notas sobre el uso de inteligencia artificial en el desarrollo.
- **`Casos Edge.md`** — Descripción y análisis de casos límite contemplados.

---

## 🛠️ Tecnologías

- **Python** — Lenguaje principal

---

## 📄 Licencia

Este proyecto está bajo los términos descritos en el archivo [LICENSE](LICENSE MIT).

---
