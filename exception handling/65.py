from dbm.ndbm import library


class BookNotAvailableError(Exception):
    pass
    def __init__(self):
        self.books = ["Python", "Java"]

    def search(self, book):
        if book not in self.books:
            raise BookNotAvailableError("Book not available")
        print("Book available")
        library=BookNotAvailableError()
library.search("C")
print(not 10>15)