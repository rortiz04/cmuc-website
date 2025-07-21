# Instrucciones para subir a GitHub

## 🚀 Pasos para crear el repositorio en GitHub

### 1. Crear repositorio en GitHub
1. Ve a [GitHub.com](https://github.com)
2. Haz click en el botón "+" en la esquina superior derecha
3. Selecciona "New repository"
4. Llena los datos:
   - **Repository name**: `cmuc-website` (o el nombre que prefieras)
   - **Description**: `Sitio web oficial del Colegio Mayor Universitario de Córdoba`
   - **Visibility**: Public (recomendado) o Private
   - ❗ **NO marques** "Add a README file" (ya tienes uno)
   - ❗ **NO marques** "Add .gitignore" (ya tienes uno)
   - ❗ **NO marques** "Choose a license" (ya tienes una)
5. Haz click en "Create repository"

### 2. Conectar repositorio local con GitHub
Una vez creado el repositorio en GitHub, ejecuta estos comandos:

```bash
# Agregar el repositorio remoto (reemplaza TU_USUARIO con tu nombre de usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/cmuc-website.git

# Verificar que se agregó correctamente
git remote -v

# Subir los cambios a GitHub
git push -u origin main
```

### 3. Configurar variables de entorno en producción

#### Para Heroku:
```bash
# Instalar Heroku CLI si no lo tienes
# Luego:
heroku create tu-app-name
heroku config:set EMAIL_USER=tu_email@gmail.com
heroku config:set EMAIL_PASSWORD=tu_app_password
heroku config:set EMAIL_RECIPIENT=colegiomayorcba@gmail.com
heroku config:set SECRET_KEY=tu_clave_secreta_super_segura
git push heroku main
```

#### Para otros servicios de hosting:
- Configura las variables de entorno según el archivo `.env.example`
- No subas el archivo `.env` al repositorio (está en .gitignore)

### 4. Configuración de Email para Gmail

Para que el formulario de contacto funcione:

1. **Habilitar autenticación de 2 factores** en tu cuenta de Gmail
2. **Generar contraseña de aplicación**:
   - Ve a Configuración de Google Account
   - Seguridad → Contraseñas de aplicaciones
   - Genera una nueva contraseña para "Correo"
   - Usa esta contraseña en `EMAIL_PASSWORD`

### 5. Comandos Git útiles para el futuro

```bash
# Ver estado de archivos
git status

# Agregar cambios
git add .

# Hacer commit
git commit -m "descripción de cambios"

# Subir cambios
git push origin main

# Ver historial
git log --oneline

# Crear nueva rama
git checkout -b nueva-funcionalidad

# Cambiar de rama
git checkout main
```

### 6. Invitar colaboradores al proyecto

Para agregar editores que puedan contribuir al proyecto:

#### Opción A: Invitar colaboradores (recomendado)
1. Ve a tu repositorio en GitHub: `https://github.com/rortiz04/cmuc-website`
2. Haz clic en la pestaña **"Settings"** (en la barra superior del repositorio)
3. En el menú lateral izquierdo, haz clic en **"Collaborators"**
4. Haz clic en **"Add people"** (botón verde)
5. Escribe el **nombre de usuario** o **email** del colaborador
6. Selecciona el nivel de permisos:
   - **Write**: Pueden hacer cambios, crear branches, hacer commits
   - **Admin**: Acceso completo (cuidado con este nivel)
7. Haz clic en **"Add [username] to this repository"**
8. El colaborador recibirá una invitación por email

#### Opción B: Usar el método de Fork + Pull Request
Si prefieres un flujo más controlado:
1. Los colaboradores hacen **Fork** del repositorio
2. Trabajan en su copia personal
3. Envían **Pull Requests** con sus cambios
4. Tú revisas y apruebas los cambios antes de fusionarlos

#### Comandos útiles para colaboradores invitados:
```bash
# Clonar el repositorio (solo la primera vez)
git clone https://github.com/rortiz04/cmuc-website.git
cd cmuc-website

# Crear una rama para trabajar
git checkout -b mi-nueva-funcionalidad

# Hacer cambios, agregar y commitear
git add .
git commit -m "feat: agregar nueva funcionalidad"

# Subir la rama al repositorio
git push origin mi-nueva-funcionalidad

# Crear Pull Request desde GitHub web interface
```

#### ⚠️ Importante para colaboradores:
- Nunca trabajar directamente en la rama `main`
- Siempre crear una rama nueva para cada funcionalidad
- Escribir mensajes de commit descriptivos
- Probar los cambios antes de hacer Push
- Revisar el archivo `CONTRIBUTING.md` para las guías de estilo

## 🔧 Próximos pasos recomendados

1. **Configurar GitHub Pages** (si quieres hosting gratuito)
2. **Agregar badges** al README (build status, license, etc.)
3. **Configurar Issues templates** para bug reports
4. **Agregar GitHub Actions** para CI/CD
5. **Configurar dependabot** para actualizaciones automáticas

## 📞 ¿Necesitas ayuda?

Si tienes problemas con algún paso, revisa:
- La documentación de GitHub
- Los mensajes de error específicos
- El archivo CONTRIBUTING.md para más detalles

¡Tu proyecto ya está listo para ser compartido con el mundo! 🎉
