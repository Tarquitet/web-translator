# Translator

Breve: script para extraer datos de archivos JS (`cv_data.js`, `projects-opti.js`) y generar versiones traducidas (es → en).

Uso:

# Translator — `translator.py`

Descripción

- Extrae estructuras de datos (objetos y arrays literales) de ficheros JavaScript y genera versiones traducidas de los valores de texto.

Características

- Parseo heurístico de objetos/arrays JS (limpieza de comentarios, comillas y comas finales) para convertirlos a JSON.
- Traducción automática de cadenas desde español (`es`) a inglés (`en`) mediante `googletrans`.
- Omite campos no textuales o rutas mediante la constante `KEYS_TO_SKIP`.
- Pausa automática entre peticiones (1s) para reducir la probabilidad de bloqueos.

Requisitos

- Python 3.8+
- `googletrans==4.0.0-rc1` (el script intentará instalarlo si no está presente).

Uso

- Ejecutar desde la raíz del proyecto:

```bash
python dev/scripts/translator/translator.py
```

Archivos objetivo

- Por defecto `FILES_TO_TRANSLATE` contiene `cv_data.js` y `projects-opti.js`. Puedes editar esa lista al inicio del script para añadir o quitar archivos.

Salida

- Crea nuevos archivos en la misma carpeta `js/` con sufijo `-en` (por ejemplo `cv_data-en.js`). Mantiene el nombre de la variable JS original.

Limitaciones y recomendaciones

- No es un parser JS completo: funciona con literals de objetos y arrays. Si el archivo contiene funciones, plantillas o construcciones complejas el parseo puede fallar.
- Revisa y ajusta `KEYS_TO_SKIP` para evitar traducir rutas, identificadores o fragmentos que no deban traducirse.
- Si vas a traducir muchos textos considera revisar el tiempo entre peticiones o usar una API con clave según necesidad.

Nota sobre backends

- El script intenta usar `googletrans` por defecto. Si la importación o instalación de `googletrans` falla, el script ahora intenta usar `deep-translator` como fallback (se instalará automáticamente si es posible). Si ambos fallan, el script informará y saldrá.

Evolución (resumen)

- Implementación inicial: extracción y conversión de objetos JS a JSON.
- Añadida lista `KEYS_TO_SKIP` para evitar traducir rutas/identificadores.
- Integración con `googletrans` y autoinstalador de dependencias.
- Mejora en heurísticas para omitir strings que parecen código y en manejo de errores y logging.

Nota sobre parseo JS

- Los archivos de entrada son JavaScript, no JSON estricto. Cuando el parseo heurístico en Python no pueda extraer el objeto, el script intentará llamar a un helper Node.js (`js_to_json.js`) que usa `acorn` para parsear el archivo y extraer objetos/arrays top-level.

Requisitos para usar el helper Node.js:

```bash
cd dev/scripts/translator
npm install acorn
```

Si no quieres usar Node, el parseo seguirá intentando con heurísticas en Python, pero puede fallar en archivos JS más complejos.
