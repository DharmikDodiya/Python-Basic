import datetime
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book added: {book}")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book removed: {book}")
                return
        print("Book not found.")

    def search_by_title(self, title):
        matches = [book for book in self.books if title.lower() in book.title.lower()]
        if matches:
            print("Search results:")
            for book in matches:
                print(f"- {book}")
        else:
            print("No books found with that title.")

if __name__ == "__main__":
    library = Library()

    library.add_book("The Alchemist", "Paulo Coelho")
    library.add_book("Atomic Habits", "James Clear")
    library.add_book("Think and Grow Rich", "Napoleon Hill")

    library.search_by_title("Atomic")
    library.remove_book("The Alchemist")
    library.search_by_title("The")
