from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mpesa import mpesa_api
import json
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm
from .models import Payment
from escorts.models import Escort

# @login_required
def push_stk(request):
    context = {}
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_phone = str(form.cleaned_data['payment_phone'])
            amount = str(form.cleaned_data['amount'])
            escort_phone = str(form.cleaned_data['escort_phone'])
            response_code = mpesa_api.send_stk_push(payment_phone, amount, escort_phone)['ResponseCode']
            if response_code == '0':
                return render(request, 'mpesa/processing.html')
            return render(request, 'mpesa/error.html')
    context['form'] = PaymentForm()
    return render(request, 'mpesa/stk_pay.html', context)


@csrf_exempt
def get_callback(request):
    print("Callback received")  # Debugging line to confirm callback is hit
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            print("Callback Body:", json.dumps(body, indent=4))  # Print the body for debugging

            result_code = body.get("Body", {}).get("stkCallback", {}).get("ResultCode")
            result_desc = body.get("Body", {}).get("stkCallback", {}).get("ResultDesc")
            callback_metadata = body.get("Body", {}).get("stkCallback", {}).get("CallbackMetadata", {})

            # Log or process the extracted data
            print(f"Result Code: {result_code}")
            print(f"Result Description: {result_desc}")
            print(f"Callback Metadata: {callback_metadata}")

            # Respond to M-Pesa with a success message
            return JsonResponse({"message": "Callback received successfully"})
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

def test_post(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        print(f"Received amount: {amount}")  # Debugging line to confirm amount is received
        return HttpResponse(f"Amount received: {amount}")
    return render(request, 'mpesa/testpost.html')  # Render the form for testing