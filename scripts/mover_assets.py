import shutil
import os
import sys

def mover_assets(export_dir):
    """
    Mueve la carpeta assets desde el directorio de exportación a public/assets
    """
    print("=== Script de movimiento de assets ===")
    
    # Rutas dinámicas basadas en el directorio de exportación
    source_assets = os.path.join(export_dir, "assets")
    
    # Determinar la carpeta public (asumiendo que export_dir es src/pages)
    project_root = os.path.dirname(os.path.dirname(export_dir))  # subir 2 niveles desde src/pages
    target_public = os.path.join(project_root, "public")
    target_assets = os.path.join(target_public, "assets")
    
    print(f"Directorio de exportación: {os.path.basename(export_dir)}")
    print(f"Buscando assets en: {os.path.relpath(source_assets, export_dir)}")
    
    # Verificar si existe la carpeta assets en el export
    if not os.path.exists(source_assets):
        print("-- No se encontró carpeta assets para mover")
        return
    
    # Crear carpeta public si no existe
    if not os.path.exists(target_public):
        os.makedirs(target_public)
        print(f"OK Carpeta public creada")
    
    # Eliminar carpeta assets existente en public si existe
    if os.path.exists(target_assets):
        shutil.rmtree(target_assets)
        print("-- Assets antiguos eliminados de public")
    
    # Copiar assets a public/assets
    try:
        shutil.copytree(source_assets, target_assets)
        print("OK Assets copiados a public/assets exitosamente")
        
        # Eliminar carpeta assets original del export
        shutil.rmtree(source_assets)
        print("OK Carpeta assets original eliminada del export")
        
        print("\nResumen:")
        print("Assets movidos exitosamente de export a public/")
        
    except Exception as e:
        print(f"ERROR moviendo assets: {str(e)}")

def main():
    """
    Función principal que recibe el directorio de exportación como argumento
    """
    if len(sys.argv) < 2:
        print("Uso: python mover_assets.py <directorio_exportacion>")
        sys.exit(1)
    
    export_dir = sys.argv[1]
    
    if not os.path.exists(export_dir):
        print(f"ERROR: El directorio no existe: {export_dir}")
        sys.exit(1)
    
    mover_assets(export_dir)
    print("=== Script completado ===")

if __name__ == "__main__":
    main()