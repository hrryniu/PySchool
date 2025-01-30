import requests #biblioteka, która pomaga połączyć się z publicznym api
from pathlib import Path
response = requests.get(f'https://api.dicebear.com/9.x/pixel-art/svg')

Path('./avatars').mkdir(exist_ok=True)
with open('./avatars/avatar.svg' , 'wb') as file:
    file.write(response.content)
