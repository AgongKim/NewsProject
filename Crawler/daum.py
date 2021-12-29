import requests
from bs4 import BeautifulSoup


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
                print(url)
                url_list.append(url)
    return url_list

def getNewsByUrl(url):
    res = requests.get(url)
    
    soup = BeautifulSoup(res.content, 'html.parser')
    title = soup.select('.tit_view')[0]
    content = soup.select('#harmonyContainer')[0]
    category = soup.select('.gnb_comm')[0]# .on .ir_wa')[0]
    print(title.string)
    print(content.text)
    print(category['data-category'])

getNewsByUrl('https://news.v.daum.net/v/20211210025101454')