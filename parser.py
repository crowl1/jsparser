import requests
from bs4 import BeautifulSoup

HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63', 'accept': '*/*'}
URL = 'https://www.imdb.com/chart/top'

films = []

def parser():
    page = requests.get(URL, headers = HEADERS)

    if page.status_code != 200:
        raise Exception("Сторінка не знайдена")
    
    html_pars = BeautifulSoup(page.text, 'html.parser')

    table = html_pars.find_all('td', class_='titleColumn')

    for item in table:

        films.append(
        {
            'title': item.find('a').get_text(),
            'year' : item.find('span', class_= 'secondaryInfo').get_text()[1:-1],
            'members' : item.find('a').get('title').split(',')
        }
    )
    print(films)

    


parser()