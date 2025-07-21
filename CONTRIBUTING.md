# Contribuir al Proyecto CMUC

¡Gracias por tu interés en contribuir al sitio web del Colegio Mayor Universitario de Córdoba!

## 🤝 Cómo Contribuir

### Reportar Bugs

Si encuentras un error, por favor:

1. Verifica que el bug no haya sido reportado anteriormente en [Issues](../../issues)
2. Crea un nuevo issue con:
   - Descripción clara del problema
   - Pasos para reproducir el error
   - Comportamiento esperado vs actual
   - Screenshots si es aplicable
   - Información del navegador/sistema

### Sugerir Mejoras

Para proponer nuevas funcionalidades:

1. Revisa los issues existentes para evitar duplicados
2. Crea un nuevo issue con el label "enhancement"
3. Describe claramente la funcionalidad propuesta
4. Explica por qué sería útil para el proyecto

### Enviar Pull Requests

1. **Fork** el repositorio
2. Crea una rama desde `main`:
   ```bash
   git checkout -b feature/mi-nueva-funcionalidad
   ```
3. Realiza tus cambios siguiendo las convenciones del proyecto
4. Asegúrate de que el código funcione correctamente
5. Commit tus cambios con mensajes descriptivos:
   ```bash
   git commit -m "feat: agregar funcionalidad de galería de fotos"
   ```
6. Push a tu fork:
   ```bash
   git push origin feature/mi-nueva-funcionalidad
   ```
7. Crea un Pull Request con:
   - Título descriptivo
   - Descripción detallada de los cambios
   - Referencias a issues relacionados

## 📝 Convenciones de Código

### HTML/CSS
- Usar indentación de 4 espacios
- Nombres de clases descriptivos en español
- Comentarios para secciones importantes

### Python
- Seguir PEP 8
- Usar docstrings para funciones
- Nombres de variables y funciones en inglés
- Comentarios en español cuando sea necesario

### Commits
Usar el formato de [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` nuevas funcionalidades
- `fix:` corrección de bugs
- `docs:` cambios en documentación
- `style:` cambios de formato (espacios, punto y coma, etc.)
- `refactor:` cambios de código que no agregan funcionalidad ni corrigen bugs
- `test:` agregar o modificar tests
- `chore:` tareas de mantenimiento

### Ejemplo:
```
feat: agregar modal para galería de fotos

- Implementar modal responsivo para mostrar fotos en tamaño completo
- Agregar navegación entre fotos con flechas
- Incluir descripción de cada foto
- Cerrar modal con ESC o click fuera del contenido

Closes #123
```

## 🧪 Testing

Antes de enviar tu PR:

1. Verifica que el servidor Flask inicie correctamente
2. Prueba la funcionalidad en diferentes navegadores
3. Verifica que el diseño sea responsivo
4. Prueba el formulario de contacto (si tienes configuración de email)

## 📞 Contacto

Si tienes preguntas sobre cómo contribuir:

- Abre un issue con el label "question"
- Contacta al mantenedor del proyecto
- Email: colegiomayorcba@gmail.com

## 🙏 Reconocimientos

Todos los contribuidores serán reconocidos en el proyecto. ¡Gracias por ayudar a mejorar el sitio web del CMUC!

---

**Código de Conducta**: Este proyecto sigue un código de conducta. Al participar, te comprometes a mantener un ambiente respetuoso y colaborativo.
