class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self ]
    def book(self):
        return[contract.book for contract in Book.all if book.title == self]
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    def total_royalties(self):
     return sum([])
    @property
    def contract(self):
        return self._contract
    @contract.setter
    def contract(self, value):
        if not isinstance (value, Contract):
            raise TypeError("Contract must be an instance of Contract class")
        self._contract = value

class Book:
    all =[]
    def __init__(self, title):
        Book.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self ]


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if not isinstance (value, Author):
            raise TypeError("Author must be an instance of Author class")
        self._author = value
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise TypeError("Book must be an instance of Book class")
        self._book = value
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception
        self._royalties = value
        


    