import unittest
from unittest import patch, mock
from unit_3.lesson_18.presentation.library.book import Book


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book('Name', 'Author', 'file_path')



    # def test_count_if_lines(self):
    #     open_mock = mock.MagicMock()
    #     with mock.patch('__builtin__.open', open_mock):
    #         self.book.count_of_lines()
    #         open_mock.assert_called()




    @mock.patch('unit_2.lesson_17.refactor.library.open')
    def test_count_if_lines(self, open_mock):
        open_mock.return_value = 'djflsj'
        self.book.count_of_lines()
        open_mock.assert_called()


if __name__ == '__main__':
    unittest.main()