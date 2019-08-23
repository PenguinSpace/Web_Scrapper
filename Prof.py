from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from lxml import html

# Accessing the url and getting the html data
url_name = "https://bme.duke.edu/faculty/biomedical-imaging-biophotonics"
url = requests.get(url_name)

soup = BeautifulSoup(url.content, 'lxml')

# making the lists for all everything we are
# looking to scrape
name = []
title = []
description = []
url = []

# we want a particular div and within that div
# we want to access all the other divs

div_tag = soup.find('div', class_='view-content')

for tag in div_tag.find_all('div', class_='views-row'):
    name.append(tag.div.a.text)
    url.append("https://bme.duke.edu" + tag.div.a['href'])
    title.append(tag.find('p', class_='title').text)
    # desc_text = tag.find('p', class_='description').text
    # print(desc_text)
    # real = re.sub('.', '.\n', desc_text)
    description.append(tag.find('p', class_='description').text)


df = pd.DataFrame({'Name': name, 'Title': title, 'Description': description, 'URL': url})


df.to_csv('Duke Professors.csv')