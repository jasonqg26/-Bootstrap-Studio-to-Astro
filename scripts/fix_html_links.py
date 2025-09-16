import os
import sys
import re

"""
Corrige los enlaces href="/pagina.html" a href="/pagina" en el archivo.
"""


def fix_html_links_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Buscar patrones href="/archivo.html" y href="/archivo.htm"
        pattern = re.compile(r'href="(/[^"]*?)\.html?"', re.IGNORECASE)
        matches = pattern.findall(content)
        
        if matches:
            # Función para reemplazar con lógica especial para index
            def replace_link(match):
                path = match.group(1)
                if path == '/index' or path == '/INDEX':
                    return 'href="/"'
                else:
                    return f'href="{path}"'
            
            # Reemplazar todas las ocurrencias
            updated_content = pattern.sub(replace_link, content)
            changes_made = len(matches)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            # Mostrar solo el nombre del archivo relativo
            rel_path = os.path.relpath(file_path, sys.argv[1])
            print(f"OK {rel_path}: {changes_made} enlaces corregidos")
            
            # Mostrar algunos ejemplos de cambios (máximo 3)
            for i, match in enumerate(matches[:3]):
                print(f"   {match}.html -> {match}")
            if len(matches) > 3:
                print(f"   ... y {len(matches) - 3} cambios más")
            
            return changes_made
        else:
            # Mostrar solo el nombre del archivo relativo
            rel_path = os.path.relpath(file_path, sys.argv[1])
            print(f"-- {rel_path}: No se encontraron enlaces .html")
            return 0

    except Exception as e:
        rel_path = os.path.relpath(file_path, sys.argv[1])
        print(f"ERROR procesando {rel_path}: {str(e)}")
        return 0

def fix_html_links_in_directory(directory_path, file_extensions=['.html', '.htm', '.astro']):
    """
    Procesa todos los archivos en el directorio especificado.
    """
    total_files = 0
    total_changes = 0
    
    print(f"Procesando directorio: {os.path.basename(directory_path)}")
    print()
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file)
                total_files += 1
                changes = fix_html_links_in_file(file_path)
                total_changes += changes
    
    print()
    print("Resumen:")
    print(f"Archivos procesados: {total_files}")
    print(f"Total de enlaces corregidos: {total_changes}")
    
    return total_files, total_changes

def main():
    """
    Función principal que recibe el directorio como argumento.
    """
    if len(sys.argv) < 2:
        print("Uso: python fix_html_links.py <directorio>")
        sys.exit(1)
    
    export_dir = sys.argv[1]
    
    if not os.path.exists(export_dir):
        print(f"ERROR: El directorio no existe: {export_dir}")
        sys.exit(1)
    
    print("=== Script de corrección de enlaces HTML ===")
    
    # Procesar archivos
    total_files, total_changes = fix_html_links_in_directory(export_dir)
    
    print("=== Script completado ===")

if __name__ == "__main__":
    main()