from bs4 import BeautifulSoup

with open('/Users/hi/homework1-2/index.html', 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    #print(wb_data)

    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings >p:nth-of-type(2) > span ')
#    print(titles,images,prices,reviews,stars,sep='\n-----------\n')

for title, price, image, review, star in zip(titles, prices, images, reviews, stars):
    data = {
        'title': title.get_text(),
        'price': price.get_text(),
        'image': image.get('src'),
        'review': review.get_text(),
        'star': len(star.find_all('span', class_='glyphicon glyphicon-star'))
    }

    print(data)