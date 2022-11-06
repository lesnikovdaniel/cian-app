import requests, re
from bs4 import BeautifulSoup

# Обязательные фильтры
# Районы Москвы: district={1-132}
# Количество комнат: room{1-9}=1
# Сегмент(новостройки и вторичка): object_type=1 - новостройка,2-вторичка
# Этажей в доме: maxfloor=4&minfloor=1
# Материал стен: house_material=1 - кирпич, 2-панельный, 3-монолитный


# Фильтры для корректировки
# Этаж maxfloor=2&minfloor=1
# Площадь maxtarea=51&mintarea=42
# Площадь кухни maxkarea=123&minkarea=12
# Балкон/Лоджия loggia=1&min_balconies=1
# Удаленность от метро foot_min=45
# Состояние
# decorations_list%5B0%5D=fine&
# decorations_list%5B1%5D=fineWithFurniture&
# decorations_list%5B2%5D=rough&
# decorations_list%5B3%5D=without



url = "https://www.cian.ru/cat.php?"\
    "deal_type=sale&"\
    "district=132&"\
    "engine_version=2&"\
    "offer_type=flat&"\
    "room1=1&"\
    "room2=1&"\
    "room9=1"


def getList(url):
    result = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    list = soup.findAll('article', {'data-name':'CardComponent'})
    for item in list[0:10]:
        linkArea = item.findAll('div',{'data-name':"LinkArea"})
        result.append(linkArea[0].findAll('a')[0]['href'])
    return result

def getListItem(url_list:list):
    result = []
    for url in url_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        info = soup.findAll('span',{'class':re.compile(r'[A-Za-z0-9]{10}--value--[A-Za-z0-9]{5}')})
        floors = soup.findAll('div',{'data-testid':"object-summary-description-value"})[-2].text
        floor = re.findall(r'\d+', floors)
        
        underground = soup.findAll('span', {'class': re.compile(r'[A-Za-z0-9]{10}--underground_time--[A-Za-z0-9]{5}')})[0].text.replace(' ⋅  ', '')[0:6]
        location = soup.findAll('span', {'itemprop':'name'})[-1]['content']
        rooms_count = soup.findAll('h1', { 'class': re.compile(r'[A-Za-z0-9]{10}--title--[A-Za-z0-9]{5}') })[0].text[0]
        segment = info[0].text
        floor_count = floor[1]
        walls = soup.findAll('div',{'data-name':"Item"})[2].findAll('div',{'class':re.compile(r'[A-Za-z0-9]{10}--value--[A-Za-z0-9]{5}')})[0].text
        floor_number = floor[0]  
        square = soup.findAll('div',{'data-testid':"object-summary-description-value"})[0].text.replace('\xa0м²','')
        kitchen = soup.findAll('div',{'data-testid':"object-summary-description-value"})[-3].text.replace('\xa0м²','')
        balcony = info[-3].text
        from_metro = ''
        wall_decoration = info[-2].text
        obj = {
                'location':location,
                'rooms_count':rooms_count,
                'segment': segment,
                'floors': floor_count,
                'walls': walls,
                'floor_number': floor_number,
                'square': square,
                'kitchen': kitchen,
                'balcony': balcony,
                'from_metro': from_metro,
                'wall_decoration': wall_decoration
            }
        print(obj)

    # return result

list = getList(url)
getListItem(list)