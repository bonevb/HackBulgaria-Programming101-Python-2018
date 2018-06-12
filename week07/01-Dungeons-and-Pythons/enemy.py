class Enemy:
    def __init__(self, health=100, mana=100, damage=20):
        self.health = health
        self.mana = mana
        self.damage = damage

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def can_cast(self):
        if self.mana <= 0:
            return False
        return True

    def get_health(self):
        if self.health < 0:
            return 0
        else:
            return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if self.health <= 0:
            return False
        if self.health + healing_points > 100:
            self.health = 100
        else:
            self.health += healing_points
        return True

    def take_mana(self, mana_potion=None):
        if mana_potion:
            if self.mana + mana_potion > 100:
                self.mana = 100
            else:
                self.mana += mana_potion

    def attack(self):
        return self.damage

    def take_damage(self, damage):
        self.health -= damage
