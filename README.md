# 🌐 JSON Auto-Translator (i18n Tool)

> **A lightweight desktop tool to automate translation of JSON localization files.**

JSON Auto-Translator is a small terminal/GUI Python app designed to quickly translate `.js` or `.json` localization files during development. You can add files from the UI list and run batch translations.

![1769442012384](images/README/1769442012384.png)

## ✨ Main Features

- **Translate Values Only:** The tool translates JSON values while keeping keys unchanged to avoid breaking code.
- **Multithreaded Processing:** UI remains responsive while large files are translated.
- **Progress Bar:** Shows per-item progress.
- **Free Translation API:** Uses `googletrans` (no paid API required).
- **Simple GUI:** Built with Tkinter for quick use.

---

## ⚙️ Requirements & Installation

- Python 3.8 or newer.

The tool attempts to install required packages automatically. Use the included UI to add files and configure keys to exclude from translation.

[![Leer en Español](https://img.shields.io/badge/Leer%20en%20Espa%C3%B1ol-ES-blue?style=flat-square&logo=github)](README_es.md)

## Clone & Install

```bash
git clone https://github.com/Tarquitet/web-translator.git
cd translator
```

It is recommended to use the candidate (`rc1`) version of `googletrans` because some stable releases have connectivity issues. The tool attempts to install dependencies automatically on first run.

## Usage

- Replace the filenames in the UI with the files you want to translate.
- Configure keys that should be excluded from translation.
- Run translations from the GUI; the app shows per-item progress.

## License & Credits

Built with Python standard libraries (`tkinter`, `threading`, `json`) and the `googletrans` library (unofficial Google Translate client).
