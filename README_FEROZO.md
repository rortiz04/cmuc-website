# Despliegue en Ferozo (Migración a PHP)

## Estructura recomendada
Colocar los archivos en el public root:
```
index.php (próximo paso: convertir index.html)
static/ (carpeta existente)
```

## Paso 1: Instalar PHPMailer localmente y subir vendor/
Si puedes usar Composer localmente:
```
composer require phpmailer/phpmailer
```
Esto generará `vendor/` y `composer.json`. Sube ambas cosas al hosting.

Si no tienes Composer, descarga release ZIP de PHPMailer y coloca la carpeta `src/` en `static/assets/mail/phpmailer/` y ajusta el `require_once`.

## Paso 2: Configuración SMTP
Copia `static/assets/mail/config.sample.php` a `config.php` y edita:
```php
return [
  'smtp_host' => 'smtp.gmail.com',
  'smtp_port' => 465,
  'smtp_secure' => 'ssl', // o 'tls' con puerto 587
  'smtp_user' => 'USUARIO',
  'smtp_pass' => 'APP_PASSWORD',
  'from_email' => 'USUARIO',
  'from_name' => 'Sitio CMUC',
  'to_email' => 'colegiomayorcba@gmail.com',
  'to_name' => 'CMUC Contacto',
];
```
Usar “App Password” de Gmail (activar 2FA y generar contraseña de aplicación) o credenciales SMTP de Ferozo.

## Paso 3: Convertir index.html a index.php
Reemplazar expresiones Flask `{{ url_for('static', filename='...') }}` por rutas relativas:
```
static/css/styles.css
static/img/portfolio/CMUCblancof4f6ff.png
static/assets/... etc.
```
Asegurarse que `<script src="static/assets/mail/quick_contact.js"></script>` apunta al nuevo JS.

## Paso 4: Probar formulario
1. Abrir el sitio en hosting.
2. Abrir consola (F12) y enviar mensaje de prueba.
3. Si hay error 500 revisar log de errores de PHP (panel Ferozo) y confirmar que `config.php` existe y permisos 640/600.

## Paso 5: Seguridad básica
- Mantener `config.php` fuera de repositorio público (agregar a .gitignore si se versiona).
- Limitar origen: reemplazar `header('Access-Control-Allow-Origin: *')` por dominio real cuando publiques.
- Posible añadir reCAPTCHA v3 si aumenta el spam.

## Paso 6: Retirar backend Python
Archivar o borrar: `server.py`, `requirements.txt`, `deploy.py`, `build.py`. Añadir nota en README.

## Opcional: Mejoras
- Guardar mensajes en archivo CSV (apéndice) como backup.
- Enviar auto-respuesta al usuario (`$mail->addAddress` duplicado y/o segundo PHPMailer).
- reCAPTCHA.

## Troubleshooting
| Problema | Causa probable | Solución |
|----------|----------------|----------|
| 500 genérico | Falta vendor PHPMailer | Subir vendor o ajustar require |
| 422 Email inválido | Formato incorrecto | Revisar campo email | 
| 429 | Demasiados envíos seguidos | Esperar 1 min |
| No llega correo | SMTP bloqueado | Probar puerto 587 + tls, revisar credenciales |

## Comandos Composer (local)
```
composer init (si no existe)
composer require phpmailer/phpmailer
```

---
Actualizado: Sept 2025
