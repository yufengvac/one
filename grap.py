# -*- coding:utf-8 -*-
import sys
import requests
import json
import time
import random


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    data = json.loads(html)['cmts']
    for item in data:
        yield {
            'comment': item['content'],
            'data': item['time'].split(' ')[0],
            'rate': item['score'],
            'city': item['cityName'],
            'nickname': item['nickName']
        }


def save_to_txt():
    for i in range(1, 1001):
        url = 'http://m.maoyan.com/mmdb/comments/movie/248566.json?_v_=yes&offset=' + str(i)
        html = get_one_page(url)
        print('正在保存第%d页'%i)
        for item in parse_one_page(html):
            with open('xie_zheng.txt', 'a') as f:
                f.write(item['data'] + ',' + item['nickname'] + ','
                        + item['city'] + ','+str(item['rate']) + ','+item['comment']+'\n')
        time.sleep(5+float(random.randint(1, 100)) / 20)


if __name__ == '__main__':
    print(sys.getdefaultencoding())
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print(sys.getdefaultencoding())
    save_to_txt()
