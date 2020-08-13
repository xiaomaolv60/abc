'''
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
'''

class Animal:
    def __init__(self, name,food):
        self.name = name
        self.food = food

    def eat(self):
        print(f"{self.name}最喜欢吃{self.food}")


class RreptileAnimal(Animal):
    def __init__(self, name, food, color):
        super().__init__(name, food)
        self.color = color

    def crawl(self):
        print(f"{self.name}可以贴近地面爬行")


class FlyingAnimal(Animal):
    def __init__(self, name, food, fatherColor):
        super().__init__(name, food)
        self.fatherColor = fatherColor

    def fly(self):
        print(f"{self.name}可以自由飞翔")


Dog = Animal("dog", "bone")
Dog.eat()
Cat = Animal("cat", "fish")
Cat.eat()
Snake = RreptileAnimal("snake","mouse","green")
Snake.crawl()
Snake.eat()
Crow = FlyingAnimal("crow", "worm", "black")
Crow.fly()
Crow.eat()
Eagle = FlyingAnimal("eagle", "rabbit", "black")
Eagle.eat()
Eagle.fly()
