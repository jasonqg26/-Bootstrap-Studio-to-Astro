# 🚀 Bootstrap Studio to Astro - Automation Suite

Sistema avanzado para automatizar la conversión de exportaciones de Bootstrap Studio en componentes Astro optimizados, organizados y listos para usar.

---

**🆕 Actualización v2.1**: Limpieza automática de HTML residual tras extraer componentes. Mejor organización, integración y robustez.

---

## 📁 Estructura del Proyecto

```
Scrips/
├── bootstrap_studio_processor.bat      # Script principal de automatización
├── README.md                           # Este archivo
├── scripts/                            # Scripts Python especializados
│   ├── extract_components_by_id.py     # Extrae componentes por ID
│   ├── fix_html_links.py               # Corrige enlaces HTML
│   ├── fix_inline_scripts.py           # Agrega is:inline a scripts
│   ├── fix_viewbox.py                  # Corrige viewBox en SVGs
│   ├── mover_assets.py                 # Organiza assets en estructura Astro
│   ├── html_to_astro.py                # Renombra .html → .astro
│   ├── fix_nested_links.py             # Corrige enlaces anidados
├── config/
│   └── components_config.json          # Configuración de componentes
├── docs/
│   ├── README.md                       # Documentación principal
│   └── README_components_config.md     # Guía de configuración de componentes
├── logs/
│   └── bootstrap_studio_log.txt        # Log de ejecuciones
├── backups/
│   └── components/                     # Backups de componentes extraídos
```

---

## 🎯 Uso Rápido

### 1. Integración directa con Bootstrap Studio (Recomendado)
1. Ve a **File → Export Settings → Advanced**
2. En **Export Script** coloca la ruta de `bootstrap_studio_processor.bat`
3. Exporta tu diseño normalmente

### 2. Ejecución manual
Mantiene la organización por carpetas (`css`, `js`, `img`, `fonts`):

```bash
cd  bootstrap studio to astro
bootstrap_studio_processor.bat "C:\ruta\a\tu\exportacion"
```
Convierte automáticamente `.html` → `.astro` y procesa sólo el directorio principal.

---

## ⚙️ Flujo de Automatización

El script ejecuta **7 pasos** secuenciales:
1. **🔧 Corrección de ViewBox**: Arregla atributos SVG para compatibilidad total.
2. **📂 Organización de Assets**: Mueve archivos a las ubicaciones correctas del proyecto Astro.
3. **🔄 Renombrado HTML → ASTRO**: Convierte extensiones de archivos HTML a Astro.
4. **🔗 Corrección de Enlaces**: Normaliza rutas y referencias, especialmente para navegación SPA.
   - Ejemplo: `href="/page.html"` → `href="/page"`
   - Especial: `href="/index.html"` → `href="/"` (raíz Astro)
5. **⚡ Scripts is:inline**: Configura todos los scripts de assets para Astro agregando `is:inline`.
6. **🧩 Extracción de Componentes**: Genera componentes Astro automáticamente basados en IDs configurados.
7. **📊 Reporte Final**: Log detallado de todas las operaciones.

---

## 🧩 Configuración de Componentes

Puedes definir los componentes a extraer en `config/components_config.json`:
```json
{
  "components": [
    {
      "id": "nav-bar-public",
      "component_name": "NavBarPublic",
      "subfolder": "NavBars",
      "description": "Barra de navegación para usuarios no autenticados"
    }
    // ...más componentes
  ]
}
```
Cada elemento por ID se convierte en un componente Astro organizado y con imports relativos.
**IMPORTANTE TENER CONFIGURADAS LAS RUTAS RELATIVAS EN TU PROYECTO ASTRO**

**Las rutas usadas son @/Components**
---

## 📊 Registro y Monitoreo

- **Logs automáticos**: Todas las operaciones se guardan en `logs/bootstrap_studio_log.txt`
- **Backups**: Se generan respaldos automáticos antes de modificar componentes
- **Control de errores**: El proceso se detiene ante fallos críticos

---

## 📚 Documentación

- [Documentación Principal](docs/README.md): Guía completa de uso y personalización
- [Guía de Configuración de Componentes](docs/README_components_config.md): Ejemplos y recomendaciones de configuración

---

## 📋 Requisitos

- **Python 3.x** instalado y agregado al PATH
- **Bootstrap Studio** para exportación automática
- **Proyecto Astro** correctamente configurado

---

## ✅ Estado del Sistema

- ✔️ **7 scripts Python** funcionando y probados
- ✔️ **Configuración JSON** dinámica
- ✔️ **Sistema de backups** automático
- ✔️ **Logs detallados** para debugging
- ✔️ **Integración directa con Bootstrap Studio**

---

## 🔧 Personalización

### Agregar scripts Python
1. Crea el script en `scripts/`
2. Añade la llamada en `bootstrap_studio_processor.bat`
3. Sigue el patrón de manejo de errores existente

### Modificar componentes
1. Edita `config/components_config.json`
2. Agrega/modifica configuraciones según tus necesidades
3. Asigna los IDs correspondientes en Bootstrap Studio

---

## 🐛 Solución de Problemas

### Error "No se encontró script"
- Verifica que Python esté en PATH
- Revisa la ubicación de los scripts

### Error de configuración
- Valida el formato JSON en `config/components_config.json`
- Confirma que los IDs existan en el HTML exportado

### Componentes no extraídos
- Revisa que los elementos tengan el ID correcto en Bootstrap Studio
- Consulta el log para detalles y errores específicos

---

## 🎉 Resultado Final

- ✅ **Componentes Astro** organizados y reutilizables
- ✅ **Imports automáticos** con rutas relativas correctas
- ✅ **Assets optimizados** para Vite/Astro
- ✅ **Enlaces corregidos** para navegación SPA
- ✅ **SVGs compatibles** con frameworks modernos
- ✅ **Estructura limpia** y mantenible

---

**💡 Tip:** Mantén respaldos de tu configuración y revisa los logs tras cada ejecución para optimizar el flujo.

---

*Última actualización: 15 de septiembre de 2025*  
*Versión: 2.1 (Reorganizada, optimizada y robusta)*
