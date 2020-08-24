'''
课后作业
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
'''
import pytest
import yaml
import sys

from pytest_practice.calculatorCode.calculator import Calculator

print(sys.path)
sys.path.append('..')

def get_datas():
    with open('./datas/calculator.yml',encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        addids = mydatas['add']['myids']
        divdatas = mydatas['div']['datas']
        divids = mydatas['div']['myids']
    return [adddatas,addids,divdatas,divids]

class TestCalculator:
    def setup_class(self):
        print("开始-------------测试")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束-------------测试")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect",[
        (1,1,2),
        (0.1,0.2,0.3),
        (-10,-30,-50)
    ],ids=['int', 'float', 'minus'])  # 参数化 , ids命名测试用例结果
    def test_add0(self,a,b,expect):
        # calc = Calculator()
        print("测试相加")
        result = round(self.calc.add(a,b),2)
        assert expect == result

    @pytest.mark.parametrize("a,b,expect",get_datas()[0],ids=get_datas()[1])  # 参数化 , ids命名测试用例结果
    def test_add1(self,a,b,expect):
        # calc = Calculator()
        print("测试相加")
        result = self.calc.add(a,b)
        assert expect == result

    @pytest.mark.parametrize("a,b,expect", get_datas()[2], ids=get_datas()[3])  # 参数化 , ids命名测试用例结果
    def test_div0(self, a, b, expect):
        # calc = Calculator()
        print("测试相加")
        result = self.calc.div(a, b)
        assert expect == result