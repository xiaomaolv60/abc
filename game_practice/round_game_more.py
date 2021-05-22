"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""



from random import randint

def game():
    print("欢迎来到游戏世界!")
    print("游戏初始化...")
    my_hp = 1000
    your_hp = 1000
    lun =0
    my_power = randint(50,101)
    your_power = randint(50,101)
    print("我的初始血量：%d,敌人的初始血量：%d"%(my_hp, your_hp))
    while True:
        my_hp = my_hp - your_power   #敌人发起进攻，我的剩余血量
        your_hp = your_hp - my_power  #我发起进攻，敌人的剩余血量
        lun +=1
        print("第%d轮后，我的剩余血量：%d,敌人的剩余血量：%d"%(lun,my_hp,your_hp))
        # 三目运算
        # print("我赢了") if my_hp > your_hp else print("你赢了")

        if my_hp <= 0:
            print("我输了")
            break
        elif your_hp <= 0:
            print("你输了")
            break

game()