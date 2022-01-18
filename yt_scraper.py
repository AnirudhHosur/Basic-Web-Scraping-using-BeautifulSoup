# Web Scraper rentals

# Import libraries
from bs4 import BeautifulSoup
import requests
from csv import writer

# Check for response from webpage
url = 'https://www.nobroker.in/flats-for-rent-in-bangalore_bangalore'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

lists = soup.find_all("div", {"id" : "app"})
#print(lists)

with open('hotels.csv', 'w', encoding='utf-8', newline='') as f:
    thewriter = writer(f)
    header = ["title", "address", "deposit", "features"]
    thewriter.writerow(header)

    for li in lists:
        title = li.find('span', 
                        {"class" : "overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full"}).text.replace('\n', '')
        address = li.find('div', 
                          {"class" : "mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95"}).text.replace('\n', '')
        deposit = li.find('div', 
                          {"class" : "font-semi-bold heading-6"})
        features = li.find('div',
                           {"class" : "border-3 border-double border-property-views-border-color flex flex-col"}).text.replace('\n', '')
        info = [title, address, deposit, features]
        thewriter.writerow(info)
    