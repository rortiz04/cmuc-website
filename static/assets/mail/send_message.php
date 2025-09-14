<?php
// send_message.php - endpoint JSON para contacto rápido
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *'); // Ajustar si se necesita restringir
header('X-Content-Type-Options: nosniff');

$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
if ($method !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Método no permitido']);
    exit;
}

// Cargar config
$configPath = __DIR__ . '/config.php';
if (!file_exists($configPath)) {
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Falta config.php']);
    exit;
}
$config = require $configPath;

// Validaciones básicas
$fields = [
    'name' => FILTER_SANITIZE_FULL_SPECIAL_CHARS,
    'email' => FILTER_VALIDATE_EMAIL,
    'message' => FILTER_UNSAFE_RAW,
];

$input = [];
foreach ($fields as $field => $filter) {
    $value = trim($_POST[$field] ?? '');
    if ($field === 'email') {
        if (!filter_var($value, $filter)) {
            http_response_code(422);
            echo json_encode(['success' => false, 'error' => 'Email inválido']);
            exit;
        }
    } else {
        if ($value === '') {
            http_response_code(422);
            echo json_encode(['success' => false, 'error' => 'Campos incompletos']);
            exit;
        }
    }
    $input[$field] = $value;
}

// Anti-spam (honeypot opcional)
if (!empty($_POST['telefono'])) { // Campo que no existe en el formulario real
    http_response_code(200);
    echo json_encode(['success' => true]);
    exit;
}

// Rate limit muy simple por IP (archivo temporal)
$ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
$tmpDir = sys_get_temp_dir();
$rlFile = $tmpDir . '/cmuc_contact_' . md5($ip);
$now = time();
$window = 60; // 1 minuto
$maxRequests = 5;
$requests = [];
if (file_exists($rlFile)) {
    $raw = file_get_contents($rlFile);
    $requests = array_filter(array_map('intval', explode("\n", $raw)), function($ts) use ($now, $window) {return $ts >= ($now - $window);});
}
$requests[] = $now;
if (count($requests) > $maxRequests) {
    http_response_code(429);
    echo json_encode(['success' => false, 'error' => 'Demasiados intentos, espera un momento.']);
    exit;
}
file_put_contents($rlFile, implode("\n", $requests));

// Enviar email con PHPMailer
require_once __DIR__ . '/../../../vendor/autoload.php'; // Composer autoload esperado en mismo folder o ajustar ruta

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

try {
    $mail = new PHPMailer(true);
    $mail->CharSet = 'UTF-8';
    $mail->isSMTP();
    $mail->Host = $config['smtp_host'];
    $mail->SMTPAuth = true;
    $mail->Username = $config['smtp_user'];
    $mail->Password = $config['smtp_pass'];
    $mail->SMTPSecure = $config['smtp_secure'];
    $mail->Port = $config['smtp_port'];

    $mail->setFrom($config['from_email'], $config['from_name']);
    $mail->addAddress($config['to_email'], $config['to_name']);
    $mail->addReplyTo($input['email'], $input['name']);

    $subject = 'Nuevo contacto desde el sitio CMUC';
    $bodyText = "Nuevo mensaje de contacto:\n\n" .
        "Nombre: {$input['name']}\n" .
        "Email: {$input['email']}\n" .
        "Mensaje:\n{$input['message']}\n";

    $mail->isHTML(false);
    $mail->Subject = $subject;
    $mail->Body = $bodyText;

    $mail->send();
    echo json_encode(['success' => true]);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'No se pudo enviar el correo']);
}
