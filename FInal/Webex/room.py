import requests

access_token = 'MzkwYTljZDMtZjgwNy00ZjEyLTk3MjUtYjYwZDE4NDE4ZTdjNjQ2NGM5YTgtNGI5_P0A1_9a8a306f-5965-407f-a4b3-63b85af39c54'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'WebEx SE Teams group (L1 and L2 SEs)'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
