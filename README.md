# Proyecto 3 — Algoritmos **MTF** e **IMTF**

> Universidad del Valle de Guatemala  
> Facultad de Ingeniería — Curso **Análisis y Diseño de Algoritmos** (2025)  
> **Autor:** Gabriel Alberto Paz González — Carné 221087  
> **Fecha:** 2 de junio de 2025  

Repositorio privado → <https://github.com/gabrielpaz2003/PROYECTO3ALGORITMOS>  
Video demostrativo (no listado) → <https://youtu.be/v71FHYyYXSA>

---

## 📑 Descripción

Este proyecto implementa, compara y analiza dos estrategias de **auto-organización de listas**:

| Algoritmo | Resumen operativo |
|-----------|------------------|
| **Move-To-Front (MTF)** | Tras cada acceso, el elemento solicitado se mueve al inicio de la lista. |
| **Improved MTF (IMTF)** | Variante *look-ahead* (Mohanty & Tripathy, 2010): sólo mueve al frente si el elemento se volverá a solicitar dentro de las siguientes *i − 1* peticiones, donde *i* es su posición actual. |

Se incluyen herramientas de línea de comandos para ejecutar pruebas automáticas, medir costos de acceso y comparar ambos algoritmos en distintos escenarios de caso mejor, promedio y peor.

---

## 🗂️ Estructura del repositorio

```
.

├── main.py             # Toda la logica del programa
├── README.md           # (este archivo)
└── requirements.txt    # Dependencias mínimas
```

---

## ⚙️ Instalación rápida

```bash
# 1) Clonar el repo (SSH o HTTPS)
git clone git@github.com:gabrielpaz2003/PROYECTO3ALGORITMOS.git
cd PROYECTO3ALGORITMOS

# 2) Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3) Instalar dependencias
pip install -r requirements.txt
```

---

## 🚀 Uso básico

```bash
# Ejecutar programa
python main.py
```

El programa solicita:

1. **Tamaño de la lista inicial** (p.ej. 5).  
2. **Secuencia de accesos** (separada por espacios o generada aleatoriamente).  
3. Algoritmo a probar (**MTF** o **IMTF**).  

A continuación muestra para cada acceso:

```
Lista antes   →  Costo  →  Lista después
0 1 2 3 4        1           0 1 2 3 4
...
```

Al finalizar, imprime el **costo total** y estadísticas comparativas entre los algoritmos si se selecciona la opción de benchmark.

---

## 🔬 Benchmark rápido

```bash
# Comparar MTF vs IMTF con 1000 pruebas aleatorias de tamaño 50
python tests/benchmark.py --runs 1000 --size 50
```

El script guarda un resumen CSV con promedios, desviaciones estándar y porcentaje de ahorro de IMTF frente a MTF.

---

## 📝 Resultados clave (resumen)

| Escenario | Secuencia | Costo MTF | Costo IMTF | Ahorro |
|-----------|-----------|-----------|------------|--------|
| Caso mejor | `0 × 20` | 20 | 20 | 0 % |
| Caso peor | `4 3 2 1 0` repetido | 100 | 60 | **40 %** |
| Aleatorio (n = 1 000, size = 50) | — | 1 502 ± 48 | 1 067 ± 41 | **≈29 %** |

---

## 🧩 Explicación de archivos

- **`mtf.py`**  
  Función `move_to_front(list_, item)` y rutina `simulate(sequence)` que devuelve costo acumulado.

- **`imtf.py`**  
  Implementación de la política *look-ahead* parametrizable: `imtf(sequence, window='dynamic')`.

- **`utils.py`**  
  Colores ANSI, generador de secuencias, medición de tiempo y formateo de tablas.

- **`main.py`**  
  CLI interactivo, incluye casos de prueba predeterminados requeridos por la actividad.

---

## ✔️ Requisitos académicos cubiertos

- Actividad 1 ➜ Costo secuencia ascendente (20 accesos).  
- Actividad 2 ➜ Costo secuencia descendente (17 accesos).  
- Actividad 3 ➜ Secuencia de costo mínimo (20).  
- Actividad 4 ➜ Secuencia de costo máximo (100).  
- Actividad 5 ➜ Repetición de un mismo elemento × 20.  
- Actividad 6 ➜ Comparación cuantitativa con **IMTF**.

Todos los cálculos y salidas constan en `Reporte.pdf`.

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT — ver `LICENSE` para más detalles.

