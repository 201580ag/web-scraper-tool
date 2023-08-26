import requests
import re
from bs4 import BeautifulSoup

url = input("Please enter the site address: ")
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, 'html.parser')
links = soup.find_all('a', {'href': re.compile('^http')})

with open('links.txt', 'w') as f:
    print("Saved in links.txt.")
    for link in links:
        f.write(link['href'] + '\n')