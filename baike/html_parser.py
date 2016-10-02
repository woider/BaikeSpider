'''
页面解析模块
产生新的URL链接
获取词条名称和信息
'''

import re
from urllib import parse
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

        pass

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        node = soup.find('div', {'class': 'lemma-summary'})
        links = node.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', {'class': 'lemmaWgt-lemmaTitle-title'})
        title_node = title_node.find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        sumary_node = soup.find('div', {'class': 'lemma-summary'})
        res_data['summary'] = sumary_node.get_text()

        return res_data
