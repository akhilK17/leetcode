import requests
import json

print('akhil')
# Make a GET request to the Treasury API
response = requests.get('https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates?sort=-record_date&limit=1&offset=0&account_type_code=T&realtime_start_date=2023-01-01')

# Parse the JSON response and extract the Treasury rate information
data = json.loads(response.text)
treasury_rate = data['data'][0]['average_interest_rate']
print('akhil')

# Write the Treasury rate information to a file
#with open('/path/to/treasury_rate.txt', 'w') as f:
#    f.write(str(treasury_rate))