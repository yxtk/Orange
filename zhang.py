from bs4 import BeautifulSoup
import requests


path = '/Users/hi/Desktop/a/'
headers = {
    '''
}   

full_url = ['https://www.douban.com/j/search_photo?q=%E5%BC%A0%E9%B2%81%E4%B8%80&limit=20&start={}'.format(str(i)) for i in range(0,180,20)]

for url in full_url:
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    data = soup.get_text()
    print(data)

#   links = [each['src']for each in data['image']]



