import requests
from bs4 import BeautifulSoup

url = 'http://bj.xiaozhu.com/fangzi/3840950830.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

title = soup.select('body > div.wrap.clearfix.con_bg > div > div.pho_info > h4 > em')[0].text
address =soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')[0].text
price = soup.select('#pricePart > div.day_l > span')[0].text
img = soup.select('#curBigImage')[0].get('src')
host_name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')[0].text
host_img = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')[0].get('src')
host_sex = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')[0].get('class')[0]
#print(host_sex)

def get_host(class_name):
    if class_name =='member_ico1':
        return '女'
    if class_name =='member_ico':
        return '男'

data = {
    'title':title,
    'address':address,
    'price':price,
    'img':img,
    'host_name':host_name,
    'host_img':host_img,
    'host_sex':get_host(host_sex)
}
print(data)


'''
page_link = []
def get_page_link(page_number):
    for each_number in range(1,page_number):
        full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(each_number)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        for link in soup.select('a.resule_img_a'):
            page_link.append(link)

批量获取链接,解析详情的时候就遍历这个列表
'''
