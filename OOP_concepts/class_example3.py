
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, NewAuthor):
        self,author = NewAuthor

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)


b1 = Book("Python Basics", "John")
b2 = Book("Yayati","V.S.Khandeker")

b1.display()
b2.display()

print("Old Title:", b1.get_title())

b1.set_title("Advanced Python")

print("New Title:", b1.get_title())