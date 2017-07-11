class Rule:
    """
    规则类，"处理字符串"的规则，
    首先添加标签起始标记，然后处理字符串，最后添加标签结束标记
    """
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True
