
from bs4 import BeautifulSoup
import requests

url = 'https://www.thenetnaija.net/videos/movies'
response =requests.get(url)

# Get title of website
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find('title')
print(title)