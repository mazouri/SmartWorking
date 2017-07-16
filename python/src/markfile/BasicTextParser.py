from src.markfile import HeadingRule
from src.markfile import ListItemRule
from src.markfile import ListRule
from src.markfile import ParagraphRule
from src.markfile import Parser
from src.markfile import TitleRule


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