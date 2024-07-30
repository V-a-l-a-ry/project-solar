// static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    const purchaseButtons = document.querySelectorAll('.purchase-button');

    purchaseButtons.forEach(button => {
        button.addEventListener('click', function() {
            const panelName = this.getAttribute('data-panel-name');
            window.location.href = `/payment_methods/?panel=${encodeURIComponent(panelName)}`;
        });
    });
});
