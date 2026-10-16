# 📊 EconoMetrics AI - Evaluador de Rentabilidad y Viabilidad de Negocios

Aplicación web integral diseñada para evaluar la rentabilidad financiera, ingeniería de proyectos y viabilidad estratégica de empresas. Combina **fórmulas económicas y matemáticas rigurosamente validadas** con la potencia de **Google Gemini**.

---

## 🚀 Estructura del Flujo Lineal (5 Pasos)

1. **1. Presupuestos de Inversión**: Cotizaciones de maquinaria nueva, servicios/trámites y nómina/empleados con 3 escenarios de precios en México (Económico, Estándar y Premium).
2. **2. Procesos e Ingeniería**: Flujograma horizontal con simbología Mermaid.js, tiempos y movimientos, y tabla de consumo mensual (electricidad Kw/h, agua, gas y consumibles).
3. **3. Perfil de Negocio**: Propuesta de valor, mercado meta, ubicación geográfica, competencia y ventaja competitiva.
4. **4. Parámetros Económicos**: Inversión inicial, precio, demanda estimada, costos fijos y variables, mermas/robos, tasa CETES/banco y depreciación.
5. **5. Diagnóstico y Reportes**:
   - Cálculos inmediatos sin API: VAN/NPV, TIR/IRR, Payback simple y descontado, Punto de Equilibrio y comparación vs. CETES.
   - Dictamen estratégico con IA: Veredicto ejecutivo, score 0-100, matriz de riesgos y plan de acción.
   - **Control Operativo Diario (`/tracker.html`)**: Registro diario de ventas, mermas, robos y compras con análisis de variaciones respecto a lo presupuestado.

---

## 🛠️ Cómo Ejecutar el Proyecto (Rápido)

### En Windows

Instala Python 3.10 o posterior con **Add Python to PATH**. Ejecuta `iniciar.bat` o `run.bat` con doble clic.

### En Linux

Instala Python 3.10 o posterior y el soporte de entornos virtuales. En Debian/Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-venv git
```

Desde la carpeta del proyecto:

```bash
bash run.sh
```

En macOS también puedes usar `bash run.sh` con Python 3.10 o posterior instalado.

### En ambos equipos

El arranque crea `.venv` localmente e instala las dependencias de `requirements.txt`. Abre **http://127.0.0.1:8000**. Detén el servidor con **Ctrl+C**.

Cada PC ejecuta su propia instancia. Al guardar código Python el servidor se recarga; para cambios de HTML, CSS o JavaScript recarga el navegador. Después de descargar cambios en `requirements.txt`, reinicia el programa para instalar las nuevas dependencias. El arranque necesita acceso a Internet para instalar paquetes que falten.

No copies `.venv` ni `venv` entre Windows y Linux: se crean por separado y Git los excluye. Los scripts conservan los finales de línea adecuados mediante `.gitattributes`.

---

## 🔑 Configurar la API Key de Gemini

Para usar las funciones de Inteligencia Artificial (generación de presupuestos, diagramas de flujo y dictamen estratégico):
1. Obtén una clave gratuita en [Google AI Studio](https://aistudio.google.com/).
2. Haz clic en el botón superior **"Configurar API Key"** dentro de la aplicación y pégala allí (se guarda en tu navegador de forma segura).
3. *(Opcional)* También puedes crear un archivo `.env` en la raíz con:
   ```env
   GEMINI_API_KEY=tu_clave_aqui
   ```

---

## 📂 Guía de Modificación para Desarrolladores

Si deseas personalizar o extender la aplicación, aquí tienes los archivos clave:

* **Fórmulas y Cálculos Financieros**:
  - `app/financial_engine.py`: Fórmulas matemáticas de VAN, TIR (Newton-Raphson), Payback, Punto de Equilibrio y Sensibilidad.
* **Modelos de Datos y Validación**:
  - `app/models.py`: Esquemas Pydantic para entradas financieras, perfil de negocio y respuestas.
* **Servicios de Inteligencia Artificial**:
  - `app/gemini_service.py`: Prompt de auditoría estratégica, matriz de riesgos y análisis de mercado.
  - `app/engineering_service.py`: Generador de presupuestos de maquinaria y diagramas de flujo Mermaid.js.
* **Plantillas de Ejemplo**:
  - `app/templates_engineering.py`: Datos de maquinaria, proceso y presupuestos de las plantillas (Cafetería, E-Commerce, SaaS, Gimnasio).
  - `app/main.py`: Definición de perfiles y parámetros de las plantillas base.
* **Interfaz de Usuario (Frontend)**:
  - `app/static/index.html`: Estructura de las 5 pestañas, paneles y modal de guardado.
  - `app/static/app.js`: Lógica interactiva, gráficos con Chart.js, Mermaid.js y persistencia en localStorage.
  - `app/static/tracker.html` y `app/static/tracker.js`: Aplicación de control operativo diario.


## Colaboración entre dos PCs

Consulta [COLABORACION.md](COLABORACION.md) para conectar ambas PCs y compartir cambios mediante Commit, Push y Pull.
