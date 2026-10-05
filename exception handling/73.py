class BookError(Exception):
    pass
book=input("Enter book:")
raise BookError("Book not available")
print("Book available")
print(e)