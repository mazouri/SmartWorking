class Handler:
    """
    处理器，处理各种标签，如标题，列表，段落等，主要实现方法在其子类中
    """

    # 定义回调函数，调用该类中函数名为prefix+name的方法，输入参数为*args
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method):
            return method(*args)

    # 开始标签，调用callback，组装成start_name形式的方法，进行调用
    def start(self, name):
        self.callback("start_", name)

    # 结束标签
    def end(self, name):
        self.callback("end_", name)

    def sub(self, name):
        # substitution英文意思就是"替换"
        # 该函数将作为re.sub函数的第二个参数
        # 作用是替换指定规则的字符串
        def substitution(match):
            # 只要进入这个函数，就表示有匹配的字符串
            # 若callback返回的字符串为空，则返回采用完整的匹配，
            # 否则返回回调函数中的字符串
            result=self.callback("sub_", name, match)
            if result is None:
                result=match.group(0)  # group(0)表示完整的匹配
            return result
        return substitution
