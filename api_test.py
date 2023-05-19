import requests

PATH = 'https://api.polygonscan.com/api'
ADDRESS = '0xf57C5d032a0Eb0b9e9a2081F4b7992bed90336D3'
CONTRACT = '0xAe07B360cF41C8971F6c544620A6ed428Ff3a661'
API_KEY = 'Dummy'

response = requests.get(f'{PATH}?module=account&action=tokentx&contractaddress={CONTRACT}&address={ADDRESS}&startblock=0&endblock=99999999&page=1&offset=5&sort=asc&apikey={API_KEY}')

response_value = response.json()

print(response_value['result'][0])


