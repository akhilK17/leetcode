import requests

# Define the API endpoint URL
url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
endpoint = "/v1/accounting/od/rates_of_exchange"
data = "?fields=country_currency_desc,exchange_rate,record_date&filter=record_date:gte:2023-01-01"

# Define the query parameters
params = {
    "output": "json",
    "type": "dailyTreasuryYieldCurveRate",
    "series": "10year"
}

# Send the API request
response = requests.get(url + endpoint + data, params=params)

# Parse the response JSON and extract the interest rate
print(response)
