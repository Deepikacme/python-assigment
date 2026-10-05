words = {
    "apple": "A fruit",
    "book": "A collection of pages",
    "car": "A vehicle"
}

word = input("Enter a word: ")

if word in words:
    print(words[word])
else:
    print("Word not found")