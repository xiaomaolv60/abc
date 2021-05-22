"""
写一个Bicycle(自行车)类,有run(骑行)方法, 调用时显示骑行里程km(骑行里程为传入的数字):
再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume属性通过参数传入,
 同时有两个方法：
1. fill_charge(vol) 用来充电, vol 为电量
2. run(km) 方法用于骑行,每骑行10km消耗电量1度,当电量消耗尽时调用Bicycle的run方法骑行，
通过传入的骑行里程数，显示骑行结果
"""

class Bicycle:
    def run(self,km):
        print(f"一共骑行了{km}公里") #z字面量插值

class EBicycle(Bicycle):#继承
    #重点：如果属性需要传参定义，那么可以使用构造函数
    def __init__(self,valume):
        self.valume = valume

    def fill_charge(self,vol):
        self.valume = self.valume + vol
        print(f"充了{vol}度电，现在的电量为{self.valume}")

    def run(self,km):
        """
           2. run(km) 方法用于骑行,每骑行10km消耗电量1度,当电量消耗尽时调用
           Bicycle的run方法骑行，
           通过传入的骑行里程数，显示骑行结果
           :return:
        """
        power_km = self.valume*10
        if power_km >= km:
            print(f"我使用电瓶电量骑行了{km}公里")
        else:
            print(f"我使用电瓶电量骑行了{power_km}公里")
            #非继承调用
            # bike = Bicycle()
            # bike.run(km-power_km)
            #继承调用
            super().run(km-power_km)


bike = Bicycle()
bike.run(5)
ebike = EBicycle(5)
ebike.fill_charge(10)
ebike.run(200)