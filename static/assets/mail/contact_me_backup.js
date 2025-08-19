$(function () {
    // Función para validar el formulario
    function validateForm() {
        var name = $("#name").val().trim();
        var email = $("#email").val().trim();
        var phone = $("#phone").val().trim();
        var message = $("#message").val().trim();
        
        if (!name || !email || !phone || !message) {
            showMessage("Por favor completa todos los campos", "danger");
            return false;
        }
        
        // Validar email
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            showMessage("Por favor ingresa un email válido", "danger");
            return false;
        }
        
        return true;
    }
    
    // Función para mostrar mensajes
    function showMessage(message, type) {
        $("#success").html(`<div class='alert alert-${type}'>`);
        $("#success > .alert").html(
            `<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button>`
        );
        $("#success > .alert").append(`<strong>${message}</strong>`);
        $("#success > .alert").append("</div>");
    }
    
    // Botón WhatsApp
    $("#sendWhatsAppButton").click(function(e) {
        e.preventDefault();
        
        if (!validateForm()) {
            return;
        }
        
        var name = $("#name").val();
        var email = $("#email").val();
        var phone = $("#phone").val();
        var message = $("#message").val();
        
        // Crear mensaje para WhatsApp
        var whatsappMessage = `*Nuevo contacto CMUC*%0A%0A` +
                            `*Nombre:* ${name}%0A` +
                            `*Email:* ${email}%0A` +
                            `*Teléfono:* ${phone}%0A` +
                            `*Mensaje:*%0A${message}%0A%0A` +
                            `_Enviado desde colegiomayorcba.com_`;
        
        // Abrir WhatsApp
        var whatsappURL = `https://wa.me/5493534795639?text=${whatsappMessage}`;
        window.open(whatsappURL, '_blank');
        
        showMessage("Redirigiendo a WhatsApp...", "success");
        $("#contactForm").trigger("reset");
    });
    
    // Botón Email
    $("#sendEmailButton").click(function(e) {
        e.preventDefault();
        
        if (!validateForm()) {
            return;
        }
        
        var name = $("#name").val();
        var email = $("#email").val();
        var phone = $("#phone").val();
        var message = $("#message").val();
        
        $(this).prop("disabled", true);
        $(this).html('<i class="fas fa-spinner fa-spin"></i> Enviando...');
        
        $.ajax({
            url: "/send_message",
            type: "POST",
            data: {
                name: name,
                phone: phone,
                email: email,
                message: message,
            },
            cache: false,
            success: function () {
                showMessage("¡Mensaje enviado correctamente por email!", "success");
                $("#contactForm").trigger("reset");
                $("#sendEmailButton").prop("disabled", false);
                $("#sendEmailButton").html('<i class="fas fa-envelope"></i> Enviar por Email');
            },
            error: function () {
                showMessage("Error al enviar el email. Por favor intenta de nuevo.", "danger");
                $("#sendEmailButton").prop("disabled", false);
                $("#sendEmailButton").html('<i class="fas fa-envelope"></i> Enviar por Email');
            }
        });
    });
    
    // Mantener validación original para compatibilidad
    $(
        "#contactForm input,#contactForm textarea"
    ).jqBootstrapValidation({
        preventSubmit: true,
        submitError: function ($form, event, errors) {
            // additional error messages or events
        },
        submitSuccess: function ($form, event) {
            event.preventDefault();
        },
        filter: function () {
            return $(this).is(":visible");
        }
    });
    
    // Limpiar mensajes cuando se hace focus en el nombre
    $("#name").focus(function () {
        $("#success").html("");
    });
});
