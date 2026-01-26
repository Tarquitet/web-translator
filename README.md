# 🌐 JSON Auto-Translator (i18n Tool)

> **Una herramienta de escritorio rápida y sencilla para automatizar la traducción de archivos de localización JSON.**

**JSON Auto-Translator** es una aplicación GUI ligera escrita en Python diseñada para desarrolladores web y de videojuegos. Te permite cargar un archivo de idioma (ej. `en.json`), elegir un idioma de destino y generar automáticamente un nuevo archivo traducido (ej. `es.json`) utilizando la API de Google Translate, manteniendo intacta la estructura de las claves.

## ✨ Características Principales

- **🔒 Traducción Segura (Solo Valores):** La herramienta es inteligente; traduce únicamente los _valores_ del JSON y mantiene las _claves_ originales para que tu código no se rompa.
- **⚡ Procesamiento Multihilo:** La interfaz gráfica (GUI) no se congela mientras se traducen archivos grandes, gracias a su arquitectura multihilo.
- **📊 Barra de Progreso en Tiempo Real:** Visualiza exactamente el avance de la traducción, ítem por ítem.
- **🤖 API Gratuita:** Utiliza la librería `googletrans` (API de Google Translate) sin necesidad de configuraciones de pago.
- **🖥️ Interfaz Intuitiva:** Interfaz gráfica nativa construida con Tkinter, lista para usar sin usar la terminal.

---

## ⚙️ Requisitos e Instalación

**Requisitos del sistema:**

- Python 3.8 o superior.

### 1. Clonar o descargar el repositorio

```bash
git clone [https://github.com/tu-usuario/json-auto-translator.git](https://github.com/tu-usuario/json-auto-translator.git)
cd json-auto-translator
```

2. Instalar dependencias

Es muy importante instalar la versión candidata (rc1) de googletrans, ya que las versiones estables anteriores presentan errores de conexión con la API actual de Google.
Bash

pip install googletrans==4.0.0-rc1

(Opcional: puedes usar pip install -r requirements.txt si tienes el archivo generado).
📖 Guía de Uso

    Ejecutar la herramienta:
    Bash

    python translator.py

    Cargar JSON: Haz clic en "Browse" y selecciona tu archivo fuente (por ejemplo, en.json).

    Seleccionar Idioma: Escribe el código del idioma de destino en el campo de texto (ejemplo: es para español, fr para francés, de para alemán).

    Traducir: Haz clic en "Translate". Se abrirá una ventana para que elijas dónde guardar el nuevo archivo (ej. es.json).

    ¡Listo! La barra de progreso te indicará cuando el proceso haya finalizado exitosamente.

💡 Estructura de Ejemplo

Archivo de Entrada (en.json):
JSON

{
"title": "Welcome to the game",
"start_btn": "Start Game",
"options": "Settings"
}

Archivo de Salida (es.json):
JSON

{
"title": "Bienvenido al juego",
"start_btn": "Empezar juego",
"options": "Ajustes"
}

⚖️ Licencia y Créditos

Este proyecto utiliza las siguientes tecnologías de código abierto:

    Python (tkinter, threading, json): Librerías estándar.

    Googletrans: Librería no oficial de Python para la API de Google Translate.

Desarrollado para agilizar flujos de trabajo de localización (i18n).
