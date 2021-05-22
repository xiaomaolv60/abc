#1、理解闭包函数定义
#2、理解闭包函数的调用
#3、变量在不同函数中的作用域

'''
name = "鲸鱼"
#函数定义
def func1():
    # print("aaa")
    print(name)
    #在函数func1内再定义一个函数
    def func2():
        name = "虾米"
        print("我是func2")
        print(name)
    #返回“肚子”里面的函数对象
    return func2

#不加括号的叫做函数对象
# func1
#加了括号的叫做函数调用

#函数调用
#func1的调用其实等于func2
func1()
'''

#定义装饰器，形参、实参是一个函数对象
#定义时的参数叫做形参，传递时的参数叫做实参
def func1(func):
    def func2():
        func()#调用函数对象被调用
        print("我是func2")
    return func2

# TypeError: func1() takes 0 positional arguments but 1 was given
#出现错误的原因是没有将函数传给func1

@func1  #@func1表示func1(be_decorate)
def be_decorate():
    print("被装饰器装饰的函数")


be_decorate()
#去掉@func1可以用下面的代码执行，结果一样
# print(func1(be_decorate))
# func1(be_decorate)()