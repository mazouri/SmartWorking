def lines(file):
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


class Parser:
    """
    语法分析器：读取文本文件，应用规则并控制处理程序
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


