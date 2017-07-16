from src.markfile import Rule


class ParagraphRule(Rule):
    """
    段落：其他规则没有覆盖的块
    """
    type = 'paragraph'

    def condition(self, block):
        return True
