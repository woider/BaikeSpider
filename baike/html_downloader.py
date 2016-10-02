'''
页面下载模块
下载网页HTML代码并转换为UTF-8格式
'''

from urllib import request


class HtmlDownloader(object):
    # 获取页面HTML代码
    def download(self, url):
        if url is None:
            return None
        response = request.urlopen(url)
        if response.getcode() != 200:
            return None
        else:
            return response.read().decode('utf8')
