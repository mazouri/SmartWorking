from src.markfile import HeadingRule


class TitleRule(HeadingRule):
    """
    标题是文档的第一个块，但是前提是它是一个大标题
    """
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(block)
