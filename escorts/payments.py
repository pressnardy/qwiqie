from datetime import datetime
import base64
import requests

CONSUMER_KEY = 'QrvwdFXEAALwSSUXHXnsfLVIXmAOPlP4we7p64CODndufV6B'
CONSUMER_SECRETE = "Ywe1IrV59Dxxb3zAThYG3ctCPmGUfzq1xbUPvzDGo1WCgGEysfajic2fhojgzYQ6"
SANDBOX_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
TIMESTAMP = datetime.now().strftime('%Y%m%d%H%M%S')
SHORTCODE = "174379"
PASSKEY = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
STK_PASSWORD = base64.b64encode((SHORTCODE + PASSKEY + TIMESTAMP).encode()).decode()


def get_access_token(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRETE, url=SANDBOX_URL):
    encoded_credentials = base64.b64encode(f"{consumer_key}:{consumer_secret}".encode()).decode()
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers).json()
        return str(response["access_token"])
    except Exception as e:
        raise Exception("Failed to get access token: " + str(e)) 
    

ACCESS_TOKEN = get_access_token()
SANDBOX_URL = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

LIVE_URL = 'https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

HEADERS = {
            'Authorization': 'Bearer ' + ACCESS_TOKEN,
            'Content-Type': 'application/json'
        }

REQUEST_BODY = {
            "BusinessShortCode": SHORTCODE,
            "Password": STK_PASSWORD,
            "Timestamp": TIMESTAMP,
            "TransactionType": "CustomerPayBillOnline", #till "CustomerBuyGoodsOnline"
            "Amount": "10",
            "PartyA": "254708374149",
            "PartyB": SHORTCODE,
            "PhoneNumber": "254708374149",
            "CallBackURL": 'https://cosmic-midge-presumably.ngrok-free.app/callback',
            "AccountReference": "account",
            "TransactionDesc": "test"
        }

def send_stk_push(url=SANDBOX_URL, request_body=REQUEST_BODY, headers=HEADERS):
    try:
        response = requests.post(url, json=request_body, headers=headers).json()
    except Exception as e:
        response = 'Error:', str(e)
    return response

if __name__ == "__main__":
    print(send_stk_push())



