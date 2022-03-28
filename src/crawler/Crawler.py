from bs4 import BeautifulSoup as bs
from src.services.requests import get_request
import json

BASE_URL = 'https://www.amazon.com.br'
SEARCH_URL = '{url}/s?k='.format(url=BASE_URL)

def crawler(term = 'iphone'):
    
    products = {
        'products':[]
    }

    scrapping_page('{url}{term}'.format(url=SEARCH_URL, term=term), products)

    return json.dumps(products)

def scrapping_page(link, products):
    response = get_request(link, headers=headers_search())
    
    soup = bs(response.text, 'html.parser')
    product_itens = soup.select('div.s-result-item.s-asin.sg-col-4-of-16.sg-col')

    for item in product_itens:
        title = item.select('h2 span.a-size-base-plus.a-color-base.a-text-normal')[0].text
        price = item.select('span.a-price-whole')
        price_cent = item.select('span.a-price-fraction')

        if len(price) > 0:
            price = '{price}{price_cent}'.format(price = price[0].text, price_cent=price_cent[0].text)
        else:
            price = '0,00'

        link = item.select('h2 a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')[0]['href']

        product = {
            'title':title, 
            'price':price,
            'link':link
        }

        products['products'].append(product)

    next_page = soup.findAll('a', class_='s-pagination-next')
    
    if len(next_page) > 0:
        return scrapping_page('{url}{term}'.format(url=BASE_URL, term=next_page[0]['href']), products)
    else:
        return products


def headers_search():
  return {
    'authority': 'www.amazon.com',
    'cache-control': 'no-cache',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
  }