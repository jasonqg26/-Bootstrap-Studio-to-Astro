# 🚀 Bootstrap Studio to Astro - Automation Suite# 🚀 Bootstrap Studio to Astro - Automation Suite

Sistema de automatización completo para procesar exportaciones de Bootstrap Studio y convertirlas en componentes Astro listos para usar.

**🆕 Actualización v2.1**: Ahora con limpieza automática de HTML residual después de extracción de componentes.Sistema completo de automatización para convertir exportaciones de Bootstrap Studio en proyectos Astro optimizados y organizados.

## 📁 Estructura del Proyecto## 📁 Estructura del proyecto

````

Scrips/Scrips/

├── 📄 bootstrap_studio_processor.bat  # Script principal de automatización├── 📄 bootstrap_studio_processor.bat    # Script principal de automatización

├── 📁 scripts/                        # Scripts Python especializados├── 📄 README.md                         # Este archivo

│   ├── extract_components_by_id.py    # Extracción automática de componentes├── 📂 scripts/                          # Scripts Python organizados

│   ├── fix_html_links.py             # Corrección de enlaces HTML│   ├── fix_viewbox.py                   # Corrige viewbox → viewBox en SVGs

│   ├── fix_inline_scripts.py         # Corrección de scripts is:inline│   ├── mover_assets.py                  # Organiza assets en estructura Astro

│   ├── fix_viewbox.py                # Corrección de viewBox en SVGs│   ├── html_to_astro.py                 # Renombra .html → .astro

│   ├── html_to_astro.py              # Renombrado HTML → ASTRO│   ├── fix_html_links.py                # Corrige enlaces /page.html → /page

│   ├── mover_assets.py               # Organización de assets│   ├── fix_inline_scripts.py            # Agrega is:inline a scripts

│   └── backups/                      # Respaldos de componentes│   ├── extract_components_by_id.py      # Extrae componentes por ID

├── 📁 config/                        # Configuraciones del sistema│   └── fix_nested_links.py              # Corrige enlaces anidados

│   └── components_config.json        # Configuración de componentes├── 📂 config/                           # Archivos de configuración

├── 📁 docs/                          # Documentación completa│   └── components_config.json           # Configuración de componentes

│   ├── README.md                     # Documentación principal├── 📂 docs/                             # Documentación

│   └── README_components_config.md   # Guía de configuración│   └── README_components_config.md      # Guía de configuración de componentes

├── 📁 logs/                          # Archivos de registro├── 📂 logs/                             # Archivos de log

│   └── bootstrap_studio_log.txt      # Log de ejecuciones│   └── bootstrap_studio_log.txt         # Log de ejecución

└── 📁 backups/                       # Respaldos automáticos└── 📂 backups/                          # Backups automáticos

```    └── components/                      # Backups de componentes extraídos

```

## 🎯 Uso Rápido

## 🎯 Flujo de Automatización Completo

### 1. Desde Bootstrap Studio (Recomendado)

1. Ve a **File → Export Settings**### **Paso 1: Corrección de SVG viewBox**

2. En **After Export**, configura:

   ```- Corrige `viewbox` → `viewBox` en todos los archivos SVG

   Command: C:\Users\jason\Documents\Nuxtek\Scrips\bootstrap_studio_processor.bat- Compatible con Astro y frameworks modernos

   Arguments: "$1"

   ```### **Paso 2: Organización de Assets**

3. Exporta tu diseño normalmente

- Mueve archivos de assets a la estructura `public/` de Astro

### 2. Manualmente- Mantiene organización por carpetas (css, js, img, fonts)

```cmd

cd C:\Users\jason\Documents\Nuxtek\Scrips### **Paso 3: Renombrado de Archivos**

bootstrap_studio_processor.bat "C:\ruta\a\tu\exportacion"

```- Convierte `.html` → `.astro` para compatibilidad

- Procesa solo directorio principal, no subcarpetas

## ⚙️ Proceso de Automatización

### **Paso 4: Corrección de Enlaces**

El script ejecuta **7 pasos** secuenciales:

- Convierte `href="/page.html"` → `href="/page"`

1. **🔧 Corrección de ViewBox** - Arregla problemas de SVG- **Especial**: `href="/index.html"` → `href="/"` (raíz de Astro)

2. **📂 Organización de Assets** - Mueve archivos a ubicaciones correctas

3. **🔄 Renombrado HTML → ASTRO** - Convierte extensiones### **Paso 5: Scripts Inline**

4. **🔗 Corrección de Enlaces** - Actualiza rutas y referencias

