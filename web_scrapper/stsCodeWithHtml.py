import requests
from bs4 import BeautifulSoup

# Parse the raw HTML and status code 
r = requests.get('https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=%7Bpage%7D')
# print(res.status_code)
# print(res.content)
s = BeautifulSoup(r.content, 'html.parser')
print(s.prettify())