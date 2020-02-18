from datetime import datetime, timedelta
from uuid import uuid4


class Person:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Library:

    all_books = []
    person_cards = []

    def add_books(self, *args):
        """добавить книгу в библиотеку"""
        self.all_books.extend(args)

    def is_person_registered(self, person):
        """
        вернуть True если пользователь уже зарегестрирован в библиотеке
        вернуть False если пользователь не зарегестрирован
        """
        for person_card in self.person_cards:
            if person == person_card.person:
                return True
        return False

    def register_person(self, person):
        """создать карточку для пользователя и добавить ее в список уже существующих"""
        new_person_card = PersonCard(person, id = uuid4())
        self.person_cards.append(new_person_card)

    def get_person_card(self, person):
        """вернуть карточку пользователя"""
        for card in self.person_cards:
            if person == card.person:
                return card
        else:
            raise Exception('Not exist')

    def get_book(self, person, book):
        """выдать книгу определенному пользователю если она свободна
        если пользователь зарегестрирован в библиотеке

        проверить зарегестрирован ли пользователь в библиотеке
        если нет - зарегестрировать
        """
        if not self.is_person_registered(person):
            self.register_person(person)

        person_card = self.get_person_card(person)

        for book in self.all_books:
            if book in self.all_books:
                order = {
                    "book_name": book,
                    "when_was_taken": datetime.now(),
                    "expiration_date": datetime.now() + timedelta(days=30)
                }
                person_card.take_book(order)
        if book not in self.all_books:
            raise Exception('Book is not available')

    def get_book_back(self, person, the_book):
        """вернуть книгу обратно в библиотеку"""
        person_card = self.get_person_card(person)
        for book in person_card.taken_books:
            if the_book.name == book.name:
                person_card.taken_books.remove(book)

    @property
    def book_count(self):
        """вернуть количество всех книг"""
        return len(self.all_books)

    def all_available_books(self):
        """Сделать с помощью списковых включений"""
        available_books = []
        taken_books = []

        for person_card in self.person_cards:
            for book in person_card.taken_books:
                taken_books.append(book['book_name'])

        for book in self.all_books:
            if book not in taken_books:
                available_books.append(book.name)
        return available_books


class Book:

    def __init__(self, name, author, file_path):
        self.name = name
        self.author = author
        self.file_path = file_path
        self.id = uuid4()

    @property
    def count_of_lines(self):
        with open(self.file_path) as book:
            lines_in_book = len(book.readlines())
        return lines_in_book


class PersonCard:

    def __init__(self, person, id):
        self.person = person
        self.id = id
        self.date_of_register = datetime.now()
        self.taken_books = []

    def take_book(self, order):
        self.taken_books.append(order)

    def show_all_books_info(self):
        """вывести на экран информацию о пользователе и книгах которые у него на руках"""
        books = [book.name for book in self.taken_books]
        str_books = ', '.join(books)
        return f'User name: {self.person}.\n' \
               f'User ID: {self.id}.\n' \
               f'Date of registration: {self.date_of_register}.\n' \
               f'Taken books: {str_books}.'


# den = Person('denis', 'kuzn')
# book = Book("Book name", 'self.author', '/path')
# lib_1 = Library()
# lib_1.add_books(book)
# lib_1.get_book(den, book)
# pc = lib_1.get_person_card(den)
# print(pc.taken_books)
