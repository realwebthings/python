# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by Python's built-in when certain operations
#                 are performed on instances of the class.
#                 They allow developers to define or customise the behavior of objects


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # String representation methods
    def __str__(self) -> str:
        """Human-readable string representation"""
        return f"'{self.title}' by '{self.author}'"
    
    def __repr__(self) -> str:
        """Developer-friendly string representation"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # Comparison methods
    def __eq__(self, other) -> bool:
        """Equal to (==)"""
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
    def __ne__(self, other) -> bool:
        """Not equal to (!=)"""
        return not self.__eq__(other)
    
    def __lt__(self, other) -> bool:
        """Less than (<)"""
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented
    
    def __le__(self, other) -> bool:
        """Less than or equal to (<=)"""
        if isinstance(other, Book):
            return self.pages <= other.pages
        return NotImplemented
    
    def __gt__(self, other) -> bool:
        """Greater than (>)"""
        if isinstance(other, Book):
            return self.pages > other.pages
        return NotImplemented
    
    def __ge__(self, other) -> bool:
        """Greater than or equal to (>=)"""
        if isinstance(other, Book):
            return self.pages >= other.pages
        return NotImplemented
    
    # Arithmetic methods
    def __add__(self, other):
        """Addition (+) - combine pages"""
        if isinstance(other, Book):
            return Book(f"{self.title} & {other.title}", f"{self.author} & {other.author}", self.pages + other.pages)
        elif isinstance(other, int):
            return Book(self.title, self.author, self.pages + other)
        return NotImplemented
    
    def __sub__(self, other):
        """Subtraction (-) - subtract pages"""
        if isinstance(other, Book):
            return abs(self.pages - other.pages)
        elif isinstance(other, int):
            return Book(self.title, self.author, max(0, self.pages - other))
        return NotImplemented
    
    def __mul__(self, other):
        """Multiplication (*) - multiply pages"""
        if isinstance(other, int):
            return Book(f"{self.title} (x{other})", self.author, self.pages * other)
        return NotImplemented
    
    def __truediv__(self, other):
        """Division (/) - divide pages"""
        if isinstance(other, int) and other != 0:
            return Book(f"{self.title} (/{other})", self.author, self.pages // other)
        return NotImplemented
    
    # Container methods
    def __len__(self):
        """Length - return number of pages"""
        return self.pages
    
    def __contains__(self, item):
        """Contains (in) - check if word is in title or author"""
        return item.lower() in self.title.lower() or item.lower() in self.author.lower()
    
    def __getitem__(self, key):
        """Get item by index []"""
        if key == 0 or key == 'title':
            return self.title
        elif key == 1 or key == 'author':
            return self.author
        elif key == 2 or key == 'pages':
            return self.pages
        else:
            raise KeyError(f"Invalid key: {key}")
    
    def __setitem__(self, key, value):
        """Set item by index []"""
        if key == 0 or key == 'title':
            self.title = value
        elif key == 1 or key == 'author':
            self.author = value
        elif key == 2 or key == 'pages':
            self.pages = value
        else:
            raise KeyError(f"Invalid key: {key}")
    
    # Hash method
    def __hash__(self):
        """Hash - allows Book to be used in sets and as dict keys"""
        return hash((self.title, self.author))
    
    # Boolean method
    def __bool__(self):
        """Boolean - True if book has pages"""
        return self.pages > 0
    
    # Call method
    def __call__(self):
        """Make object callable - return book info"""
        return f"Reading '{self.title}' by {self.author} ({self.pages} pages)"
    
    # Iterator methods
    def __iter__(self):
        """Make object iterable"""
        return iter([self.title, self.author, self.pages])
    
    # Context manager methods
    def __enter__(self):
        """Enter context manager"""
        print(f"Opening book: {self.title}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager"""
        print(f"Closing book: {self.title}")
        return False
    
    def compare_with_message(self, other):
        """Compare books and return descriptive message"""
        if isinstance(other, Book):
            if self.title == other.title and self.author == other.author:
                return f"'{self.title}' by '{self.author}' and '{other.title}' by '{other.author}' are equal"
            else:
                return f"'{self.title}' by '{self.author}' and '{other.title}' by '{other.author}' are not equal"
        return "Cannot compare with non-Book object"


# Create test books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("1984", "George Orwell", 328)
book4 = Book("1984", "George Orwell", 250)

print("=== String Representation ===")
print(f"str(book1): {str(book1)}")
print(f"repr(book1): {repr(book1)}")

print("\n=== Comparison Methods ===")
print(f"book1 == book2: {book1 == book2}")
print(f"book1 != book2: {book1 != book2}")
print(f"book1 < book2: {book1 < book2}")
print(f"book1 > book2: {book1 > book2}")
print(f"book1 <= book2: {book1 <= book2}")
print(f"book1 >= book2: {book1 >= book2}")

print("\n=== Arithmetic Methods ===")
book5 = book1 + book2  # Combine books
print(f"book1 + book2: {book5}")
print(f"book1 + 50 pages: {book1 + 50}")
print(f"book2 - book1 (page difference): {book2 - book1}")
print(f"book1 * 2: {book1 * 2}")
print(f"book2 / 2: {book2 / 2}")

print("\n=== Container Methods ===")
print(f"len(book1): {len(book1)} pages")
print(f"'Gatsby' in book1: {'Gatsby' in book1}")
print(f"'Python' in book1: {'Python' in book1}")
print(f"book1[0] (title): {book1[0]}")
print(f"book1['author']: {book1['author']}")

print("\n=== Hash and Boolean ===")
print(f"hash(book1): {hash(book1)}")
print(f"bool(book1): {bool(book1)}")
book_empty = Book("", "", 0)
print(f"bool(empty book): {bool(book_empty)}")

print("\n=== Callable ===")
print(f"book1(): {book1()}")

print("\n=== Iterator ===")
print("Iterating through book1:")
for item in book1:
    print(f"  {item}")

print("\n=== Context Manager ===")
with book1 as b:
    print(f"  Reading: {b.title}")

print("\n=== Set Operations (using hash) ===")
book_set = {book1, book2, book3, book4}
print(f"Unique books in set: {len(book_set)}")

print("\n=== Descriptive Messages ===")
print(book1.compare_with_message(book2))
print(book3.compare_with_message(book4))
    
