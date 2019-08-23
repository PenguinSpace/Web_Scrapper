from bs4 import BeautifulSoup
import requests
import pandas as pd
from lxml import html

url_name = "https://thekittchen.com/12-easy-recipes-for-beginners/"
url = requests.get(url_name)

# the soup object that opens up the html in the website
soup = BeautifulSoup(url.content, 'lxml')

# Checks if the URL was able to be opened
if url.status_code == 200:
    print("Success")
elif url.status_code == 404:
    print("Failed to open URL")

# print(soup.prettify())

div_tag = soup.find('div', class_='entry-content')
url_list = []
description = []
names = []

# works it finds all the p tags in the div tag and accesses
# the hyperlink.
# now we need to store the data somewhere

for tag in div_tag.find_all('p'):
    try:

        url_list.append(tag.a.get('href'))
        names.append(tag.text.split('–')[0])
        description.append(tag.text.split('–', 1)[1])
        # print(type(tag.text.split('–', 1)[1]))
        # print(tag.text.split('–', 1)[1])
        # print()

    except Exception as e:
        pass


# stores all the data in to lists which are combined in a dataframe
df = pd.DataFrame({'Names': names, 'Food Description': description, 'Website': url_list})


df.to_csv('NEW_DATA.csv', encoding='utf-8-sig')
