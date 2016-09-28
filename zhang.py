from bs4 import BeautifulSoup
import requests


path = '/Users/hi/Desktop/a/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
    'Cookie':'bid="BZ75jhzT7n4"; ll="118173"; viewed="25908991"; gr_user_id=cb4cb685-f00e-48f3-be37-e1cf9a14c6ad; ue="1097474911@qq.com"; ps=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1474871670%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DsJLzuc0lJJvelroq0PUM5OxcSrjdSJ2p-Us-lVwct4W%26wd%3D%26eqid%3Dc185c90800060c640000000357e6493f%22%5D; _pk_id.100001.8cb4=6bb7935661a85598.1456493283.9.1474871673.1474713688.; _pk_ses.100001.8cb4=*; __utmt=1; __utma=30149280.80667311.1456493284.1474713609.1474871674.10; __utmb=30149280.1.10.1474871674; __utmc=30149280; __utmz=30149280.1474709819.8.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.6196'
}

full_url = ['https://www.douban.com/j/search_photo?q=%E5%BC%A0%E9%B2%81%E4%B8%80&limit=20&start={}'.format(str(i)) for i in range(0,180,20)]

for url in full_url:
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    data = soup.get_text()
    print(data)

#   links = [each['src']for each in data['image']]



