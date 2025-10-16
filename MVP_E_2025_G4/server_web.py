#!/usr/bin/env python3
"""
Servidor web simple para compartir la página NUCLEUS GEAR PE
Permite que el profesor acceda a la página web desde cualquier dispositivo en la red local
"""

import http.server
import socketserver
import socket
import webbrowser
import os
from pathlib import Path

def get_local_ip():
    """Obtiene la IP local de la máquina"""
    try:
        # Conecta a una dirección externa para obtener la IP local
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
        return local_ip
    except Exception:
        return "127.0.0.1"

def start_server(port=8000):
    """Inicia el servidor web"""
    
    # Cambiar al directorio de la página web
    web_dir = Path(__file__).parent
    os.chdir(web_dir)
    
    # Configurar el servidor
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", port), Handler) as httpd:
        local_ip = get_local_ip()
        
        print("=" * 60)
        print("🚀 SERVIDOR WEB INICIADO - NUCLEUS GEAR PE")
        print("=" * 60)
        print(f"📱 Para el profesor (acceso desde cualquier dispositivo):")
        print(f"   http://{local_ip}:{port}")
        print()
        print(f"💻 Para ti (acceso local):")
        print(f"   http://localhost:{port}")
        print()
        print("📋 INSTRUCCIONES PARA EL PROFESOR:")
        print(f"   1. Conectarse a la misma red WiFi que tu computadora")
        print(f"   2. Abrir navegador web")
        print(f"   3. Ir a: http://{local_ip}:{port}")
        print()
        print("⚠️  IMPORTANTE:")
        print("   - Asegúrate de que el firewall permita conexiones en el puerto", port)
        print("   - Mantén esta ventana abierta mientras el profesor navega")
        print("   - Presiona Ctrl+C para detener el servidor")
        print("=" * 60)
        
        # Abrir automáticamente en el navegador local
        webbrowser.open(f'http://localhost:{port}')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Servidor detenido.")

if __name__ == "__main__":
    start_server()
