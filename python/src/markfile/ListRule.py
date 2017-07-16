from src.markfile import ListItemRule


class ListRule(ListItemRule):
    """
    列表：从不是列表项的块和随后的列表项之间。在最后一个连续列表项之后结束
    """
    type = 'list'
    inside = False  # 是否进入列表项

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
