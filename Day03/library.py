class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: list[str] = []  # Instance variable: a list of books for THIS library

    def add_book(self, book_title: str) -> None:
        """Adds a book to this library's collection."""
        self.books.append(book_title)

    def count_books(self) -> int:
        """Returns how many books are currently in the library."""
        return len(self.books)

    def __str__(self) -> str:
        """Dunder method: tells Python how to print this object."""
        return f"Library '{self.name}' has {self.count_books()} books."