from bs4 import BeautifulSoup

with open('/Users/hi/homework1-2/index.html', 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')

    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')

for title, image, review, price, star in zip(titles, images, reviews, prices, stars):
    data = {
        'title': title.get_text(),
        'image': image.get('src'),
        'review': review.get_text(),
        'price': price.get_text(),
        'star': len(star.find_all("span", class_='glyphicon glyphicon-star'))

    }
    print(data)
