import requests
import json

url = 'https://api.exchangerate.host/latest'
# url = 'https://api.exchangerate.host/convert?from=EUR&to=USD'
response = requests.get(url)
data = response.json()
pretty_data = json.dumps(data,indent=4)
print(pretty_data)

# your_json = '["foo", {"bar": ["baz", null, 1.0, 2]}]'
# >>> parsed = json.loads(your_json)
# >>> print(json.dumps(parsed, indent=4))