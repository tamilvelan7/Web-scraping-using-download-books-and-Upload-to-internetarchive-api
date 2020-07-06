import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
print("connecting to server...")
print("connected")
f=open('tamilbooks.txt',"r")
tamil=f.readlines()
for tamils in tamil:
    url = (tamils)
    response = requests.get(url)
    soup= BeautifulSoup(response.text, "html.parser")
    links=soup.select("a[href$='.pdf']")
    for link in links:
        filename = os.path.join("D:\\Tamil",link['href'].split('/')[-1])
        print(filename)
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,link['href'])).content)
