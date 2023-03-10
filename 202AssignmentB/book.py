import doctest
from book import Book
class Book:
    ''' a class to represent a book.
    Instance attributes:
    *ISBN: int
    *title: str
    *author: str
    *genre: str
    *price: float 
    '''
    
    def __init__(self, isbn, title, author, genre, price):
        ''' (int, str, str, str, float)-> NoneType
        Creates an object of type Book.
        >>>my_book= Book(100, "Catch-22", "Joseph Heller", "dark comedy", "14,99")
        >>>my_book.title
        "Catch-22"
        >>>my_book.price
        "14.99" 
        '''
        
        self.ISBN = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
   
    def __str__(self):
        '''()-> str
        Returns the title and price of the book.
        >>> my_book = Book(100, "Catch-22", "Joseph Heller", "dark comedy", "14,99")
        Catch-22 @ 14.99
        '''
        
        return self.title + "@" + str(self.price) 
    
    def on_sale(self):
        ''' ()-> NoneType
         Halves the price of a book.
         >>> my_book = Book(100, "Catch-22", "Joseph Heller", "dark comedy", "14,99")
         >>> my_book.on_sale()
         >>> my_book.price
         5.0
         '''
        self.price /= 2
        
    def is_cheaper(self, other_book):
       '''(Book)-> bool
        Returns True of the current book is cheaper than other_book and False otherwise
        >>> catch_22 = Book(100, "Catch-22", "Joseph Heller", "dark comedy", "14,99")
        >>> crime_and_punishement(101, "Crime and Punishment" "Dotoyevsky")
        >>> catch_22.is_cheaper(crime_and_punishment)
        True
        '''
    return self.price < other_book.price
    
    def display_books(books_list):
        for books in books_list:
            print(book)
        
    def start_sale(books_list):
        for book in books_list:
            book.on_sale()
    
    def books_by_genre(self, genre):
        '''(str)-> list<Book>
        returns a list of books in the bookstore
        >>>catch_22 = Book(100, "Catch-22", "Joseph Heller", "dark comedy", "14,99")
        >>>hobbbit = Book(101, "The Hobbit, "JRR Tolkien", "fantasy" "15.99")
        >>>hp = Book(102, "Harry Potter", "JK Rowling", "fantasy", "13,99")
        >>> books["catch 22, hobbit, hp"]
        >>> the_word = Booksotre("The Word", books)
        '''
        genre_books = []
        for book in self.books.values():
            genre_books.append(books)
        return genre_books
    
    def get_all_genres(self):
        '''(str)-> list<Book>
        returns a list of books in the bookstore
        >>>catch_22 = Book(100, "Catch-22", "Joseph Heller", "dark comedy", "14,99")
        >>>hobbbit = Book(101, "The Hobbit, "JRR Tolkien", "fantasy" "15.99")
        >>>hp = Book(102, "Harry Potter", "JK Rowling", "fantasy", "13,99")
        >>> books["catch 22, hobbit, hp"]
        >>> the_word = Booksotre("The Word", books)
        >>> the_word.get_all_genres()
        ['Dark Comedy', 'Fantasy']
        '''
        genres = []
        for book in self.books.values():
            if book.genre not in genres:
                genres.append(book.genre)
        return genres
    
    def find_cheapest(self, genre):
        '''(str)-> list<Book>
        returns the cheapest book in the bookstore within a cerain genre 
        >>>catch_22 = Book(100, "Catch-22", "Joseph Heller", "dark comedy", "14,99")
        >>>hobbbit = Book(101, "The Hobbit, "JRR Tolkien", "fantasy" "15.99")
        >>>hp = Book(102, "Harry Potter", "JK Rowling", "fantasy", "13,99")
        >>> books["catch 22, hobbit, hp"]
        >>> the_word = Booksotre("The Word", books)
        >>> the_word.get_all_genres()
        ['Dark Comedy', 'Fantasy']
        '''
        genre_books = self.books_by_genre(genre)
        
        cheapest_book = genre_books[0]
        for book in genre+bookss[1:]:
            if book.price < cheapest_book.price:
                cheapest_boook 
    
    if __name__== "__main__":
        doctest.testmod()
        
  