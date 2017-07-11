from markfile.Handler import Handler


class HTMLRenderer(Handler):
    """
    Handler类的子类，html渲染类，用来实现添加具体的标签
    """

    def start_document(self):
        print('<html><head><title>...</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2>')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul>')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')

    def end_title(self):
        print('</h1>')

    # 定义过滤器的回调函数
    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)  # 匹配字符串转换为html强调字符

    def sub_url(self, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))  # group(1)表示匹配子组1

    def sub_mail(self, match):
        # 之所以用子组1是添加过滤器时设置了子组
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))

    def feed(self, data):
        print(data)
