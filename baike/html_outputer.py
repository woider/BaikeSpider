'''
页面数据输出模块
将抓取的信息以MarkDown格式输出
'''


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.md', 'w', encoding='utf8')

        # 使用MarkDown语法输出
        fout.write('#百度百科\n')
        for data in self.datas:
            fout.write("##[%s](%s)##\n" % (data['title'], data['url']))
            fout.write("> %s" % (data['summary']))
            fout.write('\n\n---------\n\n')  # 分隔线

        fout.close()
