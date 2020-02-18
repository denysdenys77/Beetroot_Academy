import unittest
from unittest.mock import patch, Mock
from datetime import datetime, timedelta
from uuid import uuid4
from unit_2.lesson_17.refactor.library import *


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.person = Person("Denys", "Kuznetsov")
        self.author = Person('Albert', "Camus")
        self.author_2 = Person('Jean-Paul', 'Sartre')
        self.book = Book("The Fall", self.author, '/path')
        self.book_2 = Book('The Wall', self.author_2, '/path_2')


    @patch('unit_2.lesson_17.refactor.library.PersonCard.take_book')
    @patch('unit_2.lesson_17.refactor.library.Library.get_person_card')
    @patch('unit_2.lesson_17.refactor.library.Library.register_person')
    @patch('unit_2.lesson_17.refactor.library.Library.is_person_registered')
    def test_get_book(self, mock_is_person_registered, mock_register_person, mock_get_person_card, mock_take_book):
        self.library.all_books.append(self.book)
        # mock_is_person_registered.return_value = False
        m_r_p = Mock(taken_books=[])
        # mock_register_person.return_value = m_r_p
        self.library.person_cards.append(m_r_p)
        mock_get_person_card.return_value = m_r_p
        side_effect = m_r_p.taken_books.append(self.book)
        mock_take_book.return_value = side_effect
        self.library.get_book(self.person, self.book)
        self.assertEqual(self.book, m_r_p.taken_books[0])

        self.library.all_books.clear()
        with self.assertRaises(Exception):
            self.library.get_book(self.person, self.book_2)






if __name__ == '__main__':
    unittest.main()