// static/js/global.js

document.addEventListener('DOMContentLoaded', function() {
    // Inicializa o Bootstrap Bundle (para Navbar, Dropdowns, etc.)
    
    // Funcao simples para fechar alertas do Django apos um tempo
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alertElement) {
            // Usa o metodo do Bootstrap para fechar o alerta de forma suave
            var bsAlert = bootstrap.Alert.getOrCreateInstance(alertElement);
            if (bsAlert) {
                bsAlert.close();
            }
        });
    }, 6000); // Fecha apos 6 segundos
});