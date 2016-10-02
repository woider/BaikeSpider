'''
爬虫控制模块
调用其他模块完成数据抓取
'''

from baike import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.maxcount = 100  # 抓取数据数量
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 0
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == self.maxcount:
                    break
            except Exception as e:
                print(e)
                continue
            else:
                count += 1
                print(new_url)

        self.outputer.output_html()  # 内容输出至文件


# 程序入口
if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'  # 起始目标
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
