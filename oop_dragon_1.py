from random import randint
from pprint import pprint


class DragonConfig:
    SMOK_MAX_HP = 100
    SMOK_MIN_HP = 50
    SMOK_MAX_GOLD = 100
    SMOK_MIN_GOLD = 1
    TEXTURE_DRAGON = 'dragon.png'
    LIVE_POINTS = randint(SMOK_MIN_HP, SMOK_MAX_HP)


class Dragon:

    def __init__(self, smok_name, position_x, position_y):

        self.smok_name = smok_name
        self.position_x = position_x
        self.position_y = position_y
        self.live_points= randint(DragonConfig.SMOK_MIN_HP, DragonConfig.SMOK_MAX_HP)
        self.texture = DragonConfig.TEXTURE_DRAGON
        self.gold_content = randint(DragonConfig.SMOK_MIN_GOLD, DragonConfig.SMOK_MAX_GOLD)
        self.alive = True



    def smok_attack(self):
        return (randint(5, 20))

    def umieranie(self):
        self.alive = False
        self.texture = "dragon-dead.png"

        pprint(f'{self.smok_name} Smok jest dead ')
        pprint(f'deadnięty Smok {self.smok_name} daje {self.gold_content} złota')

    def smok_injured(self, injures):
        if self.alive:
            self.live_points = self.live_points - injures

            pprint(f'Smok {self.smok_name} HP = {self.live_points}')

            if self.live_points <= 0:
                my_dragon.umieranie()
        else:

            pprint(f'Smok {self.smok_name} jest already dead')

    def move(self, dela_poz_x, dela_poz_y):

        self.position_x = self.position_x + dela_poz_x
        self.position_y = self.position_x + dela_poz_y

        pprint(f'Smok {self.smok_name} jest na pozycji x={self.position_x} y={self.position_y}')

    def set_position(self, x, y):

        self.position_x = x
        self.position_y = y

        pprint(f'Smok {self.smok_name} jest na pozycji x={self.position_x} y={self.position_y} HP:{self.live_points}')


my_dragon = Dragon('Wawelski', 50, 120)
my_dragon.set_position(10, 20)
my_dragon.move(10, 20)
my_dragon.move(-10, 0)
my_dragon.move(15, 0)
my_dragon.move(15, 5)
my_dragon.move(5, 0)

my_dragon.smok_injured(10)
my_dragon.smok_injured(5)
my_dragon.smok_injured(3)
my_dragon.smok_injured(2)
my_dragon.smok_injured(15)
my_dragon.smok_injured(25)
my_dragon.smok_injured(75)
