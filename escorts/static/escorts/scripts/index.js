
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
        const phoneNumber = card.dataset.phoneNumber; 
        if (phoneNumber) {
            window.location.href = `/escorts/view/${phoneNumber}/`;
        }
    });
});

