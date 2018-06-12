from hero import Hero
from enemy import Enemy



class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def start(self):
        while self.hero.is_alive() or self.enemy.is_alive():
            print('A fight is started between our Hero(health={}, mana={}) and Enemey(health={}, mana={}, damage={})'.format(
                self.hero.get_health(), self.hero.get_mana(), 
                self.enemy.get_health(), self.enemy.get_mana(), self.enemy.attack()))


h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100,
         mana_regeneration_rate=2)

e = Enemy(health=100, mana=100, damage=20)


f = Fight(h, e)

f.start()
