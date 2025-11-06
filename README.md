# 🔍 Laboratorio XSS - Sistema Educativo Vulnerable

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-green.svg)
![License](https://img.shields.io/badge/License-Educational-red.svg)

## ⚠️ ADVERTENCIA IMPORTANTE

**Este laboratorio es INTENCIONALMENTE VULNERABLE y está diseñado EXCLUSIVAMENTE para fines educativos.**

- ❌ **NO** usar en producción
- ❌ **NO** exponer a internet público
- ❌ **NO** usar con datos reales o sensibles
- ❌ **NO** aplicar estas técnicas en sistemas sin autorización
- ✅ **SÍ** usar solo en entornos de aprendizaje controlados

## 📚 Descripción

Sistema educativo completo para aprender sobre vulnerabilidades **Cross-Site Scripting (XSS)** mediante práctica hands-on. Incluye cuatro ejercicios progresivos que cubren los tipos principales de XSS y técnicas de bypass.

### Ejercicios Incluidos

1. **🔄 Reflected XSS** - XSS que se refleja inmediatamente en la respuesta
2. **💾 Stored XSS** - XSS persistente almacenado en la base de datos
3. **🌐 DOM-based XSS** - Vulnerabilidades en JavaScript del cliente
4. **🔓 Bypass de Filtros** - Evasión de filtros de seguridad básicos

## 🎯 Objetivos de Aprendizaje

- Entender cómo funcionan los ataques XSS
- Identificar código vulnerable en aplicaciones web
- Practicar técnicas de explotación en un entorno seguro
- Aprender las mejores prácticas de defensa contra XSS
- Desarrollar mentalidad de seguridad ofensiva y defensiva

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno (Chrome, Firefox, Edge)

### Pasos de Instalación

```bash
# 1. Clonar o descargar el repositorio
cd xss-injection-lab

# 2. (Opcional pero recomendado) Crear entorno virtual
python -m venv venv

# Activar en Windows:
venv\Scripts\activate

# Activar en Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Inicializar base de datos (automático al iniciar)
python database.py

# 5. Ejecutar el servidor
python main.py
```

### Acceso

Una vez iniciado el servidor, abre tu navegador y visita:

```
http://localhost:8000
```

## 📖 Guía de Uso

### Para Estudiantes

1. **Comienza con el Ejercicio 1 (Reflected XSS)**
   - Lee las instrucciones y explicaciones técnicas
   - Prueba los payloads sugeridos
   - Experimenta con variaciones

2. **Progresa a ejercicios más complejos**
   - Cada ejercicio introduce nuevos conceptos
   - Usa las herramientas de desarrollador (F12)
   - Observa los mensajes en la consola del navegador

3. **Explora la página de Usuarios**
   - Entiende qué datos pueden ser robados con XSS
   - Visualiza el impacto de un ataque exitoso

### Para Profesores

1. **Preparación de la Clase**
   - Ejecuta el laboratorio en una red local aislada
   - Verifica que todos los estudiantes puedan acceder
   - Prepara ejemplos de demostración

2. **Durante la Clase**
   - Guía a los estudiantes a través de cada ejercicio
   - Explica los conceptos técnicos detrás de cada vulnerabilidad
   - Discute las implicaciones de seguridad del mundo real

3. **Evaluación**
   - Pide a los estudiantes que documenten payloads exitosos
   - Solicita explicaciones de por qué funcionan
   - Pide propuestas de mitigación

## 🎓 Estructura del Proyecto

```
xss-injection-lab/
├── main.py                 # Aplicación FastAPI principal
├── database.py             # Configuración de BD y datos de prueba
├── requirements.txt        # Dependencias Python
├── README.md              # Este archivo
├── .gitignore             # Archivos a ignorar en Git
├── templates/             # Templates HTML Jinja2
│   ├── index.html        # Página principal
│   ├── reflected.html    # Ejercicio 1: Reflected XSS
│   ├── stored.html       # Ejercicio 2: Stored XSS
│   ├── dom.html          # Ejercicio 3: DOM-based XSS
│   ├── bypass.html       # Ejercicio 4: Bypass de filtros
│   ├── users.html        # Datos de usuarios de prueba
│   └── about.html        # Información del laboratorio
└── static/
    └── style.css         # Estilos CSS (tema hacker)
```

## 💡 Ejemplos de Payloads

### Reflected XSS
```html
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
```

### Stored XSS
```html
<script>alert('Stored XSS')</script>
<img src=x onerror=alert('Persistent')>
<iframe src="javascript:alert('XSS')">
```

### DOM-based XSS
```
?name=<img src=x onerror=alert('DOM XSS')>
#<svg onload=alert('Fragment XSS')>
```

### Bypass de Filtros
```html
<ScRiPt>alert('Bypass')</ScRiPt>
<img src=x onload=alert('Bypass')>
<svg/onload=alert('Bypass')>
```

## 🛡️ Conceptos de Defensa Enseñados

- **Escape HTML**: Convertir `< > " ' &` en entidades HTML
- **Content Security Policy (CSP)**: Headers de seguridad restrictivos
- **HTTPOnly Cookies**: Prevenir acceso desde JavaScript
- **Input Validation**: Validar formato y tipo de datos
- **Output Encoding**: Codificar según contexto (HTML, JS, URL)
- **Sanitización**: Usar bibliotecas como DOMPurify
- **Trusted Types API**: API del navegador para prevenir XSS

## 🔧 Configuraciones Vulnerables Intencionales

Este laboratorio incluye las siguientes configuraciones inseguras **por diseño**:

```python
# 1. Autoescape deshabilitado en Jinja2
templates.env.autoescape = False

# 2. Headers de seguridad deshabilitados
X-XSS-Protection: 0
X-Frame-Options: ALLOW

# 3. Sin Content Security Policy
# (No hay CSP configurado)

# 4. Sin validación de entrada
# Los inputs se aceptan tal cual

# 5. Sin sanitización de output
# Los datos se muestran sin escape
```

## 📊 Datos de Prueba

### Usuarios Predeterminados

| Usuario | Email | Contraseña | Rol |
|---------|-------|-----------|-----|
| admin | admin@xsslab.com | Admin123! | Administrador |
| jperez | juan.perez@empresa.com | JuanP2024 | Usuario |
| mgarcia | maria.garcia@empresa.com | MariaG2024 | Usuario |

### Comentarios Iniciales

El sistema incluye 3 comentarios de prueba que se pueden limpiar y regenerar.

## 🐛 Solución de Problemas

### El servidor no inicia

```bash
# Verifica que Python esté instalado
python --version

# Verifica que las dependencias estén instaladas
pip list

# Reinstala las dependencias
pip install -r requirements.txt --force-reinstall
```

### Los XSS no se ejecutan

- Verifica que estés usando un navegador moderno
- Algunos navegadores tienen protecciones XSS integradas (desactívalas para este lab)
- Revisa la consola del navegador (F12) para errores
- Asegúrate de que el payload esté correctamente formateado

### Error de base de datos

```bash
# Elimina la base de datos y déjala regenerar
rm xss_lab.db
python main.py
```

## 📚 Recursos Adicionales

### Documentación Recomendada

- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [PortSwigger XSS Guide](https://portswigger.net/web-security/cross-site-scripting)
- [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security)

### Plataformas de Práctica Legal

- [HackTheBox](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [OWASP WebGoat](https://owasp.org/www-project-webgoat/)

## 🤝 Hacking Ético

### Reglas Importantes

1. ✅ **Obtén permiso explícito** antes de probar seguridad en cualquier sistema
2. ✅ **Usa solo entornos autorizados** como este laboratorio
3. ✅ **Reporta vulnerabilidades responsablemente** si las encuentras
4. ✅ **Respeta la ley** - El hacking no autorizado es ilegal
5. ✅ **Aprende para defender** - El objetivo es proteger, no atacar

## ⚖️ Consideraciones Legales

El uso indebido de técnicas de hacking es ilegal en prácticamente todas las jurisdicciones. Este laboratorio es para educación y debe usarse solo con:

- Sistemas de tu propiedad
- Sistemas para los que tienes permiso explícito por escrito
- Entornos de laboratorio diseñados para práctica

**Las consecuencias del hacking ilegal pueden incluir:**
- Cargos criminales
- Multas significativas
- Tiempo en prisión
- Antecedentes penales

## 👨‍🏫 Para Instructores

### Sugerencias de Clase

1. **Introducción (15 min)**
   - Explicar qué es XSS y por qué es importante
   - Mostrar ejemplos del mundo real
   - Demostrar el laboratorio

2. **Práctica Guiada (30 min)**
   - Ejercicio 1 y 2 con toda la clase
   - Discutir cada payload que funciona

3. **Práctica Independiente (45 min)**
   - Estudiantes completan ejercicios 3 y 4
   - Profesor circula y ayuda

4. **Discusión (30 min)**
   - ¿Qué aprendieron?
   - ¿Cómo se defienden contra XSS?
   - Casos de estudio del mundo real

### Evaluación Sugerida

- Documentar 3 payloads únicos por ejercicio
- Explicar por qué cada payload funciona
- Proponer 3 métodos de mitigación
- Ensayo corto sobre impacto de XSS en aplicaciones reales

## 🔄 Actualizaciones y Mejoras

### Características Futuras Planeadas

- [ ] Ejercicio de XSS en contexto JSON
- [ ] XSS en formularios de file upload
- [ ] mXSS (Mutation XSS)
- [ ] Sistema de puntuación/progreso
- [ ] Modo de competencia entre estudiantes

## 📝 Licencia

Este proyecto es de código abierto y está disponible únicamente para **fines educativos**. No se proporciona garantía alguna. El uso de este software es bajo tu propio riesgo.

## 🙏 Créditos

Desarrollado como material educativo para cursos de Ciberseguridad en Ingeniería de Sistemas.

**Tecnologías utilizadas:**
- FastAPI - Framework web
- Python - Lenguaje de programación
- SQLite - Base de datos
- Jinja2 - Motor de templates
- HTML/CSS/JavaScript - Frontend

---

## ⚠️ Recordatorio Final

**ESTE ES UN SISTEMA INTENCIONALMENTE VULNERABLE. NO LO USES EN PRODUCCIÓN.**

Si tienes preguntas o encuentras problemas, consulta con tu instructor o revisa la documentación.

¡Feliz aprendizaje y hackeo ético! 🔒
