from dungeon import Dungeon
from hero import Hero
from fight import Fight
from weapon import Weapon
from spell import Spell
from enemy import Enemy
from time import sleep



h = Hero(name="Bron", title="Dragonslayer", health=20, mana=100)
weapon = Weapon("weapon", 30)
h.equip(weapon)
spell = Spell()
h.learn(spell)
enemy = Enemy(health=100, mana=100, damage=20)

map = Dungeon('level1.txt')

# print('Prepare the map for the final fight')
# sleep(2)
print('A long time ago our hero {} was born in Sofia.'.format(h.name))
print()
sleep(4)
print('At the same time evil was born in the northwest.')
print()
sleep(4)
print('And now we have to prepare the map for the final fight')
sleep(4)
print()


print('The map')
map.print_map()
sleep(4)
map.spawn(h)

print()
print('The hero')
map.print_map()
sleep(4)
print()
map.move_hero('right')
print('Move right')
map.print_map()
print('Move left')
map.move_hero('left')
map.print_map()
print('move down')
map.move_hero('down')
map.print_map()
print('Move up')
map.move_hero('up')
map.print_map()
print('move down')
map.move_hero('down')
map.print_map()
print('move right')
map.move_hero('right')
map.print_map()
map.pick_treasure()
#print(map.hero.get_health())
print('move left')
map.move_hero('left')
print()
map.print_map()
print('move down')
map.move_hero('down')
map.move_hero('down')
map.print_map()
map.move_hero('right')
#print(map.pick_treasure())

# print('Healt', map.hero.get_health())
# print('Mana', map.hero.get_mana())


