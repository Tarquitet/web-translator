import os
import sys
import subprocess
import time
import re
import importlib

# ==========================================
# 1. INSTALADOR DE DEPENDENCIAS
# ==========================================
def install_dependencies():
    required = [
        ("deep_translator", "deep-translator"),
        ("googletrans", "googletrans==4.0.0-rc1")
    ]
    for import_name, install_name in required:
        try:
            importlib.import_module(import_name)
        except ImportError:
            try:
                print(f"[Instalando] {install_name}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", install_name, "--user"], stdout=subprocess.DEVNULL)
            except: pass

install_dependencies()
from deep_translator import GoogleTranslator

# ==========================================
# 2. CONFIGURACIÓN
# ==========================================
FILES_TO_TRANSLATE = [
    "projects-opti.js", 
    "cv_data.js"
]

# ¡AQUÍ ESTÁ LA MAGIA!
# Solo traduciremos el texto que pertenezca a estas claves.
# Esto evita traducir variables de código como 'fileName', 'link', 'tools', etc.
KEYS_TO_TRANSLATE = [
    'title', 
    'desc', 
    'description', 
    'summary', 
    'text', 
    'name',      # A veces contiene descripciones
    'role', 
    'Sporify',   # Vi una clave rara en tu archivo, la agrego por si acaso
    'Planty',
    'Minidocumental',
    'Brainstorming',
    'Motion',
    'Dev',
    'Digital',
    'App',
    'desc'
]

# Keys for labels in cv_data.js that should be translated
LABEL_KEYS = [
    'contact', 'languages', 'softSkills', 'techSkills', 'profile', 'education', 'projects', 'stack',
    'footerDownload', 'footerTheme', 'footerContact', 'btnWeb'
]

for k in LABEL_KEYS:
    if k not in KEYS_TO_TRANSLATE:
        KEYS_TO_TRANSLATE.append(k)

# Palabras que, aunque estén en las claves de arriba, NO deben traducirse
# (Nombres propios, marcas, URLs)
IGNORE_VALUES = [
    'Verdad & Fe', 'Tarquitet', 'Builtechraft', 'Rappi', 'Spotify', 
    'Wix', 'Unity', 'Figma', 'YouTube', 'Behance', 'Github', 
    'GymApp', 'Sudoku', 'Algebrain', 'Wumpus', 'OpenGL', 
    'Sonorus', 'Pixelation', 'David Josué','Miro','TARQUITET'
]

# ==========================================
# 3. TRADUCTOR ROBUSTO
# ==========================================
class TranslatorService:
    def __init__(self):
        self.services = []
        try:
            self.services.append(('deep', GoogleTranslator(source='es', target='en')))
        except: pass
        try:
            from googletrans import Translator
            self.services.append(('google', Translator()))
        except: pass
            
    def translate(self, text):
        if not text or len(text) < 2: return text
        # Si el texto es una URL o ruta, retornamos intacto
        if text.startswith(('http', '../', './', 'assets/')): return text
        
        # Intentar traducción
        for name, service in self.services:
            try:
                if name == 'deep': return service.translate(text)
                elif name == 'google': return service.translate(text, src='es', dest='en').text
            except:
                time.sleep(0.5)
                continue
        return text

# ==========================================
# 4. PROCESAMIENTO CON REGEX
# ==========================================

def find_js_folder():
    """Busca la carpeta js."""
    current = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.abspath(os.path.join(current, "..", "..", "..", "js")),
        os.path.join(current, "js"),
        os.getcwd(),
        os.path.abspath(os.path.join(os.getcwd(), "js"))
    ]
    for path in candidates:
        if os.path.exists(path) and any(os.path.exists(os.path.join(path, f)) for f in FILES_TO_TRANSLATE):
            return path
    return None

def process_file_regex(content, translator):
    """
    Busca patrones: key: 'valor' y traduce SOLO si la key es permitida.
    """
    
    # Esta expresión regular busca:
    # 1. Una palabra clave (ej: title)
    # 2. Dos puntos y espacios opcionales
    # 3. Una comilla (simple, doble o backtick)
    # 4. El contenido dentro (capturando escapados)
    # 5. La comilla de cierre
    pattern = re.compile(r"(?P<key>\b\w+)\s*:\s*(?P<quote>['\"`])(?P<text>(?:(?!(?P=quote)|\\).|\\.)*)(?P=quote)")

    def replacement_function(match):
        key = match.group('key')
        quote = match.group('quote')
        original_text = match.group('text')

        # 1. Filtro: ¿Es una clave que queremos traducir?
        if key not in KEYS_TO_TRANSLATE:
            return match.group(0) # Devolver original sin cambios

        # 2. Filtro: Contenido ignorado (URLs, rutas, marcas)
        if any(ign in original_text for ign in IGNORE_VALUES):
            # Aún si tiene una marca, podríamos querer traducirlo si es una frase larga.
            # Si es SOLO la marca, lo saltamos.
            if len(original_text.split()) < 3: 
                return match.group(0)

        # 3. Filtro: Si parece código (todo mayúsculas y corto)
        if original_text.isupper() and len(original_text.split()) < 3:
            return match.group(0)

        print(f"   [Trad] ({key}): {original_text[:40]}...")
        
        # 4. Traducir
        # Desescapar comillas para traducir limpio (ej: It\'s -> It's)
        clean_text = original_text.replace(f"\\{quote}", quote) 
        translated = translator.translate(clean_text)
        
        # 5. Re-escapar comillas para no romper el JS (ej: It's -> It\'s)
        if quote in translated:
            translated = translated.replace(quote, f"\\{quote}")

        # Reconstruir la cadena: key: 'traduccion'
        return f"{key}: {quote}{translated}{quote}"

    # Ejecutar el reemplazo en todo el archivo
    new_content = pattern.sub(replacement_function, content)
    return new_content

def main():
    print("\n=== TRADUCTOR JS POR REGEX (INFALIBLE) ===")
    
    source_dir = find_js_folder()
    if not source_dir:
        print("[!] ERROR: No encontré la carpeta JS.")
        return
    print(f"[Info] Carpeta: {source_dir}")

    translator = TranslatorService()

    for filename in FILES_TO_TRANSLATE:
        filepath = os.path.join(source_dir, filename)
        if not os.path.exists(filepath): continue

        print(f"\n--- Procesando: {filename} ---")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Usamos el método Regex
        new_content = process_file_regex(content, translator)
        
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}-en{ext}"
        new_path = os.path.join(source_dir, new_filename)
        
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f" [Exito] Archivo guardado: {new_filename}")

if __name__ == "__main__":
    main()