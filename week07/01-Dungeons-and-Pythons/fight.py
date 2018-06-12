from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell
from time import sleep


class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def start_fight(self):
        print('The fight between our hero and the enemy has juns begun and....')
        while self.hero.is_alive() and self.enemy.is_alive():
            self.enemy.take_damage(self.hero.bigger_damage())
            print('Our enemy health is {}'.format(self.enemy.get_health()))
            sleep(3)
            # print(self.hero.get_health())
            a = self.enemy.get_health()
            if a < 25 and a != 0:
                print('Ups, the hero almost kill me')
            self.hero.take_damage(self.enemy.attack())
            print('Our hero health is {}'.format(self.hero.get_health()))
            sleep(3)
            b = self.hero.get_health()
            if b < 25 and b != 0:
                print('Ups, the enemy almost kill me')
        if self.hero.is_alive():
            print("Enemy is dead")
        else:
            print("Hero is dead")
        return self.hero.is_alive()