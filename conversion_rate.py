import requests

from datetime import date, timedelta, datetime
from settings import CONVERSION_RATE_QUERY_STRING, CONVERSION_RATE_URI
from secret import CONVERSION_RATE_API_KEY


def GetCurrencyXChangeRate():
    payload = ""
    data = []
    yesterday = date.today() + timedelta(days= -1)
    
    url = CONVERSION_RATE_URI + yesterday.strftime("%Y-%m-%d")
    
    currency_xchange_response = requests.request("GET", url, data=payload, headers=CONVERSION_RATE_API_KEY, params=CONVERSION_RATE_QUERY_STRING)
    response = currency_xchange_response.json()
    
    # response = {
    #     "success": True,
    #     "timestamp": 1672617599,
    #     "historical": True,
    #     "base": "USD",
    #     "date": "2023-01-01",
    #     "rates": {
    #         "EUR": 0.934185,
    #         "GBP": 0.826446,
    #         "RON": 4.63494
    #     }
    # }
    
    rates = response["rates"]

    for key in rates:
        data.append({"Values": [key, date.strftime("%Y%m%d"), rates[key]]})

    return data
