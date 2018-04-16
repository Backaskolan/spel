#!/usr/bin/python3

import random
import time

def quit_game():
    print('Tack för att du spelade.')
    exit()

class GameObject:
    def __init__(self, name, fighter=None, input_component=None):
        self.name = name
        self.fighter = fighter
        self.input_component = input_component
        if self.fighter:
            self.fighter.owner = self
        if self.input_component:
            self.input_component.owner = self

class Fighter:
    def __init__(self, hp, max_damage):
        self.hp = hp
        self.max_damage = max_damage

    def attack(self, other):
        time.sleep(0.8)
        damage = random.randint(1, self.max_damage)
        other.fighter.take_damage(damage)
        print('{player} gör {damage} skada på {other}. {other} har {hp} hp kvar.'.format(player=self.owner.name, damage=damage, other=other.name, hp=other.fighter.hp))

    def take_damage(self, damage):
        self.hp = self.hp - damage

    def flee(self):
        print(f'{self.owner.name} flyr med svansen mellan benen.')
        quit_game()

class Action:
    def __init__(self, name, action, target=None):
        self.name = name
        self.action = action

class InputHandler:
    def __init__(self, owner):
        self.owner = owner
        self.actions = {
            'a': Action(name='attackera', action=self.owner.fighter.attack),
            'f': Action(name='fly', action=self.owner.fighter.flee),
            'q': Action(name='avsluta', action=quit_game)
        }

    def player_input(self):
        available_actions = ''
        for k, v in self.actions.items():
            available_actions += '{}: {} | '.format(k, v.name)
        action = input(available_actions)
        if action in self.actions.keys():
            chosen_action = self.actions[action]
            if chosen_action.name == 'attackera':
                chosen_action.action(random.choice(enemies))
            else: 
                chosen_action.action()
        else:
            print('Okänt kommando.')
            return False

fighter_component = Fighter(hp=8, max_damage=7)
kobold = GameObject(name='Kobold', fighter=fighter_component)
fighter_component = Fighter(hp=24, max_damage=9)
ork = GameObject(name='Ork', fighter=fighter_component)
enemies = [kobold, ork]

fighter_component = Fighter(hp=34, max_damage=12)
player = GameObject(name='Ewert', fighter=fighter_component)
input_component = InputHandler(owner=player)
player.input_component = input_component



while True:
    if player.fighter.hp > 0:
        player.input_component.player_input()
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
