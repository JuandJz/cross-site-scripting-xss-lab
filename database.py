"""
Base de datos SQLite para el laboratorio XSS
Incluye usuarios y comentarios de prueba
"""

import sqlite3
from datetime import datetime
from typing import List, Dict

DATABASE_FILE = "xss_lab.db"


def get_connection():
    """Crear conexión a la base de datos"""
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Inicializar base de datos con tablas y datos de prueba"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Tabla de usuarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    
    # Tabla de comentarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            comentario TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    
    # Verificar si ya hay datos
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        # Insertar usuarios de prueba
        usuarios_prueba = [
            ("admin", "admin@xsslab.com", "Admin123!", "Administrador"),
            ("jperez", "juan.perez@empresa.com", "JuanP2024", "Usuario"),
            ("mgarcia", "maria.garcia@empresa.com", "MariaG2024", "Usuario"),
            ("lrodriguez", "luis.rodriguez@empresa.com", "LuisR2024", "Moderador"),
            ("alopez", "ana.lopez@empresa.com", "AnaL2024", "Usuario"),
        ]
        
        for username, email, password, role in usuarios_prueba:
            cursor.execute("""
                INSERT INTO users (username, email, password, role, created_at)
                VALUES (?, ?, ?, ?, ?)
            """, (username, email, password, role, datetime.now().isoformat()))
    
    # Verificar si ya hay comentarios
    cursor.execute("SELECT COUNT(*) FROM comments")
    if cursor.fetchone()[0] == 0:
        # Insertar comentarios de prueba
        comentarios_prueba = [
            ("María García", "¡Excelente laboratorio! Me ayudó a entender mejor las vulnerabilidades XSS."),
            ("Juan Pérez", "Muy educativo, aunque un poco básico. ¿Habrá ejercicios más avanzados?"),
            ("Ana López", "Perfecto para empezar a aprender sobre seguridad web. Gracias por compartir."),
        ]
        
        for nombre, comentario in comentarios_prueba:
            cursor.execute("""
                INSERT INTO comments (nombre, comentario, created_at)
                VALUES (?, ?, ?)
            """, (nombre, comentario, datetime.now().isoformat()))
    
    conn.commit()
    conn.close()
    print("✅ Base de datos inicializada correctamente")


def get_users() -> List[Dict]:
    """Obtener todos los usuarios"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, username, email, password, role, created_at 
        FROM users 
        ORDER BY id
    """)
    users = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return users


def get_comments() -> List[Dict]:
    """Obtener todos los comentarios"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nombre, comentario, created_at 
        FROM comments 
        ORDER BY id DESC
    """)
    comments = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return comments


def add_comment(nombre: str, comentario: str):
    """
    Agregar un nuevo comentario
    ⚠️ VULNERABLE: No se sanitiza el input
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO comments (nombre, comentario, created_at)
        VALUES (?, ?, ?)
    """, (nombre, comentario, datetime.now().isoformat()))
    conn.commit()
    conn.close()


def clear_comments():
    """Limpiar todos los comentarios (útil para resetear ejercicios)"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM comments")
    
    # Re-insertar comentarios de prueba
    comentarios_prueba = [
        ("María García", "¡Excelente laboratorio! Me ayudó a entender mejor las vulnerabilidades XSS."),
        ("Juan Pérez", "Muy educativo, aunque un poco básico. ¿Habrá ejercicios más avanzados?"),
        ("Ana López", "Perfecto para empezar a aprender sobre seguridad web. Gracias por compartir."),
    ]
    
    for nombre, comentario in comentarios_prueba:
        cursor.execute("""
            INSERT INTO comments (nombre, comentario, created_at)
            VALUES (?, ?, ?)
        """, (nombre, comentario, datetime.now().isoformat()))
    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Reinicializar base de datos
    import os
    if os.path.exists(DATABASE_FILE):
        os.remove(DATABASE_FILE)
    init_db()
    
    print("\n📊 Usuarios de prueba:")
    for user in get_users():
        print(f"  - {user['username']}: {user['email']}")
    
    print("\n💬 Comentarios de prueba:")
    for comment in get_comments():
        print(f"  - {comment['nombre']}: {comment['comentario'][:50]}...")
