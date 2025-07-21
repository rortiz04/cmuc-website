# server.py
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Configuración de email desde variables de entorno
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECIPIENT = os.getenv('EMAIL_RECIPIENT', 'colegiomayorcba@gmail.com')

# Configurar Ngrok solo si se proporciona el token
NGROK_TOKEN = os.getenv('NGROK_TOKEN')
if NGROK_TOKEN and os.getenv('FLASK_ENV') == 'development':
    try:
        from pyngrok import ngrok, conf
        conf.get_default().auth_token = NGROK_TOKEN
        public_url = ngrok.connect(5000).public_url
        print(f" * Ngrok tunnel en: {public_url}")
    except ImportError:
        print(" * Ngrok no está disponible. Instala con: pip install pyngrok")
    except Exception as e:
        print(f" * Error configurando Ngrok: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def handle_contact():
    try:
        # Verificar que las credenciales de email estén configuradas
        if not EMAIL_USER or not EMAIL_PASSWORD:
            print("Error: Credenciales de email no configuradas")
            return jsonify(success=False, error="Email no configurado"), 500
            
        data = request.form
        send_email({
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
            'message': data.get('message')
        })
        return jsonify(success=True)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify(success=False, error=str(e)), 500

def send_email(data):
    try:
        msg = MIMEText(
            f"Nuevo mensaje de contacto desde el sitio web CMUC:\n\n"
            f"Nombre: {data['name']}\n"
            f"Email: {data['email']}\n"
            f"Teléfono: {data['phone']}\n"
            f"Mensaje: {data['message']}"
        )
        msg['Subject'] = 'Nuevo contacto desde el sitio web CMUC'
        msg['From'] = EMAIL_USER
        msg['To'] = EMAIL_RECIPIENT

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Email enviado exitosamente")
    except Exception as e:
        print(f"Error enviando email: {str(e)}")
        raise

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)