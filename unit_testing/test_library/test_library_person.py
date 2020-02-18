import unittest
from unit_2.lesson_17.refactor.library import *


class TestPerson(unittest.TestCase):

    def test_init(self):
        denys = Person("Denys", "Kuznetsov")
        self.assertEqual(denys.name, 'Denys')
        self.assertEqual(denys.last_name, "Kuznetsov")

    def test_str(self):
        denys = Person("Denys", "Kuznetsov")
        self.assertEqual(str(denys), "Denys Kuznetsov")


if __name__ == "__main__":
    unittest.main()