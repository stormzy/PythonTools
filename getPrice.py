import requests
import json
import time
import websocket
import sys
from binance.client import Client

host = "https://api3.binance.com"
proxies = {
    "http": "http://192.168.100.100:7890",
    "https": "https://192.168.100.100:7890"
}

def get_price_by_client(symbols):
    client = Client(requests_params={'proxies': proxies})
    data = client.get_symbol_ticker(symbols=symbols)
    print_info = ""
    for item in data:
        print_info += item["symbol"][:-4] + " " + item["price"].rstrip('0') + "  "
    print(str(print_info))

def main():
    # get_price_by_ws()
    if len(sys.argv) < 2:
        print("too few args.")
        return
    symbol_list = []
    for i in range(1, len(sys.argv)):
        symbol_list.append(sys.argv[i])
    
    symbol_str = ""
    for symbol in symbol_list:
        if symbol_str != "":
            symbol_str += ','
        symbol_str += '"{}USDT"'.format(symbol)
    symbol_str = '[{}]'.format(symbol_str)

    symbols = requests.utils.quote(symbol_str.upper())
    get_price_by_client(symbols)

    # while True:
    #     data = get_btc_price(symbols)
    #     print(data, end='\r')
    #     time.sleep(1)
    return 0

if __name__ == "__main__":
    main()
