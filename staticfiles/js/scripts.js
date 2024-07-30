// static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    const purchaseButtons = document.querySelectorAll('.purchase-button');
    purchaseButtons.forEach(button => {
        button.addEventListener('click', function() {
            const panel = this.getAttribute('data-panel');
            window.location.href = `/payment_methods/?panel=${encodeURIComponent(panel)}`;
        });
    });
});
