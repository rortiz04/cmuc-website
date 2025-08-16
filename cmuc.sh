#!/bin/bash
# Script de desarrollo rápido para CMUC Website

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🏛️  CMUC Website - Herramientas de Desarrollo${NC}"
echo "=============================================="

# Verificar si micromamba está disponible
if ! command -v micromamba &> /dev/null; then
    echo -e "${RED}❌ Error: micromamba no está instalado${NC}"
    exit 1
fi

# Función para activar ambiente
activate_env() {
    echo -e "${YELLOW}🔄 Activando ambiente cmuc...${NC}"
    eval "$(micromamba shell hook --shell bash)"
    micromamba activate cmuc
}

# Función para desarrollo
dev() {
    echo -e "${GREEN}🚀 Iniciando servidor de desarrollo...${NC}"
    activate_env
    python server.py
}

# Función para build
build() {
    echo -e "${GREEN}🔨 Generando build de producción...${NC}"
    activate_env
    python build.py
}

# Función para deployment
deploy() {
    echo -e "${GREEN}📦 Preparando deployment...${NC}"
    activate_env
    python deploy.py
}

# Función para limpiar
clean() {
    echo -e "${YELLOW}🧹 Limpiando archivos de build...${NC}"
    rm -rf dist/
    echo -e "${GREEN}✅ Carpeta dist eliminada${NC}"
}

# Función para servir archivos estáticos
serve() {
    echo -e "${GREEN}🌐 Sirviendo archivos estáticos desde dist/...${NC}"
    if [ ! -d "dist" ]; then
        echo -e "${RED}❌ Error: Carpeta dist no existe. Ejecuta build primero.${NC}"
        exit 1
    fi
    python -m http.server 8000 --directory dist
}

# Menú principal
case "$1" in
    "dev")
        dev
        ;;
    "build")
        build
        ;;
    "deploy")
        deploy
        ;;
    "clean")
        clean
        ;;
    "serve")
        serve
        ;;
    "help"|"")
        echo "Uso: $0 {dev|build|deploy|clean|serve|help}"
        echo ""
        echo "Comandos disponibles:"
        echo "  dev     - Iniciar servidor de desarrollo (localhost:5000)"
        echo "  build   - Generar archivos para producción en carpeta dist/"
        echo "  deploy  - Preparar paquete ZIP para subir a Ferozoo"
        echo "  clean   - Limpiar carpeta dist/"
        echo "  serve   - Servir archivos estáticos desde dist/ (localhost:8000)"
        echo "  help    - Mostrar esta ayuda"
        echo ""
        echo "Ejemplos:"
        echo "  $0 dev      # Desarrollo local"
        echo "  $0 build    # Generar producción"
        echo "  $0 deploy   # Preparar para subir"
        ;;
    *)
        echo -e "${RED}❌ Comando no válido: $1${NC}"
        echo "Usa '$0 help' para ver los comandos disponibles"
        exit 1
        ;;
esac
