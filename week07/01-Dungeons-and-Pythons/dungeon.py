from hero import Hero
from enemy import Enemy
from random import choice
from fight import Fight


h = Hero(name="Bron", title="Dragonslayer", health=10, mana=10, mana_regeneration_rate=2)
enemy = Enemy(health = 100, mana = 10, damage = 15)

class Dungeon:

    def __init__(self, filename, hero=None):
        self.filename = filename
        self.matrix = []
        self.rows = 0
        self.cols = 0
        self.hero = None
        self.treasure = {'mana': 10, 'health': 50}

    def open_file(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                row = []
                for i in line:
                    row.append(i)
                self.matrix.append(row[:-1])
        return self.matrix

    def print_map(self):
        if len(self.matrix) == 0:
            self.open_file()
            for row in self.matrix:
                for col in row:
                    print(col, end='')
                print()
        else:
            for row in self.matrix:
                for col in row:
                    print(col, end='')
                print()

    def spawn(self, Hero):
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == 'S':
                    self.matrix[i][j] = 'H'
                    self.hero = Hero
                    self.hero = Hero
                    return True    
            return False

    def pick_treasure(self):
        treasure = choice(list(self.treasure))
        return treasure

    def valid_position(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        else:
            return True


        self.spawn(h)

    def move_hero(self, direction):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        for i in range(rows):
            for j in range(cols):
                if self.matrix[i][j] == 'H':

                    if direction == 'left':
                        if self.valid_position(i, j - 1):
                            if self.matrix[i][j - 1] is '.':
                                self.matrix[i][j - 1] = 'H'
                                self.matrix[i][j] = '.'
                                return True
                            if self.matrix[i][j - 1] == 'E':
                                fight = Fight(self.hero, enemy)
                                if fight.start_fight():
                                    self.matrix[i][j - 1] = 'H'
                                    self.matrix[i][j] = '.'
                                    return True
                                else:
                                    return "Game Over"
                            if self.matrix[i][j] == 'T':
                                print('Found treasure!')
                                self.matrix[i][j - 1] = 'H'
                                self.matrix[i][j] = '.'
                                hero_treasure = self.pick_treasure()
                                if hero_treasure == 'health':
                                    self.hero.healt.take_healing(self.treasure['healt'])
                                else:
                                    self.hero.mana += self.treasure['mana']

                        else:
                            return False
                    elif direction == 'right':
                        if self.valid_position(i, j + 1):
                            if self.matrix[i][j + 1] is '.':
                                self.matrix[i][j + 1] = 'H'
                                self.matrix[i][j] = '.'
                                return True
                            elif self.matrix[i][j + 1] == 'E':
                                fight = Fight(self.hero, enemy)
                                if fight.start_fight():
                                    self.matrix[i][j + 1] = 'H'
                                    self.matrix[i][j] = '.'
                                    return True
                                else:
                                    return "Game Over"
                            elif self.matrix[i][j + 1] == 'T':
                                print('Found treasure!')
                                self.matrix[i][j + 1] = 'H'
                                self.matrix[i][j] = '.'
                                hero_treasure = self.pick_treasure()
                                if hero_treasure == 'health':
                                    self.hero.take_healing(self.treasure['health'])
                                else:
                                    self.hero.mana += self.treasure['mana']
                                    print('Mana', self.hero.get_mana())
                        else:
                            return False
                    if direction == 'up':
                        if self.valid_position(i - 1, j):
                            if self.matrix[i - 1][j] is '.':
                                self.matrix[i - 1][j] = 'H'
                                self.matrix[i][j] = '.'
                                return True
                            elif self.matrix[i - 1][j] == 'E':
                                fight = Fight(self.hero, enemy)
                                if fight.start_fight():
                                    elf.matrix[i - 1][j] = 'H'
                                    self.matrix[i][j] = '.'
                                    return True
                                else:
                                    return "Game Over"
                            elif self.matrix[i - 1][j] == 'T':
                                print('Found treasure!')
                                self.matrix[i - 1][j] = 'H'
                                self.matrix[i][j] = '.'
                                hero_treasure = self.pick_treasure()
                                if hero_treasure == 'health':
                                    self.hero.take_healing(self.treasure['health'])
                                else:
                                    self.hero.mana += self.treasure['mana']
                        else:
                            return False
                    elif direction == 'down':
                        if self.valid_position(i + 1, j):
                            if self.matrix[i + 1][j] is '.':
                                self.matrix[i + 1][j] = 'H'
                                self.matrix[i][j] = '.'
                                return True
                            elif self.matrix[i + 1][j] == 'E':
                                fight = Fight(self.hero, enemy)
                                if fight.start_fight():
                                    self.matrix[i + 1][j] = 'H'
                                    self.matrix[i][j] = '.' 
                                    return True
                                else:
                                    return "Game Over"
                            elif self.matrix[i + 1][j] == 'T':
                                print('Found treasure!')
                                self.matrix[i + 1][j] = 'H'
                                self.matrix[i][j] = '.'
                                hero_treasure = self.pick_treasure()
                                if hero_treasure == 'health':
                                    self.hero.healt.take_healing(self.treasure['healt'])
                                else:
                                    self.hero.mana += self.treasure['mana']
                        else:
                            return False

