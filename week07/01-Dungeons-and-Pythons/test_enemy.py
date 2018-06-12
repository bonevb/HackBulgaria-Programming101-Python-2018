import unittest

from enemy import Enemy

enemy = Enemy(health=80, mana=90, damage=20)


class TestEnemy(unittest.TestCase):

    def test_enemy_is_alive(self):
        self.assertTrue(enemy.is_alive)

    def test_can_cast(self):
        self.assertTrue(enemy.can_cast())

    def test_get_healt(self):
        self.assertEqual(enemy.get_health(), 80)

    def test_get_mana(self):
        self.assertEqual(enemy.get_mana(), 90)


if __name__ == '__main__':
    unittest.main()
