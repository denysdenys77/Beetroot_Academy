import unittest
from unittest.mock import patch, call
from unit_2.unit_testing_2.game import Game, Player
from io import StringIO


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player = Player('Person')
        self.computer = Player('Computer')
        self.game = Game(self.player, self.computer)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('random.choice')
    @patch('random.shuffle', lambda x: x)
    def test_game_result(self, mocked_random_choice, mock_stdout):
        expected_output = 'Person wins!\n'
        mocked_random_choice.side_effect = [Player.small_hit, Player.small_hit, Player.small_hit, Player.small_hit,
                                            Player.small_hit, Player.small_hit]
        self.game.game()
        self.assertEqual(self.computer.health, 0)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    # @patch.object(Game, 'show_status')
    # @patch('random.choice')
    # @patch('random.shuffle', lambda x: x)
    # def test_game_inside(self, mock_random_shuffle, mock_random_choice, mock_show_status):
    #     mock_random_choice.side_effect = [Player.small_hit, Player.small_hit, Player.small_hit, Player.small_hit,
    #                                       Player.small_hit, Player.small_hit]
    #     self.game.game()
    #     mock_random_shuffle.assert_called()
    #     mock_random_choice.assert_called()
    #     mock_show_status.assert_called()

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_show_status(self, mock_stdout):
    #     expected_output = 'Person big_hit Computer.\nComputer health: 100.\n\n'
    #     self.game.show_status(self.player.big_hit, self.player, self.computer)
    #     self.assertEqual(expected_output, mock_stdout.getvalue())
    #
    # @patch('sys.stdout', new_callable=StringIO)
    # def test_show_status_treatment(self, mock_stdout):
    #     expected_output = 'Person treatment. Health: 100.\n\n'
    #     self.game.show_status(self.player.treatment, self.player, self.computer)
    #     self.assertEqual(expected_output, mock_stdout.getvalue())
    #
    # def test_health_borders(self):
    #     self.player.health = 120
    #     self.game.health_borders(self.player)
    #     self.assertEqual(self.player.health, 100)
    #
    #     self.computer.health = -20
    #     self.game.health_borders(self.computer)
    #     self.assertEqual(self.computer.health, 0)


if __name__ == '__main__':
    unittest.main()