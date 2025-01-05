import requests

# Define the URL
url = "https://task.zostansecurity.ninja/?step=1&challenge=f397080d69e2bf1d873d8004b64f796fd93bfd94fbc222708d9a6589fff7b368&timestamp=1736108996"

# Send the GET request
response = requests.get(url)

# Print the response
print(response.text)