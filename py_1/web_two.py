from bs4 import BeautifulSoup
import requests
import pymongo
import time
from multiprocessing import Pool
client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
fiftyeight = ceshi['fiftyeight']
item_info = ceshi['item_info']


def get_attrations(channel, pages):
    # http: // scnj.58.com / danche / pn2 /
    list_view = '{}/pn{}/'.format(channel, str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('td', 't'):
        for i in soup.select(' td.t > a.t '):
            links = i.get('href').split('?')[0]
            fiftyeight.insert_one({'url': links})
            print(links)
    else:
        pass


def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # no_longer_exist = '404' in soup.find('script', type='text/javascript').get('src').split('/')
    # if no_longer_exist:
    #     pass
    # else:
    title = soup.title.text
    date = soup.select('.time')[0].text if soup.find_all('li', 'time') else None
    price = None
    if soup.find_all('span', 'price.c_f50'):
        price = soup.select('span.price.c_f50')[0].text
    if soup.find_all('span', 'price_now'):
        price = soup.select('span.price_now > i')[0].text
    area = None
    if soup.find_all('span', 'c_25d'):
        area = list(soup.select('.c_25d a')[0].stripped_strings)
    elif soup.find_all('div', 'palce_li'):
        area = list(soup.select('.palce_li > span > i')[0].stripped_strings)
    item_info.insert_one({'title': title, 'price': price, 'date': date, 'area': area, 'url': url})
    print({'title': title, 'price': price, 'date': date, 'area': area, 'url': url})

def  get_sale(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    crb = soup.select('span.crb_i > a')[0] if soup.find_all('span', 'crb_i') else None
    print(crb)

for i in fiftyeight.find().limit(500):
    print(i['url'])
# get_item_info('http://zhuanzhuan.58.com/detail/856403490704162822z.shtml')

    # get_attrations('http://scnj.58.com/danche/', 1)
    # soup = BeautifulSoup(requests.get('http://bj.58.com/shouji/24605954621114x.shtml').text, 'lxml')
# print(soup.prettify())