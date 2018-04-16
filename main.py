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
    def __init__(self, hp, max_damage, enemy=False):
        self.hp = hp
        self.max_damage = max_damage
        self.enemy = enemy
        self.already_dead = False

    def attack(self, other):
        time.sleep(0.8)
        damage = random.randint(1, self.max_damage)
        other.fighter.take_damage(damage)
        print('{player} gör {damage} skada på {other}. {other} har {hp} hp kvar.'.format(player=self.owner.name, damage=damage, other=other.name, hp=other.fighter.hp))

    def take_damage(self, damage):
        self.hp = self.hp - damage

    def is_alive(self):
        return self.hp > 0

    def flee(self):
        print(f'{self.owner.name} flyr med svansen mellan benen.')
        quit_game()

    def death_function(self):
        if not self.already_dead:
            print(f'{self.owner.name} är död.')
            self.already_dead = True

class Action:
    def __init__(self, name, action, targeted=False):
        self.name = name
        self.action = action
        self.targeted = targeted

class InputHandler:
    def __init__(self, owner):
        self.owner = owner
        self.actions = {
            'a': Action(name='attackera', action=self.owner.fighter.attack, targeted=True),
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
            if chosen_action.targeted:
                targets = ''
                for k, v in objects.items():
                    if v.fighter and v.fighter.is_alive():
                        targets += f'{k}: {v.name} | '
                target = input(targets)
                chosen_action.action(objects[target])
            else: 
                chosen_action.action()
        else:
            print('Okänt kommando.')
            return False

fighter_component = Fighter(hp=8, max_damage=7, enemy=True)
kobold = GameObject(name='Kobold', fighter=fighter_component)
fighter_component = Fighter(hp=24, max_damage=9, enemy=True)
ork = GameObject(name='Ork', fighter=fighter_component)

fighter_component = Fighter(hp=34, max_damage=12)
player = GameObject(name='Ewert', fighter=fighter_component)
input_component = InputHandler(owner=player)
player.input_component = input_component

objects = {
    player.name[0].lower(): player,
    kobold.name[0].lower(): kobold,
    ork.name[0].lower(): ork
}


while True:
    if player.fighter.is_alive:
        player.input_component.player_input()
    else:
        print('{} är död.'.format(player.name))
        break
    for name, obj in objects.items():
        if obj.fighter.enemy:
            if obj.fighter.is_alive():
                obj.fighter.attack(player)
            else:
                obj.fighter.death_function()
    if len([obj for obj in objects.values() if obj.fighter.enemy and obj.fighter.is_alive()]) == 0:
        print('{} går segrande ur striden!'.format(player.name))
        # break
