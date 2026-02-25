# 🌐 JSON Auto-Translator (Herramienta i18n)

> **Una herramienta ligera de escritorio para automatizar la traducción de archivos JSON de localización.**

JSON Auto-Translator es una pequeña aplicación en Python (terminal/GUI) diseñada para traducir rápidamente archivos `.js` o `.json` durante el desarrollo. Permite añadir archivos desde la interfaz y ejecutar traducciones por lotes.

![1769442012384](images/README/1769442012384.png)

## ✨ Características Principales

- **Traduce solo valores:** Traduce únicamente los valores del JSON manteniendo las claves para evitar romper el código.
- **Procesamiento multihilo:** La interfaz no se congela con archivos grandes.
- **Barra de progreso:** Progreso visible ítem por ítem.
- **API de traducción gratuita:** Usa `googletrans` (sin necesidad de API de pago).
- **Interfaz simple:** Construida con Tkinter para uso rápido.

---

## ⚙️ Requisitos e Instalación

El script intenta instalar las dependencias automáticamente. Usa la UI incluida para agregar archivos y configurar claves a excluir de la traducción.

[![Read in English](https://img.shields.io/badge/Read%20in%20English-EN-blue?style=flat-square&logo=github)](README.md)

## Clonar e instalar

```bash
git clone https://github.com/Tarquitet/web-translator.git
cd translator
```

Se recomienda usar la versión candidata (`rc1`) de `googletrans`, ya que algunas versiones estables presentan problemas de conexión. El script intenta instalar las dependencias automáticamente en la primera ejecución.

## Uso

- Reemplaza los nombres de archivo en la interfaz por los archivos que desees traducir.
- Configura las claves que NO deben traducirse (ej. identificadores o rutas).
- Ejecuta la traducción desde la GUI; la aplicación muestra el progreso ítem por ítem.

## Licencia y Créditos

Construido con librerías estándar de Python (`tkinter`, `threading`, `json`) y la librería `googletrans` (cliente no oficial de Google Translate).
