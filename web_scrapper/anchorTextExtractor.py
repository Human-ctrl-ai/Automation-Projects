from lxml import html
import requests

url = "https://www.geeksforgeeks.org/python/python-web-scraping-tutorial/"
res = requests.get(url)
doc = html.fromstring(res.content)

# Extract all link texts
links = doc.xpath('//a/text()')

for t in links:
    print(t)