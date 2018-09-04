import requests
import json
response=requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
data=response.json()
del data['quoteLink']
del data['senderLink']
del data['senderName']
print(json.dumps(data))
