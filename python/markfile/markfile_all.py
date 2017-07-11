#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys, re  # 导入sys和re模块，sys为系统模块，re为正则表达式模块


def lines(file):
    """
    该函数从file中读取每一行并建立迭代对象，并在末尾加上换行符
    简而言之，就是凡事包含yield的函数，都可当作for的对象使用，lines(file)生成器
    a = lines(file)， a可以作为for关键字的对象，a还可以使用__next__内建属性
    之所以最后加上一个换行符，是为了block中的判断，将最后一个块输出，
    如果去掉yield '\n' 并且读的文件中最后一行不为空，会发现最后块无法输出
    """
    for line in file: yield line
    yield '\n'


def blocks(file):
    """
    读取文件，将文件分成块，
    """
    block = []
    for line in lines(file):  # 读取文件的每一行
        if line.strip():  # 去掉string的前后端的空格，判断是否为真
            block.append(line)  # 如果为真，将string添加到block中
        elif block:  # 如果line为假，判断block是否为空
            # 如果不为空，将block中所有元素连接起来为一个新的string，元素之间的连接字符为空，
            # 去掉新string的前后端空格, 将新string添加到生成器中
            yield ''.join(block).strip()
            block = []  # 重新将block赋值为空，以便读取后面内容


class Handler:
    """
    处理器，处理各种标签，如标题，列表，段落等，主要实现方法在其子类中
    """

    # 定义回调函数，调用该类中函数名为prefix+name的方法，输入参数为*args
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method): return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        # 定义substitution函数，该函数将作为re.sub函数的第二个参数
        # 该函数的作用是替换指定规则的字符串
        def substitution(match):
            # 只要进入这个函数，就表示有匹配的字符串
            # 若callback返回的字符串为空，则返回采用完整的匹配，
            # 否则返回回调函数中的字符串
            result = self.callback('sub_', name, match)
            if result is None: match.group(0)  # group(0)表示完整的匹配
            return result

        return substitution


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


class Rule:
    """
    规则类，处理字符串的规则，
    首先添加标签起始标记，然后处理字符串，最后添加标签结束标记
    """

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    type = 'heading'

    # 每一个规则的子类，都应该有condition函数，用来判断当前字符串是否符合子类规则
    def condition(self, block):
        # string中没有换行符，且string的长度小于等于70，且字符串最后一个字符不等于':'
        # 满足以上条件，该字符串即为标题
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'


class TitleRule(HeadingRule):
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):
    type = 'listitem'

    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(ListItemRule):
    type = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ParagraphRule(Rule):
    type = 'paragraph'

    def condition(self, block):
        return True


class Parser:
    """
    A parser reads a text file, applying rules and controlling a  handler.
    """

    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)

        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):  # 判断字符串属于哪一类规则
                    last = rule.action(block, self.handler)  # 运行规则处理字符串
                    if last: break
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    解析类子类
    """

    def __init__(self, handler):
        Parser.__init__(self, handler)  # 调用父类构造函数

        # 添加解析规则类
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())  # 最后在添加段落规则，应为段落规则condition始终返回True

        # 在此处添加匹配转换规则(过滤字符串并进行转换)，
        # 正则表达式中括号表示保存为子组，与HTMLRenderer中的过滤器函数对应
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')  # url规则可以改进
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')  # 邮件规则还可以改进


handler = HTMLRenderer()  # 定义渲染类
parser = BasicTextParser(handler)  # 初始化解析类
parser.parse(sys.stdin)  # 解析输入的文件，转换为html文件
