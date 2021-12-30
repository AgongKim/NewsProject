import requests
from bs4 import BeautifulSoup
import pika

def getRankUrlList(date):
    url = 'https://news.daum.net/ranking/popular'
    if date:
        url + f'?regDate={date}'
    res = requests.get(url)

    url_list = []

    soup = BeautifulSoup(res.content, 'html.parser')
    # print('뉴스' in soup.text)
    # print()
    items = soup.select('a')
    for item in items:
        url = item['href']
        if url:
            if 'https://v.daum.net/v/' in url and not '?' in url:
                url_list.append(url)

    #중복제거
    url_set = set(url_list)
    url_list = list(url_set)
    return url_list

def getNewsByUrl(url):
    
    res = requests.get(url)
    
    soup = BeautifulSoup(res.content, 'html.parser')
    title = soup.select('.tit_view')[0]
    content = soup.select('#harmonyContainer')[0]
    try:
        category = soup.select('.gnb_comm')[0]
    except IndexError as e:
        #스포츠의 경우
        category = {'data-category':'sports'}

    news_object ={}
    news_object['title'] = title.string
    news_object['content'] = content.text
    news_object['category'] = category['data-category']
    return news_object


# getRankUrlList(None)

#RabbitMQ 
def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='POST_NEWS')

    rank_url_list = getRankUrlList(None)

    for idx,url in enumerate(rank_url_list):
        print(f'{idx+1} / {len(rank_url_list)}')
        news = str(getNewsByUrl(url))
        channel.basic_publish(exchange='',
                            routing_key='POST_NEWS',
                            body=news)

run()