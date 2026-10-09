import requests as r
# # GET METHOD
# # Syntax for get req...
# # requests.get(url, params={key: value}, **kwargs) # It returns a response object.
# response = r.get("https://www.google.com/search?q=hello") #  The GET method sends the encoded user information appended to the page request. The page and the encoded information are separated by the ‘?’ character.
# print(response)
# print(response.status_code)
# print(response.content)

# # POST METHOD
# # Syntax for post method...
# # requests.post(url, params={key: value}, args)
# response = requests.post('https://httpbin.org/post', data={'key':'value'})
# print(response.content)
# print(response)
# print(response.status_code)
# print(response.json())

# # PUT METHOD
# # Syntax for put method...
# # requests.put(url, params={key: value}, **args)
# res = r.put('https://httpbin.org/put', data={'key':'value'})
# print("Status Code:", res.status_code)
# print()
# print("Response Body:", res.content)
# print()
# print("Response Body:", res.content.decode())








