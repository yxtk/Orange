import requests,pymongo
from bs4 import BeautifulSoup

client = pymongo.MongoClient('localhost',27017)
xiaozhu = client['xiaozhu']
sheet_tab = xiaozhu['sheet_tab']

url = 'http://bj.xiaozhu.com/search-duanzufang-p2-0/'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > a > span')
prices = soup.select('#page_list > ul > li > div > span.result_price > i')
for title,price in zip(titles,prices):
    data = {
        'title': title.get_text(),
        'price': price.get_text()
    }
    sheet_tab.insert_one(data)
print('done')

def get_page_within(pages):
    for page_num in range(1,pages+1):
        wb_data = requests.get('http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(page_num))
        soup = BeautifulSoup(wb_data.text,'lxml')
        titles = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > a > span')
        prices = soup.select('#page_list > ul > li > div > span.result_price > i')
        for title,price in zip(titles,prices):
            data = {
                'title': title.get_text(),
                'price': int(price.get_text())
            }
            sheet_tab.insert_one(data)
    print('done')

get_page_within(3)

for item in sheet_tab.find({'price':{'$gte':500}}):
    print(item)
