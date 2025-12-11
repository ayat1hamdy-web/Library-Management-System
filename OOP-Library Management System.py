# -------------------------
# CLASS: Book
# -------------------------

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn        # private attribute
        self.available = True

    # Getter for ISBN
    def get_isbn(self):
        return self.__isbn

    # Setter for ISBN
    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.__isbn}")
        print(f"Available: {self.available}")
        print("-" * 30)


# -------------------------
# CLASS: Member
# -------------------------

class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id       # private attribute
        self.borrowed_books = []

    # Getter for membership ID
    def get_membership_id(self):
        return self.__membership_id

    # Setter for membership ID
    def set_membership_id(self, new_id):
        self.__membership_id = new_id

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed the book '{book.title}'.")
        else:
            print(f"The book '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned the book '{book.title}'.")
        else:
            print(f"{self.name} does not have this book.")


# -------------------------
# CLASS: StaffMember (Inheritance)
# -------------------------

class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, book):
        library.add_book(book)
        print(f"Staff member {self.name} added the book '{book.title}' to the library.")


# -------------------------
# CLASS: Library
# -------------------------

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_all_books(self):
        print("\n----- Library Books -----")
        for book in self.books:
            book.display_info()


# -------------------------
# TESTING THE SYSTEM
# -------------------------

# Creating library
library = Library()

# Creating books
book1 = Book("Python Programming", "Ali Ahmed", "12345")
book2 = Book("OOP Concepts", "Omar Hany", "67890")

# Staff adds books to the library
staff = StaffMember("Ahmed", "M100", "S001")
staff.add_book(library, book1)
staff.add_book(library, book2)

# Show all books
library.show_all_books()

# Member actions
member1 = Member("Ayat", "MEM200")

member1.borrow_book(book1)
member1.borrow_book(book1)  # trying again (should be unavailable)
member1.return_book(book1)

# Show updates
library.show_all_books()
