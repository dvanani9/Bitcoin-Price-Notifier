import requests
import keys
import pandas as pd
from time import sleep

def get_rates(base_currency='EUR', assets='BTC,ETH,XRP'):
    url = 'https://api.nomics.com/v1/currencies/ticker'

    payload = {'key' : keys.nomics_api_key, 'convert' : base_currency, 'ids': assets, 'interval' : '1d'}

    response = requests.get(url, params=payload)

    data = response.json()


    crypto_currecny, crypto_price, crypto_timestamp = [], [], []

    for asset in data:
        crypto_currecny.append(asset['currency'])
        crypto_price.append(asset['price'])
        crypto_timestamp.append(asset['price_timestamp'])


    raw_data = {
        'assets' : crypto_currecny,
        'rates': crypto_price,
        "timestamp": crypto_timestamp 

        }

    df = pd.DataFrame(raw_data)
    return df
    
 
def set_alert(dataframe, asset, alert_high_price):
    crypto_value = float(dataframe[dataframe['assets'] == asset]['rates'].item())
    
    
    details = f'{asset}: {crypto_value}, Target: {alert_high_price}'

    if crypto_value>= alert_high_price:
        print(details + '<<TARGET VALUE REACHED!!')

    else:
        print(details)


#Alert While Loop

loop = 0
while True:
    print(f'.............({loop}).............')

    try:
        df = get_rates()

        set_alert(df, 'BTC', 50300.50)
        set_alert(df, 'ETH', 1800.80)
        set_alert(df, 'XRP', .870)

    except Exception as e:
        print('couldnt retrieve the data...trying again')

        loop+=1
        sleep(30)





























    






