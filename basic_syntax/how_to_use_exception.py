"""
created by nzh
Date: 2019/1/27 4:04 PM
"""

# 异常相关用法
# 我们最常用的应该就是except Exception as e:这样的语法了
# 但是这是捕获所有异常的，为什么这么说呢？
# 因为我们都知道python的类是支持集成的，我们常见的ValueError，TypeError等类
# 都是集成自Exception，所以，当你捕获Exception异常时，这些类型的异常都会被捕获到。
# 在python2中是这么写的： except Exception, e:
# 为了防止','混淆视听，python3中不再支持','作为分隔符，只支持as语句。


# 那么e代表什么呢？
# e代表捕获异常的实例。


# 如果捕获多个异常呢？
# 上面说到了python3中不再支持','分隔异常类型了，而我们想捕获多个异常时要用一个元组来
# 把我们要捕获的异常都包起来。
# 比如可以这样写：
# try:
#     2 / 0
# except (ZeroDivisionError, TypeError, IOError) as e:
#     print(e)


# 关于抛出异常
# 语法：raise ValueError("Invalid value")
# raise是抛出异常的关键字，然后紧跟异常类型，给异常类型传入一个描述异常的字符串
# 这个字符串是我们自定义的。方便快速定位问题所在。
# 其实从上面的语法中不难看书，抛出异常其实是一个实例化异常类的过程，而被抛出的正是
# 我们实例化的这个异常对象。


# 关于内置异常，你应该知道的
# 在exceptions模块中包含了内置的异常，执行任何程序之前都会先载入这个模块。
# 这些异常都被定义为类(class)，比如TypeError等等异常类。
# 在python中所有异常类都派生(或者说继承)自BaseException类。

# 那么Exception呢？
# 没错，Exception也是派生自BaseException，但是Exception表示与程序相关的所有异常类。

# 你还需要知道一些系统异常类，SystemExit、GeneratorExit、KeyboardInterrupt，他们都是
# 派生自BaseException类。


# 自定义异常
# 有时，我们在编写某个功能的代码时，需要有一种类来代表某种异常，那么就会用到自定义异常。
# 首先，我们要创建一个异常类，并让这个异常类派生自Exception。
# 然后在类中定义一些属性或者方法来处理异常。
# 比如这样：
# class SomeFuncError(Exception):
#     pass

# 根据蔡神的建议，标准的做法是把这些异常类都放在一个py文件中，可以取名func_exception.py之类的名字
# 有关某个功能的所有异常都在这个文件中定义。在程序调用的文件中再引入func_exception中的各个异常类就行了。


# 然后再说说常见的异常类吧
# ArithmeticError
# 算数异常类，包括OverflowError, ZeroDivisionError和FloatingPointError。
# LookupError
# 索引和键错误的基类，包括IndexError和KeyError。
# EnvironmentError
# 在python外部发生的错误基类，包括IOError和OSError。


# 一些常见异常引发的原因

# AssertError
# 失败的assert语句

# AttributeError
# 失败的属性引用或者赋值

# EOFError
# 文件末尾。由内置函数input()和raw_input()生成。
# 大多数文件操作函数，例如read(),readline()方法都返回空字符串来表示文件末尾，而非引发异常。

# FloatingPointError
# 失败的浮点操作。

# GeneratorExit
# 在生成器函数内部引发的错误，比如在使用所有生成器的值之前销毁生成器，或者调用生成器的close()方法
# 时会引发该错误。

# IOError
# 失败的I/O操作。
# 一个IOError实例一般包含3个属性，erno是整数错误编号，strerror是字符串错误消息，filename是可选的文件名

# ImportError
# 无法import相关模块时报错

# IndentationError
# 缩进错误，是SyntaxError的子类。

# IndexError
# 索引超出范围, 是LookupError的子类。

# KeyError
# 在映射中为找到键，也是LookupError的子类。

# KeyboardInterrupt
# 用户终端程序(CTRL+C组合键)

# MemoryError
# 可恢复内存不足错误。

# NameError
# 在局部或者全局命名空间中未找到名称

# 太多了，不写了，告辞。



