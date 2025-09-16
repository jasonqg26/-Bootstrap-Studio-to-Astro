#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de extraccion de componentes por ID
Convierte elementos HTML con IDs especificos en componentes Astro
"""

import os
import re
import json
import sys

def load_components_config(config_path):
    """Carga la configuracion de componentes desde JSON"""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Convertir la estructura de array a diccionario para compatibilidad
            components_dict = {}
            for component in data['components']:
                components_dict[component['id']] = {
                    'name': component['component_name'],
                    'category': component['subfolder'] or 'General',
                    'description': component['description']
                }
            return components_dict
    except Exception as e:
        print(f"ERROR: No se pudo cargar la configuracion: {e}")
        return {}

def extract_element_by_id_robust(html_content, element_id):
    """
    Extrae un elemento HTML completo usando algoritmo de contador robusto
    """
    # Buscar el elemento inicial
    pattern = rf'<(\w+)[^>]*\bid\s*=\s*["\']?{re.escape(element_id)}["\']?[^>]*>'
    match = re.search(pattern, html_content, re.IGNORECASE)
    
    if not match:
        return None
    
    tag_name = match.group(1).lower()
    start_pos = match.start()
    
    print(f"[DEBUG] Encontrado elemento <{tag_name}> con ID '{element_id}' en posicion {start_pos}")
    
    # Si es un elemento self-closing, retornarlo directamente
    if html_content[match.start():match.end()].rstrip().endswith('/>'):
        element_content = html_content[start_pos:match.end()]
        print(f"[DEBUG] Elemento self-closing extraido: {len(element_content)} caracteres")
        return element_content
    
    # Usar contador para encontrar el elemento completo
    counter = 1  # Empezamos con 1 porque ya encontramos la etiqueta de apertura
    pos = match.end()
    
    print(f"[DEBUG] Iniciando contador para <{tag_name}> con ID '{element_id}': contador = {counter}")
    
    while counter > 0 and pos < len(html_content):
        # Buscar proxima etiqueta (apertura o cierre)
        next_tag = re.search(rf'</?{re.escape(tag_name)}(?:\s[^>]*)?>', html_content[pos:], re.IGNORECASE)
        
        if not next_tag:
            print(f"[DEBUG] No se encontraron mas etiquetas <{tag_name}>")
            break
        
        # Ajustar posicion absoluta
        tag_start = pos + next_tag.start()
        tag_end = pos + next_tag.end()
        tag_content = html_content[tag_start:tag_end]
        
        # Verificar si es etiqueta de cierre
        if tag_content.startswith('</'):
            counter -= 1
            print(f"[DEBUG]    -> Etiqueta de cierre {tag_content[:20]}... en pos {tag_start} - contador: {counter}")
        else:
            # Es etiqueta de apertura, verificar si es self-closing
            if tag_content.rstrip().endswith('/>'):
                print(f"[DEBUG]    -> Etiqueta self-closing {tag_content[:20]}... en pos {tag_start} - contador: {counter}")
            else:
                counter += 1
                print(f"[DEBUG]    -> Etiqueta de apertura {tag_content[:20]}... en pos {tag_start} - contador: {counter}")
        
        pos = tag_end
        
        if counter == 0:
            # Elemento completo encontrado
            element_content = html_content[start_pos:tag_end]
            print(f"[DEBUG] Elemento completo extraido para ID '{element_id}' - {len(element_content)} caracteres")
            return element_content
    
    print(f"[DEBUG] No se pudo completar la extraccion para ID '{element_id}' - contador final: {counter}")
    return None

def create_astro_component(element_content, component_info, components_dir):
    """Crea un archivo de componente Astro"""
    category = component_info.get('category', 'General')
    component_name = component_info['name']
    
    # Crear directorio de categoria si no existe
    category_dir = os.path.join(components_dir, category)
    os.makedirs(category_dir, exist_ok=True)
    
    # Crear contenido del componente Astro
    astro_content = f"""---
// Componente {component_name} extraido automaticamente
---

{element_content}
"""
    
    # Escribir archivo del componente
    component_file = os.path.join(category_dir, f"{component_name}.astro")
    
    try:
        with open(component_file, 'w', encoding='utf-8') as f:
            f.write(astro_content)
        return True
    except Exception as e:
        print(f"ERROR creando componente {component_name}: {e}")
        return False

def add_import_to_astro(file_path, component_name, category, components_base_path="@components"):
    """Agrega import de componente al archivo Astro"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Crear import statement
        import_path = f"{components_base_path}/{category}/{component_name}.astro"
        import_statement = f"import {component_name} from '{import_path}';"
        
        # Verificar si ya existe el import
        if import_statement in content:
            print(f"[DEBUG] Import ya existe para {component_name}")
            return True
        
        print(f"[DEBUG] Agregando import para {component_name} desde {import_path}")
        
        # Buscar la seccion de imports existente o crearla
        if content.strip().startswith('---'):
            # Ya existe frontmatter
            end_frontmatter = content.find('---', 3)
            if end_frontmatter != -1:
                frontmatter = content[3:end_frontmatter].strip()
                rest_content = content[end_frontmatter + 3:]
                
                # Agregar import al frontmatter
                if frontmatter:
                    new_frontmatter = f"{frontmatter}\n{import_statement}"
                else:
                    new_frontmatter = import_statement
                
                new_content = f"---\n{new_frontmatter}\n---{rest_content}"
                print(f"[DEBUG] Frontmatter existente actualizado")
            else:
                print(f"[DEBUG] ERROR: Frontmatter incompleto")
                return False
        else:
            # No existe frontmatter, crearlo al inicio del archivo
            new_content = f"---\n{import_statement}\n---\n\n{content}"
            print(f"[DEBUG] Nuevo frontmatter creado al inicio")
        
        # Escribir archivo actualizado
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"[DEBUG] Archivo {os.path.basename(file_path)} actualizado con import")
        return True
    except Exception as e:
        print(f"ERROR agregando import a {file_path}: {e}")
        return False

