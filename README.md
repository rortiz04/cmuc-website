# Colegio Mayor Universitario de Córdoba - Sitio Web

Sitio web oficial del Colegio Mayor Universitario de Córdoba (CMUC), una institución educativa sin fines de lucro fundada en la década del 50 por el monseñor Eladio Bordagaray.

## 🏛️ Acerca del Proyecto

Este sitio web presenta la historia, valores y servicios del Colegio Mayor Universitario de Córdoba, que se rige bajo tres pilares fundamentales:
- **Estudio**
- **Colaboración** 
- **Integración**

## 🚀 Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 4
- **Iconos**: Font Awesome
- **Email**: SMTP con Gmail
- **Túnel público**: Ngrok (desarrollo)

## 📋 Características

- ✅ Diseño responsivo y moderno
- ✅ Galería de imágenes con modales
- ✅ Formulario de contacto funcional
- ✅ Información institucional completa
- ✅ Enlaces a documentos históricos (PDFs)
- ✅ Integración con redes sociales
- ✅ Mapa de ubicación

## 🛠️ Instalación y Configuración

### Prerrequisitos

- Python 3.7+
- pip (gestor de paquetes de Python)

### Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/cmuc-website.git
cd cmuc-website
```

2. Crea un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno:
   - Copia el archivo `.env.example` a `.env`
   - Completa las configuraciones necesarias

### Configuración del Email

Para que el formulario de contacto funcione, necesitas configurar:

1. **Gmail App Password**: 
   - Ve a tu cuenta de Google
   - Habilita la autenticación de 2 factores
   - Genera una contraseña de aplicación
   - Úsala en lugar de tu contraseña regular

2. **Configuración en el código**:
   - Edita `server.py`
   - Reemplaza `EMAIL_USER` y `EMAIL_PASSWORD` con tus credenciales

### Configuración de Ngrok (Opcional)

Para desarrollo con túnel público:
1. Regístrate en [ngrok.com](https://ngrok.com)
2. Obtén tu token de autenticación
3. Reemplaza el token en `server.py`

## 🚀 Ejecución

### Desarrollo Local

```bash
python server.py
```

El sitio estará disponible en `http://localhost:5000`

### Producción

Para despliegue en producción, considera usar:
- **Gunicorn** como servidor WSGI
- **Nginx** como proxy reverso
- **SSL/TLS** para HTTPS

Ejemplo con Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 server:app
```

## 📁 Estructura del Proyecto

```
cmuc-website/
├── server.py              # Aplicación Flask principal
├── requirements.txt       # Dependencias de Python
├── .env.example          # Variables de entorno de ejemplo
├── .gitignore            # Archivos ignorados por Git
├── static/               # Archivos estáticos
│   ├── css/             # Estilos CSS
│   ├── js/              # JavaScript
│   ├── img/             # Imágenes
│   └── assets/          # Documentos y recursos
└── templates/           # Plantillas HTML
    └── index.html       # Página principal
```

## 🔧 Configuración de Variables de Entorno

Crea un archivo `.env` con:

```env
# Configuración de Email
EMAIL_USER=tu_email@gmail.com
EMAIL_PASSWORD=tu_app_password_de_gmail
EMAIL_RECIPIENT=colegiomayorcba@gmail.com

# Configuración de Ngrok (opcional)
NGROK_TOKEN=tu_token_de_ngrok

# Configuración Flask
FLASK_ENV=development
FLASK_DEBUG=True
```

## 📧 Configuración del Formulario de Contacto

El formulario incluye validación para:
- Nombre (requerido)
- Email (requerido, formato válido)
- Teléfono (requerido)
- Mensaje (requerido)

Los mensajes se envían automáticamente al email configurado.

## 🎨 Personalización

### Colores y Estilos
Edita `/static/css/styles.css` para modificar:
- Colores del tema
- Tipografías
- Espaciados
- Efectos visuales

### Imágenes
Reemplaza las imágenes en `/static/img/cmuc/` con:
- Formato recomendado: JPG/PNG
- Optimización para web
- Resolución apropiada para responsive design

### Contenido
Modifica `/templates/index.html` para actualizar:
- Textos institucionales
- Enlaces a documentos
- Información de contacto

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👥 Contacto

**Colegio Mayor Universitario de Córdoba**
- Email: colegiomayorcba@gmail.com
- Facebook: [@cmuccba](https://www.facebook.com/cmuccba)
- Instagram: [@colegiomayorcba](https://www.instagram.com/colegiomayorcba/)
- Ubicación: Láprida 30/37, Nueva Córdoba, Córdoba

## 🙏 Reconocimientos

- Padre Eladio Bordagaray - Fundador del CMUC
- Departamento de Cultura - Desarrollo y mantenimiento
- Bootstrap Team - Framework CSS
- Font Awesome - Iconografía

---

*"No te conformes con ser bueno, ¡Sé santo!" - Padre Eladio Bordagaray*
