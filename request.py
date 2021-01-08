import requests

response=requests.get("https://v6.exchangerate-api.com/v6/766d3191664b8a0cf66adbe8/latest/USD")
responsej = response.json()
rates = responsej['conversion_rates']
print(rates)