def process_html_file(file_path, components_config, components_dir):
    """Procesa un archivo HTML/Astro buscando componentes a extraer"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"ERROR procesando {os.path.basename(file_path)}: {e}")
        return []
    
    extracted_components = []
    modified_content = content
    
    for component_id, component_info in components_config.items():
        # Extraer elemento
        element_content = extract_element_by_id_robust(content, component_id)
        
        if element_content:
            component_name = component_info['name']
            category = component_info.get('category', 'General')
            description = component_info.get('description', 'Componente extraido')
            
            # Crear componente Astro
            if create_astro_component(element_content, component_info, components_dir):
                # Reemplazar elemento con componente en el contenido modificado
                component_tag = f"<{component_name} />"
                modified_content = modified_content.replace(element_content, component_tag)
                
                extracted_components.append({
                    'id': component_id,
                    'name': component_name,
                    'category': category,
                    'description': description
                })
                
                print(f"OK {os.path.basename(file_path)}:")
                print(f"   - {component_id} -> <{component_name} /> [{category}] ({description})")
            else:
                print(f"ERROR creando componente para ID '{component_id}' en {os.path.basename(file_path)}")
        else:
            print(f"-- No se encontro elemento con ID '{component_id}' en {os.path.basename(file_path)}")
    
    # Si hay componentes extraidos, agregar imports y escribir archivo
    if extracted_components:
        # Primero agregar todos los imports
        final_content = modified_content
        
        # Verificar si necesita frontmatter
        if not final_content.strip().startswith('---'):
            # Crear frontmatter con todos los imports
            import_statements = []
            for comp in extracted_components:
                import_path = f"@components/{comp['category']}/{comp['name']}.astro"
                import_statement = f"import {comp['name']} from '{import_path}';"
                import_statements.append(import_statement)
            
            frontmatter = '\n'.join(import_statements)
            final_content = f"---\n{frontmatter}\n---\n\n{final_content}"
            print(f"[DEBUG] Frontmatter creado con {len(import_statements)} imports")
        else:
            # Ya existe frontmatter, agregar imports
            end_frontmatter = final_content.find('---', 3)
            if end_frontmatter != -1:
                existing_frontmatter = final_content[3:end_frontmatter].strip()
                rest_content = final_content[end_frontmatter + 3:]
                
                # Agregar imports que no existan
                import_statements = []
                for comp in extracted_components:
                    import_path = f"@components/{comp['category']}/{comp['name']}.astro"
                    import_statement = f"import {comp['name']} from '{import_path}';"
                    if import_statement not in existing_frontmatter:
                        import_statements.append(import_statement)
                
                if import_statements:
                    new_imports = '\n'.join(import_statements)
                    if existing_frontmatter:
                        new_frontmatter = f"{existing_frontmatter}\n{new_imports}"
                    else:
                        new_frontmatter = new_imports
                    
                    final_content = f"---\n{new_frontmatter}\n---{rest_content}"
                    print(f"[DEBUG] Agregados {len(import_statements)} imports al frontmatter existente")
        
        # Escribir archivo final
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            print(f"[DEBUG] Archivo {os.path.basename(file_path)} actualizado con componentes e imports")
        except Exception as e:
            print(f"ERROR escribiendo archivo modificado {file_path}: {e}")
    else:
        print(f"-- {os.path.basename(file_path)}: No se encontraron componentes que extraer")
    
    return extracted_components

def main():
    if len(sys.argv) != 2:
        print("Uso: python extract_components_by_id.py <directorio_html>")
        sys.exit(1)
    
    html_dir = sys.argv[1]
    
    if not os.path.isdir(html_dir):
        print(f"ERROR: El directorio '{html_dir}' no existe")
        sys.exit(1)
    
    # Rutas de configuracion
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_dir = os.path.join(os.path.dirname(script_dir), 'config')
    config_file = os.path.join(config_dir, 'components_config.json')
    
    # Cargar configuracion
    components_config = load_components_config(config_file)
    if not components_config:
        print("ERROR: No se pudo cargar la configuracion de componentes")
        sys.exit(1)
    
    # Determinar directorio de componentes
    if "nux" in html_dir:
        # Estamos en el proyecto nux
        components_dir = html_dir.replace('pages', 'components')
    else:
        # Directorio por defecto
        nux_dir = os.path.join(os.path.dirname(os.path.dirname(script_dir)), 'nux', 'src', 'components')
        components_dir = nux_dir
    
    print("=== Script de extraccion de componentes por ID ===")
    print(f"Procesando directorio: {os.path.basename(html_dir)}")
    print(f"Componentes objetivo: {len(components_config)}")
    print()
    
    # Procesar archivos HTML/Astro
    total_extracted = 0
    files_processed = 0
    
    for filename in os.listdir(html_dir):
        if filename.lower().endswith(('.html', '.astro')):
            file_path = os.path.join(html_dir, filename)
            extracted = process_html_file(file_path, components_config, components_dir)
            total_extracted += len(extracted)
            files_processed += 1
    
    print()
    print("Resumen:")
    print(f"Archivos procesados: {files_processed}")
    print(f"Componentes extraidos: {total_extracted}")
    print(f"Directorio de componentes: {components_dir}")
    print("=== Script completado ===")

if __name__ == "__main__":
    main()