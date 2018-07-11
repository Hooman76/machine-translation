import requests
from bs4 import BeautifulSoup

page = requests.get("https://ganjoor.net/hafez/ghazal/#z")

# Creating beautifulSoap object
soap = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the poem div
poem_list = soap.find(class_='poem')

# Pull text from all instances of <a> tag within poem div
poem_list_items = poem_list.find_all('a')

pure_poem_links = []

# Extracting Pure links
for item in poem_list_items:
    if item.get('href') is not None:
        if len(item.get('href')) > 7:
            pure_poem_links.append(item.get('href'))

pure_poem_links = pure_poem_links[3:len(pure_poem_links)-1]

# Extracting content of poem links
counter = 0
file = open('sheer.txt', 'w', encoding='utf-8')

for link in pure_poem_links:
    counter += 1
    poem_page = requests.get(link)

    # Creating soap
    html_soap = BeautifulSoup(poem_page.text, 'html.parser')

    # Pull all text from the poem div
    poem_list = html_soap.find(class_='poem')

    first_mesra_list = html_soap.find_all(class_='m1')
    second_mesra_list = html_soap.find_all(class_='m2')

    for i in range(len(first_mesra_list)):
        file.write(first_mesra_list[i].text + "        " + second_mesra_list[i].text)
        file.write("\n")


file.close()
