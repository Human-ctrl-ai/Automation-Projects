import requests
# Syntax for get req...
# requests.get(url, params={key: value}, **kwargs) # It returns a response object.
response = requests.get("https://www.google.com/search?q=hello") #  The GET method sends the encoded user information appended to the page request. The page and the encoded information are separated by the ‘?’ character.
print(response)
print(response.status_code)
print(response.content)
