from weapon import Weapon
from spell import Spell


class Hero:
    def __init__(self, name= None, title= None, health= 100, mana= 100, mana_regeneration_rate= 2):
        self.name = name
        self.title = title
        self.health = health
        self.maximum_health = self.health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapon = Weapon()
        self.spell = Spell()
        self.damage = 0

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        return self.mana > 0

    def take_damage(self, damage_points):
        if self.health < damage_points:
            self.health = 0
        else:
            self.health = self.health - damage_points

    def bigger_damage(self):
        if self.weapon.damage > self.spell.damage:
            return self.weapon.damage
        else:
            return self.spell.damage

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        if self.health + healing_points > self.maximum_health:
            self.health = self.maximum_health
        else:
            self.health += healing_points
        return True

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def atack(self, by=''):
        if by == 'weapon':
            if self.weapon:
                return self.weapon
            else:
                return 0
        if by == 'magic':
            if self.spell:
                return self.spell
            else:
                return 0

