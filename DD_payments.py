import requests, simplejson

def request_addAccount():
    url = "http://openmobileglobal.com/openmobile/accountChecker/AddAccount"
    data = {
        'authentication'='ExampleExampleExample==',
        'name': 'Mr.Joe Bloggs' ,
        'bank_account_title': 'MR',
        'bank_account_forename': 'JOE',
        'bank_account_surname' :'BLOGGS',
        'sort_code': 121212,
        'account_no': 12345678,
        'bacs_account_ref': 'REF123',
        'plan_frequency_type':'M',
        'regular_amount':15.00,
        'first_amount':20.00,
        'last_amount':25.00,
        'start_year': 2012,
        'start_month': 10,
        'start_day': 1,
        'num_debits':5,
        'plan_interval_1':1,
        'plan_interval_2':1,
        'client_name': 'MyClient',
        'custom1':'Ford',
        'custom2':'Focus',
        'custom3':'Blue’
    }
    # sending post request and saving the response as response object
    response = requests.post(url, data = data)
    # converting unicode object to json
    result = simplejson.loads(response.text)
    return result
