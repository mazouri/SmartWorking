前面的是mac，后面是win/linux


# 基本使用
保存：Command+S，Control+S

同步：Command＋Option＋Y，Control＋Alt＋Y

添加到左边栏五角星那里：Option+Shift+F，Alt+Shift＋F

快速调出选择对话框:Control + `,Control + `    选择IDE的颜色，主题，keymap等

打开设置对话框：Command+, Control+Alt+S

工程结构（Project Structure）对话框：Command＋;  ， Control＋Alt+Shift+S

切换tab窗口：Control＋Tab，Control＋Tab    可以方便的切换当前的文件和工具窗口

# 导航与搜索
全局搜索：Double S，Double Shift

文件内查找：Command＋F，Control＋F

文件内查找下一处：Command＋G，F3

文件内查找上一处：Command＋Shift＋G，Shift＋F3

文件内替换:Command＋R,Control＋R

查找Studio的功能:Command＋Shift＋A

条件(根据名字)查找:Command+Option+O,Control＋Alt+Shift+N

查找Class:Command＋O,Control＋N  仅仅查找类

查找文件名：Command＋Shift＋O，Control＋Shift＋N  不仅仅是类，包括其他类型的文件

在文件路径中查找：Command＋Shift＋F，Control＋Sfift＋F  全局搜索,可以设置搜索的文件类型

文件结构对话框：Command＋F12 可以查看类的字段和方法

跳到源码：F4 / Command + Down Arrow， F4 / Control + Enter  不常用，一般Control/Command ＋鼠标左键

把当前编辑以一个新的窗口打开：Shift + F4

显示最近打开过的文件：Command + E，Control + E

显示最近编辑过的文件：Command＋Shift+E，Control＋Shift＋E

光标回到最后一次编辑的位置：Command + Shift + Backspace(delete)，Control + Shift + Backspace

关闭当前激活的编辑窗口：Command+W， Control + F4

跳转到某行：Command + L，Control + G 处理Bug时候，看到堆栈异常，然后可以快速定位到某行

打开类型层级：Control + H 继承关系,使用时光标要在类文件里面

查看方法层级：Command + Shift + H，Control + Shift + H 光标放在方法上才行

方法调用层级：Control + Option + H，Control + Alt + H 光标放在方法上才行


# 代码编辑相关
生成代码：Command+N, Alt+Insert setter、getter、toString等

重写方法：Control+O，Control+O O是Override

实现方法：Control+I，I是implements

快速生成代码块：Command+Option+T，Control+Alt+T if…else\try…catch…等等

删除光标所在行：Command+Backspace(delete)，Control+Y

折叠代码：Command + minus/plus，Control + minus/plus 加号减号

折叠所有代码：Command +Shift+ minus/plus，Control + Shift+minus/plus

复制当前行到下一行或复制选中内容到后面：Command+ D，Control + D

完成代码片段：Command+ Shift + Enter，Control + Shift + Enter 

快速查看文档:Control + J,Control + Q 比如某个方法的注释文档

显示选中方法的参数：Command+P， Control + P	

跳转至声明：Command+B(Click)，Control+B(Click)  经常用的按住Ctrl+鼠标左键

跳转至实现处：Command + Alt + B，Control+Alt+B 实现类或方法,如果直接点击就会去声明处而不是实现

跳转至当前类的父类或当前方法的父类方法：Command+U， Control+U 

快速查看实现：Command + Y， Control+Shit+I 查看一个方法的内部实现

显示/隐藏项目（左侧Project）窗口：Command+1，Alt+1(数字1)

创建书签：F3，F11  某个类的某处

扩大代码块选中区域：Option + Up，Control + W

减小代码块选中区域：Option + Down，Control + Shift + W

移动到代码块开始：Option + Command + [，Control+[

移动到代码块结尾：Option + Command + ]，Control+]

按单词向后删除：Option + Delete，Control+Delete

按单词向前删除：Option + Backspace，Control + Backspace

整理导包：Control + Option + O，Control + Alt + O

格式化代码：Command+Option + L，Control + Alt + L

智能减少行：Control + Shift + J

智能分割行：Command+回车   当前行下面增加行，光标不动

增加一行：Shift+回车，增加行，光标移到下一行，当前行内容不变


# 编译运行
编译并运行：Control+R,Shift+F11	

# 调试
Debug:Control+D,Shift+F9

单步执行:F8

进入函数里面:F7

智能进入:Shift+F7

跳出函数:Shift+F8

打断点:Command+F8

查看所有断点:Command+Shift+F8	

# 重构
复制:F5

移动:F6  移动函数到其他类文件

安全删除:Command+Delete	 会检查其他地方有没有使用到

重命名:Shift+F6

重置参数:Command+F6

抽取方法:Command + Option + M

抽取变量:Command + Option + V

抽取字段:Command + Option + F,Control+Alt+F

抽取常量:Command + Option + C

抽取参数:Command + Option + P












