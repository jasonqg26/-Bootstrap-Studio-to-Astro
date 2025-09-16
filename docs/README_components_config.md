# 📋 Configuración de Componentes - Extract Components by ID

## 📄 Archivo: `components_config.json`

Este archivo define qué elementos HTML extraer y convertir en componentes Astro.

### 🔧 Estructura de configuración:

```json
{
  "components": [
    {
      "id": "elemento-id",
      "component_name": "NombreComponente",
      "subfolder": "Subcarpeta",
      "description": "Descripción del componente"
    }
  ]
}
```

### 📝 Campos explicados:

- **`id`**: ID del elemento en Bootstrap Studio (ej: `"nav-bar-public"`)
- **`component_name`**: Nombre del componente Astro a crear (ej: `"NavBarPublic"`)
- **`subfolder`**: Subcarpeta donde crear el componente (`null` = raíz de components)
- **`description`**: Descripción para logs y documentación

### 📁 Estructura de carpetas generada:

```
src/components/
├── FooterPublic.astro           (subfolder: null)
├── SocialLinks.astro           (subfolder: null)
├── NavBars/
│   ├── NavBarPublic.astro      (subfolder: "NavBars")
│   ├── NavBarLogin.astro       (subfolder: "NavBars")
│   └── NavBarNewAccont.astro   (subfolder: "NavBars")
├── Forms/
│   └── ContactForm.astro       (subfolder: "Forms")
├── Products/
│   └── ProductGrid.astro       (subfolder: "Products")
├── Sections/
│   ├── HeroSection.astro       (subfolder: "Sections")
│   └── Testimonials.astro      (subfolder: "Sections")
└── Menus/
    └── OffcanvasMenu.astro     (subfolder: "Menus")
```

### 🎯 Imports automáticos generados:

```astro
---
import NavBarPublic from '../components/NavBars/NavBarPublic.astro';
import FooterPublic from '../components/FooterPublic.astro';
import ContactForm from '../components/Forms/ContactForm.astro';
---
```

### ✏️ Cómo modificar la configuración:

1. **Abrir** `components_config.json`
2. **Agregar/modificar** elementos en el array `"components"`
3. **Asignar IDs** correspondientes en Bootstrap Studio
4. **Ejecutar** el script

### 🚀 Uso del script:

```bash
python extract_components_by_id.py "C:\ruta\export\directorio"
```

### ⚠️ Notas importantes:

- Los IDs deben existir en el HTML de Bootstrap Studio
- Los nombres de componentes deben seguir convención PascalCase
- Las subcarpetas se crean automáticamente si no existen
- Se hacen backups automáticos antes de modificar archivos