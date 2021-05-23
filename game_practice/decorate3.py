#定义装饰器，形参、实参是一个函数对象
#定义时的参数叫做形参，传递时的参数叫做实参
import time


def func1(func):
    def func2(m_time):
        print("开始的时间为：",time.strftime("%S"))
        func(m_time)#调用函数对象被调用
        print("开始的时间为：", time.strftime("%S"))
        print("我是func2")
    return func2

# TypeError: func1() takes 0 positional arguments but 1 was given
#出现错误的原因是没有将函数传给func1

@func1  #@func1表示func1(be_decorate)
def be_decorate(m_time): #传参
    time.sleep(m_time)
    print("被装饰器装饰的函数")

be_decorate(5)