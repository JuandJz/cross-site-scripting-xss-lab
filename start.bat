@echo off
REM ============================================================================
REM Script de Inicio Rápido - Laboratorio XSS (Windows)
REM ============================================================================

echo ================================================================
echo.
echo        🔍 LABORATORIO XSS - INICIO RÁPIDO 🔍
echo.
echo ================================================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python no está instalado
    echo    Por favor instala Python 3.8 o superior desde python.org
    pause
    exit /b 1
)

echo ✅ Python encontrado
python --version
echo.

REM Verificar si el entorno virtual existe
if not exist "venv\" (
    echo 📦 Creando entorno virtual...
    python -m venv venv
    echo ✅ Entorno virtual creado
) else (
    echo ✅ Entorno virtual encontrado
)
echo.

REM Activar entorno virtual
echo 🔌 Activando entorno virtual...
call venv\Scripts\activate.bat
echo ✅ Entorno virtual activado
echo.

REM Instalar/Actualizar dependencias
echo 📥 Instalando dependencias...
python -m pip install --upgrade pip -q
pip install -r requirements.txt -q
echo ✅ Dependencias instaladas
echo.

REM Inicializar base de datos si no existe
if not exist "xss_lab.db" (
    echo 🗄️  Inicializando base de datos...
    python database.py
    echo ✅ Base de datos inicializada
) else (
    echo ✅ Base de datos encontrada
)
echo.

REM Mensaje final
echo ================================================================
echo.
echo  🚀 ¡Todo listo! Iniciando servidor...
echo.
echo  📍 URL: http://localhost:8000
echo  📚 API Docs: http://localhost:8000/docs
echo.
echo  ⚠️  SOLO PARA USO EDUCATIVO
echo.
echo ================================================================
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

REM Iniciar servidor
python main.py

pause
