import json
import requests

# Get your Polygon API key from https://polygon.io/
API_KEY = "N6oezGlLcHzxPhi34z2F6wKV0Ql9nG87"

# Get the symbol of the stock that you want to track
SYMBOL = "AAPL"

# Get the real-time price of the stock
url = "https://api.polygon.io/v2/aggs/ticker/" + SYMBOL + "/range/1/month/2024-01-01/2024-06-13"
response = requests.get(url, headers={"Authorization": "Bearer " + API_KEY})

print("status code: ", response.status_code)
print("result", response.json())
# Check if the response is successful
if response.status_code == 200:
    price = response.json()["price"]
else:
    print("Error:", response.status_code)

# Print the real-time price of the stock
print("The current price of AAPL is $", price)

# Get the real-time volume of the stock
url = "https://api.polygon.io/v2/tickers/" + SYMBOL + "/volume"
response = requests.get(url, headers={"Authorization": "Bearer " + API_KEY})

# Check if the response is successful
if response.status_code == 200:
    volume = response.json()["volume"]
else:
    print("Error:", response.status_code)

# Print the real-time volume of the stock
print("The current volume of AAPL is", volume)

# Get the real-time bid and ask prices of the stock
url = "https://api.polygon.io/v2/tickers/" + SYMBOL + "/book"
response = requests.get(url, headers={"Authorization": "Bearer " + API_KEY})

# Check if the response is successful
if response.status_code == 200:
    bid = response.json()["bid"]
    ask = response.json()["ask"]
else:
    print("Error:", response.status_code)

# Print the real-time bid and ask prices of the stock
print("The current bid price of AAPL is $", bid)
print("The current ask price of AAPL is $", ask)

# Get the real-time 52-week high and low prices of the stock
url = "https://api.polygon.io/v2/tickers/" + SYMBOL + "/stats"
response = requests.get(url, headers={"Authorization": "Bearer " + API_KEY})

# Check if the response is successful
if response.status_code == 200:
    week_high_52 = response.json()["52_week_high"]
    week_low_52 = response.json()["52_week_low"]
else:
    print("Error:", response.status_code)

# Print the real-time 52-week high and low prices of the stock
print("The 52-week high price of AAPL is $", week_high_52)
print("The 52-week low price of AAPL is $", week_low_52)

# Analyze the real-time data
# You can use the real-time data to analyze the stock and to make trading decisions.
# For example, you can use the real-time price to determine if the stock is overbought or oversold.
# You can also use the real-time volume to determine if the stock is seeing increased or decreased trading activity.
