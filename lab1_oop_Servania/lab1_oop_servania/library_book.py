class LibraryBook:
    total_books = 0   # counter: ilang libro na ang nagawa

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        LibraryBook.total_books += 1   # tataas tuwing may bagong libro

    def borrow(self):
        if self.is_borrowed:
            print(f'"{self.title}" ay hiram na.')
        else:
            self.is_borrowed = True
            print(f'Nahiram mo ang "{self.title}".')

    def return_book(self):
        if not self.is_borrowed:
            print(f'"{self.title}" ay hindi pa nahihiram.')
        else:
            self.is_borrowed = False
            print(f'Naibalik na ang "{self.title}".')

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} [{status}]"

    def __repr__(self):
        return f"LibraryBook('{self.title}', '{self.author}')"


b1 = LibraryBook("The Idiot", "Fyodor Dostoyevsky")
b2 = LibraryBook("The Handmaid's Tale", "Margaret Atwood")
b3 = LibraryBook("Crime and Punishment", "Fyodor Dostoyevsky")

print("Total books:", LibraryBook.total_books)
print(b1)
b1.borrow()
b1.borrow()          # hiram na, dapat may babala
print(b1)
b1.return_book()
b1.return_book()     # hindi naman hiram, dapat may babala
print(b1)
print(repr(b2))
print([b1, b2, b3])