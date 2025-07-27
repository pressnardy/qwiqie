from mpesa.models import Payment

def save_payment(item):
    payment_details = {}
    for i in item:
        payment_details[i['Name']] = i['Value']

    payment = Payment(
        amount=payment_details['Amount'],
        mpesa_receipt_number=payment_details['MpesaReceiptNumber'],
        phone_number=payment_details['PhoneNumber'],
        transaction_date=payment_details['TransactionDate']

    )
    payment.save()
    print(payment)
    
    