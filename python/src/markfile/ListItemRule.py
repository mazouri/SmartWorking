from src.markfile import Rule


class ListItemRule(Rule):
    """
    列表项是以连字符开始的段落，作为格式化的一部分，要移除连字符
    """
    type = 'listitem'

    def condition(self, block):
        return block[0] == '--'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True
