import os
import re
import sys
"""
Agrega is:inline a todos los scripts que referencian /assets/
"""


def fix_inline_scripts_in_file(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Buscar scripts que referencian /assets/ y no tienen is:inline
        pattern = r'<script\s+src="(/assets/[^"]+)"([^>]*)></script>'
        
        def replace_script(match):
            src = match.group(1)
            other_attrs = match.group(2)
            # Solo reemplazar si no tiene is:inline ya
            if 'is:inline' not in match.group(0):
                return f'<script src="{src}" is:inline{other_attrs}></script>'
            else:
                return match.group(0)
        
        # Contar scripts originales sin is:inline
        original_scripts = len([m for m in re.finditer(pattern, content) if 'is:inline' not in m.group(0)])
        
        # Hacer el reemplazo
        updated_content = re.sub(pattern, replace_script, content)
        
        if original_scripts > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"OK {os.path.basename(file_path)}: {original_scripts} scripts corregidos")
            return original_scripts
        else:
            print(f"-- {os.path.basename(file_path)}: No se encontraron scripts que corregir")
            return 0

    except Exception as e:
        print(f"ERROR procesando {file_path}: {str(e)}")
        return 0

def fix_inline_scripts_in_directory(directory_path):
    """
    Procesa todos los archivos .astro y .html en el directorio
    """
    print(f"=== Script de corrección is:inline ===")
    print(f"Procesando directorio: {os.path.basename(directory_path)}")
    print()
    
    total_files = 0
    total_changes = 0
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(('.astro', '.html', '.htm')):
                file_path = os.path.join(root, file)
                total_files += 1
                total_changes += fix_inline_scripts_in_file(file_path)
    
    print()
    print(f"Resumen:")
    print(f"Archivos procesados: {total_files}")
    print(f"Scripts corregidos: {total_changes}")
    print("=== Script completado ===")
    
    return total_files, total_changes

def main():
    if len(sys.argv) < 2:
        print("Uso: python fix_inline_scripts.py <directorio>")
        sys.exit(1)
    
    export_dir = sys.argv[1]
    fix_inline_scripts_in_directory(export_dir)

if __name__ == "__main__":
    main()

