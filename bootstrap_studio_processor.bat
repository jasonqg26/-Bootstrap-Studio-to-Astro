@echo off
REM filepath: c:\Users\jason\Documents\Nuxtek\Scrips\bootstrap_studio_processor.bat
REM Script para Bootstrap Studio - Post Export Processing
REM Ejecuta corrección de viewBox y guarda log en .txt

set LOGFILE=%~dp0logs\bootstrap_studio_log.txt
echo [%date% %time%] Inicio de procesamiento > "%LOGFILE%"

REM Verificar si se pasó el directorio de exportación
if "%1"=="" (
    echo ERROR: No se proporcionó el directorio de exportación >> "%LOGFILE%"
    echo Uso: %0 [DIRECTORIO_EXPORTACION] >> "%LOGFILE%"
    pause
    exit /b 1
)

REM Guardar el directorio de exportación
set EXPORT_DIR=%1
echo Directorio de exportación: %EXPORT_DIR% >> "%LOGFILE%"

REM Verificar que el directorio existe
if not exist "%EXPORT_DIR%" (
    echo ERROR: El directorio de exportación no existe: %EXPORT_DIR% >> "%LOGFILE%"
    pause
    exit /b 1
)

REM Cambiar al directorio donde están los scripts Python
cd /d "%~dp0"

REM Verificar que el script Python existe
if not exist "scripts\fix_viewbox.py" (
    echo ERROR: No se encontró scripts\fix_viewbox.py >> "%LOGFILE%"
    pause
    exit /b 1
)

echo. >> "%LOGFILE%"
echo ======================================== >> "%LOGFILE%"
echo Paso 1: Corrigiendo viewBox en archivos >> "%LOGFILE%"
echo ======================================== >> "%LOGFILE%"
python scripts\fix_viewbox.py "%EXPORT_DIR%" >> "%LOGFILE%" 2>&1

REM Verificar si el script fue exitoso
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: fix_viewbox.py falló con código %ERRORLEVEL% >> "%LOGFILE%"
    pause
    exit /b %ERRORLEVEL%
)

echo ✓ Corrección de viewBox completada >> "%LOGFILE%"

REM Verificar si existe el script de mover assets
if exist "scripts\mover_assets.py" (
    echo. >> "%LOGFILE%"
    echo ======================================== >> "%LOGFILE%"
    echo Paso 2: Moviendo archivos de assets >> "%LOGFILE%"
    echo ======================================== >> "%LOGFILE%"
    python scripts\mover_assets.py "%EXPORT_DIR%" >> "%LOGFILE%" 2>&1
    
    REM Verificar si el segundo script fue exitoso
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: scripts\mover_assets.py falló con código %ERRORLEVEL% >> "%LOGFILE%"
        exit /b %ERRORLEVEL%
    )
    
    echo ✓ Movimiento de assets completado >> "%LOGFILE%"
)

REM Verificar si existe el script de renombrado HTML a ASTRO
if exist "scripts\html_to_astro.py" (
    echo. >> "%LOGFILE%"
    echo ======================================== >> "%LOGFILE%"
    echo Paso 3: Renombrando archivos HTML a ASTRO >> "%LOGFILE%"
    echo ======================================== >> "%LOGFILE%"
    python scripts\html_to_astro.py "%EXPORT_DIR%" >> "%LOGFILE%" 2>&1
    
    REM Verificar si el tercer script fue exitoso
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: scripts\html_to_astro.py falló con código %ERRORLEVEL% >> "%LOGFILE%"
        exit /b %ERRORLEVEL%
    )
    
    echo ✓ Renombrado de archivos completado >> "%LOGFILE%"
)

REM Verificar si existe el script de corrección de enlaces HTML
if exist "scripts\fix_html_links.py" (
    echo. >> "%LOGFILE%"
    echo ======================================== >> "%LOGFILE%"
    echo Paso 4: Corrigiendo enlaces HTML >> "%LOGFILE%"
    echo ======================================== >> "%LOGFILE%"
    python scripts\fix_html_links.py "%EXPORT_DIR%" >> "%LOGFILE%" 2>&1
    
    REM Verificar si el cuarto script fue exitoso
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: scripts\fix_html_links.py falló con código %ERRORLEVEL% >> "%LOGFILE%"
        exit /b %ERRORLEVEL%
    )
    
    echo ✓ Corrección de enlaces completada >> "%LOGFILE%"
)

REM Verificar si existe el script de corrección de scripts is:inline
if exist "scripts\fix_inline_scripts.py" (
    echo. >> "%LOGFILE%"
    echo ======================================== >> "%LOGFILE%"
    echo Paso 5: Corrigiendo scripts is:inline >> "%LOGFILE%"
    echo ======================================== >> "%LOGFILE%"
    python scripts\fix_inline_scripts.py "%EXPORT_DIR%" >> "%LOGFILE%" 2>&1
    
    REM Verificar si el quinto script fue exitoso
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: scripts\fix_inline_scripts.py falló con código %ERRORLEVEL% >> "%LOGFILE%"
        exit /b %ERRORLEVEL%
    )
    
    echo ✓ Scripts is:inline corregidos >> "%LOGFILE%"
)

REM Verificar si existe el script de extracción de componentes por ID
if exist "scripts\extract_components_by_id.py" (
    echo. >> "%LOGFILE%"
    echo ======================================== >> "%LOGFILE%"
    echo Paso 6: Extrayendo componentes por ID >> "%LOGFILE%"
    echo ======================================== >> "%LOGFILE%"
    python scripts\extract_components_by_id.py "%EXPORT_DIR%" >> "%LOGFILE%" 2>&1
    
    REM Verificar si el sexto script fue exitoso
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: scripts\extract_components_by_id.py falló con código %ERRORLEVEL% >> "%LOGFILE%"
        exit /b %ERRORLEVEL%
    )
    
    echo ✓ Componentes extraídos exitosamente >> "%LOGFILE%"
)

REM Verificar si existe el script de limpieza de HTML residual
if exist "scripts\clean_component_residue.py" (
    echo. >> "%LOGFILE%"
    echo ======================================== >> "%LOGFILE%"
    echo Paso 7: Limpiando HTML residual >> "%LOGFILE%"
    echo ======================================== >> "%LOGFILE%"
    python scripts\clean_component_residue.py "%EXPORT_DIR%" >> "%LOGFILE%" 2>&1
    
    REM Verificar si el séptimo script fue exitoso
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: scripts\clean_component_residue.py falló con código %ERRORLEVEL% >> "%LOGFILE%"
        exit /b %ERRORLEVEL%
    )
    
    echo ✓ HTML residual limpiado exitosamente >> "%LOGFILE%"
)

echo. >> "%LOGFILE%"
echo ======================================== >> "%LOGFILE%"
echo ✓ Procesamiento completado exitosamente >> "%LOGFILE%"
echo ======================================== >> "%LOGFILE%"
echo Directorio procesado: %EXPORT_DIR% >> "%LOGFILE%"

echo.
echo Log guardado en: "%LOGFILE%"

REM No hacer pausa para que Bootstrap Studio termine más rápido
exit /b 0