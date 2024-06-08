import requests
import json
import time
import websocket
from binance.client import Client

host = "https://api3.binance.com"
proxies = {
    "http": "http://192.168.100.120:7890",
    "https": "https://192.168.100.120:7890"
}

def get_btc_price(symbols):
    
    # get_symbol_ticker(self, **params)
    params = "symbols=" + requests.utils.quote(symbols)

    response = requests.get(host + "/api/v3/ticker/price?"+params, proxies=proxies)
    
    if response.status_code == 200:
        price_info = response.json()
        print_info = ""
        for item in price_info:
            print_info += item["symbol"][:-4] + " " + item["price"].rstrip('0') + "  "

        return str(print_info)
    if response.status_code == 429:
        print("recv http code 429!")
        exit()
    else:
        print(f"Failed to retrieve data: HTTP {response.status_code}")
        return None

def get_price_by_client(symbols):
    client = Client(requests_params={'proxies': proxies})
    # res = client.get_exchange_info()
    # print(client.response.headers)
    while True:
        try:
            data = client.get_symbol_ticker(symbols=symbols)
            # print(type(data))
            # print(type(data[0]))
            print_info = ""
            for item in data:
                print_info += item["symbol"][:-4] + " " + item["price"].rstrip('0') + "  "
            print(str(print_info), end='\r')
        except BinanceRequestException as e:
            print("BinanceRequestException: " + str(e))
        finally:
            time.sleep(1.1)

def main():
    # get_price_by_ws()
    
    symbols = requests.utils.quote('["BTCUSDT","ETHUSDT","BNBUSDT","SOLUSDT","NEARUSDT","RNDRUSDT","COMPUSDT","SNXUSDT","SCUSDT"]')
    get_price_by_client(symbols)

    # while True:
    #     data = get_btc_price(symbols)
    #     print(data, end='\r')
    #     time.sleep(1)
    return 0

if __name__ == "__main__":
    main()
