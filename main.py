import random
import time

class GameObject:
    def __init__(self, name, fighter=None, inventory=None, item=None):
        self.name = name
        self.fighter = fighter
        self.inventory = inventory
        self.item = item
        if self.fighter:
            self.fighter.owner = self
        if self.inventory:
            self.inventory.owner = self
        if self.item:
            self.item.owner = self

class Fighter:
    def __init__(self, hp, max_damage):
        self.max_hp = hp
        self.hp = hp
        self.max_damage = max_damage

    def attack(self, other):
        time.sleep(0.3)
        damage = random.randint(1, self.max_damage)
        other.fighter.hp = other.fighter.hp - damage
        print('{player} gör {damage} skada på {other}. {other} har {hp} hp kvar.'.format(player=self.owner.name, damage=damage, other=other.name, hp=other.fighter.hp))

    def heal(self, amount):
        self.hp = self.hp + amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print('{} får tillbaka {} hp och har nu {} hp.'.format(self.owner.name, amount, self.hp))

class Inventory:
    def __init__(self):
        self.items = {}

class Item:
    def __init__(self, amount, use_function=None):
        self.amount = amount
        self.use_function = use_function

    def use(self):
        if self.amount > 0:
            self.use_function()
            self.amount = self.amount - 1
        else:
            print('{} har slut på {}.'.format(player.name, self.owner.name))

def cast_heal():
    player.fighter.heal(10)

fighter_component = Fighter(hp=34, max_damage=12)
player = GameObject(name='Ewert', fighter=fighter_component, inventory=Inventory())

item_component = Item(amount=5, use_function=cast_heal)
hp_potion = GameObject(name='HP-potion', item=item_component)
player.inventory.items['hp_potion'] = hp_potion

fighter_component = Fighter(hp=8, max_damage=7)
kobold = GameObject(name='Kobold', fighter=fighter_component)
fighter_component = Fighter(hp=24, max_damage=9)
ork = GameObject(name='Ork', fighter=fighter_component)

enemies = [kobold, ork]

while True:
    if player.fighter.hp > 0:
        if player.fighter.hp < 5 and player.inventory.items.get('hp_potion').item.amount > 0:
            player.inventory.items.get('hp_potion').item.use()
            continue # Enemy loses its turn when player uses health potion
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
