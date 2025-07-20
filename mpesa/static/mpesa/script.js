
const payButton = document.getElementById('stk-pay-button');
const paymentNumber = document.getElementById('payment-phone')
const escortNumber = document.getElementById('escort-phone')

const paymentForm = document.getElementById('stk-pay-form')

payButton.addEventListener('click', (e)=> {
    e.preventDefault()
    if (!isValidFormat(escortNumber.value) || !isValidFormat(paymentNumber.value)) {
        alert('Phone number should not start with "0" or "+". \ Accepted format is "254723654723" where the first 3 digits are country code')
        return;
    }
    paymentForm.submit()
})


function isValidFormat(number) {
    
    const cleaned = number.replace(/\D/g, '');
    const regex = /^[1-9]\d{1,3}[1-9]\d{6,14}$/;

    return regex.test(cleaned);
}

