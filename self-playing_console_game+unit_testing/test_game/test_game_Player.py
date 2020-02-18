import unittest
from unittest.mock import patch
from unit_2.unit_testing_2.game import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player('Player')
        self.computer = Player('Computer')

    @patch('random.randint')
    def test_small_hit(self, mock_randint):
        mock_randint.return_value = 20
        self.player.small_hit(self.computer)
        self.assertEqual(self.computer.health, 80)

    @patch('random.randint')
    def test_big_hit(self,  mock_randint):
        mock_randint.return_value = 20
        self.player.big_hit(self.computer)
        self.assertEqual(self.computer.health, 80)

    @patch('random.randint')
    def test_treatment(self, mock_randint):
        mock_randint.return_value = 20
        self.player.treatment()
        self.assertEqual(self.player.health, 120)


if __name__ == '__main__':
    unittest.main()