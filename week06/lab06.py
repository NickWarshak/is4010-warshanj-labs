class Book:
    """
    A class representing a physical book.
    """
    def __init__(self, title, author, year):
        """Initialize the book with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def get_age(self):
        """Calculate the age of the book based on the year 2025."""
        current_year = 2025
        return current_year - self.year

    def __str__(self):
        """Return a user-friendly string representation of the book."""
        return f"\"{self.title}\" by {self.author} ({self.year})"


class EBook(Book):
    """
    A class representing an electronic book, inheriting from Book.
    """
    def __init__(self, title, author, year, file_size):
        """Initialize EBook using the parent constructor plus file_size."""
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        """Return the parent string representation plus the file size."""
        parent_str = super().__str__()
        return f"{parent_str} ({self.file_size} MB)"


if __name__ == '__main__':
    # Part 1 Testing
    my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    print(f"Testing Book: {my_book}")
    print(f"Book Age: {my_book.get_age()} years")

    # Part 2 Testing
    my_ebook = EBook("Digital Fortress", "Dan Brown", 1998, 2)
    print(f"Testing EBook: {my_ebook}")
    print(f"EBook Age (inherited): {my_ebook.get_age()} years")