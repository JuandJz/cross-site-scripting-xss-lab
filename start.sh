#!/bin/bash

# ============================================================================
# Script de Inicio Rápido - Laboratorio XSS
# ============================================================================

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║        🔍 LABORATORIO XSS - INICIO RÁPIDO 🔍                ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    echo "   Por favor instala Python 3.8 o superior"
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Verificar si el entorno virtual existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
    echo "✅ Entorno virtual creado"
else
    echo "✅ Entorno virtual encontrado"
fi
echo ""

# Activar entorno virtual
echo "🔌 Activando entorno virtual..."
source venv/bin/activate
echo "✅ Entorno virtual activado"
echo ""

# Instalar/Actualizar dependencias
echo "📥 Instalando dependencias..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✅ Dependencias instaladas"
echo ""

# Inicializar base de datos si no existe
if [ ! -f "xss_lab.db" ]; then
    echo "🗄️  Inicializando base de datos..."
    python database.py
    echo "✅ Base de datos inicializada"
else
    echo "✅ Base de datos encontrada"
fi
echo ""

# Mensaje final
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║  🚀 ¡Todo listo! Iniciando servidor...                      ║"
echo "║                                                              ║"
echo "║  📍 URL: http://localhost:8000                              ║"
echo "║  📚 API Docs: http://localhost:8000/docs                    ║"
echo "║                                                              ║"
echo "║  ⚠️  SOLO PARA USO EDUCATIVO                                ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo ""

# Iniciar servidor
python main.py
