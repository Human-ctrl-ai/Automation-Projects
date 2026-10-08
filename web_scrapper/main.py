from lxml import html
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.request
import pyautogui
import schedule

# Static scrapping...
# # Parse the raw HTML and status code 
# r = requests.get('https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=%7Bpage%7D')
# # print(res.status_code)
# # print(res.content)
# s = BeautifulSoup(r.content, 'html.parser')
# print(s.prettify())

# # Gets the text stored under <p> as articles
# content = s.find('div', class_= 'article--viewer_content')
# if content:
#     for para in content.find_all('p'):
#         print(para.text.strip())
# else:
#     print("No article content found.")



# # Dynamic Scrapping...
# # # Opens google search page with query "geeksforgeeks"
# # driver = webdriver.Firefox()
# # driver.get("https://www.google.co.in/search?q=geeksforgeeks")

# # automate a real e-commerce test website using Selenium and Chrome
# element_list = []

# # Set up Chrome options
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# # Use a proper Service object
# service = Service(ChromeDriverManager().install())

# for page in range(1, 3):
#     # driver initialization
#     driver = webdriver.Chrome(service = service, options = options)
#     # url load
#     url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=%7Bpage%7D"
#     driver.get(url)
#     time.sleep(2) # Optional wait to ensure page loads
    
#     # Extract product details
#     titles = driver.find_elements(By.CLASS_NAME, "title")
#     prices = driver.find_elements(By.CLASS_NAME, "price")
#     descriptions = driver.find_elements(By.CLASS_NAME, "description")
#     ratings = driver.find_elements(By.CLASS_NAME, "ratings")
    
#     for i in range(len(titles)):
#         element_list.append([
#             titles[i].text,
#             prices[i].text,
#             descriptions[i].text,
#             ratings[i].text
#         ])
        
#     driver.quit()
    
# # Display extracted data
# for row in element_list:
#     print(row)

# # extracting link texts...
# url = "https://www.geeksforgeeks.org/python/python-web-scraping-tutorial/"
# res = requests.get(url)
# doc = html.fromstring(res.content)

# links = doc.xpath('//a/text()')
# for t in links:
#     print(t)

# # Working with URLs
# url = 'https://www.example.com/'

# try:
#     r = urllib.request.urlopen(url)
#     data = r.read()
#     html = data.decode('utf-8')
#     print(html)
    
# except Exception as e:
#     print("Error fetching URL:", e)

# # Moving mouse pointer
# for i in range(3):
#     pyautogui.moveTo(519, 1060, duration=1)
#     pyautogui.click()

#     pyautogui.moveTo(1717, 352, duration=1)
#     pyautogui.click()

# # scheduler
# def func():
#     print("Geeksforgeeks")
    
# schedule.every(1).seconds.do(func)
# while True: 
#     schedule.run_pending() 
#     time.sleep(1) 