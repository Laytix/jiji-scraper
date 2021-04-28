import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time
import random


df = pd.DataFrame(columns=['title', 'price', 'category', 'region','seller_id', 'seller_number', 'short_description', 'url', 'image_url'])
url = input('url: ')

# url = 'query=' + url_part
pages = 6
start = 1
s = requests.Session()
while start < pages:
    time.sleep(random.randint(1,4))
    headers = {
        'referer': 'https://jiji.com.et/' + url,
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'authority': 'jiji.com.et',
        'scheme': 'https',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }



    response = s.get('https://jiji.com.et/api_web/v1/listing?slug=' + url +'&webp=true&page='+ str(start), headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.text)
    data = json.loads(soup.text)
    lists = data['adverts_list']['adverts']

    for list in lists:
        title = list['title']
        price = list['price_obj']['view']
        category = list['category_name']
        region = list['region_name']
        short_desc = list['short_description']
        seller_id = list['user_id']
        seller_phone = list['user_phone']
        url = 'https://jiji.com.et' + list['url']
        image_url = list['image_obj']['url']

        print(title)
        df_length = len(df)
        df.loc[df_length] = [title, price, category, region, seller_id, seller_phone, short_desc, url,image_url]

    start = start + 1

df.to_excel("jiji-" +url +".xlsx", index=False)