5. **⚡ Scripts is:inline** - Configura scripts para Astro- Agrega `is:inline` a todos los scripts en `/assets/`

6. **🧩 Extracción de Componentes** - Crea componentes automáticamente- Soluciona errores de Vite/Astro con assets en public/

7. **📊 Reporte Final** - Log detallado de operaciones



## 🧩 Configuración de Componentes### **Paso 7: Extracción de Componentes**



El sistema puede extraer automáticamente componentes basados en IDs HTML:- Extrae automáticamente elementos por ID configurado

- Crea componentes Astro organizados en subcarpetas

```json- Genera imports relativos automáticamente

{

  "components": [## 🚀 Uso Rápido

    {

      "id": "nav-bar-public",### **Configuración en Bootstrap Studio**

      "component_name": "NavBarPublic",

      "subfolder": "NavBars",1. Ve a **Settings → Export**

      "description": "Barra de navegación para usuarios no autenticados"2. En **"After Export"** selecciona **"Run Script"**

    }3. Apunta al archivo: `bootstrap_studio_processor.bat`

  ]

}### **Uso Manual**

```

```bash

## 📊 Registro y Monitoreobootstrap_studio_processor.bat "C:\ruta\export\directorio"

```

- **Log automático**: Todas las operaciones se registran en `logs/bootstrap_studio_log.txt`

- **Respaldos**: Los componentes extraídos se respaldan automáticamente## ⚙️ Configuración de Componentes

- **Control de errores**: El proceso se detiene si hay fallos críticos

Edita `config/components_config.json` para definir qué elementos extraer:

## 🔧 Mantenimiento

```json

### Agregar nuevos componentes{

1. Edita `config/components_config.json`  "components": [

2. Agrega la configuración del nuevo componente    {

3. El sistema lo extraerá automáticamente en la próxima ejecución      "id": "nav-bar-public",

      "component_name": "NavBarPublic",

### Ver logs detallados      "subfolder": "NavBars",

```cmd      "description": "Barra de navegación pública"

type logs\bootstrap_studio_log.txt    }

```  ]

}

## 📚 Documentación Completa```



- **[Documentación Principal](docs/README.md)** - Guía completa del sistema**En Bootstrap Studio**, asigna IDs únicos a los elementos que quieres convertir en componentes.

- **[Configuración de Componentes](docs/README_components_config.md)** - Guía detallada de configuración

## 📋 Requisitos

## ✅ Estado del Sistema

- **Python 3.x** instalado y en PATH

- ✅ **7 scripts Python** funcionando correctamente- **Bootstrap Studio** (para exportación automática)

- ✅ **Configuración JSON** cargada dinámicamente- **Proyecto Astro** configurado

- ✅ **Sistema de respaldos** automático

- ✅ **Logs detallados** para debugging## 🔧 Personalización

- ✅ **Integración Bootstrap Studio** configurada

### **Agregar nuevos scripts**

---

1. Crea el script en `scripts/`

**Última actualización**: 15 de septiembre de 2025  2. Agrega la llamada en `bootstrap_studio_processor.bat`

**Versión**: 2.0 (Reorganizada y optimizada)3. Sigue el patrón de manejo de errores existente

### **Modificar componentes**

1. Edita `config/components_config.json`
2. Agrega/modifica configuraciones según necesites
3. Asigna IDs correspondientes en Bootstrap Studio

## 📊 Logging y Debug

- **Logs completos**: `logs/bootstrap_studio_log.txt`
- **Backups automáticos**: `backups/` antes de modificaciones
- **Salida en consola**: Resumen de operaciones realizadas

## 🎉 Resultado Final

Convierte automáticamente exportaciones de Bootstrap Studio en:

✅ **Componentes Astro** organizados y reutilizables
✅ **Imports automáticos** con rutas relativas correctas
✅ **Assets optimizados** para Vite/Astro
✅ **Enlaces corregidos** para navegación SPA
✅ **SVGs compatibles** con frameworks modernos
✅ **Estructura limpia** y mantenible

## 🐛 Solución de Problemas

### **Error "No se encontró script"**

- Verifica que Python esté en PATH
- Revisa que los archivos estén en `scripts/`

### **Error de configuración**

- Valida que `config/components_config.json` tenga formato JSON válido
- Revisa que los IDs existan en el HTML exportado

### **Componentes no extraídos**

- Confirma que los elementos tengan el ID correcto en Bootstrap Studio
- Revisa logs para ver errores específicos

---

**💡 Tip**: Mantén backups de tu configuración y revisa los logs después de cada ejecución para optimizar el flujo.
````
