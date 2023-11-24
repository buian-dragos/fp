from src.domain.book import Book
from src.services.book_service import BookService

class Test:
    def test_Book(self):
        book = Book("617-212", "G.R.R. Martin", "A feast for crows")
        assert book.get_isbn() == "617-212"
        assert book.get_author() == "G.R.R. Martin"
        assert book.get_title() == "A feast for crows"
        assert str(book) == "A feast for crows by G.R.R. Martin ISBN: 617-212"
        print("Test passed")

    def test_BookService(self):
        book_service = BookService()
        book_service.add_book(Book("721-222", "J.R.R. Tolkien", "The Lord of the Rings"), 1)
        book_service.add_book(Book("432-221", "G.R.R. Martin", "A feast for crows"), 1)
        assert len(book_service.get_books()) == 2
        book_service.filter_books("The", 1)
        assert str(book_service) == "Books:\nA feast for crows by G.R.R. Martin ISBN: 432-221\n"
        assert len(book_service.get_books()) == 1
        book_service.undo(1)
        assert len(book_service.get_books()) == 2
        book_service.add_the_books(1)
        try:
            book_service.add_the_books(2)
        except ValueError as error:
            print(str(error))
        try:
            book_service.add_the_books(3)
        except ValueError as error:
            print(str(error))

        assert len(book_service.get_books()) == 12
        book_service.filter_books("The", 2)
        book_service.filter_books("bbb", 3)

        assert  len(book_service.get_books()) == 6

        book_service.undo(2)
        book_service.undo(3)

        assert len(book_service.get_books()) == 12

        book_service.add_book(Book("111-222", "test", "test"),2)
        book_service.add_book(Book("333-444", "test1", "test1"),3)

        assert len(book_service.get_books()) == 14

        print("Test passed")

if __name__ == '__main__':
    test = Test()
    test.test_Book()
    test.test_BookService()