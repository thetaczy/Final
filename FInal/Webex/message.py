import requests

access_token = 'MzkwYTljZDMtZjgwNy00ZjEyLTk3MjUtYjYwZDE4NDE4ZTdjNjQ2NGM5YTgtNGI5_P0A1_9a8a306f-5965-407f-a4b3-63b85af39c54'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYzUxMWY3OTAtZTJjMC0xMWVjLTkwMjUtN2QzNTY2ZTVjNzI5'

message = '***Announcement of Manual Configuration Changes Please See the Attached Files***'

url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
