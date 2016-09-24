from bs4 import  BeautifulSoup
import requests


url = 'https://knewone.com/discover?page='

def get_page(url,data=None):

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('section.content > h4 > a')
    links = soup.select('section.content > h4 > a')
    imgs = soup.select('a.cover-inner > img')

    if data==None:
        for title,link,img in zip(titles,links,imgs):
            data = {
                'img':img.get('src'),
                'title':title.get_text(),
                'link':link.get('href')
            }
            print(data)
def get_more_page(start,end):
    for one in range(start,end):
        get_page(url+str(one))

get_more_page(1,5)