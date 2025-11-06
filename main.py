"""
🔍 LABORATORIO XSS - APLICACIÓN VULNERABLE
==========================================
⚠️  ADVERTENCIA: Esta aplicación es INTENCIONALMENTE VULNERABLE
    Solo para uso educativo en entornos controlados.
    NO usar en producción ni exponer a internet.
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import database

# Crear aplicación FastAPI
app = FastAPI(
    title="🔍 Laboratorio XSS - VULNERABLE",
    description="Sistema educativo para aprender sobre vulnerabilidades XSS"
)

# Configurar archivos estáticos y templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ⚠️ CONFIGURACIÓN INSEGURA INTENCIONAL
# Deshabilitar escape automático en Jinja2
templates.env.autoescape = False

# Inicializar base de datos
database.init_db()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Página principal con menú de ejercicios"""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "🔍 Laboratorio XSS"
    })


# ==========================================
# EJERCICIO 1: REFLECTED XSS
# ==========================================

@app.get("/reflected", response_class=HTMLResponse)
async def reflected_get(request: Request, query: str = ""):
    """
    VULNERABILIDAD: Reflected XSS
    El parámetro 'query' se refleja directamente en la página sin sanitizar
    """
    results = []
    mensaje = ""
    
    if query:
        # Buscar en productos (simulado)
        productos = [
            "Laptop HP", "Mouse Logitech", "Teclado Mecánico",
            "Monitor Samsung", "Webcam HD", "Auriculares Gamer"
        ]
        results = [p for p in productos if query.lower() in p.lower()]
        
        # ⚠️ VULNERABLE: Inyectar query directamente sin escape
        if results:
            mensaje = f"Se encontraron {len(results)} resultados para: {query}"
        else:
            mensaje = f"No se encontraron resultados para: {query}"
    
    return templates.TemplateResponse("reflected.html", {
        "request": request,
        "query": query,
        "results": results,
        "mensaje": mensaje
    })


@app.post("/reflected", response_class=HTMLResponse)
async def reflected_post(request: Request, search: str = Form("")):
    """POST handler para búsqueda reflected XSS"""
    return RedirectResponse(f"/reflected?query={search}", status_code=303)


# ==========================================
# EJERCICIO 2: STORED XSS
# ==========================================

@app.get("/stored", response_class=HTMLResponse)
async def stored_get(request: Request):
    """
    VULNERABILIDAD: Stored XSS
    Los comentarios se almacenan y muestran sin sanitizar
    """
    comentarios = database.get_comments()
    
    return templates.TemplateResponse("stored.html", {
        "request": request,
        "comentarios": comentarios
    })


@app.post("/stored", response_class=HTMLResponse)
async def stored_post(
    request: Request,
    nombre: str = Form(...),
    comentario: str = Form(...)
):
    """
    Guardar comentario sin validación
    ⚠️ VULNERABLE: No se sanitiza el input antes de almacenar
    """
    database.add_comment(nombre, comentario)
    return RedirectResponse("/stored", status_code=303)


@app.post("/stored/clear")
async def clear_comments():
    """Limpiar todos los comentarios"""
    database.clear_comments()
    return RedirectResponse("/stored", status_code=303)


# ==========================================
# EJERCICIO 3: DOM-BASED XSS
# ==========================================

@app.get("/dom", response_class=HTMLResponse)
async def dom_based(request: Request):
    """
    VULNERABILIDAD: DOM-based XSS
    JavaScript manipula el DOM usando parámetros de URL sin validar
    """
    return templates.TemplateResponse("dom.html", {
        "request": request
    })


# ==========================================
# EJERCICIO 4: BYPASS DE FILTROS
# ==========================================

@app.get("/bypass", response_class=HTMLResponse)
async def bypass_get(request: Request, message: str = ""):
    """
    VULNERABILIDAD: Filtros débiles
    Intenta bloquear XSS pero puede ser evadido
    """
    filtered_message = ""
    bypass_detected = False
    
    if message:
        # ⚠️ FILTRO DÉBIL: Solo bloquea patrones básicos
        blocked_patterns = ["<script>", "javascript:", "onerror"]
        
        filtered_message = message
        for pattern in blocked_patterns:
            if pattern.lower() in message.lower():
                bypass_detected = True
                # Intenta "limpiar" pero de forma insegura
                filtered_message = message.lower().replace(pattern.lower(), "[BLOCKED]")
    
    return templates.TemplateResponse("bypass.html", {
        "request": request,
        "message": message,
        "filtered_message": filtered_message,
        "bypass_detected": bypass_detected
    })


# ==========================================
# ENDPOINTS ADICIONALES
# ==========================================

@app.get("/users", response_class=HTMLResponse)
async def users(request: Request):
    """Mostrar usuarios de prueba (datos a 'robar' con XSS)"""
    usuarios = database.get_users()
    return templates.TemplateResponse("users.html", {
        "request": request,
        "usuarios": usuarios
    })


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """Información sobre el laboratorio"""
    return templates.TemplateResponse("about.html", {
        "request": request
    })


# ==========================================
# CONFIGURACIÓN DE SEGURIDAD INSEGURA
# ==========================================

@app.middleware("http")
async def add_insecure_headers(request: Request, call_next):
    """
    ⚠️ HEADERS INSEGUROS INTENCIONALES
    Para permitir que XSS funcione sin restricciones
    """
    response = await call_next(request)
    
    # Deshabilitar protecciones del navegador
    response.headers["X-XSS-Protection"] = "0"
    response.headers["X-Frame-Options"] = "ALLOW"
    response.headers["X-Content-Type-Options"] = "nosniff"
    
    # No usar Content Security Policy
    # response.headers["Content-Security-Policy"] = "default-src 'none'"
    
    return response


if __name__ == "__main__":
    import uvicorn
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║  🔍 LABORATORIO XSS - SISTEMA VULNERABLE                  ║
    ║                                                           ║
    ║  ⚠️  ADVERTENCIA: Aplicación intencionalmente vulnerable  ║
    ║     Solo para uso educativo                               ║
    ║                                                           ║
    ║  🌐 Servidor iniciando en: http://localhost:8000         ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    uvicorn.run(app, host="0.0.0.0", port=8000)
