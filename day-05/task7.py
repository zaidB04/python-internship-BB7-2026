class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title):
        self.__books.append(title)
        print(title, "added successfully.")

    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
            print(title, "removed successfully.")
        else:
            print(title, "not found.")

    def list_books(self):
        print("Available Books:")
        for book in self.__books:
            print(book)


lib = Library()

lib.add_book("Python Programming")
lib.add_book("Javascript Programming")
lib.add_book("Game Development")

lib.list_books()

lib.remove_book("Javascript Programming")

lib.list_books()