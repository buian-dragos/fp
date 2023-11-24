from src.domain.book import Book
from src.repository.repository import MemoryRepository
from src.repository.repository import TextFileRepository
from src.repository.repository import BinaryFileRepository
from copy import deepcopy


class BookService:
    def __init__(self):
        self.__books = []
        self.__undo_list = []

    def add_book(self, book: Book, rtype):
        book_list = self.get_books()
        for book_in_list in range(len(book_list)):
            if book.get_isbn() in book_list[book_in_list].__str__():
                raise ValueError("Book already exists!")
        dc = deepcopy(self.__books)
        self.__undo_list.append(dc)
        self.__books.append(book)
        if rtype == 2:
            repo = TextFileRepository()
            repo.update_file(self.__books)
        elif rtype == 3:
            repo = BinaryFileRepository()
            repo.update_file(self.__books)

    def get_books(self):
        return self.__books

    def filter_books(self, word, rtype):
        dc = deepcopy(self.__books)
        self.__undo_list.append(dc)
        self.__books = [book for book in self.__books if not book.get_title().startswith(word)]
        if rtype == 2:
            tf = TextFileRepository()
            tf.update_file(self.__books)
        elif rtype == 3:
            bf = BinaryFileRepository()
            bf.update_file(self.__books)

    def undo(self,rtype):
        if len(self.__undo_list) > 0:
            self.__books = self.__undo_list.pop()
            if rtype == 2:
                tf = TextFileRepository()
                tf.update_file(self.__books)
            elif rtype == 3:
                bf = BinaryFileRepository()
                bf.update_file(self.__books)

    def __str__(self):
        string = "Books:\n"
        for book in self.__books:
            string += book.get_title() + " by " + book.get_author() + " ISBN: " + book.get_isbn() + '\n'
        return string

    def add_the_books(self, rtype):
        if rtype == 1:
            repo = MemoryRepository()
        elif rtype == 2:
            repo = TextFileRepository()
        else:
            repo = BinaryFileRepository()
        addBooks = repo.get_books()                                                                                                       # NOQA
        for book in addBooks:
            self.add_book(book,rtype)

