#!/usr/bin/env python3
"""
Script para instalar todas las librerías necesarias para Florence 2-Large
"""

import subprocess
import sys
import os

def run_command(command):
    """Ejecuta un comando y muestra el resultado"""
    print(f"🔄 Ejecutando: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Comando ejecutado exitosamente")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ Error en el comando:")
            print(result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Excepción: {e}")
        return False

def install_packages():
    """Instala todas las librerías necesarias"""
    packages = [
        "torch",
        "torchvision", 
        "transformers",
        "accelerate",
        "Pillow",
        "numpy",
        "matplotlib",
        "pandas",
        "requests",
        "bitsandbytes"
    ]
    
    print("🚀 Iniciando instalación de librerías para Florence 2-Large...")
    print(f"📦 Librerías a instalar: {', '.join(packages)}")
    print("=" * 60)
    
    # Actualizar pip primero
    if not run_command(f"{sys.executable} -m pip install --upgrade pip"):
        print("⚠️ Advertencia: No se pudo actualizar pip")
    
    # Instalar cada paquete
    for package in packages:
        print(f"\n📥 Instalando {package}...")
        success = run_command(f"{sys.executable} -m pip install {package}")
        if success:
            print(f"✅ {package} instalado correctamente")
        else:
            print(f"❌ Error instalando {package}")
    
    print("\n" + "=" * 60)
    print("🔍 Verificando instalaciones...")
    
    # Verificar instalaciones
    verification_code = """
import sys
packages = ['torch', 'transformers', 'PIL', 'numpy', 'matplotlib', 'pandas', 'requests']
for pkg in packages:
    try:
        module = __import__(pkg)
        version = getattr(module, '__version__', 'versión desconocida')
        print(f'✅ {pkg}: {version}')
    except ImportError as e:
        print(f'❌ {pkg}: No instalado - {e}')
"""
    
    run_command(f'{sys.executable} -c "{verification_code}"')

if __name__ == "__main__":
    print("🎯 Instalador de dependencias para Florence 2-Large")
    print(f"🐍 Python: {sys.version}")
    print(f"📍 Ejecutable: {sys.executable}")
    print()
    
    install_packages()
    
    print("\n🎉 ¡Instalación completada!")
    print("💡 Ahora puedes ejecutar el notebook de Florence 2-Large")
