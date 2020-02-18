import unittest
from unit_2.lesson_17.refactor.library import *


class TestPersonCard(unittest.TestCase):

    def setUp(self):
        self.person_card = PersonCard('Denys Kuznetsov', id='123')
        self.book = Book("The Fall", 'self.author', '/path')
        self.book_2 = Book('The Wall', "self.author_2", '/path_2')

    def test_take_book(self):
        order = '123'
        self.person_card.take_book(order)
        self.assertIn(order, self.person_card.taken_books)

    def test_show_all_books_info(self):
        self.person_card.taken_books.extend([self.book, self.book_2])
        self.person_card.date_of_register = 123
        show_must_return = f'User name: Denys Kuznetsov.\n'\
                      f'User ID: 123.\n' \
                      f'Date of registration: 123.\n' \
                      f'Taken books: The Fall, The Wall.'
        show_return = self.person_card.show_all_books_info()
        self.assertEqual(show_must_return, show_return)


if __name__ == "__main__":
    unittest.main()