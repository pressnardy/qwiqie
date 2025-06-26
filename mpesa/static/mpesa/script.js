
const payButton = document.getElementById('stk-pay-button');
const paymentNumber = document.getElementById('payment-phone')
const escortNumber = document.getElementById('escort-phone')

const paymentForm = document.getElementById('stk-pay-form')

payButton.addEventListener('click', (e)=> {
    e.preventDefault()
    if (!isValidFormat(escortNumber.value) || !isValidFormat(paymentNumber.value)) {
        alert('wrong format for phone number: Enter phone number thats does not start with 0 or + e.g 254723654723')
        return;
    }
    paymentForm.submit()
})


function isValidFormat(number) {
    
    const cleaned = number.replace(/\D/g, '');
    const regex = /^[1-9]\d{1,3}[1-9]\d{6,14}$/;

    return regex.test(cleaned);
}

