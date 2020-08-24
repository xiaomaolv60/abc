import os
from typing import List


# id设置中文
import pytest
import yaml

from pytest_practice1.calculatorCode.calculator import Calculator


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


#设置fixture
@pytest.fixture(scope="module")
def get_calculator():
    print("-------------开始测试------------")
    calc = Calculator()
    yield calc
    print("------------- 结束测试------------")

@pytest.fixture()
def get_calculator1():
    print("开始计算")
    yield
    print("结束计算")

def get_datas():
    # with open('./datas/calculator.yml',encoding='utf-8') as f:
    mydatapath = os.path.dirname(__file__) + '/datas/calculator.yml'
    with open(mydatapath,encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        addids = mydatas['add']['ids']
        divdatas = mydatas['div']['datas']
        divids = mydatas['div']['ids']
        subdatas = mydatas['sub']['datas']
        subids = mydatas['sub']['ids']
        muldatas = mydatas['mul']['datas']
        mulids = mydatas['mul']['ids']
    return [adddatas,addids,subdatas,subids,muldatas,mulids,divdatas,divids]
