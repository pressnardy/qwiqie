import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer PJeaGgc14KmClbOf3WeM0ch5vCFy'
}

body = {    
   "Body": {        
      "stkCallback": {            
         "MerchantRequestID": "29115-34620561-1",            
         "CheckoutRequestID": "ws_CO_191220191020363925",            
         "ResultCode": 0,            
         "ResultDesc": "The service request is processed successfully.",            
         "CallbackMetadata": {                
            "Item": [{                        
               "Name": "Amount",                        
               "Value": 3000.00                    
            },                    
            {                        
               "Name": "MpesaReceiptNumber",                        
               "Value": "NLJ7RT61SV"                    
            },                    
            {                        
               "Name": "TransactionDate",                        
               "Value": 20191219102115                    
            },                    
            {                        
               "Name": "PhoneNumber",                        
               "Value": 254708374149                    
            }]            
         }        
      }    
   }
}

body = json.dumps(body)
response = requests.request(
    "POST", "https://cosmic-midge-presumably.ngrok-free.app/payments/callback", headers = headers, data=body)
# print(response.text.encode('utf8'))

