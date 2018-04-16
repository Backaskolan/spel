import random
import time

class GameObject:
    def __init__(self, name, fighter=None):
        self.name = name
        self.fighter = fighter
        if self.fighter:
            self.fighter.owner = self

class Fighter:
    def __init__(self, hp, max_damage):
        self.hp = hp
        self.max_damage = max_damage

    def attack(self, other):
        time.sleep(0.8)
        damage = random.randint(1, self.max_damage)
        other.fighter.hp = other.fighter.hp - damage
        print('{player} gör {damage} skada på {other}. {other} har {hp} hp kvar.'.format(player=self.owner.name, damage=damage, other=other.name, hp=other.fighter.hp))

fighter_component = Fighter(hp=34, max_damage=12)
player = GameObject(name='Ewert', fighter=fighter_component)

fighter_component = Fighter(hp=8, max_damage=7)
kobold = GameObject(name='Kobold', fighter=fighter_component)
fighter_component = Fighter(hp=24, max_damage=9)
ork = GameObject(name='Ork', fighter=fighter_component)

enemies = [kobold, ork]

while True:
    if player.fighter.hp > 0:
        player.fighter.attack(random.choice(enemies))
    else:
        print('{} är död.'.format(player.name))
        break
    for enemy in enemies:
        if enemy.fighter.hp > 0:
            enemy.fighter.attack(player)
        else:
            print('{} är död.'.format(enemy.name))
            enemies.remove(enemy)
    if len(enemies) == 0:
        print('{} går segrande ur striden!'.format(player.name))
        break
