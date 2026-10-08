import requests
from bs4 import BeautifulSoup

# Fetch and parse the page
res = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')
soup = BeautifulSoup(res.content, 'html.parser')

# Find the main content container
content = soup.find('div', class_='article--viewer_content')
if content:
    for para in content.find_all('p'):
        print(para.text.strip())
else:
    print("No article content found.")