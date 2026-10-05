class BookNotAvailableError(Exception):
    book = input("Enter book name: ")

raise BookNotAvailableError("Book Not Avaliable")
print("book available")
print()
