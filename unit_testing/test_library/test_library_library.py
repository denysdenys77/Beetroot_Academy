import unittest
from unittest.mock import patch, Mock
from unit_2.lesson_17.refactor.library import *


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.person = Person("Denys", "Kuznetsov")
        self.author = Person('Albert', "Camus")
        self.author_2 = Person('Jean-Paul', 'Sartre')
        self.book = Book("The Fall", self.author, '/path')
        self.book_2 = Book('The Wall', self.author_2, '/path_2')

    def test_add_books(self):
        self.assertEqual(self.library.all_books, [])
        self.library.add_books(self.book)
        self.assertEqual(self.library.all_books, [self.book])

    def test_is_person_registered(self):
        self.library.person_cards.append(Mock(person=self.person))
        is_reg = self.library.is_person_registered(self.person)
        self.assertTrue(is_reg)
        self.library.person_cards.clear()

    def test_is_person_registered_false(self):
        is_not_reg = self.library.is_person_registered(self.person)
        self.assertFalse(is_not_reg)

    @patch('unit_2.lesson_17.refactor.library.uuid4')
    def test_register_person(self, mock_uuid):
        mock_uuid.return_value = 123456
        self.library.register_person(self.person)
        self.assertEqual(self.library.person_cards[0].id, 123456)

    def test_get_person_card(self):
        self.library.person_cards.clear()
        self.library.person_cards.append(Mock(person=self.person))
        person_card = self.library.get_person_card(self.person)
        self.assertEqual(person_card.person, self.person)
        self.library.person_cards.clear()

        with self.assertRaises(Exception):
            self.library.get_person_card(self.person)

    @patch('unit_2.lesson_17.refactor.library.Library.get_person_card')
    @patch('unit_2.lesson_17.refactor.library.Library.register_person')
    @patch('unit_2.lesson_17.refactor.library.Library.is_person_registered')
    def test_get_book(self, mock_ipr, mock_register_person ,mock_get_per_card):
        mock_ipr.return_value = False
        self.library.all_books.append(self.book)
        self.library.get_book(self.person, self.book)
        mock_ipr.assert_called()

        m_r_p = Mock(name=self.person.name, last_name=self.person.last_name)
        mock_register_person.return_value = m_r_p
        mock_register_person.assert_called()

        mock_per_card = Mock(taken_books=[])
        mock_get_per_card.return_value = mock_per_card
        mock_get_per_card.assert_called()

    @patch('unit_2.lesson_17.refactor.library.PersonCard.take_book')
    def test_get_book_result(self, mock_take_book):
        self.library.all_books.append(self.book)
        self.library.get_book(self.person, self.book)

        m_t_b = True
        mock_take_book.return_value = m_t_b
        mock_take_book.assert_called()
        self.library.all_books.clear()

    def test_get_book_raise(self):
        self.library.all_books.clear()
        with self.assertRaises(Exception):
            self.library.get_book(self.person, self.book_2)

    @patch('unit_2.lesson_17.refactor.library.Library.get_person_card')
    def test_get_book_back(self, mock_person_card):
        m = Mock(taken_books=[self.book])
        mock_person_card.return_value = m
        self.library.get_book_back(self.person, self.book)
        self.assertEqual(m.taken_books, [])
        self.library.person_cards.clear()  # очищаем self.person_cards для отработки других тестов

    def test_book_count(self):
        self.library.all_books.clear()
        self.library.all_books.append(self.book)
        book_count_return = self.library.book_count
        self.assertEqual(book_count_return, 1)
        self.library.all_books.clear()
    #
    def test_all_available_books(self):
        self.library.all_books.clear()

        self.library.all_books.append(self.book)
        mock_person_card = Mock(taken_books=[{'book_name': 'book_name',
                                              'when_was_taken': '22.11.19',
                                              'expiration_date': '31.12.19'}])
        self.library.person_cards.append(mock_person_card)
        all_available_books_return = self.library.all_available_books()
        self.assertEqual([self.book.name], all_available_books_return)

        self.library.all_books.clear()


if __name__ == "__main__":
    unittest.main()