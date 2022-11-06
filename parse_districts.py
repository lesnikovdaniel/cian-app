import requests, re
from bs4 import BeautifulSoup

list = []
for item in range(1,140):
    url = "https://www.cian.ru/cat.php?deal_type=sale&district="+str(item)+"&engine_version=2&offer_type=flat&room1=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    
    districtName = soup.findAll('h1', {"class":re.compile(r'_(.{10})--color_black_100--(.{5})\s(.{8,11})--lineHeight_36px--(.{5})\s(_(.){10})--fontWeight_bold--(.{5})\s_(.{10})--fontSize_28px--(.{5})\s_(.){10}--display_block--(.{5})\s_(.){10}--text--(.{5})\s_(.){10}--text_letterSpacing__normal--(.{5})')})[0].text
    # result = districtName.replace(r'.*(в округе |в районе )| в Москве','')
    result = str(districtName).replace(r'.*(в округе |в районе )| в Москве','')
    print(result)
