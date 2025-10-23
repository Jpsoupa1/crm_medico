// static/js/patient_list.js

document.addEventListener('DOMContentLoaded', function() {
    
    // Torna a linha da tabela clicavel para navegacao rapida
    const patientRows = document.querySelectorAll('.patient-row');
    
    patientRows.forEach(row => {
        row.addEventListener('click', function(event) {
            // Ignora cliques em botoes ou links de acao (Editar/Deletar)
            if (event.target.closest('.btn') || event.target.closest('a:not(.patient-link)')) {
                return; 
            }
            
            // Redireciona para o link de detalhes
            const detailLink = this.querySelector('.patient-link');
            if (detailLink) {
                window.location.href = detailLink.href;
            }
        });
    });
    
    // Implementacao futura: Logica de busca em tempo real aqui
    // const searchInput = document.getElementById('search-input');
    // searchInput.addEventListener('keyup', filterPatients);
});