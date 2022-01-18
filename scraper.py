# Web Scraper
from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://www.kijiji.ca/b-apartments-condos/canada/halifax/k0c37l0?rb=true'
page = requests.get(url)
#print(page)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

lists = soup.find_all("div", {"class" : "info"})
#print(lists)

with open('halifax.csv', 'w', encoding='utf-8', newline='') as f:
    thewriter = writer(f)
    header = ['price', 'title', 'location', 'date_posted', 'description']
    thewriter.writerow(header)
    
    for li in lists:
        price = li.find('div', {"class" : "price"}).text.replace('\n', '')
        title = li.find('div', {"class" : "title"}).text.replace('\n', '')
        location = li.find('div', {"class" : "location"}).text.replace('\n', '')
        date_posted = li.find('span', {"class" : "date-posted"}).text.replace('\n', '')
        description = li.find('div', {"class" : "description"}).text.replace('\n', '')
        info = [price, title, location, date_posted, description]
        thewriter.writerow(info)



