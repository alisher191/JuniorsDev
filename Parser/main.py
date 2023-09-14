import requests
from bs4 import BeautifulSoup
import csv

host = 'https://www.kijiji.ca'

for i in range(1, 101):
    URL = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/c37l1700273'
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }

    req = requests.get(url=URL, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    #
    # with open(f"pages/page_{i}.html", "w") as file:
    #     file.write(src)

    # with open(f"pages/page_{i}.html") as file:
    #     src = file.read()
    #
    # soup = BeautifulSoup(src, "lxml")
    block = soup.find("div", class_="col-2 new-real-estate-srp")

    titles = block.find_all("div", class_='title')
    places = block.find_all("span", class_='intersection')
    descriptions = block.find_all("div", class_="description")
    prices = block.find_all(class_='price')
    location_and_date = block.find_all('div', class_='location')
    images = block.find_all("div", class_="image")

    title = [title.text.replace('\n', '').strip() for title in titles]
    item_href = [host + item.find_next().get('href') for item in titles]
    street = [item.text for item in places]
    description = [item.next_element.text.replace('\n', '').strip() for item in descriptions]
    price = [item.text.replace('\n', '').strip() for item in prices]
    city = [" ".join(item.find_next().text.split()) for item in location_and_date]
    date_of_add = [item.find_next().find_next().text for item in location_and_date]
    image = [item.find_next("img").get('data-src') for item in images]

    # for t in range(len(titles)):
    #     print(f'Публикация №{t}.\n'
    #           f'Ссылка на публикацию: {item_href[t]},\n'
    #           f'Изображение: {image[t]},\n'
    #           f'Описание: {description[t]},\n'
    #           f'Цена: {price[t]},\n'
    #           f'Город: {city[t]},\n'
    #           f'Расположение: {street[t]},\n'
    #           f'Дата добавления: {date_of_add[t]}.\n')

    with open(f'contents/{i}_page_content.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Публикация №', 'Заголовок', 'Ссылка на публикацию', 'Изображение', 'Описание', 'Цена', 'Город', 'Расположение', 'Дата добавления'])
        for k in range(len(titles)):
            writer.writerow([k+1, title[k], item_href[k], image[k], description[k], price[k], city[k], street[k], date_of_add[k]])


"""
https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273
https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-2/c37l1700273
"""