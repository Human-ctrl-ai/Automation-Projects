import urllib.request
url = 'https://www.example.com/'

try:
    res = urllib.request.urlopen(url)
    data = res.read()
    html = data.decode('utf-8')
    print(html)

except Exception as e:
    print("Error fetching URL:", e)