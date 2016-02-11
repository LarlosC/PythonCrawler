from bs4 import BeautifulSoup

import requests

url = str(raw_input("Enter a url please: "))

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

file = open('crawled.txt', 'wb')


for link in soup.find_all('a'):
    links = link.get('href')
    print(links)
    file.write(links + "\n")

file.flush()
file.close()
