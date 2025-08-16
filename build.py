#!/usr/bin/env python3
"""
Script para generar la versión estática del sitio web para producción.
Genera una carpeta 'dist' con todos los archivos HTML estáticos optimizados.
"""

import os
import shutil
import sys
from urllib.parse import urljoin
import re
from pathlib import Path

# Añadir el directorio actual al path para importar la app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server import app

def clean_dist():
    """Limpia la carpeta dist si existe"""
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    os.makedirs('dist', exist_ok=True)

def copy_static_files():
    """Copia todos los archivos estáticos a dist"""
    static_src = 'static'
    static_dst = 'dist'
    
    if os.path.exists(static_src):
        # Copiar todo el contenido de static a dist
        for item in os.listdir(static_src):
            src_path = os.path.join(static_src, item)
            dst_path = os.path.join(static_dst, item)
            
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path)
            else:
                shutil.copy2(src_path, dst_path)

def generate_static_html():
    """Genera el HTML estático desde las plantillas Flask"""
    # Configurar Flask para modo producción
    app.config['SERVER_NAME'] = 'colegiomayorcba.com'
    app.config['APPLICATION_ROOT'] = '/'
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    
    with app.app_context():
        # Crear un contexto de request simulado
        with app.test_request_context():
            from flask import url_for, render_template
            
            # Generar index.html
            html_content = render_template('index.html')
            
            # Reemplazar URLs de Flask por URLs relativas
            html_content = fix_static_urls(html_content)
            
            # Guardar el archivo
            with open('dist/index.html', 'w', encoding='utf-8') as f:
                f.write(html_content)

def fix_static_urls(html_content):
    """Convierte las URLs de Flask a URLs relativas para archivos estáticos"""
    # Reemplazar url_for('static', filename='...') por rutas relativas
    # Patrón para encontrar /static/... URLs
    html_content = re.sub(r'/static/', '', html_content)
    
    return html_content

def create_htaccess():
    """Crea archivo .htaccess para configuración del servidor web"""
    htaccess_content = """# Configuración para colegiomayorcba.com
RewriteEngine On

# Redirigir a HTTPS
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Configuración de cache para archivos estáticos
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType image/png "access plus 1 month"
    ExpiresByType image/jpg "access plus 1 month"
    ExpiresByType image/jpeg "access plus 1 month"
    ExpiresByType image/gif "access plus 1 month"
    ExpiresByType image/svg+xml "access plus 1 month"
</IfModule>

# Compresión GZIP
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/xml
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/x-javascript
</IfModule>

# Página de error personalizada
ErrorDocument 404 /index.html
"""
    
    with open('dist/.htaccess', 'w', encoding='utf-8') as f:
        f.write(htaccess_content)

def create_deployment_info():
    """Crea archivo con información del deployment"""
    from datetime import datetime
    
    info_content = f"""# Deployment Info
Sitio: Colegio Mayor Universitario de Córdoba
Dominio: colegiomayorcba.com
Fecha de build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Versión: 1.0.0

## Instrucciones de deployment:
1. Subir todo el contenido de esta carpeta 'dist' a public_html en Ferozoo
2. Verificar que el dominio apunte correctamente
3. Probar la funcionalidad del sitio

## Estructura:
- index.html: Página principal
- css/: Archivos de estilos
- js/: Archivos JavaScript
- img/: Imágenes
- assets/: Documentos y recursos adicionales
- .htaccess: Configuración del servidor
"""
    
    with open('dist/README_DEPLOYMENT.md', 'w', encoding='utf-8') as f:
        f.write(info_content)

def main():
    """Función principal del script de build"""
    print("🚀 Iniciando build para producción...")
    
    # Limpiar carpeta dist
    print("🧹 Limpiando carpeta dist...")
    clean_dist()
    
    # Copiar archivos estáticos
    print("📁 Copiando archivos estáticos...")
    copy_static_files()
    
    # Generar HTML estático
    print("🔨 Generando HTML estático...")
    generate_static_html()
    
    # Crear .htaccess
    print("⚙️ Creando configuración del servidor...")
    create_htaccess()
    
    # Crear info de deployment
    print("📝 Creando información de deployment...")
    create_deployment_info()
    
    print("✅ Build completado!")
    print("📦 Los archivos están listos en la carpeta 'dist'")
    print("🌐 Puedes subir el contenido de 'dist' a public_html en Ferozoo")
    print("🔗 El sitio estará disponible en: https://colegiomayorcba.com")

if __name__ == '__main__':
    main()
