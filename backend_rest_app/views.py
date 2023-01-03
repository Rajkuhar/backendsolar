import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bs4 import BeautifulSoup

# Create your views here.


@api_view(['GET'])
def country_info(request, country_name):
    required_data = {
        'flag_link': '',
        'capital': [],
        'largest_city': [],
        'official_languages': [],
        'area': 0,
        'population': 0,
        'gdp': ''
    }
    flag_link, capital, largest_city, official_language, area, population, gdp = '', [], [], [], 0, 0, ''
    url = "https://en.wikipedia.org/wiki/"+country_name
    try:
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        table = soup.find("table", attrs={"class": "infobox ib-country vcard"})

        # fetch website
        flag_link = table.find("a", attrs={'class': "image"}).find("img")
        flag_link = "https:" + flag_link.get('src')
        required_data['flag_link'] = flag_link

        pairs = table.find_all('tr')
        for pair in pairs:
            if pair.find('th'):
                heading = pair.find('th')
                detail = pair.find('td')
                if heading.text == 'Capitaland largest city':
                    capital = [i.get('title') for i in detail.find_all(
                        'a') if i.get('title') is not None]
                    largest_city = capital
                    if len(capital) == 1:
                        capital = capital[0]
                        largest_city = capital
                if heading.text == 'Capital':
                    capital = [i.get('title') for i in detail.find_all(
                        'a') if i.get('title') is not None]
                    if len(capital) == 1:
                        capital = capital[0]
                if heading.text == 'Largest city':
                    largest_city = [i.text for i in detail.find_all(
                        'a') if i.get('title') is not None]
                    if len(largest_city) == 1:
                        largest_city = largest_city[0]
                if 'Official' in heading.text and 'language' in heading.text:
                    official_language = [i.text for i in detail.find_all(
                        'a') if i.get('title') is not None]
                    if len(official_language) == 1:
                        official_language = official_language[0]
        for c in range(len(pairs)):
            th_data = pairs[c].find('th')
            if (th_data != None and th_data.find('a') != None and th_data.find('a').get_text() == "Area "):
                area = pairs[c +
                             1].find('td').get_text().split('[')[0].split('(')[0]

            if (th_data != None and th_data.find('a') != None and th_data.find('a').get_text() == "Population"):
                population = pairs[c +
                                   1].find('td').get_text().split('[')[0].split('(')[0]

            if (th_data != None and th_data.find('a') != None and th_data.find('a').get_text() == "GDP" and th_data.find('span').get_text() == "(nominal)"):
                gdp = pairs[c+1].find('td').get_text().split('[')[0]
        required_data = {
            'flag_link': flag_link,
            'capital': capital,
            'largest_city': largest_city,
            'official_languages': official_language,
            'area_total': area,
            'Population': population,
            'GDP_nominal': gdp
        }
        return Response(required_data)
    except:
        return Response({"error": "Country not found"}, status=404)
