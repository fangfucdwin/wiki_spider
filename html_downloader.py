import string
from urllib import request
from urllib.parse import quote

import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        #url_ = quote(url, safe=string.printable)
        #response = request.urlopen(url_)
        kv = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.18 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }

        response = requests.get(url, headers=kv)
        response.encoding = response.apparent_encoding

        #if response.getcode() != 200:
        #    return None
        if response.status_code != 200:
            return None

        #return response.read()
        return response.text