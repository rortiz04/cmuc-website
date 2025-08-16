# Colegio Mayor Universitario de Córdoba - Website

Sitio web oficial del CMUC con flujo de desarrollo local y deployment a producción.

## 🌐 Dominio
- **Producción**: [https://colegiomayorcba.com](https://colegiomayorcba.com)
- **Hosting**: Ferozoo
- **Desarrollo**: http://localhost:5000

## 🚀 Configuración Inicial

### 1. Instalar Dependencias de Python
```bash
pip install -r requirements.txt
```

### 2. Configurar Variables de Entorno
```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar con tus credenciales
nano .env
```

### 3. Instalar Node.js (para scripts de build)
```bash
# Verificar que Node.js esté instalado
node --version
npm --version
```

## 🛠️ Flujo de Desarrollo

### Desarrollo Local
```bash
# Iniciar servidor de desarrollo
npm run dev
# o directamente:
python server.py
```

El sitio estará disponible en: http://localhost:5000

### Desarrollo con Ngrok (opcional)
Si tienes configurado el token de Ngrok, automáticamente se creará un túnel público para testing.

## 📦 Build y Deployment

### 1. Generar Versión de Producción
```bash
# Generar carpeta dist con archivos estáticos
npm run build
```

Esto ejecuta `build.py` que:
- Limpia la carpeta `dist`
- Copia todos los archivos estáticos
- Genera HTML estático optimizado para producción
- Crea configuraciones del servidor (.htaccess)
- Prepara todo para subir a hosting

### 2. Deployment Automatizado
```bash
# Preparar paquete de deployment
python deploy.py
```

Esto:
- Ejecuta el build
- Crea un archivo ZIP con timestamp
- Proporciona instrucciones para subir a Ferozoo

### 3. Deployment Manual en Ferozoo

1. **Acceder al Panel de Control**
   - Ir a panel.ferozoo.com
   - Iniciar sesión con tus credenciales

2. **Administrador de Archivos**
   - Ir a "Administrador de archivos"
   - Navegar a la carpeta `public_html`

3. **Subir Archivos**
   - Subir el archivo ZIP generado
   - Extraer en `public_html`
   - Verificar que `index.html` esté en la raíz

4. **Verificar Deployment**
   - Visitar https://colegiomayorcba.com
   - Probar todas las funcionalidades

## 📝 Scripts Disponibles

```bash
# Desarrollo
npm run dev              # Iniciar servidor de desarrollo
npm run serve            # Servir archivos estáticos desde dist

# Build y Deploy
npm run build            # Generar versión de producción
npm run clean            # Limpiar carpeta dist
npm run deploy:prepare   # Limpiar y hacer build

# Python directo
python server.py         # Servidor de desarrollo
python build.py          # Generar build de producción
python deploy.py         # Preparar deployment
```

## 🗂️ Estructura del Proyecto

```
CMUCordoba-main/
├── server.py              # Servidor Flask para desarrollo
├── build.py               # Script de build para producción
├── deploy.py              # Script de deployment
├── package.json           # Scripts NPM
├── requirements.txt       # Dependencias Python
├── .env                   # Variables de entorno (local)
├── .env.production        # Variables de entorno (producción)
├── templates/
│   └── index.html         # Template principal
├── static/                # Archivos estáticos
│   ├── css/
│   ├── js/
│   ├── img/
│   └── assets/
└── dist/                  # Archivos generados para producción
    ├── index.html         # HTML estático optimizado
    ├── .htaccess          # Configuración del servidor
    ├── css/               # Estilos
    ├── js/                # JavaScript
    ├── img/               # Imágenes
    └── assets/            # Documentos y recursos
```

## 🔧 Configuración del Hosting

### Ferozoo Configuration
- **Dominio**: colegiomayorcba.com
- **Directorio**: public_html
- **SSL**: Automático (Let's Encrypt)
- **PHP**: Disponible (si se necesita)

### Archivos Importantes para Producción
- `.htaccess`: Configuración del servidor web
- `index.html`: Página principal estática
- Estructura de carpetas optimizada

## 🚨 Solución de Problemas

### Build Fallido
```bash
# Verificar dependencias
pip install -r requirements.txt

# Limpiar y volver a intentar
npm run clean
npm run build
```

### Problemas de Email
- Verificar credenciales en `.env`
- Usar contraseñas de aplicación de Gmail
- Revisar configuración SMTP

### Problemas de Deployment
- Verificar que `dist/` existe y tiene contenido
- Comprobar permisos en Ferozoo
- Verificar configuración DNS del dominio

## 📞 Contacto y Soporte

Para issues técnicos, revisar:
1. Logs del servidor Flask
2. Console del navegador
3. Configuración de variables de entorno
4. Estado del hosting en Ferozoo

## 🔄 Flujo de Trabajo Recomendado

1. **Desarrollo Local**
   ```bash
   npm run dev
   ```

2. **Testing**
   - Probar funcionalidades
   - Verificar responsive design
   - Testear formularios

3. **Build para Producción**
   ```bash
   npm run build
   ```

4. **Deployment**
   ```bash
   python deploy.py
   ```

5. **Verificación**
   - Visitar https://colegiomayorcba.com
   - Probar todas las funciones
   - Verificar rendimiento
