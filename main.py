import random

class Player:
    def __init__(self):
        self.hp = 25
        self.max_damage = 10

    def attack(self, other):
        damage = random.randint(1, self.max_damage)
        other.hp = other.hp - damage
        print('{player} gör {damage} skada på {other}. {other} har {hp} hp kvar.'.format(player=self.name, damage=damage, other=other.name, hp=other.hp))

class Enemy:
    def __init__(self, hp, max_damage, name):
        self.hp = hp
        self.max_damage = max_damage
        self.name = name

    def attack(self, other):
        damage = random.randint(1, self.max_damage)
        other.hp = other.hp - damage
        print('{player} gör {damage} skada på {other}. {other} har {hp} hp kvar.'.format(player=self.name, damage=damage, other=other.name, hp=other.hp))

player = Player()
player.name = 'Tyko'
kobold = Enemy(hp=18, max_damage=7, name='Kobold')

while True:
    if player.hp > 0:
        player.attack(kobold)
    else:
        print('{} är död.'.format(player.name))
        break
    if kobold.hp > 0:
        kobold.attack(player)
    else:
        print('{} är död.'.format(kobold.name))
        break
