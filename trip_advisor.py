from bs4 import BeautifulSoup
import requests

url = 'http://www.tripadvisor.cn/Attractions-g298184-Activities-Tokyo_Tokyo_Prefecture_Kanto.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')

titles = soup.select('div.property_title > a[target="_blank]')
imgs = soup.select('img[width="160"]')
cates = soup.select('div.p13n_reasoning_v2')

for title, img, cate in zip(titles, imgs, cates):
    data = {
        'title': title.get_text(),
        'img': img.get('src'),
        'cate': list(cate.stripped_strings)
    }
    print(data)
print('\n---------------------------------------------------\n')


headers = {
    'User-Agent': '...',
    'Cookie': '...'
}
url_saves = 'http://www.tripadvisor.cn/Saves#1'
wb_data = requests.get(url_saves, headers=headers)  #headers=headers默认参数，刚才的参数用关键字参数传入一次get的请求中
soup = BeautifulSoup(wb_data.text, 'lxml')

titles = soup.select('a.location-name')            #不确定是否为a.location-name时可以在源代码中检验
images = soup.select('img.photo_image')
metas = soup.select('span.format_address')

for title, image, meta in zip(titles, images, metas):
    data ={
        'title': title.get_text(),
        'image': image.get('src'),
        'meta': meta.get_text()
    }
    print(data)


