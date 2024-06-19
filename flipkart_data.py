from bs4 import BeautifulSoup
import requests
import time
image = []
title = []
describe = []
price = []
review = []
for i in range(32,42) :
    time.sleep(4)
    url = f"https://www.flipkart.com/search?q=smartphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
    r = requests.get(url)
    print(r.status_code)
    if r.status_code == 200 :
        print(url)
        soup = BeautifulSoup(r.text,"html.parser")
        soup.prettify
        container = soup.find('div', class_ ='DOjaWF gdgoEp')
        items = container.find_all('div',class_='_75nlfW')
        # print(items)
        for value in items:
            images = value.find('img',class_='DByuf4')
            image.append(images.get('src'))
            titles = value.find("div",class_='KzDlHZ')
            title.append(titles.text) 
            prices = value.find("div",class_ = "_4b5DiR")
            if prices:
                     price.append(prices.text)
            else :
                price.append('')
            descriptions = value.find('ul',class_='G4BRas')
            describe.append(descriptions.text)
            reviews = value.find('div',class_='XQDdHH')
            if reviews:
                review.append(reviews.text)
            else :
                review.append(0)
        print(len(image),len(title),len(describe),len(price),len(review))
    else :
        break 
import pandas as pd
list = pd.DataFrame({
    "title": title,
    'describe': describe,
    'image': image,
    'price':price,
    'review':review
})
list.to_csv('smartphone_list3.csv')
