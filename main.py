import random
import time

class Player:
    def __init__(self, hp, max_damage, name):
        self.hp = hp
        self.max_damage = max_damage
        self.name = name

    def attack(self, other):
        time.sleep(0.8)
        damage = random.randint(1, self.max_damage)
        other.hp = other.hp - damage
        print('{player} gör {damage} skada på {other}. {other} har {hp} hp kvar.'.format(player=self.name, damage=damage, other=other.name, hp=other.hp))

class Enemy:
    def __init__(self, hp, max_damage, name):
        self.hp = hp
        self.max_damage = max_damage
        self.name = name

    def attack(self, other):
        time.sleep(0.8)
        damage = random.randint(1, self.max_damage)
        other.hp = other.hp - damage
        print('{player} gör {damage} skada på {other}. {other} har {hp} hp kvar.'.format(player=self.name, damage=damage, other=other.name, hp=other.hp))

player = Player(hp=34, max_damage=12, name='Ewert')
player2 = Player(hp=29, max_damage=15, name='Smulan')

kobold = Enemy(hp=8, max_damage=7, name='Kobold')
ork = Enemy(hp=24, max_damage=9, name='Ork')

party = [player, player2]
enemies = [kobold, ork]

while True:
    for player in party:
        if player.hp > 0:
            player.attack(random.choice(enemies))
        else:
            print('{} är död.'.format(player.name))
            break
    for enemy in enemies:
        if enemy.hp > 0:
            enemy.attack(random.choice(party))
        else:
            print('{} är död.'.format(enemy.name))
            enemies.remove(enemy)
    if len(enemies) == 0:
        print('{} går segrande ur striden!'.format(player.name))
        break
