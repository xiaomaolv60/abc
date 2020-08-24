'''
作业1：
1、补全计算器（加减乘除）的测试用例
2、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
3、将 Fixture 方法存放在conftest.py ，设置scope=module
作业2：
1、编写用例顺序：加- 除-减-乘
2、控制测试用例顺序按照【加-减-乘-除】这个顺序执行
3、本地生成测试报告
'''
import allure
import pytest
import sys

from pytest_practice1.conftest import get_datas

print(sys.path)
sys.path.append('..')

@allure.feature("计算器功能测试")
class TestCalculator:
    # @pytest.mark.run(order=0)
    @pytest.mark.first
    @allure.story("测试加法计算功能")
    @pytest.mark.parametrize("a,b,expect",get_datas()[0],ids=get_datas()[1])  # 参数化 , ids命名测试用例结果
    def test_add(self,get_calculator,a,b,expect,get_calculator1):
        print("测试相加")
        result = round(get_calculator.add(a,b),2)
        assert expect == result

    # @pytest.mark.run(order=4)
    @pytest.mark.last
    @allure.story("测试除法计算功能")
    @pytest.mark.parametrize("a,b,expect", get_datas()[6], ids=get_datas()[7])  # 参数化 , ids命名测试用例结果
    def test_div(self,get_calculator, a, b, expect,get_calculator1):
        print("测试相除")
        result = round(get_calculator.div(a, b),2)
        assert expect == result

    # @pytest.mark.run(order=2)
    @pytest.mark.second
    @allure.story("测试减法计算功能")
    @pytest.mark.parametrize("a,b,expect", get_datas()[2], ids=get_datas()[3])  # 参数化 , ids命名测试用例结果
    def test_sub(self,get_calculator, a, b, expect,get_calculator1):
        print("测试相减")
        result = round(get_calculator.sub(a, b),2)
        assert expect == result

    # @pytest.mark.run(order=3)
    @pytest.mark.second_to_last
    @allure.story("测试乘法计算功能")
    @pytest.mark.parametrize("a,b,expect", get_datas()[4], ids=get_datas()[5])  # 参数化 , ids命名测试用例结果
    def test_mul(self,get_calculator, a, b, expect):
        print("测试相乘")
        result = round(get_calculator.mul(a, b),2)
        assert expect == result