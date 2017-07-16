#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys

from markfile.HTMLRenderer import HTMLRenderer

from src.markfile.BasicTextParser import BasicTextParser

if __name__ == '__main__':
    handler = HTMLRenderer()#定义渲染类
    parser = BasicTextParser(handler)#初始化解析类
    parser.parse(sys.stdin)#解析输入的文件，转换为html文件
