#!/usr/bin/env python3
"""
Script de deployment para subir el sitio a Ferozoo hosting.
Este script prepara los archivos y puede ayudar con el deployment.
"""

import os
import zipfile
import shutil
from datetime import datetime
import subprocess

def create_deployment_package():
    """Crea un paquete ZIP con todos los archivos de dist para subir"""
    
    if not os.path.exists('dist'):
        print("❌ Error: La carpeta 'dist' no existe. Ejecuta 'npm run build' primero.")
        return False
    
    # Crear nombre del archivo con timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_filename = f'colegiomayorcba_deploy_{timestamp}.zip'
    
    print(f"📦 Creando paquete de deployment: {zip_filename}")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk('dist'):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, 'dist')
                zipf.write(file_path, arcname)
    
    print(f"✅ Paquete creado: {zip_filename}")
    print(f"📋 Instrucciones para deployment en Ferozoo:")
    print(f"   1. Accede al panel de control de Ferozoo")
    print(f"   2. Ve al administrador de archivos")
    print(f"   3. Navega a la carpeta public_html")
    print(f"   4. Sube y extrae el archivo: {zip_filename}")
    print(f"   5. Verifica que index.html esté en la raíz de public_html")
    print(f"   6. Prueba el sitio en: https://colegiomayorcba.com")
    
    return True

def run_build():
    """Ejecuta el proceso de build"""
    print("🔨 Ejecutando build...")
    try:
        result = subprocess.run(['python', 'build.py'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Build completado exitosamente")
            return True
        else:
            print(f"❌ Error en build: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error ejecutando build: {e}")
        return False

def deploy():
    """Proceso completo de deployment"""
    print("🚀 Iniciando proceso de deployment para colegiomayorcba.com")
    print("=" * 60)
    
    # Ejecutar build
    if not run_build():
        return False
    
    # Crear paquete
    if not create_deployment_package():
        return False
    
    print("=" * 60)
    print("🎉 Deployment preparado exitosamente!")
    print("📝 Próximos pasos manuales:")
    print("   - Subir el archivo ZIP al panel de Ferozoo")
    print("   - Extraer en public_html")
    print("   - Verificar el sitio en https://colegiomayorcba.com")
    
    return True

if __name__ == '__main__':
    deploy()
