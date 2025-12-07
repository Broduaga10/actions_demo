import unittest
from src.library import Book, PrintedBook, User, Library


class TestBook(unittest.TestCase):
    def test_book_fields(self):
        book = Book("Война и мир", "Толстой", 1869)
        self.assertEqual(book.get_title(), "Война и мир")
        self.assertEqual(book.get_author(), "Толстой")
        self.assertEqual(book.get_year(), 1869)


class TestPrintedBook(unittest.TestCase):
    def test_repair(self):
        book = PrintedBook("Война и мир", "Толстой", 1869, 1225, "bad")
        book.repair()
        self.assertEqual(book.condition, "good")

    def test_take_and_return(self):
        book = PrintedBook("Война и мир", "Толстой", 1869, 1225, "good")
        self.assertTrue(book.is_available())
        book.mark_as_taken("Анна")
        self.assertFalse(book.is_available())
        book.mark_as_returned()
        self.assertTrue(book.is_available())


class TestUser(unittest.TestCase):
    def test_borrow(self):
        user = User("Анна")
        book = PrintedBook("Война и мир", "Толстой", 1869, 1225, "good")

        user.borrow(book)
        self.assertIn("Война и мир", user.show_books())

        user.return_book(book)
        self.assertEqual(user.show_books(), [])


class TestLibrary(unittest.TestCase):
    def test_add_and_find_book(self):
        lib = Library()
        b = PrintedBook("Война и мир", "Толстой", 1869, 1225, "good")
        lib.add_book(b)

        found = lib.find_book(title="Война и мир")
        self.assertEqual(found.get_title(), "Война и мир")

    def test_add_user(self):
        lib = Library()
        user = User("Анна")
        lib.add_user(user)

        found = lib.find_user("Анна")
        self.assertEqual(found.name, "Анна")


if __name__ == "__main__":
    unittest.main()
