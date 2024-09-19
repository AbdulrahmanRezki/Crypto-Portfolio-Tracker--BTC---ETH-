from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# Fetch Bitcoin price
def get_btc_price():
    urlBTC = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": "API KEY INSERT HERE"
    }
    responseBTC = requests.get(urlBTC, headers=headers)
    objBTC = json.loads(responseBTC.text)
    return objBTC["bitcoin"]["usd"]

# Fetch Ethereum price
def get_eth_price():
    urlETH = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": "API KEY INSERT HERE"
    }
    responseETH = requests.get(urlETH, headers=headers)
    objETH = json.loads(responseETH.text)
    return objETH["ethereum"]["usd"]

@app.route('/', methods=['GET', 'POST'])
def index():
    btc_value = 0
    eth_value = 0
    btc_total = 0
    eth_total = 0
    
    if request.method == 'POST':
        # Get the user inputs for Bitcoin and Ethereum amounts
        btc_value = float(request.form['btcValue'])
        eth_value = float(request.form['ethValue'])

        # Fetch current prices
        btc_price = get_btc_price()
        eth_price = get_eth_price()

        # Calculate portfolio value
        btc_total = btc_value * btc_price
        eth_total = eth_value * eth_price
    
    return render_template('index.html', btc_total=btc_total, eth_total=eth_total)

if __name__ == '__main__':
    app.run(debug=True)
