#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

# target url
url = 'https://portswigger.net/bappstore/b011be53649346dd87276bca41ce8e8f'

# making requests instance
reqs = requests.get(url)

# using the BeaitifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')

# displaying the title
print("Title of the website is : ")
for title in soup.find_all('title'):
    print(title.get_text())

html_page = reqs.text.lower()
title = html_page[html_page.find('<title>')+7 : html_page.find('</title>')]
print(title)