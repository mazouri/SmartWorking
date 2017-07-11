from markfile.Rule import Rule


class HeadingRule(Rule):
    type = 'heading'

    # 每一个规则的子类，都应该有condition函数，用来判断当前字符串是否符合子类规则
    def condition(self, block):
        # string中没有换行符，且string的长度小于等于70，且字符串最后一个字符不等于':'
        # 满足以上条件，该字符串即为标题
        # '\n' not in block == not '\n' in block
        return '\n' not in block and len(block) <= 70 and not block[-1] == ':'
