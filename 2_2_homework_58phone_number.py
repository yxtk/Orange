import requests
from bs4 import BeautifulSoup
import pymongo


client = pymongo.MongoClient('localhost',27017)
tongcheng_info = client['tongcheng_info']
phone_number = tongcheng_info['phone_number']

url = 'http://bj.58.com/shoujihao/'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
numbers = soup.select('strong.number')
prices = soup.select('b.price')
links = soup.select('a.t')

for number,price,link in zip(numbers,prices,links):
    data = {
        'number':number.get_text(),
        'price':price.get_text(),
        'link':link.get('href')
    }
    phone_number.insert_one(data)
#print('Done')

def get_pages(pages):
    for page_num in range(1,pages+1):
        wb_data = requests.get('http://bj.58.com/shoujihao/pn{}/'.format(page_num))
        soup = BeautifulSoup(wb_data.text,'lxml')
        numbers = soup.select('strong.number')
        prices = soup.select('b.price')
        links = soup.select('a.t')

        for number,price,link in zip(numbers,prices,links):
            data = {
                'number':number.get_text(),
                'price':price.get_text(),
                'link':link.get('href')
            }
            phone_number.insert_one(data)
 #           print('Done')

get_pages(1)
for item in phone_number.find():
    print(item)



