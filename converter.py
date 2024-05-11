import requests

API_ACCESS_KEY = '3560d97784d6a5b4a2dca53ea6df275e'
BASE_URL = f"http://api.exchangerate.host/live?access_key={API_ACCESS_KEY}"

# API call that returns 'quotes' - all of the currency names & exchange rates in {}
# ex. of response: "USDAED": 3.672982"

def get_exchange_rates():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            # list comprehension to take out usd from every quote
            output = {key[3:]: value for key, value in data.get('quotes', {}).items()}
            return output
    return {}


def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates()
    
    # checks if exchange rates are available and both input currencies 
    if rates and from_currency in rates and to_currency in rates: 
        exchange_rate = rates[to_currency]
        # Converts the amount from the source currency to the target currency
        converted_amount = int(amount) * exchange_rate
        return round(converted_amount, 2)
    # if not valid, return none
    return None

# validates whether the input currency type is supported
def validate_currency_type(currency_type):
    rates = get_exchange_rates()
    if rates:
        # checks if the input currency type is included in the list of supported currencies
        return currency_type.upper() in rates
    # returns false if exchange rates are unavailable
    return False
