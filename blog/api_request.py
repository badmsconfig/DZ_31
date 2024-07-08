import requests
import pprint


#esponse = requests.get('http://127.0.0.1:8000/categories/categories/')
# response = requests.get('http://127.0.0.1:8000/api/v0/tags/', auth=('anlord', 'natalisa'))
#
#
# pprint.pprint(response.json())

token = '5f3527e704ee279a0d19b78c91b944da28ca6d74'
headers = {'Authorization': f'Token {token}'}
#response = requests.get('http://127.0.0.1:8000/api/v0/tags/')
response = requests.get('http://127.0.0.1:8000/api/v0/tags/', headers=headers)
pprint.pprint(response.json())