import os
import sys

def rename_html_to_astro(directory_path):
    """
    Renombra archivos .html a .astro solo en el directorio principal (no en subcarpetas)
    """
    renamed_files = 0
    
    print("=== Script de renombrado HTML -> ASTRO ===")
    print(f"Procesando directorio: {os.path.basename(directory_path)}")
    print()
    
    # Solo procesar archivos en el directorio principal (no subcarpetas)
    try:
        files = os.listdir(directory_path)
        
        for filename in files:
            file_path = os.path.join(directory_path, filename)
            
            # Solo procesar archivos (no directorios) y que terminen en .html
            if os.path.isfile(file_path) and filename.lower().endswith('.html'):
                # Crear el nuevo nombre con extensión .astro
                name_without_ext = os.path.splitext(filename)[0]
                new_filename = name_without_ext + '.astro'
                new_file_path = os.path.join(directory_path, new_filename)
                
                try:
                    # Renombrar el archivo
                    os.rename(file_path, new_file_path)
                    print(f"OK {filename} -> {new_filename}")
                    renamed_files += 1
                    
                except Exception as e:
                    print(f"ERROR renombrando {filename}: {str(e)}")
        
        # Mostrar archivos que no se renombraron (si los hay)
        remaining_files = [f for f in os.listdir(directory_path) 
                          if os.path.isfile(os.path.join(directory_path, f)) 
                          and not f.lower().endswith(('.html', '.astro'))]
        
        if remaining_files:
            print()
            for filename in remaining_files[:5]:  # Mostrar solo los primeros 5
                print(f"-- {filename}: No es archivo HTML")
            if len(remaining_files) > 5:
                print(f"-- ... y {len(remaining_files) - 5} archivos más")
    
    except Exception as e:
        print(f"ERROR accediendo al directorio: {str(e)}")
        return 0
    
    print()
    print("Resumen:")
    print(f"Archivos renombrados: {renamed_files}")
    
    return renamed_files

def main():
    """
    Función principal que recibe el directorio como argumento
    """
    if len(sys.argv) < 2:
        print("Uso: python html_to_astro.py <directorio>")
        sys.exit(1)
    
    export_dir = sys.argv[1]
    
    if not os.path.exists(export_dir):
        print(f"ERROR: El directorio no existe: {export_dir}")
        sys.exit(1)
    
    if not os.path.isdir(export_dir):
        print(f"ERROR: La ruta no es un directorio: {export_dir}")
        sys.exit(1)
    
    # Renombrar archivos
    renamed_count = rename_html_to_astro(export_dir)
    
    print("=== Script completado ===")

if __name__ == "__main__":
    main()