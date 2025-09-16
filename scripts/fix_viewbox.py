import os
import re
import sys

def fix_viewbox_in_file(file_path):
    """
    Corrige cualquier variante de viewbox por viewBox en el archivo.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Buscar viewbox en cualquier contexto (case insensitive)
        pattern = re.compile(r'viewbox', re.IGNORECASE)
        matches = pattern.findall(content)
        
        if matches:
            updated_content = pattern.sub('viewBox', content)
            changes_made = len(matches)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            # Mostrar solo el nombre del archivo relativo
            rel_path = os.path.relpath(file_path, sys.argv[1])
            print(f"OK {rel_path}: {changes_made} cambios realizados")
            return changes_made
        else:
            # Mostrar solo el nombre del archivo relativo
            rel_path = os.path.relpath(file_path, sys.argv[1])
            print(f"-- {rel_path}: No se encontraron cambios necesarios")
            return 0

    except Exception as e:
        rel_path = os.path.relpath(file_path, sys.argv[1])
        print(f"ERROR procesando {rel_path}: {str(e)}")
        return 0

def fix_viewbox_in_directory(directory_path, file_extensions=['.html', '.htm', '.astro', '.svg']):
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
                changes = fix_viewbox_in_file(file_path)
                total_changes += changes
    
    print()
    print(f"Resumen:")
    print(f"Archivos procesados: {total_files}")
    print(f"Total de correcciones: {total_changes}")
    
    return total_files, total_changes

def main():
    """
    Función principal que recibe el directorio como argumento.
    """
    if len(sys.argv) < 2:
        print("Uso: python fix_viewbox.py <directorio>")
        sys.exit(1)
    
    export_dir = sys.argv[1]
    
    if not os.path.exists(export_dir):
        print(f"ERROR: El directorio no existe: {export_dir}")
        sys.exit(1)
    
    print("=== Script de corrección viewbox -> viewBox ===")
    
    # Procesar archivos
    total_files, total_changes = fix_viewbox_in_directory(export_dir)
    
    print("=== Script completado ===")

if __name__ == "__main__":
    main()