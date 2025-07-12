import requests


response = requests.get('https://www.google.com')

# print(response.text[:300])

response = requests.get('https://www.google.com', stream=True)

# print(response.ok)
# print(response.status_code)
# print(response.raise_for_status())
# print(response.raw.read()[:100])
# print(response.request.headers['Accept-Encoding'])
# print(response.headers['Content-Encoding'])


p = {"search": "grey kitten",
     "max_results": 15}
response1 = requests.get("https://example.com/path/to/api", params=p)
print(response1.request.url)