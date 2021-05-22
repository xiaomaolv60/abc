#定义装饰器，形参、实参是一个函数对象
#定义时的参数叫做形参，传递时的参数叫做实参
import time

def func1(time_1):  # 最外层管理 装饰器的参数
    def func2(func): # 管理传入的函数对象
        # 不定长参数， arg代表一个元组，通过位置参数进行传参， kwargs 代表字典， 通过关键字参数进行传参
        # def func2(*args, **kwargs):
        def func3(m_time): # 最内层管理被装饰函数的参数
            if time_1:
                print("开始的时间为：",time.strftime("%S"))
                func(m_time)#调用函数对象被调用
                print("开始的时间为：", time.strftime("%S"))
                print("我是func3")
            else:
                print("我是func3")
        return func3
    return func2

# TypeError: func1() takes 0 positional arguments but 1 was given
#出现错误的原因是没有将函数传给func1

@func1(time_1 = True)  #@func1表示func1(be_decorate)
def be_decorate(m_time): #传参
    time.sleep(m_time)
    print("被装饰器装饰的函数")


be_decorate(5)

# f1 = func1(time_1 = True) #返回func2函数对象
# f2 = f1(be_decorate) #相当于func2() == 返回func3函数对象
# f2(2)
